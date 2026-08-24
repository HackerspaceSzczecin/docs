"""Render the association's Markdown documents to archival PDF.

Metadata handling: every document may carry a YAML front matter block. Any
field it omits falls back to config.yaml, so plain Markdown files without front
matter still produce properly described PDFs. The resulting values are written
into the PDF document information dictionary by WeasyPrint.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
from pathlib import Path

import yaml
from markdown_it import MarkdownIt
from weasyprint import HTML

STYLE_DIR = Path(__file__).parent / "style"
DEFAULT_CONFIG = Path(__file__).parent / "config.yaml"

FRONT_MATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
PAGEBREAK = re.compile(r"<!--\s*pagebreak\s*-->")
# A paragraph made only of the dotted fill characters used for signature lines.
SIGNATURE_LINE = re.compile(r"<p>([…\.\s]{6,})</p>")


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def split_front_matter(text: str) -> tuple[dict, str]:
    match = FRONT_MATTER.match(text)
    if not match:
        return {}, text
    data = yaml.safe_load(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError("front matter must be a YAML mapping")
    # Keep line numbers aligned with the source file for readable error output.
    body = text[match.end() :]
    return data, body


def first_heading(markdown_text: str) -> str | None:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def last_modified(path: Path) -> str:
    """When the text last changed, not when the container happened to run.

    Prefers the git commit date; inside the container git is usually absent (and
    the mounted .git belongs to another uid), so the file mtime is the fallback.
    """
    import subprocess

    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", path.name],
            capture_output=True,
            text=True,
            cwd=path.parent,
            timeout=10,
        )
        stamp = out.stdout.strip()
        if out.returncode == 0 and stamp:
            return stamp
    except (OSError, subprocess.SubprocessError):
        pass

    mtime = dt.datetime.fromtimestamp(path.stat().st_mtime).astimezone()
    return mtime.isoformat(timespec="seconds")


def to_iso(value) -> str:
    """PDF dates must be ISO 8601. YAML turns an unquoted date into a
    datetime/date object whose str() uses a space instead of 'T', which
    WeasyPrint silently rejects - so normalise before handing it over."""
    if value in (None, ""):
        return ""
    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat()
    return str(value)


def build_metadata(config: dict, front: dict, source: Path, markdown_text: str) -> dict:
    defaults = config.get("metadata", {})
    title = front.get("title") or first_heading(markdown_text) or source.stem
    keywords = front.get("keywords", defaults.get("keywords", []))
    if isinstance(keywords, str):
        keywords = [k.strip() for k in keywords.split(",") if k.strip()]

    modified = front.get("modified") or last_modified(source)
    created = front.get("created") or defaults.get("created") or modified

    return {
        "title": str(title),
        "author": str(front.get("author", defaults.get("author", ""))),
        "description": str(front.get("subject", defaults.get("subject", ""))),
        "keywords": ", ".join(str(k) for k in keywords),
        "generator": str(defaults.get("generator", "haszcze-docs")),
        "lang": str(front.get("lang", defaults.get("lang", "pl"))),
        "created": to_iso(created),
        "modified": to_iso(modified),
    }


def markdown_to_html(markdown_text: str) -> str:
    # linkify is off on purpose: bare URLs in a legal text stay literal, and
    # the repo convention writes links in explicit Markdown syntax anyway.
    md = MarkdownIt(
        "gfm-like",
        {
            "html": True,
            "typographer": False,
            "linkify": False,
        },
    )
    body = md.render(markdown_text)
    body = PAGEBREAK.sub('<div class="pagebreak"></div>', body)
    body = SIGNATURE_LINE.sub(r'<p class="signature-line">\1</p>', body)
    return body


def meta_tag(name: str, value: str) -> str:
    if not value:
        return ""
    return f'  <meta name="{name}" content="{html.escape(value, quote=True)}">\n'


def build_document(body_html: str, meta: dict, css_text: str, style_vars: dict) -> str:
    overrides = "".join(
        f"  --{key.replace('_', '-')}: {value};\n" for key, value in style_vars.items()
    )
    root_override = f":root {{\n{overrides}}}\n" if overrides else ""

    head = [
        f"  <title>{html.escape(meta['title'])}</title>\n",
        meta_tag("author", meta["author"]),
        meta_tag("description", meta["description"]),
        meta_tag("keywords", meta["keywords"]),
        meta_tag("generator", meta["generator"]),
        meta_tag("dcterms.created", meta["created"]),
        meta_tag("dcterms.modified", meta["modified"]),
    ]
    return (
        f'<!DOCTYPE html>\n<html lang="{html.escape(meta["lang"])}">\n<head>\n'
        '  <meta charset="utf-8">\n'
        + "".join(head)
        + f"  <style>\n{css_text}\n{root_override}  </style>\n"
        "</head>\n<body>\n"
        f"{body_html}"
        "</body>\n</html>\n"
    )


def render_one(source: Path, out_dir: Path, config: dict, args) -> Path:
    text = source.read_text(encoding="utf-8")
    front, markdown_text = split_front_matter(text)
    meta = build_metadata(config, front, source, markdown_text)

    style_vars = dict(config.get("style", {}))
    style_vars.update(front.get("style", {}))
    css_text = (STYLE_DIR / "document.css").read_text(encoding="utf-8")

    document_html = build_document(
        markdown_to_html(markdown_text), meta, css_text, style_vars
    )

    out_dir.mkdir(parents=True, exist_ok=True)
    stem = source.stem
    if args.html:
        html_path = out_dir / f"{stem}.html"
        html_path.write_text(document_html, encoding="utf-8")

    pdf_path = out_dir / f"{stem}.pdf"
    variant = None if args.no_pdfa else config.get("pdf", {}).get("variant", "pdf/a-3b")

    # base_url lets relative image paths in the Markdown resolve.
    HTML(string=document_html, base_url=str(source.parent)).write_pdf(
        pdf_path,
        pdf_variant=variant,
        uncompressed_pdf=False,
    )
    return pdf_path


def count_bookmarks(outline) -> int:
    """Outlines nest, so the top-level length alone understates the count."""
    total = 0
    for item in outline or []:
        if isinstance(item, list):
            total += count_bookmarks(item)
        else:
            total += 1
    return total


def pdfa_claim(reader) -> str:
    """What conformance level the file declares, read back from its own XMP."""
    try:
        xmp = reader.xmp_metadata
    except Exception:  # noqa: BLE001 - a missing/broken XMP is not fatal here
        return "brak"
    if xmp is None:
        return "brak"
    part = getattr(xmp, "pdfaid_part", None)
    conformance = getattr(xmp, "pdfaid_conformance", None)
    if part:
        return f"PDF/A-{part}{(conformance or '').lower()}"
    return "brak"


def describe(pdf_path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    info = reader.metadata or {}
    size_kb = pdf_path.stat().st_size // 1024
    lines = [
        f"  {pdf_path.name}  ({len(reader.pages)} str., {size_kb} KB, "
        f"{count_bookmarks(reader.outline)} zakladek, {pdfa_claim(reader)})"
    ]
    for label, key in [
        ("Tytul", "/Title"),
        ("Autor", "/Author"),
        ("Temat", "/Subject"),
        ("Slowa kluczowe", "/Keywords"),
        ("Utworzono", "/CreationDate"),
        ("Zmodyfikowano", "/ModDate"),
    ]:
        value = info.get(key)
        if value:
            lines.append(f"      {label}: {value}")
    return "\n".join(lines)


def preview_png(pdf_path: Path, pages: int = 1) -> None:
    import pypdfium2 as pdfium

    pdf = pdfium.PdfDocument(str(pdf_path))
    for index in range(min(pages, len(pdf))):
        image = pdf[index].render(scale=1.6).to_pil()
        image.save(pdf_path.with_suffix(f".p{index + 1}.png"))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Render Markdown documents to archival PDF."
    )
    parser.add_argument(
        "sources",
        nargs="*",
        default=[],
        help="Markdown files (default: every tracked document)",
    )
    parser.add_argument("--out-dir", default="out", type=Path)
    parser.add_argument("--config", default=DEFAULT_CONFIG, type=Path)
    parser.add_argument(
        "--html", action="store_true", help="also write the intermediate HTML preview"
    )
    parser.add_argument(
        "--png", action="store_true", help="also write a PNG of the first page"
    )
    parser.add_argument(
        "--no-pdfa",
        action="store_true",
        help="skip PDF/A conformance (smaller, non-archival)",
    )
    args = parser.parse_args(argv)

    config = load_config(args.config)
    sources = [Path(s) for s in args.sources]
    if not sources:
        exclude = set(config.get("exclude", []))
        sources = sorted(
            p
            for p in Path(".").rglob("*.md")
            if not any(part.startswith(".") for part in p.parts)
            and str(p) not in exclude
            and p.name != "README.md"
        )

    if not sources:
        print("Nie znaleziono zadnych dokumentow do wygenerowania.", file=sys.stderr)
        return 1

    failures = 0
    for source in sources:
        if not source.is_file():
            print(f"! pomijam {source}: brak pliku", file=sys.stderr)
            failures += 1
            continue
        try:
            pdf_path = render_one(source, args.out_dir, config, args)
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"! {source}: {exc}", file=sys.stderr)
            failures += 1
            continue
        if args.png:
            preview_png(pdf_path)
        print(describe(pdf_path))

    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\nGotowe ({stamp}), katalog: {args.out_dir}/")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

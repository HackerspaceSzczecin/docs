# Hackerspace Szczecin - dokumenty

Repozytorium dokumentów ustrojowych Stowarzyszenia Zwykłego **"Hackerspace
Szczecin"** (skrót: **"HaSzcze"**). Wszystkie dokumenty są utrzymywane jako
Markdown, żeby zmiany były wersjonowane, przeglądalne i możliwe do omówienia
przed przyjęciem uchwałą.

## Dokumenty

| Dokument | Zakres |
| --- | --- |
| [Regulamin Stowarzyszenia Zwykłego](regulaminy/regulamin-stowarzyszenia.md) | Nazwa, cele, teren działania, członkostwo, władze, reprezentacja, posiedzenia i głosowania, majątek, utrata członkostwa, zmiana regulaminu i rozwiązanie. |
| [Regulamin korzystania z przestrzeni](regulaminy/regulamin-przestrzeni.md) | Zasady współżycia, dostęp, bezpieczeństwo, porządek, narzędzia i maszyny, rezerwacje, wydarzenia, alkohol, monitoring, reagowanie na naruszenia. |
| [Protokół zebrania założycielskiego](regulaminy/protokol-zebrania-zalozycielskiego.md) | Utworzenie Stowarzyszenia, uchwały nr 1-4 (powołanie Stowarzyszenia, regulamin, adres siedziby, Przedstawiciel do spraw urzędowych) wraz z wynikami głosowań. |

Spis dokumentów wraz z krótkim opisem znajduje się także w
[regulaminy/README.md](regulaminy/README.md).

## Hierarchia dokumentów

1. Powszechnie obowiązujące przepisy prawa, w szczególności ustawa Prawo
   o stowarzyszeniach.
2. **Regulamin Stowarzyszenia Zwykłego** - dokument ustrojowy, odpowiednik
   statutu.
3. **Regulamin korzystania z przestrzeni** - nie może być sprzeczny
   z Regulaminem Stowarzyszenia Zwykłego; w razie sprzeczności pierwszeństwo ma
   Regulamin Stowarzyszenia Zwykłego.
4. Szczegółowe zasady wykonawcze przyjmowane uchwałami.

## Najważniejsze ustalenia ustrojowe

- Jedyną władzą Stowarzyszenia jest **Zebranie Członków** - nie ma zarządu ani
  komisji rewizyjnej (§ 12 Regulaminu Stowarzyszenia).
- Uchwały zapadają większością **co najmniej 2/3 głosów** członków obecnych
  i uprawnionych do głosowania, przy kworum wynoszącym połowę członków
  (§ 19). Zmiana Regulaminu i rozwiązanie Stowarzyszenia wymagają obecności
  co najmniej 2/3 wszystkich członków (§ 25).
- Stowarzyszenie działa przez **Przedstawicieli Stowarzyszenia** powoływanych
  do określonej sprawy albo do spraw urzędowych, wyłącznie w granicach
  umocowania nadanego uchwałą (§ 14-16).
- Członkowie odpowiadają za zobowiązania Stowarzyszenia bez ograniczeń, całym
  majątkiem, solidarnie - jest to ustawowa cecha stowarzyszenia zwykłego
  (§ 11a).
- Zebrania mogą odbywać się stacjonarnie, zdalnie albo w sposób mieszany,
  a uchwały mogą być podejmowane elektronicznie (§ 19).

Powyższe jest skrótem ułatwiającym orientację. Wiążąca jest treść samych
dokumentów.

## Zmiana dokumentów

1. Zmiana proponowana jest jako pull request, żeby można było przejrzeć
   dokładny diff.
2. Po dyskusji zmiana jest przyjmowana uchwałą Zebrania Członków, zgodnie
   z trybem właściwym dla danego dokumentu.
3. Scalenie pull requesta następuje po podjęciu uchwały. Commit powinien
   odsyłać do numeru i daty uchwały.

Historia gita nie zastępuje dokumentacji uchwał - jest jedynie zapisem
technicznym.

## Generowanie PDF

Dokumenty źródłowe są w Markdown, ale do archiwum i do urzędu potrzebny jest
PDF. Generator działa w kontenerze Dockera, więc nie wymaga niczego
zainstalowanego lokalnie poza Dockerem i daje identyczny skład na każdym
komputerze:

```bash
bin/make-pdf                                        # wszystkie dokumenty
bin/make-pdf regulaminy/regulamin-stowarzyszenia.md # jeden dokument
bin/make-pdf --html --png                           # dodatkowo podgląd HTML i PNG
bin/make-pdf --rebuild                              # wymuszenie przebudowy obrazu
```

Wynik trafia do katalogu `out/`, który jest poza kontrolą wersji - źródłem
prawdy pozostaje Markdown. Obraz przebudowuje się sam, gdy zmieni się przepis
lub styl, więc poprawka w CSS nigdy nie renderuje się ze starego obrazu.

Powstający plik jest zgodny z **PDF/A-3b**: fonty są osadzone, a dokument jest
samowystarczalny, czego wymaga długoterminowa archiwizacja. Nawigacja po
paragrafach (zakładki PDF) budowana jest automatycznie z nagłówków.

### Metadane

Każdy PDF zawiera tytuł, autora, temat, słowa kluczowe oraz daty utworzenia
i modyfikacji. Wartości wspólne dla wszystkich dokumentów są
w [tools/pdf/config.yaml](tools/pdf/config.yaml); tytuł domyślnie pochodzi
z nagłówka `#`, a data - z ostatniej zmiany pliku.

Pojedynczy dokument może nadpisać dowolne pole blokiem YAML na początku pliku:

```yaml
---
title: Uchwała nr 7 Zebrania Członków
author: Zebranie Członków Stowarzyszenia
subject: Uchwała w sprawie wysokości składek członkowskich
keywords: [uchwała, składki, 2026]
created: 2026-09-01T18:00:00+02:00
---
```

Blok jest opcjonalny - dokumenty bez niego generują się poprawnie.

### Wygląd i łamanie stron

Cały wygląd opisuje [tools/pdf/style/document.css](tools/pdf/style/document.css).
Krój pisma i stopień można zmienić dla wszystkich dokumentów naraz
w `config.yaml` (sekcja `style`), bez dotykania CSS. Wymuszony podział strony
zapisuje się w Markdownie jako `<!-- pagebreak -->`.

## Konwencje i narzędzia

Dokumenty przechodzą lint bez błędów. Cały zestaw kontroli uruchamia jedno
polecenie:

```bash
bin/lint          # sprawdzenie
bin/lint --fix    # sprawdzenie i poprawienie tego, co da się poprawić automatycznie
```

Skrypt sprawdza Markdown (markdownlint-cli2, konfiguracja
w [.markdownlint.jsonc](.markdownlint.jsonc), czytana także przez rozszerzenie
markdownlint do VS Code) oraz Pythona generatora PDF (ruff - format i lint,
konfiguracja w [ruff.toml](ruff.toml)). Obie wersje narzędzi są przypięte
w skrypcie i pobierane na żądanie przez `npx` i `uvx`, więc nic nie trzeba
instalować globalnie. Jeśli na maszynie nie ma `npx` albo `uvx`, dana część
kontroli jest pomijana z ostrzeżeniem.

Formatowanie plików opisuje [.editorconfig](.editorconfig) (UTF-8, LF, znak
końca linii na końcu pliku).

### Hooki gita

Lint może działać automatycznie przy commicie i przy pushu. Hooki są w repo,
w katalogu [.githooks/](.githooks/); po sklonowaniu wystarczy raz wskazać je
gitowi:

```bash
bin/setup-hooks
```

- `pre-commit` - poprawia i sprawdza wyłącznie pliki z indeksu. Poprawki są
  dopisywane do commita. Plik, który ma jednocześnie niezaindeksowane zmiany,
  jest tylko sprawdzany - hook nie przepisuje treści, której nie zamierzasz
  commitować.
- `pre-push` - sprawdza całe repozytorium i niczego nie zmienia.

Pominięcie jednorazowo: `git commit --no-verify`, `git push --no-verify`.
Wyłączenie na stałe: `git config --unset core.hooksPath`.

Konwencje redakcyjne:

- Tekst dokumentów po polsku, komunikaty commitów po angielsku.
- Wyłącznie znaki ASCII poza polskimi literami diakrytycznymi - dywiz `-`
  zamiast półpauzy, proste cudzysłowy `"` zamiast typograficznych. Wyjątkiem
  jest `§` oraz wielokropek `…` w polach do wypełnienia.
- Jeden akapit w jednej linii, bez twardego zawijania. Diffy pozostają wtedy
  czytelne na poziomie akapitu.
- Numeracja paragrafów i ustępów jest częścią treści prawnej - odsyłacze
  wewnątrz dokumentów (`§ 13 pkt 3`) trzeba sprawdzić przy każdej zmianie
  numeracji.

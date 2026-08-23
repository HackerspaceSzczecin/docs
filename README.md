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
| [Protokół zebrania założycielskiego](regulaminy/protokol-zebrania-zalozycielskiego.md) | Utworzenie Stowarzyszenia, uchwały nr 1-3 (regulamin, adres siedziby, Przedstawiciel do spraw urzędowych) wraz z wynikami głosowań. |

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

## Konwencje i narzędzia

Dokumenty przechodzą lint bez błędów. Konfiguracja znajduje się
w [.markdownlint.jsonc](.markdownlint.jsonc) i jest czytana zarówno przez
rozszerzenie markdownlint do VS Code, jak i przez CLI:

```bash
npx markdownlint-cli2 "**/*.md"
```

Formatowanie plików opisuje [.editorconfig](.editorconfig) (UTF-8, LF, znak
końca linii na końcu pliku).

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

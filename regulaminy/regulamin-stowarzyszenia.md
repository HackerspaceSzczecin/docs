# Poprawki regulaminu stowarzyszenia - opis zmian

## O co chodzi

Regulamin w obecnej wersji ma trzy rodzaje problemów: braki, które mogą wywołać wezwanie do uzupełnienia przy wpisie do ewidencji, wewnętrzne sprzeczności oraz dziury ustrojowe, które w praktyce blokują członkom możliwość kontrolowania Zarządu. Ten PR naprawia wszystkie trzy.

Dokument urósł z 30 do 41 paragrafów i został przeorganizowany, więc diff jest duży. Poniżej mapa zmian.

**Zastrzeżenie:** to nie jest opinia prawna. Przed złożeniem do ewidencji warto, żeby ktoś z uprawnieniami rzucił okiem, szczególnie na § 25.

---

## 1. Braki formalne, które mogły zablokować wpis

| Problem w starej wersji | Rozwiązanie |
| --- | --- |
| § 13 ust. 2 - organ kontroli wewnętrznej „którego zasady określa Regulamin", a zasad nie było | Skreślony. Nowy § 17 ust. 3 wprost stwierdza brak takiego organu i wskazuje, co go zastępuje |
| Brak kworum Zarządu - jeden obecny członek głosujący „za" podejmował uchwałę | § 24 ust. 3: co najmniej połowa składu, nie mniej niż dwie osoby |
| Brak zasad zwoływania posiedzeń Zarządu - część Zarządu mogła obradować bez reszty | § 24 ust. 1-2: zwołuje każdy członek, zawiadomienie 5 dni, tryb skrócony za zgodą wszystkich |
| § 17 ust. 1 - definicja kołowa, reprezentacja niemajątkowa nieokreślona | § 25 ust. 2-3: niemajątkowa - każdy członek Zarządu samodzielnie; majątkowa - dwóch łącznie |
| § 5 (teren = Szczecin) kontra § 8 pkt 8 (organizacje zagraniczne) | § 5: teren = Rzeczpospolita Polska, siedziba pozostaje Szczecin |
| § 24 ust. 1 - „w szczególności" przy katalogu, który ustawa zamyka | Skreślone, katalog wyliczony wprost (§ 34 ust. 1) |
| Nagłówek „Walne Zebranie" kontra „Zebranie Członków" w treści | Ujednolicone na „Zebranie Członków"; nagłówek wskazuje Zebranie Założycielskie |

---

## 2. Nowy paragraf, który jest najważniejszy w całym PR

**§ 25 - zaciąganie zobowiązań.**

Stara wersja machała ręką na przepisy o czynnościach przekraczających zwykły zarząd (§ 17 ust. 9: „przepisy mają pierwszeństwo"). W praktyce oznacza to, że Zarząd mógł w dobrej wierze podpisać umowę, która jest nieskuteczna.

Ustawa wymaga **uprzedniej zgody wszystkich członków oraz pełnomocnictwa od każdego z nich** m.in. przy: nabyciu nieruchomości, kredycie, pożyczce, poręczeniu oraz **każdym zobowiązaniu powyżej 10 000 zł**.

Nowy § 25 wprowadza trzy niezależne progi:

1. **ust. 4** - powyżej 1000 zł jednorazowo: zgoda Zebrania Członków (nasz próg wewnętrzny)
2. **ust. 8** - każde zobowiązanie cykliczne (najem, abonament): zgoda Zebrania niezależnie od kwoty
3. **ust. 9** - czynności przekraczające zwykły zarząd: zgoda wszystkich członków plus pełnomocnictwa (próg ustawowy)

Progi są kumulatywne (ust. 11) - spełnienie jednego nie zastępuje pozostałych.

Do tego trzy przepisy, które sprawiają, że próg nie jest fikcją:

- **ust. 5 - antydzielenie.** Zakup rozbity na kilka faktur wobec tego samego kontrahenta albo w ramach tego samego przedsięwzięcia w okresie 30 dni liczy się jako jedno zobowiązanie. Bez tego 4000 zł da się przepuścić jako cztery transakcje po 1000
- **ust. 6 - refundacje.** Zwrot członkowi wydatku poniesionego na rzecz Stowarzyszenia wlicza się do limitu. Bez tego wystarczy, że ktoś kupi za swoje i wystawi rachunek
- **ust. 7 - budżet roczny.** Zebranie może uchwalić limity wydatków w kategoriach; w ich granicach Zarząd działa bez odrębnych uchwał. To wentyl, który sprawia, że niski próg nie zablokuje bieżącego życia - ale nie omija wymogów z ust. 8 i 9

Plus **ust. 10**: Zarząd musi uprzedzić członków *przed* rozpoczęciem negocjacji umowy z ust. 8 lub 9, żeby nikt nie odkrył wymogu zgody wszystkich na dzień przed podpisaniem najmu.

**To jest realny koszt formy zwykłej.** Roczna umowa najmu prawie na pewno przekroczy 10 000 zł, więc przy każdej takiej umowie trzeba zebrać podpisy wszystkich członków. Przy 12 osobach wykonalne, przy 30 - nie. Argument za przejściem na KRS, gdy tylko lokal będzie wasz.

---

## 3. Dziury ustrojowe

**Zakleszczenie: Zebranie zwoływał tylko Zarząd, a tylko Zebranie mogło Zarząd odwołać.**

- § 18 ust. 2: Zwyczajne Zebranie obowiązkowo raz w roku, do 31 marca
- § 18 ust. 3-4: Nadzwyczajne na wniosek 1/3 członków, minimum pięciu; Zarząd zwołuje w 21 dni, termin nie później niż 45 dni od wniosku
- § 18 ust. 5: jeśli Zarząd nie zwoła, zwołują wnioskodawcy albo dowolnych trzech członków
- § 28 ust. 6: jeśli Zarząd przestał istnieć, Zebranie zwołuje trzech członków

**Martwa ścieżka odwoławcza.** Stara wersja dawała 14 dni na odwołanie, ale nikt nie miał obowiązku zwołać Zebrania ani terminu na rozpatrzenie. § 10 ust. 5: Zarząd przedstawia odwołanie najbliższemu Zebraniu, nie później niż w 60 dni, w razie potrzeby zwołując je w tym celu. § 15 ust. 5 dodaje skutek zawieszający - wykluczenie nie wchodzi w życie do rozpatrzenia odwołania, z wyjątkiem wstępu do przestrzeni, jeśli chodzi o bezpieczeństwo.

**Brak kworum Zebrania.** Przy 30 członkach dwie osoby mogły zmienić Regulamin. § 20: kworum 1/3, drugi termin bez kworum po 30 minutach (musi być zapowiedziany w zawiadomieniu), a przy zmianie Regulaminu i rozwiązaniu Stowarzyszenia kworum połowy bez możliwości drugiego terminu.

**Zero sprawozdawczości.** To była najpoważniejsza dziura, biorąc pod uwagę, że członkowie odpowiadają majątkiem osobistym za długi.

- § 19 ust. 1 pkt 6-7: roczne sprawozdanie z działalności i finansów plus absolutorium
- § 11 pkt 7: prawo wglądu w dokumentację finansową
- § 34 ust. 3-5: obowiązek prowadzenia ewidencji, udostępnienie sprawozdania 7 dni przed Zebraniem, na żądanie trzech członków wykaz zobowiązań w 14 dni

**Zarząd praktycznie nieusuwalny.** Kadencja skrócona z 4 lat do 2 (§ 21 ust. 6), próg odwołania obniżony z 2/3 do zwykłej większości (§ 27 ust. 2). Skoro kadencja krótka, wysoki próg nie jest już potrzebny, a razem tworzyły blokadę.

**Zawieszenie bez terminu.** § 27 ust. 3: do najbliższego Zebrania i nie dłużej niż trzy miesiące.

**Głosowania zawsze jawne.** § 30 ust. 9: tajne obowiązkowo przy wyborze i odwołaniu Zarządu, zawieszeniu członka Zarządu, wykluczeniu członka i rozpatrywaniu odwołania. Ust. 10: tajne na żądanie 1/5 obecnych.

---

## 4. Pozostałe zmiany

- **§ 2 ust. 3-4** - odpowiedzialność członków za zobowiązania Stowarzyszenia napisana wprost, plus obowiązek oświadczenia w deklaracji. Nikt nie powinien wchodzić w to nieświadomie
- **§ 8 ust. 2-3** - wprost: brak działalności gospodarczej i odpłatnej pożytku publicznego, przestrzeń dla nieczłonków nieodpłatnie
- **§ 9** - członkostwo od 18 lat, młodsi jako uczestnicy za zgodą opiekuna (patrz punkt 5 poniżej)
- **§ 13** - doprecyzowanie, że ograniczenie odpowiedzialności za szkody działa tylko wewnątrz i nie dotyka odpowiedzialności z § 2 ust. 3
- **§ 16** - zaległości składkowe: zawieszenie prawa głosu po 2 miesiącach, wykluczenie po 4; plus możliwość zawieszenia obowiązku składkowego na wniosek, do 6 miesięcy
- **§ 15 ust. 6** - osoba wykluczona może wrócić po 6 miesiącach, a przy wykluczeniu za składki po uregulowaniu zaległości
- **§ 22** - obowiązek ujawnienia bliskich relacji przed wyborem do Zarządu, zakaz stanowienia przez nie większości składu (patrz punkt 5)
- **§ 23 ust. 2** - granica między instrukcjami Zarządu a *Regulaminem korzystania z przestrzeni*: Zarząd tylko technicznie, jak obsługiwać urządzenie, bez sankcji, opłat i zasad dostępu
- **§ 28 ust. 3, 5** - kooptacja ograniczona do 1/3 składu, tryb awaryjny gdy Zarząd spadnie poniżej trzech osób
- **§ 29 ust. 5-6** - członek może wnieść sprawę do porządku obrad na 3 dni przed; zakaz uchwał spoza porządku obrad
- **§ 30 ust. 3** - głosowanie obiegowe z minimalnym oknem 72 godzin, wyłączone przy sprawach wymagających tajności
- **§ 32** - spory: termin 30 dni dla Zarządu, przejście do Zebrania przy bezczynności, prawo do przedstawienia stanowiska
- **§ 37** - obowiązek zgłoszenia organowi nadzorującemu zmiany regulaminu, składu Zarządu itd. w 7 dni
- **§ 40** - wejście w życie, pierwsza kadencja, termin 6 miesięcy na przedstawienie *Regulaminu korzystania z przestrzeni*
- Rozdział o utracie członkostwa przeniesiony sprzed rozdziału o majątku tuż za rozdział o członkostwie
- Nowy plik `deklaracja-czlonkowska.md`

---

## 5. Do decyzji na spotkaniu - wybrałem wariant, ale to nie jest przesądzone

### 5.1. Osoby bliskie w Zarządzie (§ 22)

Trzyosobowy Zarząd, w którym dwie osoby są parą, to formalnie trzy głosy, faktycznie dwa. Jedna para kontroluje organ.

**Wybrany wariant:** obowiązek ujawnienia relacji przed wyborem plus zakaz stanowienia przez osoby bliskie większości składu Zarządu.

**Konsekwencja:** przy Zarządzie trzyosobowym para musi wybrać jedno z siebie. Jeśli oboje mają być w Zarządzie, Zarząd musi liczyć pięć osób.

**Warianty alternatywne:**

- (a) sam obowiązek ujawnienia, bez zakazu - Zebranie wybiera świadomie i tyle
- (b) zakaz tylko przy Zarządzie liczącym mniej niż pięć osób
- (c) bez żadnej regulacji, zostaje ogólne wyłączenie przy konflikcie interesów z § 27 ust. 4

### 5.2. Małoletni (§ 9)

Zgoda rodzica nie przenosi na rodzica odpowiedzialności za długi Stowarzyszenia - ta obciąża członka, także szesnastoletniego.

**Wybrany wariant:** członkostwo od 18 lat, młodsi jako uczestnicy za pisemną zgodą opiekuna - wchodzą do przestrzeni na zasadach *Regulaminu korzystania z przestrzeni*, nie głosują, nie odpowiadają majątkiem.

**Wariant alternatywny:** ustawa dopuszcza członkostwo osób 16-18 z prawem wyborczym czynnym i biernym, pod warunkiem że większość Zarządu stanowią osoby o pełnej zdolności do czynności prawnych. Jeśli grupa chce tej drogi, § 9 wymaga przepisania, a deklaracja - osobnej wersji z podpisem opiekuna. Warto wtedy zapytać prawnika, bo obciążanie małoletniego solidarną odpowiedzialnością za długi organizacji to nie jest oczywista sprawa.

### 5.3. Próg 1000 zł (§ 25 ust. 4)

Próg jest celowo niski, bo Stowarzyszenie startuje bez środków i bez historii wydatków, a każde zobowiązanie bez pokrycia obciąża prywatne majątki członków. Najem i inne koszty stałe łapie osobno ust. 8, więc ust. 4 dotyczy wyłącznie zakupów jednorazowych: sprzętu, materiałów, ubezpieczenia.

Rozluźnienie ma się odbywać przez **budżet roczny z ust. 7**, a nie przez podnoszenie progu. Uchwalacie raz w roku limity w kategoriach i przez rok Zarząd działa w ich granicach bez pytania. Dzięki temu zaczynamy ciasno, a poluzowujemy wtedy, gdy znamy realne liczby, zamiast zgadywać je dziś.

Do rozważenia, gdy pojawią się pierwsze faktury: czy 30 dni w ust. 5 to właściwe okno, czy zbyt szerokie przy zakupach materiałów do jednego projektu.

### 5.4. Kworum 1/3 (§ 20 ust. 1)

Przy 12 członkach to cztery osoby. Przy 40 - czternaście, co przy realnej frekwencji może okazać się nieosiągalne. Drugi termin to zabezpiecza, ale warto o tym pomyśleć, zanim baza urośnie.

### 5.6. Odpowiedzialność byłych i nowych członków - do zapytania prawnika

Art. 40 ust. 1b stanowi, że odpowiedzialność członka **powstaje z chwilą, gdy egzekucja z majątku Stowarzyszenia okaże się bezskuteczna** - nie z chwilą zaciągnięcia zobowiązania. Ustawa mówi przy tym o „członkach", nie o osobach, które nimi były.

Rodzi to dwa pytania, na które przepisy nie dają jasnej odpowiedzi:

- **Czy wystąpienie zwalnia?** Część komentatorów uważa, że skuteczne wystąpienie przed wniesieniem powództwa przez wierzyciela powinno chronić byłego członka. Nie ma tu przepisu analogicznego do art. 10 § 3 Kodeksu spółek handlowych, który przesądzałby sprawę.
- **Czy nowy członek przejmuje stare długi?** Jeżeli odpowiedzialność powstaje przy bezskutecznej egzekucji, to osoba, która przystąpiła po zaciągnięciu zobowiązania, może zostać nim objęta. To jest ryzyko realniejsze i praktycznie nieopisywane.

**Rozwiązanie przyjęte w PR:** nie rozstrzygamy tego w regulaminie, bo nie możemy. Zamiast tego:

- § 14 ust. 3 wprost stwierdza, że kwestię rozstrzygają przepisy, nie Regulamin
- § 14 ust. 4 - występujący dostaje na żądanie zestawienie zobowiązań na dzień wystąpienia
- § 10 ust. 6 - kandydat dostaje zestawienie zobowiązań **przed** przyjęciem, wraz z pouczeniem o momencie powstania odpowiedzialności
- deklaracja opisuje obie niepewności zamiast udawać, że ich nie ma

**To jest pytanie numer jeden do prawnika**, ważniejsze niż cała reszta dokumentu. Jeśli odpowiedź brzmi „nowy członek odpowiada za stare długi", to zamyka dyskusję o pozostawaniu przy formie zwykłej dłużej niż do podpisania najmu.

### 5.5. Kadencja dwa lata (§ 21 ust. 6)

Rok oznacza wybory bez przerwy i zero ciągłości przy dłuższych sprawach, jak umowa najmu. Dwa lata przy progu odwołania obniżonym do zwykłej większości dają i stabilność, i możliwość szybkiej reakcji.

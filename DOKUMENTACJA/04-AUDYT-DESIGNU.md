# Audyt designu i poprawki — 28.10.2026

Zakres: wszystkie dokumenty witryny (`/`, `/o-firmie/`, `/oferta/` + 4 podstrony usług,
`/galeria/`, `/kontakt/`, `/polityka-prywatnosci/`, `/polityka-cookies/`,
`/obowiazek-informacyjny/`, `/404.html`), każda sekcja, szerokości 320, 360, 390, 768, 1024,
1440 i 1920 px. Strona `/tabela-cookies/` została usunięta na życzenie właściciela
(runda 3), więc witryna liczy obecnie 12 stron + 404.

Zasada: układ i treść 1:1 z projektem — poprawione zostały tylko błędy, wyrównania
i czytelność. Nie dodano sekcji, funkcji ani nowych elementów interfejsu.

---

## 1. Metoda

- pomiar DOM w prawdziwej przeglądarce (Chrome, CDP): `scrollWidth` vs `clientWidth`,
  prostokąty elementów, `getComputedStyle`, kontrast par tokenów;
- testy interakcji: ścieżka kursora nad podmenu, kliknięcia, Tab/Esc, lightbox;
- Lighthouse 13.6 (mobile i desktop, kategoria accessibility + best-practices);
- kontrola linków i zasobów: 59 linków wewnętrznych, 57 zasobów — 0 braków;
- porównanie z generatorem: `python _tools/build.py` odtwarza `site/` bajt w bajt.

## 2. Znalezione i naprawione

| # | Obszar | Problem (dowód) | Poprawka |
|---|--------|-----------------|----------|
| 1 | Nagłówek, ≥1000 px | Rozwijane podmenu „Oferta” pozycjonowało się względem `<header>`, nie względem pozycji menu: panel startował na `left: 0` (x = 0 px zamiast 1012 px), a kareta 16×16 lądowała przy prawej krawędzi ekranu (x = 1424–1440 px). | `position: relative` na `.nav__item` i `.nav__row` w `@media (min-width: 1000px)` — panel otwiera się pod „Ofertą”, kareta siedzi w linku. |
| 2 | Nagłówek, desktop | Po najechaniu na „Ofertę” panel był widoczny, ale już 2 px poniżej linku `:hover` znikał (`display: none` przy y = 60), więc nie dało się dojść kursorem do pozycji podmenu — 10 px odstępu `top: calc(100% + 10px)`. | Niewidoczny most `::before` (12 px) nad odstępem; przetestowana ścieżka kursora 56 → 130 px utrzymuje panel otwarty. |
| 3 | Nagłówek, mobile | Otwarte menu przykrywało własny pasek: `elementFromPoint(60, 30)` zwracał `NAV.nav`, więc logo i przycisk zamykania były niewidoczne i nieklikalne (zamykanie tylko klawiszem Esc). | `is-nav-open` na `.site-header` (JS) + podniesienie `.brand` i `.bar__actions` (`z-index: 130`), przezroczyste tło i jasne logo; klik w hamburger zamyka menu. Przetestowane też po przewinięciu (`is-stuck`). |
| 4 | Nawigacja, desktop | Kolor pozycji podmenu na białym panelu to `--on-dark-muted` (#9ea3a8) — kontrast **2,5:1**. | Na desktopie `--muted` (#4f5358) → **7,75:1**; hover/aktywna `--text`. |
| 5 | Atuty (`/`), 320 px | Siatka `1fr 1fr` nie mogła zejść poniżej `min-content` (311,5 px w kolumnie 280 px) → poziomy pasek przewijania: `scrollWidth 332` vs `clientWidth 320`. | Jedna kolumna poniżej 360 px (`@media (max-width: 359px)`); strona ma teraz `scrollWidth = 320`. |
| 6 | Atuty, 560–859 px | Cztery kolumny od 560 px: na 768 px na tekst zostawało ~112 px („17 lat w / branży / remontowo- / budowlanej”), na 560 px jeszcze mniej. | Przełożenie układu 4-kolumnowego do `min-width: 860px` — na 768 px jest 2×2 (353 px na komórkę), na 560 px 2×2 (258 px). |
| 7 | `/polityka-prywatnosci/`, 320 px | Długi token `budujzkaszubami.pl` w H1 wymuszał kolumnę 304 px w kontenerze 280 px; nadmiar był obcinany przez `overflow-x: hidden` (h1 `right = 324`). | `overflow-wrap: anywhere` na `.page-head .h1` + rozmiar 1.9 rem poniżej 360 px; tytuł łamie się na trzy pełne linie, bez sieroty „pl”. |
| 8 | `/tabela-cookies/`, wszystkie | Tabela 853 px w kontenerze 280 px przewija się poziomo, ale `div.table-wrap` nie miał `tabindex` ani roli — z klawiatury nie dało się jej przewinąć (WCAG 2.1.1). | `tabindex="0" role="region" aria-label="Tabela plików cookies"` w `site/` i w `_tools/legal.py`. |
| 9 | Nagłówek, desktop | Przycisk `nav__sub-toggle` (16×16) nachodził na prostokąt linku „Oferta” → Lighthouse `target-size` 0 pkt, accessibility **96**. | Na desktopie przycisk ukryty, kareta rysowana jako `::before` linku; podmenu nadal otwiera hover i `:focus-within`. Accessibility **100**. |
| 10 | Wszystkie strony | W `shell.py` emitowany był osierocony `</span>` po logo → 14/14 stron z błędem walidacji HTML. | Usunięty z `_tools/shell.py` i ze wszystkich wygenerowanych stron. |
| 11 | Narzędzia | `_tools/common.py` i `_tools/server.js` miały wpisane na sztywno ścieżki `C:\Users\KRYBAR\OneDrive - Inwido\Pulpit\Strona` — generator i serwer Brotli nie działały w tej lokalizacji. | Ścieżki liczone od położenia pliku; `python _tools/build.py` odtwarza witrynę, `node _tools/server.js` serwuje `site/`. |

### Runda 2 — uwagi właściciela (6 zrzutów)

| # | Obszar | Problem (dowód) | Poprawka |
|---|--------|-----------------|----------|
| 12 | Hero i CTA | Akcentowy przycisk na ciemnym tle po najechaniu zmieniał tło na `--ink` — dokładnie kolor tła (`rgb(12,13,15)` w pikselu przycisku), więc przycisk znikał i zostawał sam biały napis. | Na ciemnych tłach (`hero`, `section--dark`, `cta`, menu mobilne) hover przechodzi w biel z ciemnym tekstem — jak `.btn--light`; na jasnych tłach zostaje dotychczasowy hover. |
| 13 | Karty usług (`/oferta/`, `/o-firmie/`) | `.card__body` miało `padding: 1.25rem 0 0` — tytuł i opis dotykały krawędzi białej karty, a podkreślenie „Czytaj więcej” leżało na samej krawędzi karty (link kończył się 0 px od dołu). | `padding: 1.25rem 1.25rem 1.4rem`; link ma teraz 22 px oddechu od dołu karty. |
| 14 | Lista „Sprawdź, co możemy…” (`/oferta/`) | Tylko jedna pozycja („prace wykończeniowe”) była linkiem, więc jako jedyna była pogrubiona i podkreślona — lista wyglądała niekonsekwentnie. | Wszystkie cztery nazwy usług są linkami do swoich podstron w tym samym stylu. |
| 15 | `/kontakt/` | Prawy panel „Najszybszy kontakt” powielał numer telefonu i e-mail z sekcji „Dane kontaktowe” powyżej (decyzja właściciela: zbędny). | Panel usunięty wraz z martwym CSS (`.call-card*`, `.split--top`); trzy osoby odpowiedzialne ułożone w trzech kolumnach na pełnej szerokości. |
| 16 | Link `link-arrow` | Podkreślenie akcentem leżało ~7 px pod tekstem (wysokość linii 1,4 + `padding-bottom`), przez co wyglądało jak osobna kreska oderwana od linku. | `line-height: 1.25` — linia przylega do tekstu (ok. 3 px), spójnie we wszystkich odnośnikach ze strzałką. |

### Runda 3 — kolejne uwagi właściciela

| # | Obszar | Problem / decyzja | Poprawka |
|---|--------|-------------------|----------|
| 17 | „Dane kontaktowe” (`/kontakt/`) | Blok wyglądał jak niedomknięta tabela: górna i dolna linia, dwa piony i dwie puste komórki; po usunięciu panelu był wizualnie identyczny z listą osób poniżej, choć pełni inną rolę. | Wydzielony kafel: tło `--soft`, padding `clamp(1.5rem,3vw,2.25rem)`, nagłówek wewnątrz, brak linii między kolumnami; lista osób poniżej zostaje na białym tle z cienkimi liniami. Trzy kolumny od 860 px, na mobile stos. |
| 18 | `/tabela-cookies/` | Decyzja właściciela: strona zbędna. | Usunięta strona, wpis w stopce (13 plików HTML), pozycja w `sitemap.xml`, blok w generatorze (`build.py`, `legal.py`, `common.py`); zdanie w Polityce Cookies przepisane bez odwołania do tabeli; 301 na `/polityka-cookies/` w `_redirects` i `vercel.json`. |
| 19 | `/galeria/` | Decyzja właściciela: usunąć podpowiedź „Kliknij zdjęcie…”. | Usunięty akapit wraz z pustym kontenerem `.prose` i martwym CSS `.gallery__hint`; galeria startuje bezpośrednio po nagłówku strony. |
| 20 | Mapa (`/kontakt/`) | Decyzja właściciela: mapa ma być widoczna bez klikania w guzik. | Osadzona od razu przez OpenStreetMap (`loading="lazy"`, tytuł opisowy, pinezka na ul. Długiej 127); po czystym odświeżeniu strony **0 plików cookie**, więc nie trzeba banera zgody. Pod mapą pozostaje odnośnik „Otwórz w Mapach Google”. Na telefonie kadr 4:3, na desktopie 16:6. |

### Runda 4 — ładowanie zdjęć

| # | Obszar | Problem / decyzja | Poprawka |
|---|--------|-------------------|----------|
| 21 | Obrazy (`loading="lazy"`) | Natywne lazy w Chrome odkłada żądanie o ~0,9 s po wejściu obrazu w kadr (pomiar CDP: obraz widoczny w 739 ms, żądanie dopiero w 1654 ms, mimo że plik 32 KB pobiera się 34 ms). Efekt: „doczytywanie” przy przewijaniu. | Skrypt podnosi obraz do `loading="eager"`, gdy jest ~400 px przed viewportem (bez JS zostaje natywny lazy), a pierwsze 4 zdjęcia galerii mają `fetchpriority="high"`. Po zmianie żądanie startuje 250–330 ms **przed** wejściem w kadr. Lighthouse galeria: 0,92 / LCP 3,0 s (przed 0,92 / 3,4 s), strona główna 100 / LCP 1,5 s. |


## 3. Zweryfikowane jako poprawne

- Brak poziomego przewijania na 13 dokumentach × 7 szerokościach (320–1920 px).
- Kontrast tokenów: `--muted` 7,75:1, `--muted-2` 5,7:1 (na `--soft` 5,12:1),
  `--on-dark-muted` na `--ink` 7,65:1, akcent na ciemnym tle 5,12:1; akcent jako tekst
  występuje wyłącznie w liczbach 86 px (próg 3:1).
- Menu mobilne: blokada przewijania, `aria-expanded`, Esc zamyka i wraca fokus.
- Lightbox: 41 zdjęć, fokus na „zamknij”, strzałki, Esc, powrót fokusu, swipe.
- Bez JavaScriptu: treść widoczna (0 elementów ukrytych klasą `reveal`), podmenu na miejscu.
- `prefers-reduced-motion`: animacje i liczniki wyłączone, wartości końcowe.
- Linki wewnętrzne i zasoby: 0 braków; 0 złamanych obrazów.
- Mapa (`/kontakt/`) po czystym wczytaniu: `Network.getAllCookies` = **[]** — osadzenie
  OpenStreetMap nie zapisuje żadnego pliku cookie, więc brak banera zgody pozostaje zasadny.
- Lighthouse (strona główna i `/kontakt/`): accessibility **100**, best-practices **100**,
  SEO **100**;
  desktop performance **100**. Mobile 98 na serwerze `python -m http.server`
  (bez kompresji, LCP 2,3 s) — wynik referencyjny 100 pochodzi z serwera Brotli
  (`node _tools/server.js`), patrz `03-RAPORT-TESTOW.md`.

## 4. Świadomie niezmienione

- Etykieta „Zobacz realizacje” przy krawędzi zdjęcia hero — tak w projekcie źródłowym.
- Osadzenie mapy dopiero po kliknięciu (polityka prywatności) — bez zmian.
- Brak filtra kategorii w galerii, brak banera cookies, brak formularza — zgodnie z decyzjami projektu.
- Układ 4-kolumnowy paska statystyk hero od 560 px — mieści się i nie powoduje przepełnień
  (na 560 px najdłuższe pole łamie się na dwie linie); zostawiony bez zmian, aby nie przebudowywać hero.
- Ostatni, pojedynczy kafelek galerii (41 zdjęć w siatce 4-kolumnowej) — naturalna konsekwencja liczby zdjęć.

## 5. Jak powtórzyć

```powershell
cd "D:\Projekty\Buduj z kaszubami"
node _tools/server.js 8900          # serwer z Brotli i nagłówkami cache
npx lighthouse http://127.0.0.1:8900/ --chrome-flags="--headless=new"
npx lighthouse http://127.0.0.1:8900/ --preset=desktop --chrome-flags="--headless=new"
```

Kopie plików sprzed zmian: `_backup/2026-10-28/`.

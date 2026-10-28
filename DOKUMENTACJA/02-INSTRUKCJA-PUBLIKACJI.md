# Instrukcja publikacji i edycji


## 0. Podgląd lokalny (zanim cokolwiek wgrasz)

**Nie otwieraj `index.html` podwójnym kliknięciem.** Witryna używa adresów
względem katalogu głównego domeny (`/assets/...`), więc przy otwarciu z dysku
przeglądarka szuka plików w `C:\assets\` — strona pokaże się bez stylów i zdjęć.

Zamiast tego:

1. Kliknij dwukrotnie **`PODGLAD.cmd`** (leży obok katalogu `site/`).
2. Otworzy się przeglądarka pod adresem `http://localhost:8080/`.
3. Podgląd działa bez instalowania Pythona, Node.js ani niczego innego —
   serwer jest napisany w PowerShellu (jest w każdym Windowsie).
4. Zatrzymanie: `Ctrl + C` w oknie konsoli lub zamknięcie okna.

Jeśli strona została i tak otwarta z pliku, na górze pojawi się żółty pasek
z przypomnieniem — to nie błąd witryny.

---

## 1. Co wysłać na serwer

Katalogiem publikacji jest **`site/`**. Wgraj jego **całą zawartość** do katalogu
głównego domeny (`public_html`, `www` itp.):

```
site/
├── index.html
├── o-firmie/index.html
├── oferta/index.html
├── oferta/uslugi-budowlane/index.html
├── oferta/uslugi-wykonczeniowe/index.html
├── oferta/uslugi-remontowe/index.html
├── oferta/uslugi-koparko-ladowarka/index.html
├── galeria/index.html
├── kontakt/index.html
├── polityka-prywatnosci/index.html
├── polityka-cookies/index.html
├── obowiazek-informacyjny/index.html
├── tabela-cookies/index.html
├── 404.html
├── robots.txt
├── sitemap.xml
├── .htaccess            ← Apache (większość polskich hostingów)
├── _headers             ← Netlify / Cloudflare Pages
├── _redirects           ← Netlify / Cloudflare Pages
├── vercel.json          ← Vercel
└── assets/
    ├── css/main.css
    ├── js/site.js
    ├── fonts/archivo-var.woff2
    └── img/  (357 plików: logo, ikony, zdjęcia w AVIF i WebP)
```

Ważne:
- plik `.htaccess` zaczyna się kropką — w kliencie FTP włącz „pokaż pliki ukryte”;
- nie zmieniaj struktury katalogów — adresy podstron zależą od plików `index.html`;
- pliki `_headers`, `_redirects`, `vercel.json` są ignorowane przez Apache i odwrotnie.

## 2. Wymagania hostingu

| Element | Wymóg |
|---|---|
| Serwer | Apache 2.4+ z `.htaccess` (mod_rewrite, mod_headers, mod_deflate, mod_expires) **lub** Netlify / Cloudflare Pages / Vercel |
| HTTPS | certyfikat SSL (Let's Encrypt) — bez niego nie ma HSTS ani poprawnego SEO |
| PHP / baza | **nie są potrzebne** — witryna jest w pełni statyczna |
| Kompresja | Brotli lub Gzip (`.htaccess` włącza ją, jeśli moduł jest dostępny) |
| Node.js | niepotrzebny do działania strony |

## 3. Wdrożenie krok po kroku

1. **Kopia zapasowa** obecnej witryny (pliki + baza Joomla) — na wypadek decyzji o powrocie.
2. Wgraj zawartość `site/` do katalogu głównego.
3. Sprawdź, czy `https://budujzkaszubami.pl/` otwiera się bez `index.php`.
4. Sprawdź przekierowania: `https://budujzkaszubami.pl/o-firmie` powinno zwrócić
   **301** na `https://budujzkaszubami.pl/o-firmie/`.
5. Sprawdź `https://budujzkaszubami.pl/sitemap.xml` i `/robots.txt` (HTTP 200).
6. Wgraj `sitemap.xml` w Google Search Console i zgłoś zmianę adresów
   („Zmiana adresu witryny” nie jest potrzebna — domena bez zmian; wystarczy
   ponowne przesłanie mapy).
7. Po 2–3 dniach sprawdź w Search Console raport „Indeksowanie stron”.

## 4. Kontakt — bez formularza

Strona nie zawiera formularza kontaktowego. Klient kontaktuje się wyłącznie
telefonicznie lub e-mailem — bezpośrednio z osobą odpowiedzialną za dany zakres:

| Zakres | Osoba | Telefon |
|---|---|---|
| Płyty fundamentowe i budowa domów | Mateusz | 609 630 625 |
| Elewacja i roboty wykończeniowe | Tadeusz | 691 858 193 |
| Usługi koparką | Piotr | 609 518 723 |

Wszystkie odnośniki `tel:` i `mailto:` działają bez dodatkowej konfiguracji —
na komputerze otwierają program pocztowy lub komunikator, na telefonie
uruchamiają połączenie. **Nie ma tu żadnej usługi zewnętrznej ani klucza API.**

Strona `/kontakt/` zawiera kartę „Najszybszy kontakt” z głównym numerem
telefonu, listę osób, dane adresowe oraz mapę wczytywaną po kliknięciu.

## 5. Jak edytować treść

Strona jest statyczna, więc treść zmienia się w plikach HTML:

| Co chcesz zmienić | Plik |
|---|---|
| Telefon, e-mail, adres w stopce | `index.html` oraz wszystkie `*/index.html` (sekcja `<footer>`) |
| Treść strony głównej | `index.html` |
| Opis usługi | `oferta/uslugi-*/index.html` |
| Zdjęcia w galerii | `galeria/index.html` + pliki w `assets/img/` |
| Dokumenty prawne | `polityka-*/index.html`, `obowiazek-informacyjny/index.html`, `tabela-cookies/index.html` |
| Tytuł/opis SEO | `<title>` i `<meta name="description">` w `<head>` danej strony |
| Kolory i typografia | `assets/css/main.css` — sekcja `:root` (na górze pliku) |

**Dodanie zdjęcia do galerii**

Przygotuj **jeden plik WebP** (np. w [squoosh.app](https://squoosh.app/)) o szerokości
ok. 800 px i wrzuć go do `assets/img/`, np. `assets/img/moje-zdjecie.webp`.
W `galeria/index.html` skopiuj istniejący blok `<figure class="gallery__item">`
i podmień: `src`, `href`, `data-full` (wszystkie trzy na tę samą nazwę pliku),
`alt`, `width`/`height`, `data-w`/`data-h` oraz licznik w `aria-label`.

**Ważne po każdej zmianie plików w `assets/`:** zmień nazwę pliku (np. dopisz
`-v2`) — pliki mają cache na rok.

## 6. Alternatywa: generator treści

W katalogu `_tools/` (poza katalogiem publikacji) leżą skrypty, którymi witryna
została wygenerowana:

```
_tools/
├── common.py      konfiguracja (telefony, e-mail, adres, nawigacja), helpery obrazów
├── shell.py       <head>, nagłówek, nawigacja, stopka
├── pages.py       treść strony głównej, /o-firmie, /oferta i 4 podstron usług
├── pages_more.py  galeria (41 zdjęć), kontakt, 404, podziękowanie
├── legal.py       dokumenty prawne + tabela cookies
├── build.py       generator → zapisuje HTML, sitemap.xml i robots.txt
└── images.py      przetwarzanie zdjęć źródłowych na AVIF/WebP (wymaga Pillow)
```

Użycie (Python 3.10+ z Pillow):

```powershell
cd _tools
python build.py
```

Generator nadpisuje pliki HTML w `site/`. Edycja treści w `pages*.py` jest
wygodniejsza przy większych zmianach (jeden telefon aktualizuje się wszędzie).
Jeśli nie chcesz używać Pythona — edytuj bezpośrednio pliki HTML, są kompletne
i samodzielne.

## 7. Publikacja na Netlify / Cloudflare Pages

1. Nowa strona → „Deploy manually” → przeciągnij katalog `site/`.
2. Katalog publikacji: `site` (bez kroku budowania).
3. Pliki `_headers` i `_redirects` zadziałają automatycznie.
4. Podłącz domenę i włącz „Force HTTPS”.

## 8. Po wdrożeniu — checklista

- [ ] HTTPS działa, `http://` przekierowuje na `https://`
- [ ] `www` przekierowuje na wersję bez `www`
- [ ] `/o-firmie` → 301 → `/o-firmie/`
- [ ] `/index.php` → 301 → `/`
- [ ] `sitemap.xml` i `robots.txt` zwracają 200
- [ ] wszystkie numery telefonów i adres e-mail są klikalne
- [ ] mapa ładuje się po kliknięciu „Pokaż mapę”
- [ ] galeria: lightbox, strzałki, Esc
- [ ] menu mobilne otwiera się i zamyka
- [ ] PageSpeed Insights ≥ 95/100 na mobile i desktop

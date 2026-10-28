# Inwentaryzacja starej witryny i tabela migracji

**Domena:** https://budujzkaszubami.pl/
**Data analizy:** 28.10.2026
**Zakres:** wszystkie podstrony osiągalne z menu, stopki i odnośników w treści (13 adresów + strona błędu).

---

## 1. Struktura nawigacji (stan pierwotny)

```
Strona główna        /
O firmie             /o-firmie
Oferta               /oferta
  ├─ Usługi budowlane            /oferta/uslugi-budowlane
  ├─ Usługi wykończeniowe        /oferta/uslugi-wykonczeniowe
  ├─ Usługi remontowe            /oferta/uslugi-remontowe
  └─ Usługi koparko-ładowarką    /oferta/uslugi-koparko-ladowarka
Galeria              /galeria
Kontakt              /kontakt

Stopka: powyższe + Polityka prywatności, Polityka Cookies, Obowiązek informacyjny
Polityka Cookies → odnośnik do /tabela-cookies (strona poza menu)
```

Strona działała na Joomla (SEO-friendly URL-e bez ukośnika na końcu), serwis produkcyjny
agencji WeNet. Brak wersji angielskiej. Brak sklepu, logowania i wyszukiwarki.

---

## 2. Inwentaryzacja podstron

| # | Adres | Tytuł `<title>` | Najważniejsze treści |
|---|-------|-----------------|----------------------|
| 1 | `/` | Firma Ogólnobudowlana Mateusz Drawc w woj. pomorskim, Linia | 2 slajdy (wykończenia, budowa), 4 atuty (Jakość, Doświadczenie, Zaangażowanie, Terminowość), akapit o firmie, 4 kafle oferty, liczniki 17 / 100%, CTA |
| 2 | `/o-firmie` | O Firmie Ogólnobudowlanej Mateusz Drawc – Linia: poznaj nas | 2 akapity (lokalizacja, 17 lat, setki projektów, podwykonawca PARATI), sekcja „Ekipa remontowo-budowlana godna zaufania”, zdjęcie paralaksy |
| 3 | `/oferta` | Usługi remontowo-budowlane: profesjonalnie, rzetelnie i terminowo | akapit wprowadzający, lista 4 usług, sekcja „Stawiamy na jakość”, 4 kafle |
| 4 | `/oferta/uslugi-budowlane` | Usługi budowlane: fundamenty, szpachlowanie, murowanie | lista 8 prac, sekcja „Domy w stanie surowym i pod klucz”, telefon Mateusza |
| 5 | `/oferta/uslugi-wykonczeniowe` | Usługi wykończeniowe mieszkań, domów, lokali użytkowych | akapit, sekcja „Co obejmują prace wykończeniowe?” + lista 11 prac, „Domy i mieszkania pod klucz”, telefon Tadeusza |
| 6 | `/oferta/uslugi-remontowe` | Usługi remontowe w mieszkaniach, domach i obiektach biurowych | lista 9 prac, „Prace remontowe mieszkań, domów i biur”, telefon Tadeusza |
| 7 | `/oferta/uslugi-koparko-ladowarka` | Usługi koparko-ładowarką – kompleksowa obsługa robót ziemnych | 2 akapity, lista 4 prac, telefon Piotra |
| 8 | `/galeria` | Galeria – zdjęcia związane z naszą codzienną działalnością | 41 zdjęć w jednej galerii (Joomla, lightbox), miniatury + pliki pełne |
| 9 | `/kontakt` | Kontakt z Firmą Ogólnobudowlaną - Mateusz Drawc, Linia | adres, e-mail, 3 kontakty bezpośrednie (Mateusz, Tadeusz, Piotr) — **bez formularza** |
| 10 | `/polityka-prywatnosci` | Polityka prywatności | pełny tekst RODO, 4 sekcje, data 13.02.2026 |
| 11 | `/polityka-cookies` | Polityka Cookies | pełny tekst, 4 sekcje, instrukcje dla 5 przeglądarek + 6 linków zewnętrznych |
| 12 | `/obowiazek-informacyjny` | Obowiązek informacyjny | pełny tekst, podstawy prawne, okres przechowywania |
| 13 | `/tabela-cookies` | Tabela Cookies | tabela 12 plików cookie (nazwa, kategoria, rodzaj, źródło, czas, opis) |

---

## 3. Materiały graficzne (zachowane w 100%)

| Zasób | Liczba | Wykorzystanie w nowym serwisie |
|-------|--------|-------------------------------|
| Zdjęcia galerii | **41** | `/galeria/` — pełna siatka + lightbox (bez zmian w kolejności) |
| Zdjęcia oferty (pionowe) | 4 | kafle oferty: `/oferta/`, `/o-firmie/` |
| Zdjęcia oferty (poziome) | 4 | kafle na stronie głównej (wycofane — patrz §6) |
| Slajdy (1920×600) | 2 | pasek hero + blok „Prace wykończeniowe” |
| Zdjęcie paralaksy | 1 | `/o-firmie/` — sekcja „Jak pracujemy” |
| Kolaż „o nas” | 1 | strona główna — sekcja „O firmie” |
| Zdjęcia treści usług | 4 | bloki na podstronach usług |
| Ikony (telefon, mail, pinezka) | 3 | zastąpione ikonami SVG (wektorowymi) |
| Logo | 1 | **oryginalne** — patrz §5 |

Każde zdjęcie to **jeden plik WebP** o szerokości dobranej do roli (galeria 450–800 px,
kafle 768 px, duże kadry do 1400 px), z jawnymi wymiarami `width`/`height`.
Przeglądarka sama skaluje obraz do rozmiaru na ekranie — nie ma wariantów
`-400`, `-768` itd.

---

## 4. Dane kontaktowe, linki zewnętrzne, profile

**Dane firmy**
- Firma Ogólnobudowlana Mateusz Drawc
- ul. Długa 127, 84-223 Linia (pomorskie)
- NIP 5882211060, REGON 367068433
- e-mail: `mateo-drawc@wp.pl` (w starym serwisie ukryty przez JavaScript — odkodowany z atrybutów `joomla-hidden-mail`)
- tel. 609 630 625 (Mateusz), 691 858 193 (Tadeusz), 609 518 723 (Piotr)

**Linki zewnętrzne w starym serwisie:** 9 — wyłącznie w Polityce Cookies
(Google, Meta/Facebook, wsparcie przeglądarek) + link do Map Google w stopce
(nowy serwis). Wszystkie zachowane.

**Profile społecznościowe:** brak jakichkolwiek odnośników do Facebooka,
Instagrama, Google Business Profile itp. — nie dodano żadnych.

---

## 5. Logo

Plik źródłowy: `/images/design/logo.webp` — 170×90 px, czarny wordmark
„Buduj z Kaszubami” z dachem nad literą „u”, przezroczyste tło, obszar treści 162×29 px.

Aby logo było ostre na ekranach Retina bez rozmycia, zostało **zwektoryzowane**
z oryginalnego pliku (potrace, próg 50%). Kształt liter, dach i proporcje są
identyczne — zmieniła się tylko technika zapisu (bitmapa → SVG).
Pliki: `assets/img/logo.svg` (wersja ciemna), `assets/img/logo-light.svg` (na ciemne tło).

Nie powstał żaden nowy znak graficzny. Favicon (`assets/img/favicon.svg`) to
uproszczony motyw dachu z logo — dodatek techniczny, nie zmiana identyfikacji.

---

## 6. Tabela migracji

Status „✅ zweryfikowane” = treść i pliki porównane ze stanem źródłowym.

| Stary adres | Nowy adres | Przenoszone treści i materiały | Status |
|---|---|---|---|
| `/` | `/` | 2 slajdy → bloki „Prace wykończeniowe” i „Prace budowlane”; 4 atuty; akapit o firmie; 4 usługi (lista + kafle); liczniki 17 / 100%; CTA | ✅ |
| `/o-firmie` | `/o-firmie/` | oba akapity, sekcja „Ekipa…”, zdjęcie paralaksy, 4 fakty (17 lat, setki projektów, cała Polska, PARATI) | ✅ |
| `/oferta` | `/oferta/` | akapit, lista 4 usług, „Stawiamy na jakość”, 4 kafle z tymi samymi zdjęciami | ✅ |
| `/oferta/uslugi-budowlane` | `/oferta/uslugi-budowlane/` | 8 pozycji listy, 2 sekcje, telefon Mateusza | ✅ |
| `/oferta/uslugi-wykonczeniowe` | `/oferta/uslugi-wykonczeniowe/` | 11 pozycji listy, 2 sekcje, telefon Tadeusza | ✅ |
| `/oferta/uslugi-remontowe` | `/oferta/uslugi-remontowe/` | 9 pozycji listy, 2 sekcje, telefon Tadeusza | ✅ |
| `/oferta/uslugi-koparko-ladowarka` | `/oferta/uslugi-koparko-ladowarka/` | 2 akapity, 4 pozycje listy, telefon Piotra | ✅ |
| `/galeria` | `/galeria/` | wszystkie 41 zdjęć, lightbox, opisy alternatywne | ✅ |
| `/kontakt` | `/kontakt/` | adres, e-mail, 3 kontakty bezpośrednie, karta „Najszybszy kontakt”, mapa (na żądanie) | ✅ |
| `/polityka-prywatnosci` | `/polityka-prywatnosci/` | pełny tekst, 4 sekcje, data 13.02.2026 | ✅ |
| `/polityka-cookies` | `/polityka-cookies/` | pełny tekst, 4 sekcje, 5 przeglądarek, 6 linków zewnętrznych | ✅ |
| `/obowiazek-informacyjny` | `/obowiazek-informacyjny/` | pełny tekst | ✅ |
| `/tabela-cookies` | `/tabela-cookies/` | tabela 12 wierszy | ✅ |
| `index.php` (Joomla) | `/` | — | ✅ 301 |
| — | `/404.html` | nowa strona błędu | ➕ nowe |

**Uwaga o adresach:** ścieżki pozostały identyczne. Jedyna zmiana techniczna to
dodanie ukośnika na końcu (`/o-firmie` → `/o-firmie/`), wymuszone przez model
katalogowy `index.html` — działa na każdym hostingu statycznym. Wejście na stary
adres bez ukośnika zwraca **301** na wersję kanoniczną (reguła 1c w `.htaccess`,
plik `_redirects` dla Netlify/Cloudflare). Treść, tytuły i opisy pozostały bez zmian.

---

## 7. Czego w starym serwisie nie było / co wymaga uwagi

Poniższe punkty to **rzeczywiste braki**, a nie elementy pominięte przy migracji:

1. **`sitemap.xml` nie działał** — adres z `robots.txt`
   (`/index.php?option=com_osmap&view=…`) zwracał **HTTP 500**. Nowa mapa witryny
   jest statyczna i poprawna.
2. **Brak formularza kontaktowego** — i tak zostaje. W starym serwisie kontakt
   odbywał się wyłącznie telefonem i e-mailem; nowa witryna zachowuje ten model.
   Nie ma żadnej usługi zewnętrznej, klucza API ani ryzyka fałszywego „wysłano”.
3. **Brak profili społecznościowych** — nie dodano żadnych.
4. **Brak cen, certyfikatów, referencji i opinii** — nie dodano żadnych.
5. **Baner cookies.** Stary serwis korzystał z Google Analytics, Meta Pixel i
   reCAPTCHA (potwierdza to Tabela Cookies). Nowa witryna **nie zawiera żadnych
   skryptów zewnętrznych ani analityki** — nie ma więc potrzeby banera zgód.
   Teksty Polityki Cookies i Tabeli Cookies przeniesiono **dosłownie**, dlatego
   opisują pliki cookie, których nowa strona nie ustawia. **Wymagana decyzja
   właściciela:** zaktualizować dokumenty albo świadomie zostawić je bez zmian.
6. **Stopka:** usunięto kredyt agencji „WeNet” (element systemu CMS, nie treść
   firmy). Zachowano własną notę o prawach autorskich © 2026.
7. **Godziny otwarcia, NIP/REGON w stopce, dane do faktury, dojazd** — brak w
   starym serwisie, nie dodano.

---

## 8. Metadane SEO — stan przed i po

| Strona | Title (zachowany) | Description |
|---|---|---|
| `/` | Firma Ogólnobudowlana Mateusz Drawc w woj. pomorskim, Linia | zachowany |
| `/o-firmie` | O Firmie Ogólnobudowlanej Mateusz Drawc – Linia: poznaj nas | zachowany |
| `/oferta` | Usługi remontowo-budowlane: profesjonalnie, rzetelnie i terminowo | zachowany |
| 4 podstrony usług | bez zmian | zachowane |
| `/galeria` | Galeria – zdjęcia związane z naszą codzienną działalnością | zachowany |
| `/kontakt` | Kontakt z Firmą Ogólnobudowlaną - Mateusz Drawc, Linia | zachowany |
| 4 strony prawne | brak opisu w starym serwisie | **dodane** (krótkie, rzeczowe) |

Dodane w nowym serwisie: Open Graph + Twitter Card, dane strukturalne
`schema.org` (GeneralContractor, WebSite, BreadcrumbList, Service, ContactPage),
favicon SVG + Apple Touch Icon, strona 404, `robots.txt`, `sitemap.xml`.
Nie dodano `aggregateRating` ani żadnych wymyślonych danych.

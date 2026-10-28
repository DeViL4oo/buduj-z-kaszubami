# Raport z testów

**Data:** 28.10.2026
**Środowisko:** Windows 11, Google Chrome (headless), serwer lokalny z kompresją Brotli
i nagłówkami cache (odwzorowanie hostingu produkcyjnego).
**Adres testowy:** `http://127.0.0.1:8900/` — kopia katalogu `site/`.
**Uwaga:** wyniki pochodzą z pomiarów laboratoryjnych (Lighthouse), a nie z danych
rzeczywistych użytkowników (CrUX). Po publikacji należy je potwierdzić w PageSpeed
Insights dla adresu `https://budujzkaszubami.pl/`.

---

## 1. Lighthouse — strona główna

| Kategoria | Mobile | Desktop |
|---|---|---|
| **Performance** | **100** | **100** |
| **Accessibility** | **100** | **100** |
| **Best Practices** | **100** | **100** |
| **SEO** | **100** | **100** |

### Core Web Vitals (laboratoryjnie)

| Metryka | Mobile | Desktop | Cel |
|---|---|---|---|
| LCP | **1,4 s** | **0,4 s** | ≤ 2,5 s ✅ |
| CLS | **0** | **0** | ≤ 0,1 ✅ |
| TBT (proxy INP) | **0 ms** | **0 ms** | ≤ 200 ms ✅ |
| FCP | 0,8 s | 0,2 s | — |
| Speed Index | 0,8 s | 0,2 s | — |
| TTI | 1,5 s | 0,4 s | — |

## 2. Lighthouse — podstrony

| Strona | Perf. | A11y | Best Pr. | SEO |
|---|---|---|---|---|
| `/galeria/` | 99–100 | 100 | 100 | 100 |
| `/kontakt/` | 100 | 100 | 100 | 100 |
| `/oferta/uslugi-wykonczeniowe/` | 100 | 100 | 100 | 100 |
| `/polityka-cookies/` | 100 | 100 | 100 | 100 |

## 3. Testy funkcjonalne (Puppeteer, 26/26 zaliczonych)

**Nawigacja mobilna**
- ✅ menu ukryte przed kliknięciem (`visibility: hidden`), niedostępne dla Tab
- ✅ otwiera się po kliknięciu, `aria-expanded="true"`, blokada przewijania tła
- ✅ podmenu „Oferta” rozwija się i zwija
- ✅ `Esc` zamyka menu i przywraca fokus na przycisk

**Galeria i lightbox**
- ✅ 41 zdjęć, licznik „1 / 41”
- ✅ otwarcie, fokus na przycisku zamknięcia, `aria-modal`
- ✅ strzałki ← →, zawijanie na krańcach
- ✅ `Esc` zamyka, przywraca przewijanie i fokus na miniaturę
- ✅ każde zdjęcie ma opis alternatywny (> 10 znaków)

**Kontakt**
- ✅ wszystkie numery `tel:` i adresy `mailto:` poprawne
- ✅ karta „Najszybszy kontakt” z głównym numerem
- ✅ brak formularza — brak jakiegokolwiek ryzyka fałszywego „wysłano”

**Mapa**
- ✅ osadzona od razu (OpenStreetMap, `loading="lazy"`, tytuł opisowy), bez klikania w guzik
- ✅ po odświeżeniu strony liczba plików cookie w przeglądarce: **0** (OpenStreetMap nie ustawia cookies)
- ✅ „Otwórz w Mapach Google” pozostaje zwykłym odnośnikiem (bez osadzania Google)

**Dostępność**
- ✅ pierwszy `Tab` trafia na „Przejdź do treści”
- ✅ widoczny fokus (`outline: 3px`)

## 4. Pozostałe sprawdzenia

| Test | Wynik |
|---|---|
| Linki wewnętrzne (76) i zasoby | **0 braków** |
| Linki zewnętrzne | 9, wszystkie zachowane z oryginału |
| Błędy w konsoli | **0** |
| Nieudane żądania sieciowe | **0** |
| Przepełnienie w poziomie (390 / 1440 px) | **0** |
| Złamane obrazy | **0** |
| Kodowanie | UTF-8 bez BOM, `lang="pl"` |
| Treść bez JavaScriptu | pełna (3 321 znaków na stronie głównej, nawigacja widoczna) |
| `prefers-reduced-motion` | wyłącza animacje, marquee i przejścia |
| Kontrast tekstu | AAA/AA — 0 błędów w Lighthouse |
| Tytuły i opisy stron | indywidualne, 12/12 |
| Dane strukturalne | JSON-LD poprawny (bez wymyślonych ocen) |

## 5. Waga zasobów

| Zasób | Rozmiar |
|---|---|
| `index.html` | 25,9 KB (≈ 6 KB po Brotli) |
| `assets/css/main.css` | 47,5 KB (**8,3 KB po Brotli**) |
| `assets/js/site.js` | 13,2 KB (≈ 4 KB po Brotli) |
| `archivo-var.woff2` (krój zmienny 100–900, subset PL) | 44,7 KB |
| Obraz hero (WebP 1400) | 60,8 KB |
| Logo SVG | 17,3 KB |
| Cała witryna (13 stron + 68 zdjęć, po jednym pliku) | 3,4 MB |

Liczba żądań przy pierwszym wczytaniu strony głównej: **HTML + CSS + JS + font + 1 zdjęcie + 3 SVG**.
Każde zdjęcie ma dokładnie jeden plik — bez `srcset` i wariantów szerokości.
Zero zewnętrznych widżetów, analityki i fontów z CDN.

## 6. Co celowo NIE zostało zrobione

- **Brak banera cookies** — witryna nie ustawia plików cookie analitycznych ani
  marketingowych (brak GA, Meta Pixel, reCAPTCHA). Baner byłby zbędnym obciążeniem.
  Wymaga to jednak przeglądu dokumentów prawnych — patrz `01-MIGRACJA.md` §7.
- **Brak danych rzeczywistych (CrUX)** — strona nie była jeszcze opublikowana,
  więc nie istnieją dane terenowe. Wynik 95–100 trzeba potwierdzić po wdrożeniu.
- **Render-blocking CSS** (oszczędność ok. 120 ms wg Lighthouse) — świadoma decyzja:
  jeden mały plik CSS (8 KB po Brotli) jest lepszy niż wstawianie krytycznego CSS
  do 15 dokumentów (gorsze cache'owanie, większy HTML). Wynik Performance = 100.

## 7. Jak powtórzyć pomiary

```powershell
# serwer z kompresją Brotli (odwzorowanie produkcji)
node _tools/server.js          # lub: python -m http.server w katalogu site/

# Lighthouse (mobile)
npx lighthouse http://127.0.0.1:8900/ --chrome-flags="--headless=new"

# Lighthouse (desktop)
npx lighthouse http://127.0.0.1:8900/ --preset=desktop --chrome-flags="--headless=new"
```

Po publikacji: <https://pagespeed.web.dev/analysis?url=https://budujzkaszubami.pl/>

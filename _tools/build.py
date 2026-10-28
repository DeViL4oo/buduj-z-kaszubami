# -*- coding: utf-8 -*-
"""Generator statycznej witryny budujzkaszubami.pl"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
from common import *
import pages
import pages_more
import legal
from pages import crumb

TODAY = "2026-10-28"

# ---------------------------------------------------------------------
# Nawigacja
# ---------------------------------------------------------------------
from shell import head_html, header_html, footer_html, nav_html, document


# ---------------------------------------------------------------------
# Dane strukturalne
# ---------------------------------------------------------------------
ORG = {
    "@type": "GeneralContractor",
    "@id": f"{BASE}/#organizacja",
    "name": FIRMA,
    "alternateName": "Buduj z Kaszubami",
    "url": f"{BASE}/",
    "logo": f"{BASE}/assets/img/icon-512.png",
    "image": f"{BASE}/assets/img/og-image.jpg",
    "telephone": "+48 609 630 625",
    "email": EMAIL,
    "taxID": NIP,
    "identifier": {"@type": "PropertyValue", "name": "REGON", "value": REGON},
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "ul. Długa 127",
        "postalCode": "84-223",
        "addressLocality": "Linia",
        "addressRegion": "pomorskie",
        "addressCountry": "PL",
    },
    "areaServed": [
        {"@type": "Country", "name": "Polska"},
        {"@type": "AdministrativeArea", "name": "województwo pomorskie"},
    ],
    "knowsAbout": [
        "budowa domów jednorodzinnych",
        "budowa domów w stanie surowym",
        "wykończenia wnętrz pod klucz",
        "remonty mieszkań i biur",
        "płyty fundamentowe",
        "roboty ziemne koparko-ładowarką",
    ],
    "contactPoint": [
        {"@type": "ContactPoint", "telephone": "+48 609 630 625", "contactType": "budowa domów i płyty fundamentowe", "areaServed": "PL", "availableLanguage": "pl"},
        {"@type": "ContactPoint", "telephone": "+48 691 858 193", "contactType": "elewacje i roboty wykończeniowe", "areaServed": "PL", "availableLanguage": "pl"},
        {"@type": "ContactPoint", "telephone": "+48 609 518 723", "contactType": "roboty ziemne", "areaServed": "PL", "availableLanguage": "pl"},
    ],
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Usługi remontowo-budowlane",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s[1], "url": f"{BASE}/oferta/{s[0]}/"}}
            for s in pages.SERVICES
        ],
    },
}


def org_schema():
    return {"@context": "https://schema.org", **ORG}


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{BASE}/#serwis",
        "url": f"{BASE}/",
        "name": "Buduj z Kaszubami — Firma Ogólnobudowlana Mateusz Drawc",
        "inLanguage": "pl-PL",
        "publisher": {"@id": f"{BASE}/#organizacja"},
    }


def crumbs_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label, "item": BASE + href if href else BASE + "/"}
            for i, (label, href) in enumerate(items)
        ],
    }


def webp_schema(p, kind="WebPage"):
    return {
        "@context": "https://schema.org",
        "@type": kind,
        "@id": BASE + p["url"] + "#strona",
        "url": BASE + p["url"],
        "name": p["title"],
        "description": p["desc"],
        "inLanguage": "pl-PL",
        "isPartOf": {"@id": f"{BASE}/#serwis"},
        "about": {"@id": f"{BASE}/#organizacja"},
    }


# ---------------------------------------------------------------------
# Definicje stron
# ---------------------------------------------------------------------
def page_head(title, lead="", img=None, img_alt="", crumbs=None, plain=False):
    return f'''<section class="page-head">
  <div class="wrap">
    {crumb(crumbs) if crumbs else ""}
    <div class="page-head__inner">
      <div>
        <h1 class="h1">{title}</h1>
        <p class="lead">{lead}</p>
      </div>
    </div>
  </div>
</section>'''


HOME = {
    "id": "home",
    "dir": "",
    "url": "/",
    "title": "Firma Ogólnobudowlana Mateusz Drawc w woj. pomorskim, Linia",
    "desc": "Zapraszamy do współpracy z doświadczoną Firmą Ogólnobudowlaną Mateusz Drawc, która znajduje się w miejscowości Linia. Działamy na terenie całej Polski.",
    "hero": pages.HOME_HERO,
    "body": pages.HOME_BODY,
    "preload": (pages.HERO_NAME, pages.HERO_SIZES),
    "schema": [website_schema(), org_schema()],
}

OFIRMIE = {
    "id": "o-firmie",
    "dir": "o-firmie",
    "url": "/o-firmie/",
    "title": "O Firmie Ogólnobudowlanej Mateusz Drawc – Linia: poznaj nas",
    "desc": "Firma Ogólnobudowlana Mateusz Drawc znajduje się w miejscowości Linia, jednak działa na terenie całej Polski. Wybierz zaufaną ekipę remontowo-budowlaną!",
    "hero": page_head(
        "O Firmie Ogólnobudowlanej Mateusz Drawc — Linia, pomorskie",
        "Firma z Linii w województwie pomorskim, realizująca inwestycje na terenie całej Polski. 17 lat doświadczenia w branży remontowo-budowlanej.",
        crumbs=[("Strona główna", "/"), ("O firmie", None)],
        plain=True,
    ),
    "body": pages.ABOUT_BODY,
}
OFIRMIE["schema"] = [webp_schema(OFIRMIE), crumbs_schema([("Strona główna", "/"), ("O firmie", "/o-firmie/")])]

OFERTA = {
    "id": "oferta",
    "dir": "oferta",
    "url": "/oferta/",
    "title": "Usługi remontowo-budowlane: profesjonalnie, rzetelnie i terminowo",
    "desc": "Szukasz doświadczonej ekipy budowlanej? Świetnie się składa – sprawdź naszą bogatą ofertę! Remontujemy, wykańczamy i budujemy. Jesteśmy do dyspozycji.",
    "hero": page_head(
        "Usługi remontowo-budowlane",
        "Budowa domów, wykończenia wnętrz, remonty i roboty ziemne — dla klientów indywidualnych i inwestorów z całej Polski.",
        crumbs=[("Strona główna", "/"), ("Oferta", None)],
        plain=True,
    ),
    "body": pages.OFERTA_BODY,
}
OFERTA["schema"] = [webp_schema(OFERTA), crumbs_schema([("Strona główna", "/"), ("Oferta", "/oferta/")])]

SERVICE_PAGES = {
    "uslugi-budowlane": dict(
        title="Usługi budowlane: fundamenty, szpachlowanie, murowanie",
        desc="Odwiedź naszą stronę i sprawdź zakres świadczonych usług budowlanych. Wykonujemy gładzie, tynki, a także szpachlujemy ściany oraz wylewamy fundamenty.",
        h1="Usługi budowlane",
        lead="Budowa domów jedno- i wielorodzinnych oraz obiektów — od fundamentu po stan surowy zamknięty.",
        img="content-uslugi-budowlane",
        alt="Wnętrze budynku w stanie surowym — betonowe ściany i otwory okienne",
        body=pages.BUDOWLANE_BODY,
    ),
    "uslugi-wykonczeniowe": dict(
        title="Usługi wykończeniowe mieszkań, domów, lokali użytkowych",
        desc="Szukasz fachowców, którym możesz zlecić prace wykończeniowe mieszkania, domu bądź lokalu użytkowego? Świetnie się składa – sprawdź naszą ofertę już dziś.",
        h1="Usługi wykończeniowe",
        lead="Wykończenia mieszkań, domów i lokali użytkowych pod klucz — od instalacji po montaż mebli.",
        img="content-uslugi-wykonczeniowe",
        alt="Wnętrze mieszkania w trakcie wykończenia — drabina i odświeżone ściany",
        body=pages.WYKONCZENIOWE_BODY,
    ),
    "uslugi-remontowe": dict(
        title="Usługi remontowe w mieszkaniach, domach i obiektach biurowych",
        desc="Szukasz doświadczonej ekipy remontowej? Jesteśmy do dyspozycji. Odmienimy wnętrze Twojego mieszkania, domu lub biura. Działamy na terenie całej Polski.",
        h1="Usługi remontowe",
        lead="Remonty mieszkań, domów i biur — od drobnych napraw po kompleksowe modernizacje.",
        img="content-uslugi-remontowe",
        alt="Prace remontowe — wygładzanie ściany pacą przez pracownika",
        body=pages.REMONTOWE_BODY,
    ),
    "uslugi-koparko-ladowarka": dict(
        title="Usługi koparko-ładowarką – kompleksowa obsługa robót ziemnych",
        desc="Świadczymy kompleksowe usługi koparko-ładowarką na terenie całej Polski. Wybierz doświadczonych profesjonalistów i zleć nam profesjonalną obsługę robót ziemnych",
        h1="Usługi koparko-ładowarką",
        lead="Roboty ziemne na terenie całej Polski — wykopy pod fundamenty i instalacje, skarpowanie, korytowanie, rozładunek.",
        img="content-uslugi-koparko-ladowarka",
        alt="Koparko-ładowarka podczas prac ziemnych na budowie",
        body=pages.KOPARKA_BODY,
    ),
}

GALERIA = {
    "id": "galeria",
    "dir": "galeria",
    "url": "/galeria/",
    "title": "Galeria – zdjęcia związane z naszą codzienną działalnością",
    "desc": "W galerii zamieściliśmy zdjęcia przedstawiające naszą pracę. Zapraszamy do zapoznania się ze wszystkimi fotografiami opublikowanymi na naszej stronie.",
    "hero": page_head(
        "Galeria",
        "Zdjęcia z prowadzonych prac: płyty fundamentowe, wznoszenie ścian i konstrukcje dachów.",
        crumbs=[("Strona główna", "/"), ("Galeria", None)],
        plain=True,
    ),
    "body": pages_more.GALERIA_BODY,
    "schema": None,
}
GALERIA["schema"] = [webp_schema(GALERIA, "CollectionPage"), crumbs_schema([("Strona główna", "/"), ("Galeria", "/galeria/")])]

KONTAKT = {
    "id": "kontakt",
    "dir": "kontakt",
    "url": "/kontakt/",
    "title": "Kontakt z Firmą Ogólnobudowlaną - Mateusz Drawc, Linia",
    "desc": "Masz pytania dotyczące oferty? Skontaktuj się z naszą firmą – chętnie udzielimy wszelkich informacji! Niezbędne dane kontaktowe znajdziesz na stronie.",
    "hero": page_head(
        "Kontakt z Firmą Ogólnobudowlaną Mateusz Drawc — Linia, pomorskie",
        "Masz pytania dotyczące naszej działalności? Chcesz skorzystać z oferty? Skontaktuj się z nami!",
        crumbs=[("Strona główna", "/"), ("Kontakt", None)],
        plain=True,
    ),
    "body": pages_more.KONTAKT_BODY,
}
KONTAKT["schema"] = [webp_schema(KONTAKT, "ContactPage"), org_schema(), crumbs_schema([("Strona główna", "/"), ("Kontakt", "/kontakt/")])]

PRIVACY = {
    "id": "polityka-prywatnosci",
    "dir": "polityka-prywatnosci",
    "url": "/polityka-prywatnosci/",
    "title": "Polityka prywatności — Buduj z Kaszubami",
    "desc": "Zasady ochrony prywatności i przetwarzania danych osobowych Użytkowników serwisu budujzkaszubami.pl, zgodnie z RODO.",
    "hero": page_head(
        "Polityka prywatności serwisu budujzkaszubami.pl",
        "Zasady ochrony prywatności i przetwarzania danych osobowych w serwisie budujzkaszubami.pl.",
        crumbs=[("Strona główna", "/"), ("Polityka prywatności", None)],
        plain=True,
    ),
    "body": legal.PRIVACY_BODY,
}
PRIVACY["schema"] = [webp_schema(PRIVACY), crumbs_schema([("Strona główna", "/"), ("Polityka prywatności", "/polityka-prywatnosci/")])]

COOKIES = {
    "id": "polityka-cookies",
    "dir": "polityka-cookies",
    "url": "/polityka-cookies/",
    "title": "Polityka Cookies — Buduj z Kaszubami",
    "desc": "Zasady wykorzystywania plików cookies w serwisie budujzkaszubami.pl oraz sposoby zarządzania zgodami w przeglądarkach.",
    "hero": page_head(
        "Polityka Cookies",
        "Zasady wykorzystywania plików cookies w serwisie budujzkaszubami.pl.",
        crumbs=[("Strona główna", "/"), ("Polityka Cookies", None)],
        plain=True,
    ),
    "body": legal.COOKIES_BODY,
}
COOKIES["schema"] = [webp_schema(COOKIES), crumbs_schema([("Strona główna", "/"), ("Polityka Cookies", "/polityka-cookies/")])]

INFO = {
    "id": "obowiazek-informacyjny",
    "dir": "obowiazek-informacyjny",
    "url": "/obowiazek-informacyjny/",
    "title": "Obowiązek informacyjny — Buduj z Kaszubami",
    "desc": "Informacje o przetwarzaniu danych osobowych zawartych w korespondencji e-mail kierowanej do Firma Ogólnobudowlana Mateusz Drawc.",
    "hero": page_head(
        "Obowiązek informacyjny",
        "Informacje o przetwarzaniu danych osobowych zawartych w korespondencji kierowanej do Administratora.",
        crumbs=[("Strona główna", "/"), ("Obowiązek informacyjny", None)],
        plain=True,
    ),
    "body": legal.INFO_BODY,
}
INFO["schema"] = [webp_schema(INFO), crumbs_schema([("Strona główna", "/"), ("Obowiązek informacyjny", "/obowiazek-informacyjny/")])]

PAGES = [HOME, OFIRMIE, OFERTA, GALERIA, KONTAKT, PRIVACY, COOKIES, INFO]
for _sid, _cfg in SERVICE_PAGES.items():
    p = {
        "id": f"oferta/{_sid}",
        "dir": f"oferta/{_sid}",
        "url": f"/oferta/{_sid}/",
        "title": _cfg["title"],
        "desc": _cfg["desc"],
        "hero": page_head(
            _cfg["h1"], _cfg["lead"],
            crumbs=[("Strona główna", "/"), ("Oferta", "/oferta/"), (_cfg["h1"], None)],
            plain=True,
        ),
        "body": _cfg["body"],
    }
    p["schema"] = [
        webp_schema(p, "Service"),
        crumbs_schema([("Strona główna", "/"), ("Oferta", "/oferta/"), (_cfg["h1"], f"/oferta/{_sid}/")]),
    ]
    # wstaw po /oferta/, zachowując kolejność menu
    idx = PAGES.index(OFERTA) + 1 + list(SERVICE_PAGES).index(_sid)
    PAGES.insert(idx, p)


# ---------------------------------------------------------------------
# Zapis
# ---------------------------------------------------------------------
def write(path, content):
    full = os.path.join(SITE_DIR, path)
    os.makedirs(os.path.dirname(full) or SITE_DIR, exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return full


built = []
for p in PAGES:
    rel = (p["dir"] + "/index.html") if p["dir"] else "index.html"
    write(rel, document(p))
    built.append((p["url"], rel))

# 404
ERR = {
    "id": "404",
    "dir": "",
    "url": "/404.html",
    "title": "Nie znaleziono strony (404) — Buduj z Kaszubami",
    "desc": "Strona o podanym adresie nie istnieje. Skorzystaj z nawigacji lub wróć na stronę główną.",
    "noindex": True,
    "hero": pages_more.ERR_BODY,
    "body": "",
}
write("404.html", document(ERR))

# sitemap
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in PAGES:
    if p.get("noindex"):
        continue
    prio = "1.0" if p["url"] == "/" else ("0.8" if p["url"].startswith("/oferta") else "0.7")
    sm.append(f'  <url><loc>{BASE}{p["url"]}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{prio}</priority></url>')
sm.append("</urlset>")
write("sitemap.xml", "\n".join(sm) + "\n")

write("robots.txt", f"""User-agent: *
Allow: /
Sitemap: {BASE}/sitemap.xml
""")

print(f"Zapisano {len(built) + 2} plików HTML")
for u, r in built:
    print(f"  {u:34s} -> {r}")

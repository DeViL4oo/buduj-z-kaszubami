# -*- coding: utf-8 -*-
"""Wspólna konfiguracja i helpery dla generatora strony budujzkaszubami.pl"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(ROOT, "site")
MANIFEST = json.load(open(os.path.join(ROOT, "_src", "manifest.json"), encoding="utf-8"))
SINGLE = json.load(open(os.path.join(ROOT, "_src", "single.json"), encoding="utf-8"))

BASE = "https://budujzkaszubami.pl"
IMG = "/assets/img"

FIRMA = "Firma Ogólnobudowlana Mateusz Drawc"
BRAND = "Buduj z Kaszubami"
TEL = "+48609630625"
TEL_TXT = "609 630 625"
EMAIL = "mateo-drawc@wp.pl"
STREET = "ul. Długa 127"
POST = "84-223"
CITY = "Linia"
REGION = "pomorskie"
NIP = "5882211060"
REGON = "367068433"

PEOPLE = [
    ("Płyty fundamentowe i budowa domów", "Mateusz", "+48609630625", "609 630 625"),
    ("Elewacja i roboty wykończeniowe", "Tadeusz", "+48691858193", "691 858 193"),
    ("Usługi koparką", "Piotr", "+48609518723", "609 518 723"),
]

ICONS = {
    "phone": '<path d="M6.4 3h3.1l1.5 4-2.1 1.6a11.4 11.4 0 0 0 5.5 5.5L16 12l4 1.5v3.1A2.4 2.4 0 0 1 17.6 19 16.4 16.4 0 0 1 5 6.4 2.4 2.4 0 0 1 6.4 3Z"/>',
    "mail": '<rect x="2.8" y="5" width="18.4" height="14" rx="1.6"/><path d="m3.4 6.6 8.6 6.1 8.6-6.1"/>',
    "pin": '<path d="M12 21.2c4.6-4.4 7-7.8 7-11.1a7 7 0 1 0-14 0c0 3.3 2.4 6.7 7 11.1Z"/><circle cx="12" cy="9.8" r="2.6"/>',
    "arrow": '<path d="M4 12h15"/><path d="m13.2 5.8 6.2 6.2-6.2 6.2"/>',
    "arrow-left": '<path d="M20 12H5"/><path d="m10.8 5.8-6.2 6.2 6.2 6.2"/>',
    "chevron": '<path d="m6 9.2 6 6 6-6"/>',
    "close": '<path d="m6 6 12 12"/><path d="m18 6-12 12"/>',
    "zoom": '<circle cx="10.8" cy="10.8" r="6.8"/><path d="m15.8 15.8 4.4 4.4"/><path d="M10.8 7.9v5.8M7.9 10.8h5.8"/>',
    "quality": '<path d="M12 3.2 5 6v5.4c0 4.4 2.9 8 7 9.6 4.1-1.6 7-5.2 7-9.6V6l-7-2.8Z"/><path d="m8.8 11.7 2.2 2.2 4.2-4.5"/>',
    "crew": '<path d="M3.6 18.5h16.8"/><path d="M6.2 18.5a5.8 5.8 0 0 1 11.6 0"/><path d="M9.6 7.1V4.4h4.8v2.7"/><path d="M12 7.1v3.4"/>',
    "commit": '<circle cx="9.2" cy="8.1" r="3.3"/><path d="M2.9 19.4a6.3 6.3 0 0 1 12.6 0"/><path d="m15.9 12.6 1.9 1.9 3.7-3.9"/>',
    "clock": '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.3V12l3.3 2.1"/>',
    "check": '<path d="m5 12.5 4.4 4.4L19 6.6"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6"/><path d="M12 7.6h.01"/>',
    "download": '<path d="M12 3v11"/><path d="m7.5 10 4.5 4.5L16.5 10"/><path d="M4 19h16"/>',
    "external": '<path d="M14 4h6v6"/><path d="M20 4 11 13"/><path d="M18 14.5V19a1.5 1.5 0 0 1-1.5 1.5H5A1.5 1.5 0 0 1 3.5 19V7.5A1.5 1.5 0 0 1 5 6h4.5"/>',
}

MARK = (
    '<svg class="brand__mark" viewBox="0 0 40 40" fill="none" aria-hidden="true" focusable="false">'
    '<path d="M5 22.4 20 9.2l15 13.2" stroke="currentColor" stroke-width="4" stroke-linejoin="miter"/>'
    '<rect x="10.5" y="27.6" width="19" height="4.2" fill="#E0A81A"/>'
    "</svg>"
)


def icon(name, cls="", size=None):
    s = f' class="{cls}"' if cls else ""
    st = f' style="width:{size}px;height:{size}px"' if size else ""
    px = size or 24
    return (
        f'<svg{s}{st} viewBox="0 0 24 24" width="{px}" height="{px}" fill="none" '
        f'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
        f'aria-hidden="true" focusable="false">{ICONS[name]}</svg>'
    )


def dims(name):
    m = SINGLE[name]
    return m["w"], m["h"]


def pic(
    name,
    alt,
    sizes="",
    cls="",
    priority=False,
    lazy=True,
    img_cls="",
    img_style="",
    aria_hidden=False,
    extra="",
):
    """Jedno zdjęcie = jeden plik WebP; przeglądarka skaluje je sama."""
    w, h = dims(name)
    classes = " ".join(c for c in (cls, img_cls) if c)
    c = f' class="{classes}"' if classes else ""
    ist = f' style="{img_style}"' if img_style else ""
    load = "" if (priority or not lazy) else ' loading="lazy"'
    prio = ' fetchpriority="high"' if priority else ""
    dec = "" if priority else ' decoding="async"'
    ah = ' aria-hidden="true"' if aria_hidden else ""
    return (
        f'<img src="{IMG}/{name}.webp" alt="{alt}"{c}{ist} '
        f'width="{w}" height="{h}"{load}{prio}{dec}{ah}{extra}>'
    )


def preload(name, sizes=""):
    return f'<link rel="preload" as="image" href="{IMG}/{name}.webp" fetchpriority="high">'


# ---------------------------------------------------------------------
# Nawigacja i dokumenty
# ---------------------------------------------------------------------
NAV = [
    ("home", "Strona główna", "/"),
    ("o-firmie", "O firmie", "/o-firmie/"),
    ("oferta", "Oferta", "/oferta/"),
    ("galeria", "Galeria", "/galeria/"),
    ("kontakt", "Kontakt", "/kontakt/"),
]

SERVICES = [
    ("uslugi-budowlane", "Usługi budowlane", "box-offer-h",
     "Budowa domów jedno- i wielorodzinnych, bliźniaków oraz obiektów — w stanie surowym i pod klucz."),
    ("uslugi-wykonczeniowe", "Usługi wykończeniowe", "box-offer-h-1",
     "Wykończenie mieszkań, domów i lokali użytkowych pod klucz — od instalacji po montaż mebli."),
    ("uslugi-remontowe", "Usługi remontowe", "box-offer-h-2",
     "Remonty mieszkań, domów i biur — adaptacje poddaszy, ścianki działowe, tynki i malowanie."),
    ("uslugi-koparko-ladowarka", "Usługi koparko-ładowarką", "box-offer-h-3",
     "Roboty ziemne: wykopy pod fundamenty i instalacje, skarpowanie, korytowanie, rozładunek."),
]

SUBMENU = [(s[0], s[1], "/oferta/" + s[0] + "/") for s in SERVICES]

LEGAL_LINKS = [
    ("polityka-prywatnosci", "Polityka prywatności", "/polityka-prywatnosci/"),
    ("polityka-cookies", "Polityka Cookies", "/polityka-cookies/"),
    ("obowiazek-informacyjny", "Obowiązek informacyjny", "/obowiazek-informacyjny/"),
]


def is_active(pid, current):
    if pid == current:
        return True
    if pid == "oferta" and current.startswith("oferta/uslugi"):
        return True
    return False

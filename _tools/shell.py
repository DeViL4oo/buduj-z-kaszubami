# -*- coding: utf-8 -*-
"""Szkielet HTML: <head>, nagłówek, nawigacja, stopka."""
import json
from common import *
from common import NAV, SUBMENU, LEGAL_LINKS, is_active


def nav_html(current):
    out = []
    for pid, label, href in NAV:
        if pid == "oferta":
            sub = []
            for sid, slabel, shref in SUBMENU:
                cur = ' aria-current="page"' if current == "oferta/" + sid else ""
                sub.append('<li><a href="' + shref + '"' + cur + ">" + slabel + "</a></li>")
            subtog = (
                '<button class="nav__sub-toggle" type="button" aria-expanded="false" '
                'aria-controls="sub-oferta" aria-label="Pokaż podmenu Oferta">' + icon("chevron") + "</button>"
            )
            cur = ' aria-current="page"' if is_active(pid, current) else ""
            out.append(
                '<li class="nav__item has-sub"><div class="nav__row">'
                '<a class="nav__link" href="' + href + '"' + cur + ">" + label + "</a>" + subtog + "</div>"
                '<ul class="submenu" id="sub-oferta">' + "".join(sub) + "</ul></li>"
            )
        else:
            cur = ' aria-current="page"' if is_active(pid, current) else ""
            out.append(
                '<li class="nav__item"><div class="nav__row">'
                '<a class="nav__link" href="' + href + '"' + cur + ">" + label + "</a></div></li>"
            )
    return (
        '<nav class="nav" id="site-nav" aria-label="Nawigacja główna">'
        '<ul class="nav__list">' + "".join(out) + "</ul>"
        '<div class="nav__cta">'
        '<a class="btn btn--accent" href="tel:' + TEL + '">' + icon("phone") + "<span>Zadzwoń " + TEL_TXT + "</span></a>"
        '<a class="btn btn--light" href="mailto:' + EMAIL + '">' + icon("mail") + "<span>" + EMAIL + "</span></a>"
        "</div>"
        '<p class="nav__meta">Linia, woj. pomorskie — realizacje w całej Polsce</p>'
        "</nav>"
    )


def header_html(current):
    return (
        '<header class="site-header">\n'
        '  <div class="wrap">\n'
        '    <div class="bar">\n'
        '      <a class="brand" href="/">\n'
        
        '          <img class="brand__logo brand__logo--light" src="/assets/img/logo-light.svg" '
        'alt="Buduj z Kaszubami — Firma Ogólnobudowlana Mateusz Drawc, strona główna" width="162" height="29">\n'
        '          <img class="brand__logo brand__logo--dark" src="/assets/img/logo.svg" alt="" '
        'width="162" height="29" aria-hidden="true">\n'
        "      </a>\n"
        "      " + nav_html(current) + "\n"
        '      <div class="bar__actions">\n'
        '        <a class="header-tel" href="tel:' + TEL + '">' + icon("phone") + "<span>" + TEL_TXT + "</span></a>\n"
        '        <a class="header-call" href="tel:' + TEL + '" aria-label="Zadzwoń: ' + TEL_TXT + '">' + icon("phone") + "</a>\n"
        '        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Otwórz menu">\n'
        '          <span class="nav-toggle__box" aria-hidden="true"><i></i><i></i><i></i></span>\n'
        "        </button>\n"
        "      </div>\n"
        "    </div>\n"
        "  </div>\n"
        "</header>"
    )


def footer_html():
    site = "".join('<li><a href="' + h + '">' + l + "</a></li>" for _, l, h in NAV)
    off = "".join('<li><a href="' + h + '">' + l + "</a></li>" for _, l, h in SUBMENU)
    legal_l = "".join('<li><a href="' + h + '">' + l + "</a></li>" for _, l, h in LEGAL_LINKS)
    return (
        '<footer class="footer">\n'
        '  <div class="wrap">\n'
        '    <div class="footer__top">\n'
        '      <div class="footer__brand">\n'
        '        <a class="brand" href="/">\n'
        '          <img class="brand__logo" src="/assets/img/logo-light.svg" '
        'alt="Buduj z Kaszubami — Firma Ogólnobudowlana Mateusz Drawc" width="162" height="29">\n'
        "        </a>\n"
        '        <p class="footer__name">' + FIRMA + "</p>\n"
        '        <p class="footer__desc">Budowa domów, wykończenia wnętrz, remonty i roboty ziemne. '
        "Linia, woj. pomorskie — realizacje w całej Polsce.</p>\n"
        "      </div>\n"
        "      <div>\n"
        '        <h2 class="footer__h">Witryna</h2>\n'
        '<nav aria-label="Witryna"><ul>' + site + "</ul></nav>\n"
        "      </div>\n"
        "      <div>\n"
        '        <h2 class="footer__h">Oferta</h2>\n'
        '<nav aria-label="Oferta"><ul>' + off + "</ul></nav>\n"
        "      </div>\n"
        "      <div>\n"
        '        <h2 class="footer__h">Kontakt</h2>\n'
        '        <ul class="footer__contact">\n'
        "          <li>" + icon("pin") + "<span>" + STREET + "<br>" + POST + " " + CITY + " (" + REGION + ")</span></li>\n"
        '          <li>' + icon("phone") + '<a href="tel:' + TEL + '">' + TEL_TXT + "</a></li>\n"
        '          <li>' + icon("mail") + '<a href="mailto:' + EMAIL + '">' + EMAIL + "</a></li>\n"
        "        </ul>\n"
        '        <p style="margin:1.25rem 0 0;font-size:.76rem;line-height:1.5">NIP ' + NIP + "<br>REGON " + REGON + "</p>\n"
        "      </div>\n"
        "    </div>\n"
        '    <div class="footer__bottom">\n'
        '      <p style="margin:0">Wszelkie prawa zastrzeżone © 2026 ' + FIRMA + "</p>\n"
        '<nav aria-label="Dokumenty"><ul>' + legal_l + "</ul></nav>\n"
        "    </div>\n"
        "  </div>\n"
        "</footer>"
    )


def head_html(p):
    url = BASE + p["url"]
    og = p.get("og", "og-image.jpg")
    og_url = (BASE + "/assets/img/" + og) if not og.startswith("http") else og
    extra = ""
    if p.get("preload"):
        name, sizes = p["preload"]
        extra += "\n" + preload(name, sizes)
    robots = (
        '<meta name="robots" content="noindex,follow">'
        if p.get("noindex")
        else '<meta name="robots" content="index,follow,max-image-preview:large">'
    )
    schema = ""
    if p.get("schema"):
        blocks = p["schema"] if isinstance(p["schema"], list) else [p["schema"]]
        for b in blocks:
            schema += '\n<script type="application/ld+json">' + json.dumps(
                b, ensure_ascii=False, separators=(",", ":")
            ) + "</script>"

    lines = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>" + p["title"] + "</title>",
        '<meta name="description" content="' + p["desc"] + '">',
        robots,
        '<link rel="canonical" href="' + url + '">',
        '<meta name="theme-color" content="#0c0d0f">',
        '<meta name="author" content="' + FIRMA + '">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Buduj z Kaszubami">',
        '<meta property="og:locale" content="pl_PL">',
        '<meta property="og:title" content="' + p["title"] + '">',
        '<meta property="og:description" content="' + p["desc"] + '">',
        '<meta property="og:url" content="' + url + '">',
        '<meta property="og:image" content="' + og_url + '">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="Buduj z Kaszubami — Firma Ogólnobudowlana Mateusz Drawc">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="' + p["title"] + '">',
        '<meta name="twitter:description" content="' + p["desc"] + '">',
        '<meta name="twitter:image" content="' + og_url + '">',
        '<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">',
        '<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">',
        '<link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>',
        '<link rel="stylesheet" href="/assets/css/main.css">',
    ]
    return "\n".join(lines) + extra + schema + (
        '\n<script>document.documentElement.className=document.documentElement.className.replace("no-js","js");</script>'
    )


BANNER = (
    "<script>if(location.protocol==='file:'){var d=document.createElement('div');"
    "d.setAttribute('style','position:relative;z-index:9999;background:#f2b01e;color:#0c0d0f;"
    "font:600 15px/1.6 system-ui,sans-serif;padding:14px 18px;text-align:center');"
    "d.innerHTML='Podgląd z pliku: style i zdjęcia wymagają serwera lokalnego. "
    "Uruchom <b>PODGLAD.cmd</b> w folderze Strona.';"
    "document.body.insertBefore(d,document.body.firstChild);}</script>"
)


def document(p):
    body = p.get("hero", "") + p.get("body", "")
    return (
        "<!doctype html>\n"
        '<html lang="pl" class="no-js">\n'
        "<head>\n" + head_html(p) + "\n</head>\n"
        "<body>\n"
        + BANNER + "\n"
        '<a class="skip" href="#main">Przejdź do treści</a>\n'
        + header_html(p["id"]) + "\n"
        '<main id="main">\n' + body + "\n</main>\n"
        + footer_html() + "\n"
        '<script src="/assets/js/site.js" defer></script>\n'
        "</body>\n"
        "</html>\n"
    )

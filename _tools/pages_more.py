# -*- coding: utf-8 -*-
"""Galeria, kontakt, 404."""
from common import *
from pages import crumb, cta_section, person_block

# (nazwa pliku bez rozszerzenia, tekst alternatywny)
GALLERY = [
    ("gal-teren-budowy-domu-1", "Wylana płyta fundamentowa domu jednorodzinnego z widocznymi krawędziami szalunku"),
    ("gal-teren-budowy-domu-9", "Płyta fundamentowa z wyprowadzonymi rurami instalacyjnymi — widok z góry"),
    ("gal-teren-budowy-domu-8", "Fundament domu jednorodzinnego na przygotowanym gruncie"),
    ("gal-teren-budowy-domu-12", "Płyta fundamentowa i teren budowy — ujęcie z boku"),
    ("gal-teren-budowy-domu-13", "Płyty fundamentowe dwóch budynków — widok z góry na wylaną powierzchnię"),
    ("gal-teren-budowy-domu-10", "Płyta fundamentowa z zaznaczonymi punktami instalacyjnymi"),
    ("gal-teren-budowy-domu-2", "Fundament domu — widok na całą powierzchnię płyty i krawędzie"),
    ("gal-teren-budowy-domu-11", "Płyta fundamentowa w otoczeniu zieleni — ujęcie z poziomu gruntu"),
    ("gal-teren-budowy-domu-6", "Płyta fundamentowa z izolacją na krawędziach"),
    ("gal-teren-budowy-domu-7", "Fundament domu jednorodzinnego — zbliżenie na krawędź płyty"),
    ("gal-teren-budowy-domu-5", "Widok na przygotowany teren budowy i płytę fundamentową"),
    ("gal-teren-budowy-domu-3", "Płyta fundamentowa z wyprowadzonymi instalacjami — widok z góry"),
    ("gal-teren-budowy-domu-4", "Fundament domu w trakcie prac — widoczna podsypka i szalunek"),
    ("gal-budowa-03", "Zbrojenie i szalunek fundamentu przed wylaniem betonu"),
    ("gal-budowa-02", "Fundament domu — widok na zbrojenie i przygotowane krawędzie"),
    ("gal-budowa-01", "Płyta fundamentowa z widocznym zbrojeniem i rurami"),
    ("gal-budowa-budynku-01", "Betonowe schody zewnętrzne przy wznoszonym budynku"),
    ("gal-budowa-budynku-03", "Ściana budynku w stanie surowym — zbliżenie na detal konstrukcji"),
    ("gal-budowa-06", "Przygotowanie podłoża pod płytę fundamentową — podsypka piaskowa"),
    ("gal-budowa-05", "Teren budowy z wytyczonymi liniami i przygotowanym podłożem"),
    ("gal-budowa-04", "Prace ziemne i przygotowanie podłoża pod fundament"),
    ("gal-budowa-budynku-02", "Utwardzony podjazd i teren wokół budowanego obiektu"),
    ("gal-budowa-budynku-04", "Budynek w stanie surowym — widok z zewnątrz"),
    ("gal-budowa-budynku-06", "Wznoszone ściany budynku — stan surowy"),
    ("gal-budowa-budynku-05", "Konstrukcja dachu na wznoszonym budynku"),
    ("gal-budowa-budynku-07", "Budynek w stanie surowym zamkniętym — widok z boku"),
    ("gal-budowa-budynku-08", "Murowane ściany budynku z bloczków betonowych"),
    ("gal-budowa-budynku-09", "Ściany z bloczków betonowych — widok na narożnik budynku"),
    ("gal-budowa-budynku-10", "Budynek w stanie surowym — mury i otwory okienne"),
    ("gal-budowa-budynku-11", "Dom jednorodzinny z konstrukcją dachu — elewacja frontowa"),
    ("gal-budowa-domu-2", "Fundament domu jednorodzinnego — widok z góry"),
    ("gal-budowa-domu-1", "Płyta fundamentowa domu — ujęcie z boku"),
    ("gal-budowa-domu-3", "Fundament z zbrojeniem i szalunkiem — widok z góry"),
    ("gal-budowa-domu-4", "Płyta fundamentowa z krawędziami szalunku"),
    ("gal-budowa-domu-5", "Fundament domu — widok na narożnik płyty"),
    ("gal-budowa-domu-6", "Płyta fundamentowa i teren wokół budowy"),
    ("gal-budowa-domu-7", "Fundament budynku — ujęcie z poziomu gruntu"),
    ("gal-budowa-domu-8", "Dom jednorodzinny w stanie surowym — widok z zewnątrz"),
    ("gal-budowa-domu-9", "Budynek w stanie surowym zamkniętym"),
    ("gal-budowa-domu-10", "Dom jednorodzinny — elewacja po wykonaniu dachu"),
    ("gal-budowa-domu-11", "Dom jednorodzinny — widok z zewnątrz po zakończeniu prac konstrukcyjnych"),
]

GAL_SIZES = "(min-width: 1000px) 23vw, (min-width: 600px) 31vw, 47vw"


def gallery_html():
    out = ['<div class="gallery">']
    for i, (name, alt) in enumerate(GALLERY, 1):
        w, h = dims(name)
        out.append(f'''<figure class="gallery__item">
  <a class="gallery__link" href="{IMG}/{name}.webp" data-full="{IMG}/{name}.webp" data-alt="{alt}" data-w="{w}" data-h="{h}" aria-label="Powiększ zdjęcie {i} z {len(GALLERY)}: {alt}">
    {pic(name, alt, sizes=GAL_SIZES, priority=(i <= 4))}
    <span class="gallery__zoom">{icon("zoom")}</span>
  </a>
</figure>''')
    out.append("</div>")
    return "\n".join(out)


GALERIA_BODY = f'''
<section class="section">
  <div class="wrap">
    {gallery_html()}
  </div>
</section>

<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Podgląd zdjęcia" hidden>
  <div class="lb__top">
    <span class="lb__counter" id="lb-counter">1 / {len(GALLERY)}</span>
    <button class="lb__close" type="button" id="lb-close" aria-label="Zamknij podgląd">{icon("close")}</button>
  </div>
  <div class="lb__stage">
    <img class="lb__img" id="lb-img" alt="" width="800" height="600">
  </div>
  <div class="lb__bar">
    <button class="lb__nav lb__nav--prev" type="button" id="lb-prev" aria-label="Poprzednie zdjęcie">{icon("arrow-left")}</button>
    <p class="lb__caption" id="lb-caption"></p>
    <button class="lb__nav lb__nav--next" type="button" id="lb-next" aria-label="Następne zdjęcie">{icon("arrow")}</button>
  </div>
</div>

{cta_section("Chcesz zobaczyć więcej?", "Zdjęcia z&nbsp;poszczególnych realizacji udostępniamy na&nbsp;życzenie — napisz lub zadzwoń.")}
'''


# =====================================================================
# KONTAKT
# =====================================================================
MAP_Q = "ul.+D%C5%82uga+127,+84-223+Linia"

KONTAKT_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="contact-panel">
      <h2 class="h3">Dane kontaktowe</h2>
      <div class="contact-grid">
        <div class="contact-box">
          <p class="contact-box__label">{icon("pin")} Adres</p>
          <p><strong>{FIRMA}</strong><br>{STREET}<br>{POST} {CITY} ({REGION})</p>
        </div>
        <div class="contact-box">
          <p class="contact-box__label">{icon("mail")} E-mail</p>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <div class="contact-box">
          <p class="contact-box__label">{icon("phone")} Telefon</p>
          <p><a href="tel:{TEL}">{TEL_TXT}</a></p>
        </div>
      </div>
    </div>

    <div style="margin-top:clamp(2.5rem,5vw,4rem)">
      <h2 class="h3">Kontakt bezpośredni</h2>
      <p class="muted" style="font-size:.94rem;margin:.3rem 0 1.1rem">Wybierz osobę odpowiedzialną za&nbsp;dany zakres prac.</p>
      <div class="grid grid-3" style="gap:.6rem">
        {person_block("Płyty fundamentowe i budowa domów", "Mateusz", TEL, TEL_TXT)}
        {person_block("Elewacja i roboty wykończeniowe", "Tadeusz", "+48691858193", "691 858 193")}
        {person_block("Usługi koparką", "Piotr", "+48609518723", "609 518 723")}
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <h2 class="h3">Jak do nas trafić</h2>
    <div class="map" id="map" style="margin-top:1.25rem">
      <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=17.8975%2C54.4518%2C17.9175%2C54.4584&amp;layer=mapnik&amp;marker=54.455112%2C17.907486" title="Mapa z lokalizacją firmy przy ul. Długiej 127 w Linii" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <p class="map__foot"><a class="link-arrow" href="https://www.google.com/maps/search/?api=1&amp;query=Firma+Og%C3%B3lnobudowlana+Mateusz+Drawc+{MAP_Q}" target="_blank" rel="noopener">Otwórz w Mapach Google {icon("external")}</a></p>
  </div>
</section>
'''

ERR_BODY = f'''
<section class="page-head">
  <div class="wrap">
    <p class="err-404__code" aria-hidden="true">404</p>
    <h1 class="h1">Nie znaleźliśmy tej strony</h1>
    <p class="lead">Adres mógł się zmienić lub zawierać literówkę. Skorzystaj z&nbsp;nawigacji albo wróć na&nbsp;stronę główną.</p>
    <div class="btn-row" style="margin-top:2rem">
      <a class="btn btn--accent" href="/"><span>Strona główna</span>{icon("arrow")}</a>
      <a class="btn btn--light" href="/oferta/"><span>Oferta</span></a>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2 class="h3" style="margin-bottom:1rem">Najczęściej szukane</h2>
    <div class="related">
      <a href="/oferta/uslugi-budowlane/"><span>Usługi budowlane</span>{icon("arrow")}</a>
      <a href="/oferta/uslugi-wykonczeniowe/"><span>Usługi wykończeniowe</span>{icon("arrow")}</a>
      <a href="/oferta/uslugi-remontowe/"><span>Usługi remontowe</span>{icon("arrow")}</a>
      <a href="/galeria/"><span>Galeria realizacji</span>{icon("arrow")}</a>
      <a href="/kontakt/"><span>Kontakt</span>{icon("arrow")}</a>
    </div>
  </div>
</section>
'''

# -*- coding: utf-8 -*-
"""Treść podstron merytorycznych."""
from common import *

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


def crumb(items):
    lis = []
    for i, (label, href) in enumerate(items):
        if href:
            lis.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{label}</li>')
    return f'<nav class="crumbs" aria-label="Ścieżka nawigacji"><ol>{"".join(lis)}</ol></nav>'


def person_block(role, name, tel, tel_txt):
    return f'''<div class="person">
  <div>
    <span class="person__role">{role}</span>
    <span class="person__name">{name}</span>
    <a class="person__tel" href="tel:{tel}">{icon("phone")}{tel_txt}</a>
  </div>
</div>'''


def cta_section(title, text):
    return f'''<section class="section section--tight">
  <div class="wrap">
    <div class="cta">
      <div>
        <h2 class="h2">{title}</h2>
        <p>{text}</p>
      </div>
      <div class="cta__actions">
        <a class="btn btn--accent" href="/kontakt/">Napisz do nas</a>
        <a class="cta__phone" href="tel:{TEL}"><span>Zadzwoń</span><strong>{TEL_TXT}</strong></a>
      </div>
    </div>
  </div>
</section>'''


def related(current):
    others = [s for s in SERVICES if s[0] != current]
    items = "".join(
        f'<a href="/oferta/{sid}/"><span>{title}</span>{icon("arrow")}</a>' for sid, title, _, _ in others
    )
    return f'''<section class="section section--tight">
  <div class="wrap">
    <p class="eyebrow">Pozostałe usługi</p>
    <div class="related">{items}</div>
  </div>
</section>'''


# =====================================================================
# STRONA GŁÓWNA
# =====================================================================
HERO_NAME = "slide-d-1-1"
HERO_SIZES = "100vw"


def service_rows():
    out = ['<div class="service-list">']
    for i, (sid, title, _img, desc) in enumerate(SERVICES, 1):
        out.append(f'''<a class="service-row" href="/oferta/{sid}/">
  <span class="service-row__title">{title}</span>
  <span class="service-row__desc">{desc}</span>
  <span class="service-row__arrow">{icon("arrow")}</span>
</a>''')
    out.append("</div>")
    return "\n".join(out)


HOME_HERO = f'''
<section class="hero">
  <div class="wrap">
    <div class="hero__top">
      <div class="hero__head">
        <p class="eyebrow" data-enter="1">Linia, woj. pomorskie · realizacje w&nbsp;całej Polsce</p>
        <h1 class="display hero__title">
          <span><span>Budujemy domy</span></span>
          <span><span>od fundamentu</span></span>
          <span><span>po wnętrze</span></span>
        </h1>
      </div>
      <div class="hero__aside">
        <p class="lead hero__lead" data-enter="2">Firma Ogólnobudowlana Mateusz Drawc realizuje prace budowlane, wykończeniowe, remontowe i&nbsp;roboty ziemne — dla klientów indywidualnych i&nbsp;inwestorów z&nbsp;całej Polski.</p>
        <div class="hero__actions" data-enter="3">
          <a class="btn btn--accent" href="/oferta/"><span>Zobacz ofertę</span>{icon("arrow")}</a>
          <a class="hero__phone" href="tel:{TEL}"><small>Zadzwoń</small><strong>{TEL_TXT}</strong></a>
        </div>
      </div>
    </div>
    <dl class="hero__meta">
      <div><dt>Doświadczenie</dt><dd>17 lat w&nbsp;branży</dd></div>
      <div><dt>Zasięg</dt><dd>cała Polska</dd></div>
      <div><dt>Partner</dt><dd>podwykonawca PARATI</dd></div>
      <div><dt>Zakres</dt><dd>od fundamentu po wnętrze</dd></div>
    </dl>
  </div>
</section>

<figure class="hero__band">
  {pic(HERO_NAME, "Dom jednorodzinny w budowie — ściany, konstrukcja dachu i rusztowania na tle projektu budowlanego", sizes=HERO_SIZES, priority=True)}
  <a class="hero__caption" href="/galeria/">{icon("zoom")} Zobacz realizacje</a>
</figure>
'''

HOME_BODY = f'''
<section class="usp">
  <div class="wrap">
    <h2 class="sr-only">Co nas wyróżnia</h2>
    <ul class="usp__list">
      <li><div class="usp__item">{icon("quality", "usp__icon")}<div><h3>Jakość</h3><p>Sprawdzone materiały od cenionych marek</p></div></div></li>
      <li><div class="usp__item">{icon("crew", "usp__icon")}<div><h3>Doświadczenie</h3><p>17 lat w branży remontowo-budowlanej</p></div></div></li>
      <li><div class="usp__item">{icon("commit", "usp__icon")}<div><h3>Zaangażowanie</h3><p>Indywidualne podejście do zlecenia</p></div></div></li>
      <li><div class="usp__item">{icon("clock", "usp__icon")}<div><h3>Terminowość</h3><p>Prace zgodnie z ustalonym terminem</p></div></div></li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="zakres-h">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Zakres prac</p>
      <h2 id="zakres-h" class="h2">Czym się zajmujemy</h2>
      <p class="lead">Cztery obszary, w których realizujemy zlecenia — dla klientów indywidualnych i inwestorów.</p>
    </div>
    {service_rows()}
  </div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee__track">
    <span>Budowa domów</span><span>Wykończenia wnętrz</span><span>Remonty</span><span>Roboty ziemne</span><span>Płyty fundamentowe</span><span>Elewacje</span>
    <span>Budowa domów</span><span>Wykończenia wnętrz</span><span>Remonty</span><span>Roboty ziemne</span><span>Płyty fundamentowe</span><span>Elewacje</span>
  </div>
</div>

<section class="section" aria-labelledby="realizacje-h">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Realizacje</p>
      <h2 id="realizacje-h" class="h2">Dwa oblicza naszej pracy</h2>
    </div>
    <div class="feature-stack" style="margin-top:clamp(2rem,4vw,3.5rem)">
      <article class="feature">
        <figure class="feature__media reveal-img">
          {pic("content-oferta", "Jasne wnętrze po wykończeniu — salon z drewnianą podłogą i wysokimi oknami", sizes="(min-width: 860px) 46vw, 100vw")}
        </figure>
        <div class="feature__body">
          <p class="eyebrow">Wykończenia</p>
          <h3>Prace wykończeniowe — domy, mieszkania, biura</h3>
          <p>Odmienimy wygląd Twojego mieszkania, domu lub biura. Działamy terminowo i&nbsp;kompleksowo — sprawdź!</p>
          <a class="link-arrow" href="/oferta/uslugi-wykonczeniowe/">Dowiedz się więcej {icon("arrow")}</a>
        </div>
      </article>
      <article class="feature feature--rev">
        <figure class="feature__media reveal-img">
          {pic("gal-budowa-budynku-06", "Ściany budynku wznoszone z bloczków betonowych — stan surowy", sizes="(min-width: 860px) 46vw, 100vw")}
        </figure>
        <div class="feature__body">
          <p class="eyebrow">Budowa</p>
          <h3>Prace budowlane — kompleksowo i&nbsp;terminowo</h3>
          <p>Realizujemy prace budowlane na terenie całego kraju. Zapraszamy do współpracy Klientów indywidualnych i&nbsp;inwestorów.</p>
          <a class="link-arrow" href="/oferta/uslugi-budowlane/">Dowiedz się więcej {icon("arrow")}</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--soft" aria-labelledby="o-firmie-h">
  <div class="wrap">
    <div class="split split--media">
      <figure class="feature__media reveal-img">
        {pic("article-main-f-1", "Kolaż zdjęć z budowy: wznoszone ściany, praca przy konstrukcji i montaż stolarki", sizes="(min-width: 860px) 44vw, 100vw")}
      </figure>
      <div>
        <p class="eyebrow">O firmie</p>
        <h2 id="o-firmie-h" class="h2">Firma Ogólnobudowlana Mateusz Drawc — Linia, woj. pomorskie</h2>
        <div class="prose" style="margin-top:1.25rem">
          <p>Wybierz <strong>doświadczoną i&nbsp;godną zaufania firmę remontowo-budowlaną</strong>. Specjaliści z&nbsp;Firmy Ogólnobudowlanej Mateusz Drawc są do&nbsp;Twojej dyspozycji. Realizujemy zlecenia na&nbsp;terenie całej Polski, co&nbsp;wyróżnia nas na&nbsp;tle konkurencji. <strong>Tworzymy funkcjonalne domy i&nbsp;lokale użytkowe</strong>, realizujemy inwestycje, a&nbsp;także odmieniamy wygląd wnętrz mieszkań, domów czy&nbsp;biur. Dodatkowo realizujemy prace ziemne — świadczymy <a href="/oferta/uslugi-koparko-ladowarka/">usługi koparko-ładowarką</a>.</p>
          <p>Przekonaj się, że&nbsp;współpraca z&nbsp;nami to&nbsp;gwarancja atrakcyjnych cen i&nbsp;terminowości. Zapraszamy!</p>
        </div>
        <p style="margin-top:1.5rem"><a class="link-arrow" href="/o-firmie/">Poznaj naszą firmę {icon("arrow")}</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="cta-h">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Kontakt</p>
        <h2 id="cta-h" class="display" style="font-size:clamp(2rem,4.4vw,3.4rem)">Napisz lub zadzwoń — czekamy na&nbsp;Ciebie</h2>
        <p class="lead">Opisz zakres prac albo zadzwoń bezpośrednio. Odpowiemy na pytania i&nbsp;ustalimy szczegóły współpracy.</p>
        <div class="btn-row" style="margin-top:2rem">
          <a class="btn btn--accent" href="/kontakt/"><span>Napisz do nas</span>{icon("arrow")}</a>
          <a class="btn btn--light" href="mailto:{EMAIL}">{icon("mail")}<span>{EMAIL}</span></a>
        </div>
      </div>
      <div class="stats">
        <div class="stat">
          <div class="stat__num"><span class="count" data-count="17">17</span></div>
          <p class="stat__label">lat doświadczenia</p>
        </div>
        <div class="stat">
          <div class="stat__num"><span class="count" data-count="100">100</span>%</div>
          <p class="stat__label">zaangażowania</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''


# =====================================================================
# O FIRMIE
# =====================================================================
ABOUT_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="split split--wide-left">
      <div class="prose">
        <p class="lead" style="margin-bottom:1.35rem"><strong>Firma Ogólnobudowlana Mateusz Drawc znajduje się w&nbsp;miejscowości Linia w&nbsp;woj. pomorskim</strong>, jednak działamy na&nbsp;terenie całej Polski. Choć działalność założyliśmy kilka lat temu, możemy poszczycić się <strong>17-letnim doświadczeniem</strong> w&nbsp;branży remontowo-budowlanej.</p>
        <p>Na koncie mamy zatem setki imponujących projektów, które zrealizowaliśmy dla osób prywatnych i&nbsp;wielu firm. Dodatkowo jesteśmy podwykonawcą producenta płyt fundamentowych PARATI.</p>
        <h2 class="h2" style="margin-top:2rem">Ekipa remontowo-budowlana godna zaufania</h2>
        <p>Jeśli marzysz o&nbsp;funkcjonalnym, stylowym domu lub odnowionym, wyremontowanym biurze — jesteśmy do&nbsp;Twojej dyspozycji. Od&nbsp;lat <strong>tworzymy zachwycające wnętrza dopasowane do&nbsp;indywidualnych potrzeb</strong>. Działamy kompleksowo — od&nbsp;szczegółowego opracowania projektu aż po&nbsp;zakup materiałów budowlanych, dzięki czemu zaoszczędzisz sporo czasu! Nie&nbsp;zwlekaj dłużej i&nbsp;już dziś dołącz do&nbsp;grona zadowolonych Klientów. Czekamy na&nbsp;Ciebie.</p>
      </div>
      <figure class="media media--4x3">
        {pic("photo-about-us", "Żółty kask budowlany, miara i narzędzia na tle projektu architektonicznego", sizes="(min-width: 860px) 38vw, 100vw")}
      </figure>
    </div>

    <div class="facts" style="margin-top:min(6vw,3.5rem)">
      <div class="fact"><span class="fact__k">Doświadczenie</span><span class="fact__v">17 lat w branży</span></div>
      <div class="fact"><span class="fact__k">Realizacje</span><span class="fact__v">setki projektów</span></div>
      <div class="fact"><span class="fact__k">Zasięg</span><span class="fact__v">cała Polska</span></div>
      <div class="fact"><span class="fact__k">Partner</span><span class="fact__v">podwykonawca PARATI</span></div>
    </div>
  </div>
</section>

<section class="section--dark section" aria-labelledby="ekipa-h">
  <div class="wrap">
    <div class="split split--media">
      <figure class="media media--3x2">
        {pic("bg-parallax-subpage-o-nas", "Ekipa remontowa przy pracy — montaż i wykończanie wnętrza", sizes="(min-width: 860px) 42vw, 100vw")}
      </figure>
      <div>
        <p class="eyebrow">Jak pracujemy</p>
        <h2 id="ekipa-h" class="h2">Kompleksowo — od projektu po&nbsp;zakup materiałów</h2>
        <ul class="checklist" style="margin-top:1.25rem">
          <li>Szczegółowe opracowanie projektu i&nbsp;ustalenie zakresu prac</li>
          <li>Pomoc w&nbsp;wyborze materiałów od sprawdzonych marek</li>
          <li>Zakup materiałów budowlanych oraz wykończeniowych</li>
          <li>Realizacja prac przez jedną ekipę — budowlaną i&nbsp;wykończeniową</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Zakres działalności</p>
      <h2 class="h2">Co możesz nam zlecić</h2>
    </div>
    <div class="grid grid-4" style="margin-top:2rem">
'''

for _sid, _title, _img, _desc in SERVICES:
    ABOUT_BODY += f'''      <article class="card">
        <figure class="card__media">
          {pic(_img, "", sizes="(min-width: 1000px) 23vw, (min-width: 600px) 45vw, 100vw", aria_hidden=True)}
        </figure>
        <div class="card__body">
          <h3 class="h3">{_title}</h3>
          <p>{_desc}</p>
          <a class="link-arrow" href="/oferta/{_sid}/">Czytaj więcej {icon("arrow")}</a>
        </div>
      </article>
'''

ABOUT_BODY += f'''    </div>
  </div>
</section>

{cta_section("Porozmawiajmy o Twojej inwestycji", "Zadzwoń lub napisz — odpowiemy na pytania dotyczące zakresu prac, terminów i materiałów.")}
'''


# =====================================================================
# OFERTA
# =====================================================================
OFERTA_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="split split--wide-left">
      <div class="prose">
        <p class="lead" style="margin-bottom:1.35rem">W Firmie Ogólnobudowlanej Mateusz Drawc od&nbsp;lat świadczymy kompleksowe <strong>usługi remontowo-budowlane</strong>. Z&nbsp;naszego wsparcia korzystają inwestorzy oraz Klienci indywidualni z&nbsp;całej Polski. Odmieniliśmy setki wnętrz domów, mieszkań i&nbsp;biur, a&nbsp;także mieliśmy okazję wybudować wiele funkcjonalnych obiektów. Przekonaj się, że&nbsp;jesteśmy partnerem biznesowym godnym zaufania!</p>
        <h2 class="h3" style="margin-top:1.6rem">Sprawdź, co możemy dla Ciebie zrobić</h2>
        <ul class="checklist" style="margin-top:.75rem">
          <li><a href="/oferta/uslugi-budowlane/">usługi budowlane</a> — domy pod klucz i&nbsp;budowa domów w&nbsp;stanie surowym, budowa obiektów,</li>
          <li><a href="/oferta/uslugi-remontowe/">prace remontowe</a>,</li>
          <li><a href="/oferta/uslugi-wykonczeniowe/">prace wykończeniowe</a>,</li>
          <li><a href="/oferta/uslugi-koparko-ladowarka/">usługi koparko-ładowarką</a>.</li>
        </ul>
      </div>
      <figure class="media media--4x3">
        {pic("content-oferta", "Wnętrze po wykończeniu — jasny salon z drewnianą podłogą i wysokimi oknami", sizes="(min-width: 860px) 38vw, 100vw")}
      </figure>
    </div>

    <hr class="rule">

    <div class="prose prose--aside">
      <h2 class="h2">Stawiamy na jakość — wykorzystujemy najlepsze materiały wykończeniowe</h2>
      <p>Aby mieć pewność, że&nbsp;odnowione wnętrze Twojego domu lub biura będzie prezentowało się nienagannie przez długi czas, istotne jest zarówno doświadczenie ekipy remontowej, jak i&nbsp;jakość użytych materiałów. Decydując się na&nbsp;współpracę z&nbsp;naszą firmą, masz gwarancję tego, że&nbsp;pomożemy Ci&nbsp;w&nbsp;doborze produktów od sprawdzonych i&nbsp;cenionych marek w&nbsp;branży. Jesteśmy do&nbsp;dyspozycji — zapraszamy!</p>
    </div>
  </div>
</section>

<section class="section section--soft" aria-labelledby="uslugi-h">
  <div class="wrap">
    <h2 id="uslugi-h" class="h2">Usługi</h2>
    <div class="grid grid-4" style="margin-top:2rem">
'''

for _sid, _title, _img, _desc in SERVICES:
    OFERTA_BODY += f'''      <article class="card">
        <figure class="card__media">
          {pic(_img, "", sizes="(min-width: 1000px) 23vw, (min-width: 600px) 45vw, 100vw", aria_hidden=True)}
        </figure>
        <div class="card__body">
          <h3 class="h3">{_title}</h3>
          <p>{_desc}</p>
          <a class="link-arrow" href="/oferta/{_sid}/">Czytaj więcej {icon("arrow")}</a>
        </div>
      </article>
'''

OFERTA_BODY += f'''    </div>
  </div>
</section>

{cta_section("Zapytaj o wycenę", "Napisz, jaki zakres prac Cię interesuje — wskażemy kolejne kroki i&nbsp;ustalimy szczegóły.")}
'''


# =====================================================================
# USŁUGI BUDOWLANE
# =====================================================================
BUDOWLANE_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="split split--wide-left">
      <div>
        <div class="prose">
          <p class="lead" style="margin-bottom:1.35rem">Świadczymy kompleksowe <strong>usługi budowlane</strong>. Działamy terminowo i&nbsp;rzetelnie, zawsze mając na&nbsp;uwadze zadowolenie Klienta. Jeśli marzysz o&nbsp;własnym domu, jesteśmy od&nbsp;tego, aby pomóc Ci&nbsp;w&nbsp;spełnieniu tego marzenia!</p>
          <p>Sprawdź, co wchodzi w&nbsp;zakres świadczonych usług:</p>
        </div>
        <ul class="checklist" style="margin-top:0.75rem">
          <li>gładzie i&nbsp;tynki</li>
          <li>wylewanie fundamentów</li>
          <li>szpachlowanie i&nbsp;malowanie ścian</li>
          <li>murowanie ścian</li>
          <li>montaż paneli i&nbsp;parkietów</li>
          <li>układanie ceramiki</li>
          <li>wykonywanie elewacji</li>
          <li>biały montaż</li>
        </ul>
        <div class="prose" style="margin-top:1.5rem">
          <p>Przekonaj się, że&nbsp;wiemy niemal wszystko o&nbsp;budowie domów! Na&nbsp;koncie mamy wiele imponujących realizacji — działamy na&nbsp;terenie całej Polski! Możesz liczyć na&nbsp;nasze wsparcie również przy wyborze działki i&nbsp;projektu.</p>
        </div>
      </div>
      <div>
        <figure class="media media--4x3">
          {pic("content-uslugi-budowlane", "Wnętrze budynku w stanie surowym — betonowe ściany i otwory okienne", sizes="(min-width: 860px) 38vw, 100vw")}
        </figure>
        <div style="margin-top:1rem">{person_block("Płyty fundamentowe i budowa domów", "Mateusz", TEL, TEL_TXT)}</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="prose prose--aside">
      <h2 class="h2">Domy w stanie surowym i&nbsp;pod klucz</h2>
      <p>Nasza oferta skierowana jest również do&nbsp;inwestorów z&nbsp;całej Polski. Budujemy <strong>domy w&nbsp;stanie surowym</strong>, a&nbsp;także te gotowe do&nbsp;zamieszkania, czyli <strong>pod klucz</strong>. Jesteśmy partnerem godnym zaufania — z&nbsp;naszym wsparciem sprawnie zrealizujesz swoją inwestycję!</p>
      <p>Od lat tworzymy funkcjonalne i&nbsp;zachwycające domy. Cechuje nas nie tylko terminowość, ale i&nbsp;godna podziwu staranność. Niezależnie od&nbsp;tego, czy&nbsp;marzysz o&nbsp;domu jednorodzinnym, czy&nbsp;chcesz postawić tzw. bliźniaka — już dziś skontaktuj się z&nbsp;nami w&nbsp;celu ustalenia szczegółów.</p>
      <p><strong>Mateusz</strong> <a href="tel:{TEL}">{TEL_TXT}</a></p>
    </div>
  </div>
</section>

{related("uslugi-budowlane")}
{cta_section("Planujesz budowę domu?", "Zadzwoń do Mateusza i&nbsp;porozmawiaj o&nbsp;zakresie prac, kolejnych etapach i&nbsp;terminie.")}
'''


# =====================================================================
# USŁUGI WYKOŃCZENIOWE
# =====================================================================
WYKONCZENIOWE_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="split split--wide-left">
      <div>
        <div class="prose">
          <p class="lead" style="margin-bottom:1.35rem">Realizujemy <strong>usługi wykończeniowe mieszkań, domów oraz&nbsp;lokali użytkowych</strong>. Współpracujemy nie tylko z&nbsp;lokalnymi firmami, ale i&nbsp;z&nbsp;osobami prywatnymi, które marzą o&nbsp;stylowych mieszkaniach. Skontaktuj się z&nbsp;nami już dziś — chcemy poznać Twoje oczekiwania, dzięki czemu będziemy mogli przygotować projekt szyty na&nbsp;miarę potrzeb.</p>
        </div>
        <h2 class="h2" style="margin-top:1.75rem">Co obejmują prace wykończeniowe?</h2>
        <div class="prose" style="margin-top:0.75rem">
          <p>Nim przystąpimy do&nbsp;realizacji zlecenia, musimy dokładnie ustalić podział mieszkania. Na&nbsp;zlecenie Klientów pomagamy w&nbsp;zmianie układów pomieszczeń, montując w&nbsp;tym celu ścianki działowe. Następnie możemy przystąpić do&nbsp;dalszych prac, które obejmują:</p>
        </div>
        <ul class="checklist" style="margin-top:0.75rem">
          <li>ułożenie instalacji elektrycznej i&nbsp;wodno-kanalizacyjnej</li>
          <li>układanie podłogi i&nbsp;wylewek</li>
          <li>tynkowanie ścian i&nbsp;sufitów</li>
          <li>montaż płyt gipsowo-kartonowych, suchych tynków lub sufitów podwieszanych</li>
          <li>układanie posadzek i&nbsp;glazury</li>
          <li>malowanie ścian</li>
          <li>układanie parkietu</li>
          <li>montaż stolarki drzwiowej</li>
          <li>montaż osprzętu elektrycznego</li>
          <li>montaż sprzętu AGD</li>
          <li>montaż mebli</li>
        </ul>
      </div>
      <div>
        <figure class="media media--4x3">
          {pic("content-uslugi-wykonczeniowe", "Wnętrze mieszkania w trakcie wykończenia — drabina i odświeżone ściany", sizes="(min-width: 860px) 38vw, 100vw")}
        </figure>
        <div style="margin-top:1rem">{person_block("Elewacja i roboty wykończeniowe", "Tadeusz", "+48691858193", "691 858 193")}</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="prose prose--aside">
      <h2 class="h2">Domy i&nbsp;mieszkania pod klucz</h2>
      <p>Oferujemy <strong>wykańczanie domów i&nbsp;mieszkań pod klucz</strong>. Usługa ta cieszy się ogromnym powodzeniem wśród Klientów, którzy nie&nbsp;mają czasu na&nbsp;pilnowanie etapów prac remontowych. Gwarantujemy, że&nbsp;sprawnie stworzymy funkcjonalną przestrzeń, w&nbsp;której będzie Ci&nbsp;się wspaniale mieszkało! Projektujemy wnętrza, które odpowiadają indywidualnym gustom i&nbsp;preferencjom. Zaufaj naszemu doświadczeniu!</p>
      <p><strong>Tadeusz</strong> <a href="tel:+48691858193">691 858 193</a></p>
    </div>
  </div>
</section>

{related("uslugi-wykonczeniowe")}
{cta_section("Chcesz wykończyć mieszkanie pod klucz?", "Opisz metraż i&nbsp;zakres — przygotujemy propozycję i&nbsp;ustalimy szczegóły.")}
'''


# =====================================================================
# USŁUGI REMONTOWE
# =====================================================================
REMONTOWE_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="split split--wide-left">
      <div>
        <div class="prose">
          <p class="lead" style="margin-bottom:1.35rem">Świadczymy kompleksowe <strong>usługi remontowe</strong>. Nasi pracownicy odmienią wygląd każdego pomieszczenia w&nbsp;domu lub biurze — przekonaj się, że&nbsp;nie&nbsp;ma dla nas rzeczy niemożliwych. Doskonale wiemy, że&nbsp;zależy Ci&nbsp;na&nbsp;czasie, dlatego gwarantujemy sprawną i&nbsp;rzetelną realizację prac.</p>
          <p>Sprawdź, co możemy dla Ciebie zrobić:</p>
        </div>
        <ul class="checklist" style="margin-top:0.75rem">
          <li>adaptacje poddaszy</li>
          <li>konstrukcje z&nbsp;płyt gipsowo-kartonowych</li>
          <li>szpachlowanie, gipsowanie i&nbsp;tynkowanie</li>
          <li>malowanie elewacji i&nbsp;dachów</li>
          <li>montaż stolarki okienno-drzwiowej</li>
          <li>montaż parapetów</li>
          <li>montaż sufitów podwieszanych</li>
          <li>ogrzewanie gazowe, elektryczne, geotermalne, podłogowe elektryczne</li>
          <li>ocieplenia dachów i&nbsp;poddaszy</li>
        </ul>
      </div>
      <div>
        <figure class="media media--4x3">
          {pic("content-uslugi-remontowe", "Prace remontowe — wygładzanie ściany pacą przez pracownika", sizes="(min-width: 860px) 38vw, 100vw")}
        </figure>
        <div style="margin-top:1rem">{person_block("Elewacja i roboty wykończeniowe", "Tadeusz", "+48691858193", "691 858 193")}</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="prose prose--aside">
      <h2 class="h2">Prace remontowe mieszkań, domów i&nbsp;biur</h2>
      <p>Niezależnie od&nbsp;tego, czy&nbsp;szukasz ekipy remontowej, której możesz <strong>zlecić remont mieszkania, domu czy&nbsp;biura</strong> — jesteśmy do&nbsp;Twojej dyspozycji. Dopasowujemy się do&nbsp;indywidualnych oczekiwań Klientów, ponieważ doskonale wiemy, że&nbsp;każdy ma inne potrzeby.</p>
      <p>Możesz nam zlecić zarówno drobne, jak i&nbsp;skomplikowane prace. Doskonale <strong>znamy obowiązujące trendy w&nbsp;branży remontowej</strong> — wiedzę tę wykorzystujemy na&nbsp;co dzień, swobodnie łącząc klasyczne rozwiązania. Stworzymy pomieszczenia, w&nbsp;których zakochasz się od pierwszego wejrzenia. Będzie estetycznie, solidnie i&nbsp;nowocześnie.</p>
      <p><strong>Tadeusz</strong> <a href="tel:+48691858193">691 858 193</a></p>
    </div>
  </div>
</section>

{related("uslugi-remontowe")}
{cta_section("Remont mieszkania lub biura?", "Napisz, co chcesz zmienić — doradzimy zakres prac i&nbsp;realny termin.")}
'''


# =====================================================================
# USŁUGI KOPARKO-ŁADOWARKĄ
# =====================================================================
KOPARKA_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="split split--wide-left">
      <div>
        <div class="prose">
          <p class="lead" style="margin-bottom:1.35rem">Szukasz firmy w&nbsp;okolicy woj. pomorskiego, która świadczy <strong>usługi koparko-ładowarką</strong>? Świetnie się składa — skontaktuj się już dziś z&nbsp;Firmą Ogólnobudowlaną Mateusza Drawca — na&nbsp;koncie mamy dziesiątki realizacji dla Klientów indywidualnych i&nbsp;biznesowych. Działamy na&nbsp;terenie całej Polski.</p>
          <p>Dysponujemy <strong>nowoczesną i&nbsp;niezawodną flotą</strong>, która sprawnie poradzi sobie z&nbsp;najbardziej skomplikowanymi zleceniami. Koparko-ładowarki to maszyny budowlane niezbędne podczas wielu inwestycji, do&nbsp;których zalicza się m.in. przygotowywanie fundamentów lub przygotowanie terenu pod inwestycję.</p>
        </div>
      </div>
      <div>
        <figure class="media media--4x3">
          {pic("content-uslugi-koparko-ladowarka", "Koparko-ładowarka podczas prac ziemnych na budowie", sizes="(min-width: 860px) 38vw, 100vw")}
        </figure>
        <div style="margin-top:1rem">{person_block("Usługi koparką", "Piotr", "+48609518723", "609 518 723")}</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="split">
      <div class="prose">
        <h2 class="h2">Wykopy pod fundamenty, skarpowanie i&nbsp;rozładunek</h2>
        <p>Jesteśmy partnerem biznesowym godnym zaufania. Wszelkie prace realizujemy sprawnie i&nbsp;z&nbsp;należytą starannością. Sprawdź, co możesz nam zlecić w&nbsp;ramach usług koparko-ładowarką.</p>
        <p>Skontaktuj się z&nbsp;nami już dziś w&nbsp;celu ustalenia szczegółów współpracy.</p>
        <p><strong>Piotr</strong> <a href="tel:+48609518723">609 518 723</a></p>
      </div>
      <ul class="checklist">
        <li><strong>wykopy pod fundamenty</strong></li>
        <li>wykopy pod instalacje elektryczne i&nbsp;wodociągowe</li>
        <li>skarpowanie i&nbsp;korytowanie</li>
        <li>rozładunek i&nbsp;załadunek</li>
      </ul>
    </div>
  </div>
</section>

{related("uslugi-koparko-ladowarka")}
{cta_section("Potrzebujesz prac ziemnych?", "Zadzwoń do Piotra i&nbsp;ustal termin oraz zakres robót.")}
'''


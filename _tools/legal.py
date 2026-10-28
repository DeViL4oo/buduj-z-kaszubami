# -*- coding: utf-8 -*-
"""Dokumenty prawne — treść przeniesiona z dotychczasowego serwisu."""
from common import *
from pages import crumb

PRIVACY_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="prose legal" style="max-width:76ch">
      <p class="lead">Ochrona prywatności Użytkowników jest dla <strong>{FIRMA}</strong> szczególnie ważna. Z&nbsp;tego względu Użytkownicy Serwisu <strong>budujzkaszubami.pl</strong> mają zagwarantowane wysokie standardy ochrony prywatności. <strong>{FIRMA}</strong> jako Administrator danych dba o&nbsp;bezpieczeństwo udostępnionych przez Użytkowników danych.</p>

      <p>Celem Administratora jest również należyte informowanie Użytkowników o&nbsp;prawach i&nbsp;obowiązkach związanych z&nbsp;przetwarzaniem danych osobowych, szczególnie wobec treści przepisów o&nbsp;ochronie danych osobowych określonych w&nbsp;rozporządzeniu Parlamentu Europejskiego i&nbsp;Rady (UE) 2016/679 z&nbsp;dnia 27.04.2016&nbsp;r. w&nbsp;sprawie ochrony osób fizycznych w&nbsp;związku z&nbsp;przetwarzaniem danych osobowych i&nbsp;w&nbsp;sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (dalej jako „RODO”).</p>

      <p>Użytkownikiem jest każda osoba fizyczna, której dane dotyczą, korzystająca z&nbsp;serwisu internetowego <strong>budujzkaszubami.pl</strong> lub usług elektronicznych dostępnych za pośrednictwem Serwisu.</p>

      <p>Administratorem danych osobowych udostępnionych przez Użytkownika w&nbsp;Serwisie <strong>budujzkaszubami.pl</strong> jest <strong>{FIRMA}, ul. Długa 127, 84-223 Linia, NIP {NIP},</strong> <em>(dalej jako „Administrator”)</em>.</p>

      <ol class="legal-list">
        <li>
          <h2>Korzystanie z Serwisu przez Użytkownika a ochrona danych osobowych</h2>
          <ol>
            <li>Korzystanie z&nbsp;Serwisu <strong>budujzkaszubami.pl</strong> jest anonimowe i&nbsp;nie&nbsp;wymaga rejestracji Użytkownika, ani przekazywania przez niego w&nbsp;trakcie korzystania z&nbsp;Serwisu jakichkolwiek danych umożliwiających Administratorowi identyfikację Użytkownika w&nbsp;sposób bezpośredni lub pośredni w&nbsp;rozumieniu przepisów Rozporządzenia Parlamentu Europejskiego i&nbsp;Rady (UE) 2016/679 z&nbsp;dnia 27 kwietnia 2016&nbsp;r. w&nbsp;sprawie ochrony osób fizycznych w&nbsp;związku z&nbsp;przetwarzaniem danych osobowych i&nbsp;w&nbsp;sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (dalej „RODO”).</li>
            <li>Administrator w&nbsp;ramach Serwisu umożliwia Użytkownikom wyłącznie przeglądanie treści opublikowanych w&nbsp;Serwisie. Administrator nie&nbsp;udostępnia w&nbsp;ramach Serwisu funkcjonalności pozwalających na&nbsp;bezpośrednie udostępnienie przez Użytkownika w&nbsp;Serwisie danych osobowych. Jednakże Użytkownik może udostępnić swoje dane osobowe poprzez kontakt z&nbsp;Administratorem w&nbsp;wykorzystaniem podanych w&nbsp;Serwisie danych kontaktowych Administratora (adresu e-mail, adresu pocztowego, telefonu) lub poprzez nawiązanie relacji handlowej (zawarcie umowy).</li>
            <li>Administrator Serwisu zastrzega sobie prawo zbierania i&nbsp;przetwarzania anonimowych statystyk dotyczących Użytkowników, w&nbsp;celu poznania ich preferencji i&nbsp;oceny respektowania zasad korzystania z&nbsp;Serwisu. Powyższe dane nie&nbsp;stanowią danych osobowych w&nbsp;rozumieniu przepisów RODO i&nbsp;nie&nbsp;podlegają ochronie w&nbsp;nich przewidzianej.</li>
          </ol>
        </li>
        <li>
          <h2>Pliki Cookies</h2>
          <ol>
            <li>Administrator informuje, iż podczas korzystania z&nbsp;Serwisu w&nbsp;urządzeniu końcowym Użytkownika zapisywane są fragmenty kodu zwane „cookies”, które są plikami tekstowymi odpowiadającymi zapytaniom HTTP kierowanym do&nbsp;serwera Administratora. Pliki „cookies” są instalowane przez każdą przeglądarkę, z&nbsp;której Użytkownik odwiedza Serwis. Pliki „cookies” wykorzystywane są w&nbsp;Serwisie w&nbsp;celu:
              <ol>
                <li>utrzymania technicznej poprawności i&nbsp;ciągłości sesji pomiędzy serwerem Serwisu a&nbsp;urządzeniem końcowym Użytkownika;</li>
                <li>optymalizacji korzystania przez Użytkownika ze stron internetowych Serwisu i&nbsp;dostosowania sposobu ich wyświetlania na&nbsp;urządzeniu końcowym Użytkownika;</li>
                <li>zapewnienia bezpieczeństwa korzystania z&nbsp;Serwisu;</li>
                <li>zbierania statystyk odwiedzin stron Serwisu wspierających ulepszanie ich struktury i&nbsp;zawartości;</li>
                <li>wyświetlania na&nbsp;urządzeniu końcowym Użytkownika treści dostosowanych do&nbsp;jego preferencji.</li>
              </ol>
              <p>Szczegółowe informacje odnośnie stosowanych przez Administratora plików cookie oraz zarządzania nimi dostępne są w&nbsp;<a href="/polityka-cookies/">Polityce Cookies</a>.</p>
            </li>
          </ol>
        </li>
        <li>
          <h2>Zmiany Polityki prywatności</h2>
          <p>W celu uaktualnienia informacji zawartych w&nbsp;niniejszej Polityce prywatności oraz jej zgodności z&nbsp;obowiązującymi przepisami prawa, niniejsza Polityka prywatności może ulec zmianie. W&nbsp;przypadku zmiany treści Polityki prywatności, zmieniona zostanie data jej aktualizacji wskazana na&nbsp;końcu jej tekstu. W&nbsp;celu zasięgnięcia informacji o&nbsp;sposobie ochrony danych osobowych, Administrator rekomenduje Użytkownikom regularne zapoznawanie się z&nbsp;postanowieniami Polityki Prywatności.</p>
        </li>
        <li>
          <h2>Informacje kontaktowe</h2>
          <p>W celu uzyskania jakichkolwiek informacji dotyczących niniejszej Polityki Prywatności, Użytkownik może skontaktować się z&nbsp;Administratorem danych osobowych: <strong>{FIRMA}, {STREET}, {POST} {CITY},</strong> z&nbsp;wykorzystaniem następujących danych kontaktowych: <strong><a href="mailto:{EMAIL}">{EMAIL}</a></strong>.</p>
          <p>Ponadto istnieje również możliwość kontaktu drogą pocztową pod adresem: <strong>{STREET}, {POST} {CITY}</strong>.</p>
        </li>
      </ol>

      <p class="legal-date">Ostatnia aktualizacja niniejszego dokumentu miała miejsce dnia 13.02.2026.</p>
    </div>
  </div>
</section>
'''


COOKIES_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="prose legal" style="max-width:76ch">
      <p class="lead">Korzystamy z&nbsp;plików cookies w&nbsp;celu poprawienia efektywności i&nbsp;zaproponowania Użytkownikowi coraz doskonalszych funkcjonalności serwisu internetowego <strong>budujzkaszubami.pl</strong> (dalej jako Serwis) oraz bardziej dopasowanych do&nbsp;Użytkownika treści. W&nbsp;celu zapewnienia przejrzystości działań zostaje przyjęta niniejsza Polityka Cookies, która określa szczegółowe zasady korzystania przez Serwis internetowy z&nbsp;plików cookies.</p>

      <p>Dane za pomocą plików cookies gromadzone są przez <strong>{FIRMA}</strong>, adres <strong>ul. Długa lok. 127, 84-223 Linia</strong>, numer NIP: <strong>{NIP}</strong>, numer REGON: <strong>{REGON}</strong>. W&nbsp;przypadku stwierdzenia, że&nbsp;dane zawarte w&nbsp;plikach cookies są danymi osobowymi <strong>{FIRMA}</strong> uznawany jest za Administratora danych, zaś Użytkownikowi przysługują wszystkie uprawnienia zawarte w&nbsp;<a href="/polityka-prywatnosci/">Polityce Prywatności</a>.</p>

      <p>Użytkownikiem jest każda osoba, której dane dotyczą, korzystająca z&nbsp;naszego Serwisu internetowego oraz innych powiązanych z&nbsp;nim witryn, komunikacji oraz usług (dalej jako <em>Użytkownik</em>).</p>

      <ol class="legal-list">
        <li>
          <h2>Pliki cookies</h2>
          <p>Pliki cookies („ciasteczka”) to fragmenty kodu, które są plikami tekstowymi odpowiadającymi zapytaniom HTTP kierowanym do&nbsp;naszego serwera. Pliki te zapisywane są przez każdą przeglądarkę, z&nbsp;której Użytkownik odwiedza nasz Serwis. Dzięki informacjom zawartym w&nbsp;plikach cookies wiemy, w&nbsp;jaki sposób Użytkownicy korzystają z&nbsp;naszego Serwisu.</p>
          <p>Pliki cookies służą nam do&nbsp;zapewnienia optymalnej obsługi wizyty Użytkownika w&nbsp;Serwisie oraz umożliwiają szybszy i&nbsp;łatwiejszy dostęp do&nbsp;informacji, a&nbsp;także w&nbsp;celu zaproponowania Użytkownikowi coraz doskonalszych funkcjonalności Serwisu internetowego oraz bardziej dopasowanych do&nbsp;Użytkownika treści.</p>
          <p>Przechowywana informacja lub uzyskiwanie do&nbsp;niej dostępu nie&nbsp;powoduje zmian konfiguracyjnych w&nbsp;urządzeniu Użytkownika i&nbsp;oprogramowaniu na&nbsp;nim zainstalowanym.</p>
          <p>Informacje zawarte w&nbsp;plikach cookies uznawane są za dane osobowe jedynie w&nbsp;powiązaniu z&nbsp;innymi danymi osobowymi dostępnymi na&nbsp;temat danego Użytkownika. My za pomocą plików cookies staramy się zbierać o&nbsp;Użytkowniku jedynie anonimowe dane, służące do&nbsp;wygody korzystania z&nbsp;portalu oraz minimalizacji uciążliwości reklam.</p>
        </li>
        <li>
          <h2>Rodzaje i cele korzystania z plików cookies</h2>
          <p>Korzystamy z&nbsp;plików cookies i&nbsp;innych podobnych technologii w&nbsp;celu rozpoznawania Użytkownika podczas jego wizyt w&nbsp;naszym Serwisie, zapamiętywania jego preferencji oraz wyświetlania mu odpowiednich, dostosowanych do&nbsp;niego treści. Dzięki plikom cookies interakcje Użytkownika z&nbsp;nami są szybsze i&nbsp;bardziej skuteczne. Ponadto pliki cookies umożliwiają nam prezentowanie Użytkownikowi dopasowanych do&nbsp;niego treści, bez konieczności przeprowadzania ankiet.</p>
          <p>W Serwisie wykorzystywane są dwa rodzaje plików cookies:</p>
          <ul>
            <li><strong>Cookies sesyjne</strong> — są to pliki tymczasowe, które pozostają na&nbsp;urządzeniu Użytkownika aż do&nbsp;opuszczenia przez niego Serwisu lub wyłączenia przeglądarki internetowej. W&nbsp;takim przypadku informacje zapisane w&nbsp;plikach cookies sesyjnych są automatycznie usuwane.</li>
            <li><strong>Cookies stałe (permanentne)</strong> — są to pliki, które pozostają na&nbsp;urządzeniu Użytkownika przez określony w&nbsp;parametrach plików cookies okres lub do&nbsp;momentu ich ręcznego usunięcia.</li>
          </ul>
          <p>W obszarze Serwisu wykorzystywane są również inne dostępne technologie, pozwalające na&nbsp;zapisywanie informacji w&nbsp;przeglądarce w&nbsp;odpowiednich magazynach danych (Session Storage, Local Storage), a&nbsp;także umieszczane są we&nbsp;fragmenty kodów narzędzi analitycznych dostarczanych przez innych dostawców, które umożliwiają zapisanie plików cookies w&nbsp;domenach tych usług.</p>
          <p>Poniżej opisane zostały poszczególne kategorie cookies, które są wykorzystywane w&nbsp;naszym Serwisie:</p>
          <p><strong>Cookies techniczne</strong> — są niezbędne, aby strona Serwisu mogła działać prawidłowo. Odnoszą się one do&nbsp;funkcjonalności naszych witryn internetowych i&nbsp;pozwalają nam ulepszyć usługi, które oferujemy za pośrednictwem naszych witryn internetowych, na przykład poprzez umożliwienie przenoszenia informacji między stronami naszej witryny internetowej, aby uniknąć konieczności ponownego wprowadzania informacji, lub rozpoznając preferencje Użytkownika po powrocie na&nbsp;stronę naszego Serwisu.</p>
          <p>Wykorzystujemy je w&nbsp;celu:</p>
          <ul>
            <li>zapewnienia bezpieczeństwa;</li>
            <li>utrzymania sesji, kiedy Użytkownik odwiedza i&nbsp;loguje się do&nbsp;swojego konta klienta;</li>
            <li>zapewnienia odpowiedniego wyświetlania strony — w&nbsp;zależności od tego, z&nbsp;jakiego urządzenia korzysta Użytkownik;</li>
            <li>dostosowywania naszych usług do&nbsp;wyborów Użytkownika;</li>
            <li>zapamiętania, czy Użytkownik wyraża zgodę na&nbsp;wyświetlanie niektórych treści.</li>
          </ul>
          <p><strong>Cookies analityczne</strong> — pozwalają nam rozpoznać i&nbsp;policzyć liczbę Użytkowników odwiedzających nasz Serwis, zobaczyć, w&nbsp;jaki sposób odwiedzający poruszają się po&nbsp;Serwisie, gdy z&nbsp;niego korzystają oraz rejestrować, które treści przeglądają i&nbsp;którymi są zainteresowani. Pomaga nam to&nbsp;określić, jak często strony i&nbsp;reklamy są odwiedzane oraz które obszary naszego Serwisu są najpopularniejsze. Umożliwia nam to&nbsp;ulepszanie oferowanych usług, sprawiając że&nbsp;nasi Użytkownicy znajdują informacje, których szukają. Są one również niezbędne, aby rozliczać się z&nbsp;naszymi Zaufanymi Partnerami, mierzyć efektywność naszych działań marketingowych bez identyfikacji danych osobowych.</p>
          <p>Wykorzystujemy je w&nbsp;celu:</p>
          <ul>
            <li>badania statystyk dotyczących ruchu na&nbsp;stronie oraz sprawdzania źródła ruchu (kierunki przekierowania);</li>
            <li>wykrywania różnego rodzaju nadużyć np.&nbsp;sztuczny ruch internetowy (boty), ataki ddos;</li>
            <li>ograniczenia niepożądanych działań marketingowych;</li>
            <li>mierzenia skuteczności akcji marketingowych prowadzonych na&nbsp;rzecz Serwisu, np.&nbsp;w&nbsp;sieci reklamowej Google, w&nbsp;programach partnerskich, na&nbsp;zewnętrznych stronach internetowych;</li>
            <li>rozliczania się z&nbsp;Zaufanymi Partnerami za usługi reklamowe w&nbsp;oparciu o&nbsp;aktywność użytkownika np.&nbsp;kliknięcia.</li>
          </ul>
          <p><strong>Cookies marketingowe</strong> — są używane, gdy Użytkownik wyrazi na&nbsp;to&nbsp;zgodę i&nbsp;tylko wtedy gdy zastosowane przez nasz Serwis funkcjonalności oraz formy reklamy tego wymagają.</p>
          <p>Wykorzystujemy je w&nbsp;celu:</p>
          <ul>
            <li>wyświetlania reklam, które są istotne i&nbsp;interesujące dla konkretnego użytkownika. Dotyczą profilowania reklam wyświetlanych zarówno na&nbsp;zewnętrznych serwisach internetowych, jak i&nbsp;na&nbsp;stronie naszego Serwisu, stosownie do&nbsp;preferencji użytkowników w&nbsp;zakresie wyboru towarów, na&nbsp;podstawie danych posiadanych przez Serwis, w&nbsp;tym zachowania użytkowników w&nbsp;Serwisie.</li>
          </ul>
          <p>Wchodząc na&nbsp;stronę Serwisu, Użytkownik może nie&nbsp;zgodzić się na&nbsp;korzystanie z&nbsp;plików cookies analitycznych i&nbsp;marketingowych. Wówczas nie&nbsp;będziemy mogli prowadzić szczegółowych statystyk oraz dostosowywać naszych reklam w&nbsp;oparciu o&nbsp;informacje zebrane w&nbsp;naszym Serwisie. Nadal jednak będą wyświetlane reklamy o&nbsp;charakterze ogólnym zarówno na&nbsp;stronie Serwisu, jak i&nbsp;na&nbsp;innych serwisach internetowych.</p>
          <p>Do emisji reklam w&nbsp;Internecie, a&nbsp;także w&nbsp;zakresie innych narzędzi takich jak Google reCAPTCHA (narzędzie do&nbsp;ochrony przed spamem), wykorzystujemy technologie dostarczane przez firmy Google i&nbsp;Meta (Facebook), dlatego zwróć uwagę, czy wyrażasz zgodę na&nbsp;stosowanie tych narzędzi, w&nbsp;tym profilowanie reklam w&nbsp;Internecie i&nbsp;na&nbsp;Facebooku. Możesz sprawdzić oraz zarządzać swoimi ustawieniami prywatności i&nbsp;bezpieczeństwa na&nbsp;koncie Google, korzystając z&nbsp;linku <a href="https://g.co/privacytools" target="_blank" rel="noopener noreferrer">g.co/privacytools</a>. Więcej informacji na&nbsp;temat polityki prywatności Google, technologii stosowanych przez Google oraz warunków korzystania z&nbsp;usług Google znajdziesz na&nbsp;stronie <a href="https://policies.google.com/privacy?hl=pl#infochoices" target="_blank" rel="noopener noreferrer">https://policies.google.com/privacy?hl=pl#infochoices</a>. Informacje na&nbsp;temat zasad ochrony prywatności stosowanych przez firmę Meta (Facebook) oraz zarządzania ustawieniami prywatności są dostępne na&nbsp;stronie <a href="https://pl-pl.facebook.com/privacy/explanation/" target="_blank" rel="noopener noreferrer">https://pl-pl.facebook.com/privacy/explanation/</a>.</p>
          <p>Szczegółowe informacje o&nbsp;plikach cookie, ich czasie przechowywania oraz sposobach zarządzania nimi znajdują się w&nbsp;niniejszej Polityce Cookies.</p>
        </li>
        <li>
          <h2>Wyłączenie obsługi plików cookies</h2>
          <p>Przeglądarki internetowe domyślnie dopuszczają przechowywanie plików cookies. Jeśli Użytkownik nie&nbsp;chce otrzymywać plików cookies, może zmienić ustawienia swojej przeglądarki na&nbsp;komputerze lub innym urządzeniu, z&nbsp;którego korzysta w&nbsp;celu dostępu do&nbsp;naszego Serwisu. Dalsze korzystanie przez Użytkownika z&nbsp;naszego Serwisu bez zmiany ustawień oznacza, że&nbsp;Użytkownik zgadza się na&nbsp;otrzymywanie plików cookies technicznych w&nbsp;naszym Serwisie, które jak wskazaliśmy są dla nas niezbędne do&nbsp;prawidłowego funkcjonowania strony Serwisu.</p>
          <p>Większość przeglądarek internetowych posiada funkcję, która pozwala Użytkownikowi przeglądać i&nbsp;usuwać pliki cookie, w&nbsp;tym pliki cookie w&nbsp;naszym serwisie. Jednakże podkreślić należy, że&nbsp;brak możliwości zapisywania lub odczytywania plików cookies przez stronę internetową naszego Serwisu może uniemożliwić pełne i&nbsp;poprawne korzystanie z&nbsp;naszego Serwisu.</p>
          <p>Jeżeli Użytkownik używa różnych urządzeń do&nbsp;uzyskania dostępu do&nbsp;naszego Serwisu oraz jego przeglądania (np.&nbsp;komputera, smartfona, tabletu), powinien upewnić się, że&nbsp;każda przeglądarka na&nbsp;każdym urządzeniu dostosowana jest do&nbsp;preferencji związanych z&nbsp;plikami cookies.</p>
          <p>Sposób wyłączenia obsługi plików cookies zależy od przeglądarki, z&nbsp;której Użytkownik korzysta. Poniżej wskazany został sposób, w&nbsp;jaki Użytkownik może wyłączyć obsługę plików cookies w&nbsp;przeglądarce Google Chrome, Firefox, Safari, Opera oraz Internet Explorer.</p>

          <div class="legal-browser">
            <h3>Wyłączenie obsługi plików cookies w przeglądarce Google Chrome</h3>
            <ol>
              <li>W prawym górnym rogu przy pasku adresu przeglądarki Google Chrome wybierz trzy kropki ustawione pionowo.</li>
              <li>Wybierz <em>Ustawienia</em>, a&nbsp;następnie po&nbsp;lewej stronie kliknij <em>Prywatność i&nbsp;bezpieczeństwo</em>.</li>
              <li>Wybierz sekcję <em>Pliki cookie innych firm</em> i&nbsp;skonfiguruj własne ustawienia dla plików cookie.</li>
            </ol>
            <p>Więcej informacji o&nbsp;ustawieniach przeglądarki Google Chrome: <a href="https://support.google.com/accounts/answer/61416?hl=pl" target="_blank" rel="noopener noreferrer">https://support.google.com/accounts/answer/61416?hl=pl</a></p>
          </div>

          <div class="legal-browser">
            <h3>Wyłączenie obsługi plików cookies w przeglądarce Firefox</h3>
            <ol>
              <li>W prawym górnym rogu okna przeglądarki Firefox wybierz trzy poziome kreski.</li>
              <li>Wybierz <em>Ustawienia</em>, a&nbsp;następnie po&nbsp;lewej stronie kliknij <em>Prywatność i&nbsp;bezpieczeństwo</em>.</li>
              <li>Wybierz odpowiedni poziom bezpieczeństwa lub skonfiguruj własny.</li>
            </ol>
            <p>Więcej informacji o&nbsp;ustawieniach przeglądarki Firefox: <a href="https://support.mozilla.org/pl/kb/usuwanie-ciasteczek-i-danych-stron-firefox" target="_blank" rel="noopener noreferrer">https://support.mozilla.org/pl/kb/usuwanie-ciasteczek-i-danych-stron-firefox</a></p>
          </div>

          <div class="legal-browser">
            <h3>Wyłączenie obsługi plików cookies w przeglądarce Safari</h3>
            <p>Wybierz polecenie menu <em>Safari &gt; Preferencje</em>, kliknij w&nbsp;<em>Prywatność</em>, a&nbsp;następnie wykonaj dowolną z&nbsp;poniższych czynności:</p>
            <ul>
              <li><em>Blokuj wszystkie cookie</em></li>
              <li><em>Zapobiegaj śledzeniu poza witryną</em></li>
            </ul>
            <p>Więcej informacji o&nbsp;ustawieniach przeglądarki Safari: <a href="https://support.apple.com/pl-pl/guide/safari/sfri11471/mac" target="_blank" rel="noopener noreferrer">https://support.apple.com/pl-pl/guide/safari/sfri11471/mac</a></p>
          </div>

          <div class="legal-browser">
            <h3>Wyłączenie obsługi plików cookies w przeglądarce Opera</h3>
            <ol>
              <li>W prawym górnym rogu przy pasku adresu przeglądarki Opera wybierz trzy linie poziome.</li>
              <li>Wybierz <em>Przejdź do pełnych ustawień przeglądarki</em>.</li>
              <li>Wybierz <em>Prywatność i&nbsp;bezpieczeństwo</em>, a&nbsp;następnie dostosuj ustawienia do&nbsp;swoich preferencji.</li>
            </ol>
            <p>Więcej informacji o&nbsp;ustawieniach przeglądarki Opera: <a href="https://help.opera.com/pl/latest/web-preferences/#cookies" target="_blank" rel="noopener noreferrer">https://help.opera.com/pl/latest/web-preferences/#cookies</a></p>
          </div>

          <div class="legal-browser">
            <h3>Wyłączenie obsługi plików cookies w przeglądarce Edge</h3>
            <ol>
              <li>W prawym górnym rogu przy pasku adresu przeglądarki Edge wybierz trzy kropki ustawione poziomo.</li>
              <li>Wybierz <em>Ustawienia</em>, a&nbsp;następnie po&nbsp;lewej stronie kliknij <em>Pliki cookie i&nbsp;uprawnienia witryn</em>.</li>
              <li>Wybierz <em>Zarządzaj plikami cookie i&nbsp;danymi witryn oraz usuwaj je</em>.</li>
              <li>Dostosuj ustawienia plików cookie do&nbsp;swoich preferencji.</li>
            </ol>
            <p>Więcej informacji o&nbsp;ustawieniach przeglądarki Edge: <a href="https://support.microsoft.com/pl-pl/microsoft-edge/usuwanie-plik%C3%B3w-cookie-w-przegl%C4%85darce-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09" target="_blank" rel="noopener noreferrer">https://support.microsoft.com/pl-pl/microsoft-edge/usuwanie-plików-cookie-w-przeglądarce-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09</a></p>
          </div>
        </li>
        <li>
          <h2>Informacje kontaktowe</h2>
          <p>W razie jakichkolwiek wątpliwości związanych z&nbsp;kwestiami niniejszej Polityki Cookies lub w&nbsp;celu uzyskania informacji dotyczących niniejszej Polityki Cookies Użytkownik może skontaktować się z&nbsp;Administratorem za pośrednictwem wiadomości e-mail <a href="mailto:{EMAIL}"><strong>{EMAIL}</strong></a> oraz drogą pocztową na&nbsp;adres Administratora.</p>
        </li>
      </ol>
    </div>
  </div>
</section>
'''


INFO_BODY = f'''
<section class="section">
  <div class="wrap">
    <div class="prose legal" style="max-width:76ch">
      <p class="lead">Przesyłając e-maila na&nbsp;adres mailowy Administratora wyrażasz zgodę na&nbsp;dołączenie Twojego adresu poczty elektronicznej do&nbsp;listy kontaktów, której administratorem jest <strong>{FIRMA}, {STREET}, {POST} {CITY}, NIP {NIP},</strong> <em>(dalej jako Administrator)</em>.</p>

      <p>Zawarte w&nbsp;treści korespondencji dane, w&nbsp;tym adres e-mail są przetwarzane przez Administratora zgodnie z&nbsp;przepisami Rozporządzenia Parlamentu Europejskiego i&nbsp;Rady (UE) 2016/679 z&nbsp;dnia 27 kwietnia 2016&nbsp;r. w&nbsp;sprawie ochrony osób fizycznych w&nbsp;związku z&nbsp;przetwarzaniem danych osobowych i&nbsp;w&nbsp;sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE („RODO”), w&nbsp;następujących celach:</p>

      <ul>
        <li>w&nbsp;celu komunikacji z&nbsp;Tobą, w&nbsp;szczególności obsługi zapytań ofertowych, rozpatrzenia reklamacji dotyczących produktów lub usług Administratora, lub innych celach wynikających z&nbsp;treści Twojej korespondencji, zgodnie z&nbsp;art.&nbsp;6 ust.&nbsp;1 lit.&nbsp;b) RODO;</li>
        <li>w&nbsp;celu zawarcia i&nbsp;realizacji ewentualnej umowy pomiędzy Tobą a&nbsp;Administratorem zgodnie z&nbsp;art.&nbsp;6 ust.&nbsp;1 lit.&nbsp;b) RODO;</li>
        <li>w&nbsp;celu realizacji obowiązków prawnych Administratora wobec Ciebie określonych w&nbsp;RODO, w&nbsp;rozumieniu art.&nbsp;6 ust.&nbsp;1 lit.&nbsp;c) RODO;</li>
        <li>w&nbsp;celu realizacji działań marketingowych Administratora w&nbsp;ramach prawnie uzasadnionego interesu Administratora w&nbsp;rozumieniu art.&nbsp;6 ust.&nbsp;1 lit.&nbsp;f) RODO, a&nbsp;także zgodnie z&nbsp;Twoimi oświadczeniami woli dotyczącymi komunikacji marketingowej złożonymi wobec Administratora. Zgody udzielone w&nbsp;zakresie komunikacji marketingowej (np.&nbsp;na&nbsp;przesyłanie informacji handlowych drogą elektroniczną lub kontakt telefoniczny w&nbsp;celach marketingu bezpośredniego) mogą być wycofane w&nbsp;dowolnym czasie, bez wpływu na&nbsp;zgodność z&nbsp;prawem przetwarzania, którego dokonano na&nbsp;podstawie zgody przed jej cofnięciem.</li>
      </ul>

      <p>Osobie udostępniającej dane przysługuje prawo żądania od Administratora dostępu do&nbsp;danych, które jej dotyczą, ich sprostowania, usunięcia lub ograniczenia przetwarzania oraz prawo do&nbsp;wniesienia sprzeciwu wobec przetwarzania, a&nbsp;także prawo do&nbsp;przenoszenia danych oraz prawo do&nbsp;wniesienia skargi do&nbsp;Prezesa Urzędu Ochrony Danych Osobowych.</p>

      <p>Udostępnione dane osobowe nie&nbsp;są przekazywane przez Administratora podmiotom trzecim.</p>

      <p>Administrator przechowuje dane osobowe przez taki okres, jaki jest konieczny do&nbsp;osiągnięcia określonych celów, tj.:</p>

      <ul>
        <li>przez okres prowadzenia działalności gospodarczej przez Administratora.</li>
      </ul>

      <p>W przypadku jakichkolwiek pytań lub problemów związanych z&nbsp;przetwarzaniem danych osobowych należy kontaktować się z&nbsp;Administratorem pod następującym adresem:<br>
      <strong>{STREET}, {POST} {CITY}, <a href="mailto:{EMAIL}">{EMAIL}</a>.</strong></p>
    </div>
  </div>
</section>
'''


COOKIE_TABLE = [
    ("unikatowa nazwa generowana dynamicznie", "niezbędne", "sesyjne", "pliki własne strony", "przez czas sesji", "Są niezbędne do poprawnego działania strony np. wyświetlania odpowiedniej wersji językowej."),
    ("cookiesDirective", "niezbędne", "stały", "pliki własne strony", "do 365 dni", "Służy do zapisywania informacji, czy dla danego użytkownika wyświetlać ponownie komunikat o plikach cookie w przypadku, kiedy użytkownik zaznaczył co najmniej jedną z opcjonalnych zgód. Dzięki niemu baner z informacją o plikach cookie nie jest wyświetlany przy każdej wizycie użytkownika."),
    ("cpnb_cookiesSettings", "niezbędne", "stały", "pliki własne strony", "do 365 dni", "Służy do zbierania informacji o statusie zgód na pliki cookie wyrażonych przez użytkownika podczas jego wizyty na stronie."),
    ("cpnbCookiesDeclined", "niezbędne", "stały", "pliki własne strony", "do 180 dni", "Ten plik służy do zapisywania informacji, czy dla danego użytkownika wyświetlać ponownie komunikat o plikach cookie w przypadku, kiedy użytkownik odrzucił wszystkie opcjonalne zgody. Dzięki niemu baner z informacją o plikach cookie nie jest wyświetlany przy każdej wizycie użytkownika."),
    ("_GRECAPTCHA", "niezbędne", "stały", "Google", "do 180 dni", "Ten plik pochodzi z narzędzia Google reCAPTCHA, które służy do ochrony przed spamem."),
    ("_ga", "analityczne", "stały", "Google", "do 2 lat", "Umożliwia rozróżnianie poszczególnych użytkowników i śledzenie w jaki sposób korzystają oni z witryny internetowej. Dane są wykorzystywane do generowania statystyk użytkowania witryny bez identyfikowania poszczególnych użytkowników. Ten plik pochodzi z narzędzia Google Analytics."),
    ("_gac", "analityczne", "stały", "Google", "do 90 dni", "Służy do mierzenia aktywności użytkowników oraz skuteczności kampanii reklamowych. Ten plik pochodzi z narzędzia Google Analytics."),
    ("_gcl_xxxx", "analityczne", "stały", "Google", "do 90 dni", "Te pliki są używane przede wszystkim do informowania, ile razy użytkownicy, którzy kliknęli reklamy, wykonali działanie w ich witrynie (na przykład dokonali zakupu). Pliki cookie służące do pomiaru współczynników konwersji nie są używane do personalizacji reklam. Te pliki pochodzą z narzędzia Google Analytics."),
    ("_gid", "analityczne", "stały", "Google", "do 24 godzin", "Służy do rozróżniania użytkowników oraz przechowywania identyfikatora sesji (odwiedzin). Ten plik pochodzi z narzędzia Google Analytics."),
    ("_gat", "analityczne", "stały", "Google", "do 1 minuty", "Służy do ograniczania szybkości żądań. Głównym celem jest poprawa wydajności witryny. Jeśli usługa Google Analytics zostanie wdrożona za pomocą Menedżera tagów Google, ten plik cookie będzie miał nazwę _gat_gtag_&lt;id_usługi&gt;."),
    ("fr", "reklamowe", "stały", "Facebook", "do 90 dni", "Ten plik wykorzystuje się do dostarczania odpowiednich reklam użytkownikom witryny, a także do pomiaru skuteczności i zwiększania trafności reklam."),
    ("_fbp", "reklamowe", "stały", "Facebook", "do 90 dni", "Służy do zliczania, ile razy wyświetlana jest dana reklama oraz do obliczenia jej kosztu. Plik ten śledzi także zachowanie użytkownika na stronach, które mają piksel Facebooka lub wtyczkę społecznościową Facebooka. Identyfikuje przeglądarki do celów dostarczania usług reklamowych i związanych z analizą witryny."),
]

_rows = "\n".join(
    f"<tr><td><code>{n}</code></td><td>{k}</td><td>{r}</td><td>{s}</td><td>{c}</td><td>{d}</td></tr>"
    for n, k, r, s, c, d in COOKIE_TABLE
)

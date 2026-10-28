const puppeteer = require("puppeteer-core");
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const BASE = "http://localhost:8080";
const OUT = process.env.TEMP + "\\bz\\shots";
const results = [];
const ok = (name, pass, extra) => results.push({ name, pass, extra: extra || "" });

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ["--no-sandbox", "--hide-scrollbars"],
  });

  /* ---------- 1. Nawigacja mobilna ---------- */
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 390, height: 844 });
    await page.goto(BASE + "/", { waitUntil: "networkidle0" });

    const before = await page.$eval("#site-nav", (n) => { const c = getComputedStyle(n); return c.display + "/" + c.visibility + "/" + c.opacity; });
    ok("nav: ukryta na mobile przed kliknieciem", before.indexOf("hidden") > 0 && before.indexOf("/1") < 0, before);

    await page.click(".nav-toggle");
    await new Promise((r) => setTimeout(r, 250));
    const st = await page.evaluate(() => {
      const n = document.querySelector("#site-nav");
      const t = document.querySelector(".nav-toggle");
      const r = n.getBoundingClientRect();
      return {
        display: getComputedStyle(n).display,
        opacity: getComputedStyle(n).opacity,
        expanded: t.getAttribute("aria-expanded"),
        bodyOverflow: document.body.style.overflow,
        h: Math.round(r.height),
        links: n.querySelectorAll("a").length,
      };
    });
    ok("nav: otwiera sie po kliknieciu", st.display === "flex" && st.h > 500 && parseFloat(st.opacity) > 0.9, JSON.stringify(st));
    ok("nav: aria-expanded=true", st.expanded === "true");
    ok("nav: blokada przewijania tla", st.bodyOverflow === "hidden");

    await page.click(".nav__sub-toggle");
    await new Promise((r) => setTimeout(r, 200));
    const sub = await page.$eval("#sub-oferta", (s) => getComputedStyle(s).display);
    ok("nav: podmenu Oferta rozwija sie", sub === "block", sub);

    await page.screenshot({ path: OUT + "\\m-nav.png" });

    await page.keyboard.press("Escape");
    await new Promise((r) => setTimeout(r, 200));
    const closed = await page.$eval(".nav-toggle", (t) => t.getAttribute("aria-expanded"));
    ok("nav: Escape zamyka menu", closed === "false");
    await page.close();
  }

  /* ---------- 2. Lightbox ---------- */
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.goto(BASE + "/galeria/", { waitUntil: "networkidle0" });

    const count = await page.$$eval(".gallery__link", (a) => a.length);
    ok("galeria: 41 zdjec", count === 41, String(count));

    await page.click(".gallery__link");
    await new Promise((r) => setTimeout(r, 350));
    const lb = await page.evaluate(() => {
      const l = document.querySelector("#lightbox");
      const img = document.querySelector("#lb-img");
      return {
        open: l.classList.contains("is-open"),
        display: getComputedStyle(l).display,
        src: img.getAttribute("src"),
        alt: img.getAttribute("alt"),
        counter: document.querySelector("#lb-counter").textContent,
        focus: document.activeElement.id,
      };
    });
    ok("lightbox: otwiera sie", lb.open && lb.display === "grid", JSON.stringify({ open: lb.open, display: lb.display }));
    ok("lightbox: licznik 1 / 41", lb.counter === "1 / 41", lb.counter);
    ok("lightbox: zdjecie ma alt", (lb.alt || "").length > 10, lb.alt);
    ok("lightbox: fokus na przycisku zamkniecia", lb.focus === "lb-close", lb.focus);
    await page.screenshot({ path: OUT + "\\d-lightbox.png" });

    await page.keyboard.press("ArrowRight");
    await new Promise((r) => setTimeout(r, 200));
    const c2 = await page.$eval("#lb-counter", (e) => e.textContent);
    ok("lightbox: strzalka w prawo", c2 === "2 / 41", c2);

    await page.keyboard.press("ArrowLeft");
    await page.keyboard.press("ArrowLeft");
    await new Promise((r) => setTimeout(r, 250));
    const c3 = await page.$eval("#lb-counter", (e) => e.textContent);
    ok("lightbox: zawija do 41", c3 === "41 / 41", c3);

    await page.keyboard.press("Escape");
    await new Promise((r) => setTimeout(r, 250));
    const cl = await page.evaluate(() => ({
      open: document.querySelector("#lightbox").classList.contains("is-open"),
      overflow: document.body.style.overflow,
      focus: document.activeElement.className,
    }));
    ok("lightbox: Escape zamyka", !cl.open);
    ok("lightbox: przywraca przewijanie", cl.overflow === "");
    ok("lightbox: przywraca fokus", (cl.focus || "").includes("gallery__link"), cl.focus);
    await page.close();
  }

  /* ---------- 3. Formularz ---------- */
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.goto(BASE + "/kontakt/", { waitUntil: "networkidle0" });

    await page.click("#cf-submit");
    await new Promise((r) => setTimeout(r, 250));
    const err = await page.evaluate(() => ({
      status: document.querySelector("#form-status").textContent,
      visible: document.querySelector("#form-status").classList.contains("is-visible"),
      invalid: document.querySelectorAll('[aria-invalid="true"]').length,
      focus: document.activeElement.id,
    }));
    ok("formularz: blokuje puste zgloszenie", err.visible && err.invalid >= 4, JSON.stringify(err));
    ok("formularz: komunikat bledu", /Uzupe/.test(err.status), err.status.slice(0, 60));
    ok("formularz: fokus na pierwszym bledzie", err.focus === "cf-name", err.focus);

    await page.type("#cf-name", "Jan Testowy");
    await page.type("#cf-phone", "600 100 200");
    await page.type("#cf-email", "jan@example.com");
    await page.type("#cf-message", "Prosze o wycene wykonczenia mieszkania 60 m2 w Linii.");
    await page.evaluate(() => document.querySelector("#cf-consent").scrollIntoView({ block: "center" }));
    await new Promise((r) => setTimeout(r, 200));
    await page.click("label[for='cf-consent']");

    await page.evaluate(() => {
      window.__mailto = null;
      document.addEventListener(
        "click",
        (e) => {
          const a = e.target.closest && e.target.closest("a");
          if (a && a.href && a.href.indexOf("mailto:") === 0) {
            window.__mailto = a.href;
            e.preventDefault();
          }
        },
        true
      );
    });
    await page.click("#cf-submit");
    await new Promise((r) => setTimeout(r, 500));
    const mail = await page.evaluate(() => ({
      href: window.__mailto,
      status: document.querySelector("#form-status").textContent,
      kind: document.querySelector("#form-status").className,
      invalid: Array.from(document.querySelectorAll('[aria-invalid="true"]')).map((e) => e.id),
      consent: document.querySelector("#cf-consent").checked,
    }));
    ok(
      "formularz: przekazuje tresc do programu pocztowego",
      (mail.href || "").indexOf("mailto:mateo-drawc@wp.pl") === 0,
      (mail.href || "brak") + " | invalid=" + JSON.stringify(mail.invalid) + " consent=" + mail.consent
    );
    ok("formularz: brak falszywego wyslano", /program pocztowy/i.test(mail.status), mail.status.slice(0, 90));
    await page.close();
  }

  /* ---------- 4. Mapa na zadanie ---------- */
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.goto(BASE + "/kontakt/", { waitUntil: "networkidle0" });
    const before = await page.$$eval("#map iframe", (f) => f.length);
    await page.click("#map-load");
    await new Promise((r) => setTimeout(r, 500));
    const after = await page.$$eval("#map iframe", (f) => f.length);
    const title = await page.$eval("#map iframe", (f) => f.title).catch(() => "");
    ok("mapa: brak iframe przed kliknieciem", before === 0, String(before));
    ok("mapa: iframe po kliknieciu", after === 1, String(after));
    ok("mapa: iframe ma tytul", title.length > 10, title);
    await page.close();
  }

  /* ---------- 5. Fokus klawiatury ---------- */
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.goto(BASE + "/", { waitUntil: "networkidle0" });
    await page.keyboard.press("Tab");
    const first = await page.evaluate(() => document.activeElement.textContent.trim().slice(0, 40));
    ok("a11y: pierwszy Tab to skip link", /Przejd\u017a do tre/i.test(first), first);
    const outline = await page.evaluate(() => {
      const cs = getComputedStyle(document.activeElement);
      return { w: cs.outlineWidth, style: cs.outlineStyle };
    });
    ok("a11y: widoczny fokus", outline.w !== "0px" && outline.style !== "none", JSON.stringify(outline));
    await page.close();
  }

  await browser.close();

  let fail = 0;
  results.forEach((r) => {
    if (!r.pass) fail++;
    console.log((r.pass ? "PASS " : "FAIL ") + r.name + (r.pass ? "" : "  ->  " + r.extra));
  });
  console.log(`\n${results.length - fail}/${results.length} testow zaliczonych`);
  process.exit(fail ? 1 : 0);
})().catch((e) => {
  console.error("ERROR", e);
  process.exit(2);
});



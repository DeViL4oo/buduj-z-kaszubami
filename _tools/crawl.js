const puppeteer = require("puppeteer-core");
const pages = ["/", "/o-firmie/", "/oferta/", "/oferta/uslugi-budowlane/", "/oferta/uslugi-wykonczeniowe/", "/oferta/uslugi-remontowe/", "/oferta/uslugi-koparko-ladowarka/", "/galeria/", "/kontakt/", "/polityka-prywatnosci/", "/polityka-cookies/", "/obowiazek-informacyjny/", "/tabela-cookies/", "/dziekujemy/", "/404.html"];
(async () => {
  const b = await puppeteer.launch({executablePath:"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", headless:true, args:["--no-sandbox","--hide-scrollbars"]});
  let total = 0;
  for (const p of pages) {
    const page = await b.newPage();
    await page.setViewport({width:1280,height:900});
    const errs = [];
    page.on("console", m => { if (m.type() === "error") errs.push(m.text()); });
    page.on("pageerror", e => errs.push("pageerror: " + e.message));
    page.on("requestfailed", r => errs.push("reqfail: " + r.url()));
    const resp = await page.goto("http://127.0.0.1:8900" + p, {waitUntil:"networkidle0", timeout:30000});
    const t = await page.title();
    const h1 = await page.$$eval("h1", els => els.length);
    const status = resp.status();
    if (errs.length || status !== 200 || h1 !== 1) { console.log("!!", p, status, "h1=" + h1, errs.slice(0,3)); total += errs.length + 1; }
    else console.log("ok", p.padEnd(36), "h1=1");
    await page.close();
  }
  console.log("PROBLEMY:", total);
  await b.close();
})();

const puppeteer = require("puppeteer-core");

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const url = process.argv[2] || "http://127.0.0.1:8899/";
const width = parseInt(process.argv[3] || "390", 10);
const out = process.argv[4] || null;
const mode = process.argv[5] || "full";

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    protocolTimeout: 45000,
    args: ["--no-sandbox", "--hide-scrollbars", "--font-render-hinting=none"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width, height: 900, deviceScaleFactor: 1 });
  const errors = [];
  page.on("console", (m) => {
    if (m.type() === "error") errors.push(m.text());
  });
  page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
  page.on("requestfailed", (r) => errors.push("reqfail: " + r.url() + " " + r.failure().errorText));

  await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });

  await page.evaluate(async () => {
    document.documentElement.style.scrollBehavior = "auto";
    const step = Math.round(window.innerHeight * 0.7);
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y < h; y += step) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 80));
    }
    window.scrollTo(0, 0);
    await new Promise((r) => setTimeout(r, 500));
  });
  await new Promise((r) => setTimeout(r, 250));

  const info = await page.evaluate(() => {
    const vw = document.documentElement.clientWidth;
    const bad = [];
    document.querySelectorAll("body *").forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) return;
      if (r.right > vw + 1) {
        if (el.closest(".marquee")) return;
        const cs = getComputedStyle(el);
        if (cs.position === "fixed") return;
        bad.push({ tag: el.tagName.toLowerCase(), cls: (el.className || "").toString().slice(0, 60), right: Math.round(r.right), w: Math.round(r.width) });
      }
    });
    const broken = Array.from(document.images).filter((i) => i.complete && i.naturalWidth === 0).map((i) => i.currentSrc || i.src);
    return {
      vw,
      scrollW: document.documentElement.scrollWidth,
      height: document.documentElement.scrollHeight,
      scrollY: window.scrollY,
      overflowCount: bad.length,
      overflow: bad.slice(0, 10),
      brokenImages: broken.slice(0, 10),
      imgCount: document.images.length,
      h1: Array.from(document.querySelectorAll("h1")).map((h) => h.textContent.trim().slice(0, 80)),
      title: document.title,
    };
  });
  console.log(JSON.stringify({ url, width, ...info, errors: errors.slice(0, 10) }, null, 1));

  if (out) {
    if (mode === "viewport") {
      await page.screenshot({ path: out });
    } else {
      const h = Math.min(info.height, 16000);
      await page.setViewport({ width, height: h, deviceScaleFactor: 1 });
      await page.evaluate(() => window.scrollTo(0, 0));
      await new Promise((r) => setTimeout(r, 450));
      await page.screenshot({ path: out });
    }
  }
  await browser.close();
})().catch((e) => {
  console.error("FAIL", e.message);
  process.exit(1);
});

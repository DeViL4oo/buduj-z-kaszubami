const http = require("http");
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const ROOT = path.join(__dirname, "..", "site");
const PORT = parseInt(process.argv[2] || "8900", 10);

const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".svg": "image/svg+xml",
  ".jpg": "image/jpeg",
  ".png": "image/png",
  ".webp": "image/webp",
  ".avif": "image/avif",
  ".woff2": "font/woff2",
  ".xml": "application/xml",
  ".txt": "text/plain; charset=utf-8",
  ".json": "application/json",
};

const COMPRESSIBLE = new Set([".html", ".css", ".js", ".svg", ".xml", ".txt", ".json"]);
const cache = new Map();

function serve(file, req, res) {
  const ext = path.extname(file).toLowerCase();
  const body = fs.readFileSync(file);
  const headers = {
    "Content-Type": TYPES[ext] || "application/octet-stream",
    "Cache-Control": ext === ".html" ? "no-cache" : "public, max-age=31536000, immutable",
  };
  const ae = req.headers["accept-encoding"] || "";
  if (COMPRESSIBLE.has(ext) && /\bbr\b/.test(ae)) {
    let buf = cache.get(file);
    if (!buf) {
      buf = zlib.brotliCompressSync(body, {
        params: { [zlib.constants.BROTLI_PARAM_QUALITY]: 11, [zlib.constants.BROTLI_PARAM_SIZE_HINT]: body.length },
      });
      cache.set(file, buf);
    }
    headers["Content-Encoding"] = "br";
    headers["Vary"] = "Accept-Encoding";
    res.writeHead(200, headers);
    res.end(buf);
    return;
  }
  res.writeHead(200, headers);
  res.end(body);
}

http
  .createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, "http://x").pathname);
    let file = path.join(ROOT, p);
    if (p.endsWith("/")) file = path.join(file, "index.html");
    if (!fs.existsSync(file) && fs.existsSync(file + "/index.html")) {
      res.writeHead(301, { Location: p + "/" });
      res.end();
      return;
    }
    if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, "index.html");
    if (!fs.existsSync(file)) {
      res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
      res.end(fs.readFileSync(path.join(ROOT, "404.html")));
      return;
    }
    serve(file, req, res);
  })
  .listen(PORT, "127.0.0.1", () => console.log("prod server on http://127.0.0.1:" + PORT));

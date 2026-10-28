import os, sys, urllib.request, json, time
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = r"C:\Users\KRYBAR\OneDrive - Inwido\Pulpit\Strona"
SRC = os.path.join(ROOT, "_src", "orig")
os.makedirs(SRC, exist_ok=True)
urls = [l.strip() for l in open(os.path.join(ROOT, "_src", "image-urls.txt"), encoding="utf-8-sig") if l.strip()]
report = []
for u in urls:
    rel = u.replace("https://budujzkaszubami.pl/", "")
    name = rel.replace("/", "_")
    dest = os.path.join(SRC, name)
    if not os.path.exists(dest):
        for attempt in range(3):
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
                    f.write(r.read())
                break
            except Exception as e:
                if attempt == 2:
                    print("FAIL", u, e)
                time.sleep(1.5)
    try:
        with Image.open(dest) as im:
            report.append({"url": u, "file": name, "w": im.width, "h": im.height,
                           "fmt": im.format, "bytes": os.path.getsize(dest)})
    except Exception as e:
        print("BAD", u, e)
json.dump(report, open(os.path.join(ROOT, "_src", "images.json"), "w", encoding="utf-8"), indent=1)
report.sort(key=lambda r: -r["bytes"])
for r in report:
    print(f'{r["file"]:66s} {r["w"]:5d}x{r["h"]:<5d} {r["bytes"]/1024:9.1f} KB')
print("COUNT", len(report))

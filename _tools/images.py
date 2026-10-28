# -*- coding: utf-8 -*-
"""Jedna wersja każdego zdjęcia: <slug>.webp, szerokość dobrana do roli."""
import os, sys, json
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"C:\Users\KRYBAR\OneDrive - Inwido\Pulpit\Strona"
SRC = os.path.join(ROOT, "_src", "orig")
OUT = os.path.join(ROOT, "site", "assets", "img")
MAN = json.load(open(os.path.join(ROOT, "_src", "manifest.json"), encoding="utf-8"))

# maksymalna szerokość pliku dla danej roli
BIG = ("slide-d-1", "slide-d-1-1", "bg-parallax-subpage-o-nas")
MID = 900


def target_width(name, srcw):
    if name in BIG:
        return min(srcw, 1400)
    if name.startswith("gal-"):
        return srcw            # galeria: źródło ma 800 / 450 px
    if name.startswith("box-offer-h"):
        return srcw            # kafle oferty: 768 px wystarczy
    return min(srcw, MID)


single = {}
total = 0
for name, meta in MAN.items():
    src = os.path.join(SRC, meta["src"])
    im = Image.open(src).convert("RGB")
    W, H = im.size
    tw = target_width(name, W)
    if tw < W:
        im = im.resize((tw, round(H * tw / W)), Image.LANCZOS)
    out = os.path.join(OUT, name + ".webp")
    im.save(out, "WEBP", quality=82, method=6)
    size = os.path.getsize(out)
    total += size
    single[name] = {"w": im.size[0], "h": im.size[1], "bytes": size}

json.dump(single, open(os.path.join(ROOT, "_src", "single.json"), "w", encoding="utf-8"), indent=1)
print("plików:", len(single), "| łącznie: %.1f MB" % (total / 1024 / 1024))
for n in ["slide-d-1-1", "content-oferta", "box-offer-h", "gal-budowa-budynku-06", "gal-teren-budowy-domu-13"]:
    if n in single:
        print(" ", n, single[n]["w"], "x", single[n]["h"], round(single[n]["bytes"] / 1024, 1), "KB")

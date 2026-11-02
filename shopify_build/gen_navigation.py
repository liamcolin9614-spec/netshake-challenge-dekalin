"""Liest das Navigationskonzept (aufgabe1/05_shopify_import/menus.md) und erzeugt navigation.json:
Menübäume, daraus abgeleitete Smart-Kollektionen (Regel: Produkt-Tag) und Seiten-Stubs.
Warum aus dem Konzept generieren: Konzept-Dokument und Shop bleiben 1:1 identisch."""
import re, json, pathlib
md = (pathlib.Path(__file__).parent.parent / "aufgabe1/05_shopify_import/menus.md").read_text(encoding="utf-8")
blocks = re.findall(r"\*\*`?([\w-]+)`?[^\n]*\n```\n(.*?)```|## 1\. Menü[^\n]*`([\w-]+)`\n.*?```\n(.*?)```", md, re.S)
def parse(text):
    root = []; stack = [(-1, root)]
    for line in text.splitlines():
        m = re.match(r"^([│├└─\s]*)(.+?)\s{2,}→\s*(\S+)", line)
        if not m: continue
        depth = len(m.group(1)) // 4
        item = {"title": m.group(2).strip(), "url": m.group(3), "items": []}
        while stack[-1][0] >= depth: stack.pop()
        stack[-1][1].append(item); stack.append((depth, item["items"]))
    return root
menus = {}
main = re.search(r"Handle `main-menu`\n\n```\n(.*?)```", md, re.S).group(1)
menus["main-menu"] = {"title": "Hauptmenü", "items": parse(main)}
for h, t in [("footer-shop", "Shop"), ("footer-hilfe", "Hilfe"), ("footer-dekalin", "Wissen & Dekalin"), ("footer-rechtliches", "Rechtliches")]:
    body = re.search(rf"`{h}`[^\n]*\n```\n(.*?)```", md, re.S).group(1)
    menus[h] = {"title": t, "items": [{"title": a.strip(), "url": b, "items": []} for a, b in re.findall(r"^(.+?)\s{2,}→\s*(\S+)", body, re.M)]}
# Kollektionen und Seiten aus allen Links ableiten
cols, pages = {}, {}
def walk(items):
    for it in items:
        u = it["url"]
        if u.startswith("/collections/"):
            h = u.split("/")[2]; cols.setdefault(h, it["title"] if not it["title"].startswith("Alle") else None)
        elif u.startswith("/pages/"):
            pages.setdefault(u.split("/")[2], it["title"])
        walk(it["items"])
for m in menus.values(): walk(m["items"])
WELTEN = {"abdichten": "Abdichten", "kleben-montieren": "Kleben & Montieren", "reparieren-schuetzen": "Reparieren & Schützen", "reinigen-zubehoer": "Reinigen & Zubehör"}
collections = []
for h, t in cols.items():
    if h in WELTEN: collections.append({"handle": h, "title": WELTEN[h], "tag": f"welt:{h}"})
    elif h == "bestseller": collections.append({"handle": h, "title": "Bestseller", "tag": "bestseller"})
    elif h == "klebesets": collections.append({"handle": h, "title": "Klebe- & Dichtsets", "tag": "set"})
    else: collections.append({"handle": h, "title": t, "tag": f"anwendung:{h}"})
pages["anleitung-solarmodul-kleben"] = "Solarpanel ohne Bohren aufs Wohnmobildach kleben"
json.dump({"menus": menus, "collections": collections, "pages": pages}, open(pathlib.Path(__file__).parent / "navigation.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(collections), "Kollektionen,", len(pages), "Seiten,", {k: len(v["items"]) for k, v in menus.items()})

"""Erzeugt aus aufgabe1/05_shopify_import/products.csv die productSet-Eingaben (Admin GraphQL) als JSON.
Warum productSet: ein Aufruf legt Produkt, Optionen, Varianten und Metafelder idempotent an (per Handle)."""
import csv, json, pathlib
src = pathlib.Path(__file__).parent.parent / "aufgabe1/05_shopify_import/products.csv"
rows = list(csv.DictReader(open(src, encoding="utf-8")))
MF = {"USP-Zeile (product.metafields.custom.usp_zeile)": "usp_zeile",
      "Klartext-Untertitel (product.metafields.custom.klartext_untertitel)": "klartext_untertitel",
      "Interne Notiz (product.metafields.custom.interne_notiz)": "interne_notiz"}
products, cur = [], None
for r in rows:
    if r["Title"]:
        opts = [r[f"Option{i} Name"] for i in (1, 2, 3) if r[f"Option{i} Name"]]
        cur = {"handle": r["Handle"], "title": r["Title"], "descriptionHtml": r["Body (HTML)"],
               "vendor": r["Vendor"].replace("[Annahme] ", ""), "productType": r["Type"],
               "tags": [t.strip() for t in r["Tags"].split(",") if t.strip()],
               "status": "ACTIVE",  # aktiv, damit die Vorschau (Online Store) die Seite zeigt
               "seo": {"title": r["SEO Title"], "description": r["SEO Description"]},
               "metafields": [{"namespace": "custom", "key": k, "type": "single_line_text_field", "value": r[c]}
                              for c, k in MF.items() if r[c]],
               "_opts": opts, "variants": []}
        products.append(cur)
    ov = [{"optionName": n, "name": r[f"Option{i} Value"]} for i, n in enumerate(cur["_opts"], 1)]
    v = {"optionValues": ov, "price": r["Variant Price"], "sku": r["Variant SKU"],
         "inventoryPolicy": "CONTINUE",
         "inventoryItem": {"tracked": False, "measurement": {"weight": {"value": float(r["Variant Grams"] or 0), "unit": "GRAMS"}}}}
    if r["Variant Barcode"]: v["barcode"] = r["Variant Barcode"]
    cur["variants"].append(v)
for p in products:
    names = p.pop("_opts")
    p["productOptions"] = [{"name": n, "values": [{"name": x} for x in dict.fromkeys(
        ov["name"] for v in p["variants"] for ov in v["optionValues"] if ov["optionName"] == n)]} for n in names]
json.dump(products, open(pathlib.Path(__file__).parent / "products.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(products), "Produkte,", sum(len(p["variants"]) for p in products), "Varianten")

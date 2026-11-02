# shopify_build – Code für den Dekalin-Test-Shop

| Datei | Läuft wo | Aufgabe |
|---|---|---|
| `gen_products.py` | lokal | `products.csv` → `products.json` (Eingabe für `productSet`) |
| `gen_navigation.py` | lokal | `menus.md` → `navigation.json` (Menübäume, Kollektionen, Seiten) |
| `gen_template_dekasyl.py` | lokal | Texte aus `04_pdp_texte.md` → `template_dekasyl.json` (Produktvorlage MS-5, inkl. Stylesheet, Preisblock, Mengenstaffel, „Oft zusammen gekauft“) |
| `gen_template_product.py` | lokal | → `template_product.json` (schlanke Standardvorlage für alle übrigen Produkte, gleicher Stil) |
| `../aufgabe1/06_shopify_bilder/promo/promo.html` | lokal, Headless-Chrome-Screenshot | Mega-Menü-Kacheln (`promo_*.png`) |
| `00_session_setup.js` | Browser, Shopify-Admin | CSRF-Token holen, Helfer `gql()` (Admin API) und `osw()` (Theme-Editor-API) |
| `01_import_daten.js` | Browser | Metafelder, Produkte, Kollektionen, Seiten, Blog, Menüs |
| `02_bilder.js` | Browser | Staged Uploads, Bilder an Produkte hängen |
| `03_apply_template.js` | Browser | Vorlagen `product.dekasyl` und `product` schreiben und speichern |
| `04_theme_header_footer.js` | Browser | Theme-Einstellungen (CI, Versandschwelle 49 €), Header-, Overlay-, Footer-Gruppe |

Warum Browser-Skripte statt Shopify CLI: Vision läuft als **Testversion**; dort sind Code-Editor und Asset-API gesperrt,
der Theme-Editor speichert aber über eine interne API – die Skripte nutzen genau diese Aufrufe mit der eingeloggten Sitzung.
Dateien gelangen per `stagedUploadsCreate` in den Shop (die Admin-Seite darf per CSP nicht auf localhost zugreifen).

Begründungen aller Entscheidungen: `../BAU_DOKUMENTATION.md`.

Nicht per Skript, sondern im Admin: Mengenrabatte (2 automatische Rabatte, ab 3 Stück 5 %, ab 6 Stück 10 %), Bewertungs-Metafelder `reviews.rating`/`rating_count` am MS-5, Theme-Texte („Jetzt sicher zur Kasse“, Suchfeld, Warenkorb-Texte) unter „Standard-Theme-Inhalte bearbeiten“.

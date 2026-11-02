# Bau-Dokumentation – Dekalin-Shop (NETSHAKE-Challenge)

Was gebaut wurde, **wie** und **warum**. Kürzel in eckigen Klammern verweisen auf das Datenblatt/Recherche ([F])
oder kennzeichnen Annahmen ([A]).
Ausführliche Begründungen je Baustein: `aufgabe1/01_navigationskonzept.md` und `aufgabe1/03_pdp_bauplan.md`.

**Vorschau (ohne Passwort):** https://795qyvp8mh4ckrcr-100512923981.shopifypreview.com/products/dekasyl-ms-5-kleb-dichtstoff
⚠️ Shopify-Vorschaulinks laufen nach **2 Tagen** ab (erzeugt am 02.11.2026). Vor der Abgabe neu erzeugen:
Admin → Onlineshop → Themes → Vision → „…“ → Vorschau → unten „Copy link“.

---

## 1. Ausgangslage & Grundentscheidungen

| Entscheidung | Warum |
|---|---|
| Eigener Test-Shop (`izv07b-rf.myshopify.com`), Vision 18.0.0 per „Try theme“ | Briefing verlangt Vision; bewusst ein separater Test-Shop, kein produktiver Shop. |
| Theme bleibt **Entwurf** (Testversion) | Kauf-Themes lassen sich ohne Kauf nicht veröffentlichen; für die Abgabe reicht der Vorschaulink. |
| Alles per Skript statt per Klick | Reproduzierbar (Konzept-Dokumente = Quelle, Skripte erzeugen daraus den Shop), keine Tippfehler, schnell änderbar. Der Code liegt in `shopify_build/`. |
| Zwei Schnittstellen | **Admin GraphQL API** für Daten (Produkte, Kollektionen, Seiten, Menüs, Dateien). **Theme-Editor-API** (dieselben Aufrufe, die der Editor beim Speichern nutzt) für Vorlagen, Header/Footer und Theme-Einstellungen – denn bei Theme-Testversionen sind Code-Editor und Asset-API gesperrt. |

## 2. Daten (Skripte `gen_products.py`, `gen_navigation.py`, `01_import_daten.js`)

| Was | Wie | Warum |
|---|---|---|
| 9 Produkte, 21 Varianten (MS-5, MS-1, MS-2, DEKASEAL 8936/1512, DEKACLEAN, DEKAVATOR, DEKAFINISHER, Kartuschenpresse) | aus `products.csv` per `productSet` | Cross-Sell und Vergleich brauchen echte Produkte; MS-1/MS-2 machen die Stufen-Logik klickbar. |
| MS-5: Weiß/Schwarz × 290 ml/600 ml, **ohne** Schwarz-600 ml | Variante nicht angelegt | Laut Datenblatt gibt es Schwarz nur als Kartusche [F]; nicht existierende Kombination wird ausgegraut statt „ausverkauft“. |
| Bestand nicht verfolgt | `inventoryItem.tracked=false` | Vorschau zeigt sonst „ausverkauft“; keine künstliche Verknappung (Bauplan Block 7). |
| Metafelder `custom.usp_zeile`, `klartext_untertitel`, `infobox_text`, `lieferhinweis` (Storefront-Zugriff) + `interne_notiz` (nicht öffentlich) | `metafieldDefinitionCreate` | Texte pflegbar ohne Theme-Code; `interne_notiz` dokumentiert jede Annahme (Preis, SKU) direkt am Produkt. |
| Solar-Montage-Set (69,95 € statt 77,75 €) | eigenes Produkt, Tag `set` | Bundle früh auf der PDP sichtbar machen (umsetzbar mit Shopify Bundles). Preis = Annahme. |
| 28 Smart-Kollektionen | Regel „Tag = welt:… / anwendung:…“ | Navigation nach **Vorhaben** statt Produktname; neue Produkte sortieren sich über Tags selbst ein. |
| 16 Seiten + Blog „Anleitungen“ | Platzhalter-Seiten, als solche gekennzeichnet | Kein Menülink führt ins Leere. |
| Menüs `main-menu` (6 × 2 Spalten × 3 Links), 4 Footer-Menüs, `mobile-extra`, `service-menu` | `menuCreate/menuUpdate`, Links als echte Ressourcen | 1:1 aus `05_shopify_import/menus.md` generiert → Konzept und Shop sind identisch. |

## 3. Bilder (`02_bilder.js`)

| Was | Warum |
|---|---|
| MS-5-Galerie = 5 Grafiken aus dem Prototyp (Kleben statt Bohren · Solarmodul · Eigenschaften · Haftgrund-Ampel · 4 Schritte), mit Alt-Texten | Keine freigegebenen Produktfotos; Kaufargumente stehen direkt im Bild statt in Tabellen; Header links oben, 3–7 Wörter – auf dem Handy in einer Sekunde erfassbar. |
| Packshot-Grafiken der Cross-Sell-Produkte, im Browser per Canvas gezeichnet, gleicher Stil | Produktkarten ohne Bild wirken kaputt; einheitlicher Look. **Platzhalter** – im echten Projekt Fotos von Dekalin. |
| Logo = Wortmarke „DEKALIN“ in #D42A3B / Barlow | **Platzhalter**, kein Original-Logo verwendet. |

## 4. Theme-Einstellungen, Header & Footer (`04_theme_header_footer.js`)

| Was | Warum |
|---|---|
| Farben Rot #D42A3B (Akzent, Buttons, Badges), Text #262626, weißer Hintergrund; Schrift Barlow | Dekalin-CI [F: dekalin.de]. |
| Buttons 8 px Radius, keine Schatten | Technischer, ruhiger Look für ein Profi-Produkt. |
| Announcement Bar: 3 rotierende Trust-Texte | Versand, Herkunft „seit 1907“, kostenlose Beratung – die drei größten Kaufhürden [04_pdp_texte.md §8]. |
| Mega-Menü je Hauptpunkt mit **einer** Promo-Kachel, Badge „TOP“ an „Kleben & Montieren“ | Keine Thumbnails je Link – machen das Menü unruhig und lang; Badge lenkt auf die Welt des Hero-Produkts. |
| Suche ausgeklappt im Header | Profis suchen gezielt nach Produktnamen – ein sichtbares Suchfeld spart den Umweg über das Menü. |
| Keine Secondary-Leiste, kein Mobile Dock | Doppelte Leisten verwirren; Platz für Inhalt. |
| Mobile-Menü dunkel, mit Zusatzlinks Bestseller · Produktfinder · Beratung · Anmelden | Mobile Nutzer brauchen die Abkürzungen ganz oben im Drawer. |
| Footer: Markentext + Beratungs-CTA, 3 Linkspalten (Shop · Hilfe · Wissen & Dekalin), Newsletter „Klebe-Tipps vom Profi“, Zahlungsicons | Zahlungs-Icons hier statt auf der PDP (dort zählt der Nutzen); Newsletter mit Nutzenversprechen statt „Newsletter abonnieren“. |

## 5. Produktseite – Vorlage `product.dekasyl` (`gen_template_dekasyl.py`, `03_apply_template.js`)

Eigene Vorlage nur für MS-5. Alle anderen Produkte nutzen die schlanke Standardvorlage `product` (`gen_template_product.py`: gleicher Stil, ohne MS-5-spezifische Inhalte – ersetzt die Demo-Sections des Themes). 10 Sections (Shopify-Limit 25). Ein gemeinsames Stylesheet (Icons in roten Kreisen, Karten, Farbfelder) steht im ersten Block des Hauptbereichs.

**Above the fold (main-product):** Titel → Preisblock (Gesamtpreis, Grundpreis, Versandschwelle) + Bestseller-Badge + Sterne → USP-Zeile → 4 Bullets mit Häkchen → Varianten (Farbfelder) + „Grau? → MS-2“ → Mengenstaffel 1/3/6 → Lieferzeile → Warenkorb-Button (volle Breite) → Trust-Leiste (3 Icons) → „Oft zusammen gekauft“. Beschreibung (offen), Technische Daten, Haftgründe, Verarbeitung, Downloads und Versand & Rückgabe als Akkordeons – auf dem Desktop unter der Galerie (linke Spalte bleibt nicht leer), mobil unter der Kaufbox.

| Entscheidung | Warum |
|---|---|
| ~~Klartext-Infobox über dem Titel~~ (gestrichen) | Sagte fast dasselbe wie die USP-Zeile darunter; die USP-Zeile direkt am Titel trägt die Botschaft allein. |
| USP-Zeile direkt unter dem Titel | Ein klares Hauptversprechen direkt am Produktnamen – der Kunde versteht sofort, was das Produkt leistet. |
| Eigener Preisblock direkt unter dem Titel: Gesamtpreis der gewählten Staffel (Streichpreis + „Spare 5/10 %“), darunter fett der Grundpreis je Liter + „ab 49 € versandkostenfrei“ | Bei Staffel- und Variantenwechsel rechnen Gesamt- und Literpreis mit (z. B. 3 × 290 ml: 56,88 € statt 59,85 €, 65,38 €/l). PAngV: Grundpreis klar erkennbar beim Gesamtpreis. Vendor-Zeile „DEKALIN“ entfernt (eigener Markenshop). Werte = Annahme. |
| Lieferzeit direkt über dem Button | Lieferzeit ist eine der häufigsten Fragen vor dem Kauf – direkt am Button beantwortet. |
| **Kein** Sticky-ATC, **kein** Express-Checkout | Sticky-ATC verdeckt auf kleinen Bildschirmen Inhalt und lenkt ab; ein einziger klarer Kaufweg statt mehrerer Buttons – Kauf so einfach wie möglich. |
| Mengenstaffel 1 / 3 / 6 Stück statt freiem Mengenfeld | Feste Packs mit sichtbarer Ersparnis statt Mengenregler. Rabatte sind echte automatische Rabatte (ab 3 Stück 5 %, ab 6 Stück 10 % – Annahme), damit der Preis im Warenkorb stimmt; das Skript rechnet die Preise je Variante neu. |
| „Oft zusammen gekauft“ (Reiniger, Haftvermittler, Presse) | Zubehör, ohne das die Klebung nicht sicher hält – vorausgewählt, ein Klick legt alles über die Cart-API in den Warenkorb. |
| Keine Set-Karte in der Kaufbox | Direkt unter „Oft zusammen gekauft“ wären es zwei konkurrierende Zubehör-Angebote; das Set hat eine eigene Section und steht im Mega-Menü. |
| Sterne am Titel | Theme liest die Standard-Metafelder `reviews.rating` / `reviews.rating_count`; Werte = Mittel der drei Beispielbewertungen (4,7 / 3). Im Live-Shop füllt die Review-App diese Felder. |
| Farbfelder statt Text-Buttons | Theme bildet die Farbe aus dem Variantennamen – deutsche Namen sind kein CSS, daher Farbwerte per Stylesheet. Nächster Schritt: Bild-Swatches mit Fugenfoto. |
| Trust-Icons unter dem Button statt Zahlungslogos | Benefit-Zeile statt Logoleiste; Beratung für Unsichere bei einem erklärungsbedürftigen Produkt. |

**Below the fold (Reihenfolge = Fragen des Kunden):**

| # | Section | Warum |
|---|---|---|
| 1 | Anwendungen als Chips (rich-text) → Kollektionen | Einstieg nach Vorhaben; verlinkt in die Navigation. |
| 2 | **Haftgrund-Ampel** – drei Ampel-Karten nebeneinander (rich-text, Custom Liquid) | Häufigste Frage vor dem Kauf, ehrlich inkl. „hält nicht auf PE/PP/Teflon“ → Vertrauen, weniger Retouren. |
| 3 | 4 Schritte (Karten) mit Produkt je Schritt (Reiniger + Haftvermittler, Presse, DEKAFINISHER; „+“ legt direkt in den Warenkorb) | Anleitung für erklärungsbedürftige Produkte; Zubehör genau dort, wo es gebraucht wird – ersetzt die frühere Zubehör-Section. |
| 4 | Solar-Montage-Set als Produktkarte: großes Bild, Bestandteile als Kacheln, Preis mit Ersparnis, „Set in den Warenkorb“ | Bundle direkt kaufbar statt nur verlinkt; weniger Leerraum. Direkt nach den Schritten: wer gerade gesehen hat, was er braucht, bekommt alles in einem Paket. |
| 5 | Zeitleiste seit 1907 (rich-text, dunkel) | Herkunft & Expertise als Vertrauensstufe; ersetzt den Scrolling-Content, dessen Bilder sich überlagerten. Kein „Made in Germany“, weil nicht belegt. |
| 6 | Vergleich MS-1/MS-2/MS-5 + MS-5 vs. Sikaflex-554 (Tabellen) | Löst die Namensverwirrung; fairer Datenblatt-Vergleich. Rechtlich vor Livegang prüfen (§ 6 UWG). |
| 7 | Bewertungen – **als Beispiel gekennzeichnet** | Social Proof vor den letzten Fragen; Platzhalter für eine Review-App (UWG: nichts Erfundenes als echt ausgeben). |
| 8 | FAQ, 10 Fragen (collapsible-content) | Letzte Einwände; dieselben Fragen wie im KI-Test (Aufgabe 2). |

**Gestrichen, weil doppelt (Seiten-Review 02.11.):** Infobox über dem Titel (= USP-Zeile), Vorteils-Karten „Klebt. Dichtet. Hält.“ (= Bullets + Bild-Callouts), „Das brauchst du dazu“ (= „Oft zusammen gekauft“ – bleibt auf den übrigen Produktseiten), Service-Karten (= Trust-Leiste; das Anwendungsversprechen steht jetzt in der Trust-Leiste), Technik-Tabs (→ Akkordeons), „Zuletzt angesehen“ (lenkt auf Alternativen statt Zubehör). Seite rund 20 % kürzer.

**Mega-Menü-Kacheln (Review 02.11.):** Jede Kachel hat jetzt ein eigenes, zum Text passendes Motiv (`aufgabe1/06_shopify_bilder/promo/`, gleicher Stil wie die Galerie): Dachluke mit Dichtnaht · Solarmodul (Set) · Riss vorher/nachher · Reiniger/Haftvermittler/Glättmittel · Ratgeber-Buch · „1907“ + Beratungs-Chat. Vorher wiederholten fünf Kacheln MS-5-Galeriebilder, die nicht zum Text passten. „Reparieren & Schützen“ verlinkte auf die leere Kollektion Unterbodenschutz – jetzt auf „Wasserschaden reparieren“ (3 Produkte).

## 6. Bewusst offen / Annahmen

- Preise, Versandschwelle, Lieferzeit, Set-Preis, Ergiebigkeit, Mengenrabatte (5 % / 10 %): **Annahmen** (auch in `custom.interne_notiz` je Produkt).
- Logo, Packshots, Bewertungen, Seiteninhalte: **Platzhalter**.
- Datenblatt-Link führt auf dekalin.de (PDF nicht hochgeladen).
- Acht Unterkategorien (v. a. „Reparieren & Schützen“) haben noch keine Produkte; die Navigation zeigt das Konzept, die Kategorieseite sagt das offen und verweist auf die Beratung.
- Rechtstexte (Impressum, AGB, Widerruf, Versand) sind als **Muster** angelegt und im Footer unter „Rechtliches“ verlinkt; Inhalte liefert Dekalin bzw. die Rechtsberatung.
- Checkout ist im Test-Shop gesperrt („Dieser Shop kann noch keine Bestellungen erhalten“) – Warenkorb funktioniert, Kauf ist bewusst nicht möglich.

## 7. Nachbauen

1. `python3 shopify_build/gen_products.py && python3 shopify_build/gen_navigation.py && python3 shopify_build/gen_template_dekasyl.py`
2. Im eingeloggten Shopify-Admin (Browser) `00_session_setup.js` ausführen, dann `01`–`04` in Reihenfolge (Details je Datei).

# Import-Reihenfolge (Testshop, nicht im Live-Shop)

1. **Metafeld- und Metaobjekt-Definitionen** anlegen (`metafields.md`), sonst werden die Metafeld-Spalten der CSV ignoriert.
2. **`products.csv`** importieren (Produkte → Importieren). Alle Produkte kommen als `Status = draft`, `Published = FALSE`.
   - `Product Category` ist bewusst leer: Shopify verwirft Zeilen mit ungültigem Taxonomie-Pfad. Nach dem Import im Admin die vorgeschlagene Kategorie übernehmen (Kleb-/Dichtstoffe z. B. unter „Hardware > Building Consumables“ → passende Unterkategorie für Klebstoffe/Dichtmassen; Presse unter Werkzeug) [?: exakten Pfad in der Taxonomie-Suche prüfen].
   - `Image Src` leer (Bilder folgen); Bild-Alt-Texte stehen in `../04_pdp_texte.md`.
   - Preise sind Annahmen (Begründung in Spalte „Interne Notiz“). SKUs mit `TBD-` sind Platzhalter; echte Artikelnummern nur für MS-5 (Datenblatt).
   - Grundpreis über `Unit Price …`-Spalten (ml → 1 l, PAngV).
3. **Kollektionen** anlegen (`collections.md`).
4. **Menüs** anlegen (`menus.md`), danach im Theme-Editor Mega-Menu-Blöcke zuweisen.
5. Solar-Montage-Set über die Shopify-Bundles-App bauen.

# 01 – Navigationskonzept Dekalin-Shop (Shopify, Vision Theme 18)

Kennzeichnung: **[F]** belegter Fakt (Quelle in `recherche/dekalin_recherche.md`), **[A]** Annahme/Empfehlung, **[V]** geprüft in der Vision-Demo (vision-main.myshopify.com, Theme-Version 18.0.0, abgerufen 01.11.2026).

---

## 1. Prinzip: Einstieg nach Vorhaben, nicht nach Produktname

**Problem:** Endkunden kennen „DEKAsyl MS-5“, „DEKASEAL 1512“ oder „DEKAVATOR 22 NF“ nicht. Sie wissen nur: *„Ich will ein Solarmodul aufs Dach kleben“* oder *„An der Dachluke kommt Wasser rein“*. Die bisherigen Dekalin-Kategorien (Reinigen, Kleben & Dichten, Dichten, Schützen, Kleben & Reparieren) sind nach Tätigkeit sortiert, aber zu technisch: Wer kennt den Unterschied zwischen „Dichten“ und „Kleben & Dichten“? [F, Recherche 5]

**Lösung in drei Ebenen:**

| Ebene | Frage des Kunden | Umsetzung im Shop |
|---|---|---|
| 1. Hauptmenü | „Was hast du vor?“ | 4 Tätigkeits-Welten: Abdichten · Kleben & Montieren · Reparieren & Schützen · Reinigen & Zubehör |
| 2. Mega-Menü-Spalte | „Woran/wo genau?“ | 2 Spalten je Welt, z. B. „Am Dach“ / „An Fenster & Türen“ |
| 3. Menü-Link → Kollektion | „Konkrete Aufgabe“ | Aufgabe in Kundensprache: „Solarmodul kleben“, „Dachluke abdichten“ |
| Kollektion | „Welches Produkt?“ | Produktname erst hier, immer mit Klartext-Unterzeile („DEKAsyl MS-5 – Kraftkleber für Solarmodule & Anbauteile“) |
| Filter | „Auf welchem Material? Welche Eigenschaft?“ | Einsatzort · Untergrund · Eigenschaft · Klebkraft · Farbe · Gebinde |

**Warum:**
- Navigation entlang der Customer Journey statt interner Produktlogik – der Kunde sucht nach seinem Problem, nicht nach dem Sortiment des Herstellers.
- Kein Caravan-Händler (Fritz Berger, Reimo, Obelink) sortiert nach Anwendung; nur Sika macht es auf der DIY-Seite per Fahrzeuggrafik. Das ist die Lücke, in der sich ein Hersteller-Shop abhebt [F, Recherche 5].
- Unbekannte Produktnamen im Menü helfen niemandem – im Menü stehen deshalb **keine Produktnamen**, nur Aufgaben.
- Dekalin selbst wertet DEKABot-Anfragen nach Themen wie „Wohnmobil Markise kleben“ aus – Kunden fragen nach Aufgaben [F, Recherche 1.5].

**Zwei Menü-Blöcke laut Briefing:**
1. **„Was kann ich kaufen?“** = Punkte 1–4 (Sortiment).
2. **„Warum soll ich kaufen?“** = Punkte 5–6 (Ratgeber & Wissen · Warum Dekalin) – Vertrauen über Know-how, Geschichte seit 1907, Schulungen, Beratung.

---

## 2. Header-Hauptmenü (Desktop, Mega-Menü)

### 2.1 Übersicht – ausbalanciert (6 Hauptpunkte × 2 Spalten × 3 Links)

Jeder Hauptpunkt hat **genau 2 Spalten mit je 3 Links = 6 Unterpunkte** plus einen Link „Alle anzeigen“ am Ende und eine Promo-Kachel. Damit ist kein Punkt deutlich schwächer besetzt (Briefing-Anforderung) und das Menü bleibt scanbar (genug Einstiege, aber nicht überladen).

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [DEKALIN-Logo]   Abdichten  Kleben & Montieren  Reparieren & Schützen  Reinigen & Zubehör │ Ratgeber  Warum Dekalin   [🔍 Wonach suchst du? z. B. Dachluke abdichten]  👤  🛒(2) │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
   └──────────── „Was kann ich kaufen?“ ───────────────────────┘  └─ „Warum kaufen?“ ─┘
```

### 2.2 Vollständige Menüstruktur

| # | Hauptpunkt (Ebene 1) | Spalte (Ebene 2) | Links (Ebene 3) → Kollektion/Seite | Promo-Kachel (Vision „mega-menu-promotion“) |
|---|---|---|---|---|
| **1** | **Abdichten** <br>*„Wasser soll draußen bleiben“* | **Am Dach** | Fenster & Dachluken abdichten · Dachhauben & Kabeldurchführungen · Fugen & Nähte außen | Bild Dachluke + „Welche Dichtmasse für die Dachluke? → Anleitung“ |
| | | **An Wänden, Türen & innen** | Serviceklappen & Türen (wiederlösbar) · Kantenleisten & Keder · Bad & Küche (innen) | |
| **2** | **Kleben & Montieren** <br>*„Soll halten – ohne Bohren“* | **Aufs Dach** | Solarmodul kleben · SAT-Anlage & Antenne kleben · Markise, Dachträger & Anbauteile | Bild Solarmodul + „Solar-Montage-Set: alles in einem Paket“ |
| | | **Bauteile & Ausbau** | Fenster & Scheiben einkleben · Halter, Leisten & Innenausbau · Seitenwände & Großflächen (Profi) | |
| **3** | **Reparieren & Schützen** <br>*„Etwas ist kaputt oder rostet“* | **Reparieren** | Kunststoff & GFK reparieren · Ausgerissene Schraublöcher · Undichte Stellen & Wasserschaden | Bild Unterboden + „Unterbodenschutz in 3 Schritten“ |
| | | **Schützen** | Unterbodenschutz · Hohlraumschutz · Radkästen | |
| **4** | **Reinigen & Zubehör** <br>*„Damit es hält“* | **Vorbereiten & Finish** | Reinigen & Entfetten · Haftvermittler (Primer) · Fugen glätten & Regenstreifen | Bild Set + „Bestseller: Was Profis immer dabeihaben“ |
| | | **Sets & Werkzeug** | Klebe- & Dichtsets · Kartuschenpressen & Werkzeug · Bestseller | |
| **5** | **Ratgeber** <br>*„Wie mache ich es richtig?“* | **Richtiges Produkt finden** | Produktfinder (3 Fragen) · Welcher DEKAsyl? MS-1, MS-2, MS-5 im Vergleich · Häufige Fragen (FAQ) | Bild Michael Windecker + Buch „Klebt nicht gibt's nicht!“ |
| | | **Anleitungen & Downloads** | Schritt-für-Schritt-Anleitungen · Video-Akademie · Datenblätter & Sicherheitsdatenblätter | |
| **6** | **Warum Dekalin** <br>*„Wem kann ich vertrauen?“* | **Erfahrung** | Seit 1907: unsere Geschichte · Der „Klebepapst“ & sein Buch · Auszeichnungen (HIPE & Plus X 2025) | Bild Schulung + „Kostenlose Anwendungsberatung“ |
| | | **Service** | Kostenlose Anwendungsberatung · Schulungen nach DIN 2304 · Für Gewerbe & Händler | |

„Alle anzeigen“-Link steht in den Kollektions-Welten 1–4 jeweils **am Ende** (nicht oben – erst die konkreten Aufgaben, dann der Sammel-Link).

**Bestseller ohne Ungleichgewicht:** Ein eigener Top-Level-Punkt „Bestseller“ ohne Unterpunkte hätte die Balance gebrochen. Deshalb liegt „Bestseller“ (a) als Link in Spalte „Sets & Werkzeug“, (b) als Menü-Badge „TOP“ an „Kleben & Montieren“ (Vision-Block „Menu Badge“ [V]) und (c) als erste Zeile im Mobile-Menü und im Such-Drawer. Bestseller-Einstiege sind besonders wichtig, weil Dichtstoffnamen für Laien gleich klingen.

**Text-Menü statt Bilder je Link:** Lifestyle-Thumbnails je Menüpunkt machen das Menü lang und unruhig. Bilder gibt es nur als **eine** Promo-Kachel rechts im Mega-Menü (Vision-Feature „In-menu promos“), die auf Anleitung/Set verlinkt.

**Kein „Über uns“, kein Blog, keine Wishlist im Hauptmenü:** werden kaum genutzt und nehmen Produkt-Einstiegen den Platz. „Warum Dekalin“ ist bewusst kein „Über uns“, sondern bündelt kaufrelevante Vertrauensbelege (Geschichte, Schulungen, Beratung, Gewerbe) – nach Livegang Klickrate prüfen und ggf. in den Footer verschieben.

### 2.3 Zuordnung aller Dekalin-Produkte

Ein Produkt erscheint in mehreren Kollektionen (automatische Kollektionen über Tags, siehe `05_shopify_import/collections.md`). Vorbereitungsprodukte (Reiniger, Primer, Presse) erscheinen zusätzlich am Ende jeder Kleben-/Abdichten-Kollektion („Das brauchst du dazu“), damit jede Aufgaben-Kollektion mindestens 3 Produkte hat (Kollektionen < 6 Produkte: verwandte Kollektionen darunter zeigen, damit keine Seite leer wirkt).

| Produkt (Klartext-Unterzeile) | Welt | Kollektionen (Ebene 3) |
|---|---|---|
| **DEKAsyl MS-5** – Kraftkleber für Solarmodule & Anbauteile | Kleben & Montieren | Solarmodul kleben · SAT-Anlage & Antenne · Markise, Dachträger & Anbauteile · Fenster & Scheiben einkleben · Halter, Leisten & Innenausbau · Kantenleisten & Keder · Dachhauben & Kabeldurchführungen · Bestseller |
| DEKAsyl MS-1 – Dichtstoff für Fugen & Nähte (Einsteiger) | Abdichten | Fugen & Nähte außen · Kantenleisten & Keder |
| DEKAsyl MS-2 – Kleb- & Dichtstoff für Nähte & Überlappungen | Abdichten | Fugen & Nähte außen · Kantenleisten & Keder · Dachhauben & Kabeldurchführungen · Undichte Stellen & Wasserschaden |
| DEKAsyl MS-6 – Allround-Dichtstoff innen & außen | Abdichten | Fugen & Nähte außen · Bad & Küche · Fenster & Dachluken · Serviceklappen & Türen · Halter, Leisten & Innenausbau |
| DEKAsyl MS-7 – transparenter Dichtstoff für Bad & Küche | Abdichten | Bad & Küche |
| DEKAsyl MS-8 – Scheibenklebstoff [F: nur auf dekalin.com gelistet] | Kleben & Montieren | Fenster & Scheiben einkleben |
| DEKASEAL 8936 – abtupfbare Dichtmasse, wieder lösbar | Abdichten | Serviceklappen & Türen · Fenster & Dachluken (verdeckte Fuge) · Kantenleisten & Keder · Undichte Stellen & Wasserschaden |
| DEKASEAL 1512 – überlackierbare Butyl-Dichtmasse | Abdichten | Fenster & Dachluken (sichtbare Fuge) · Dachhauben & Kabeldurchführungen · Kantenleisten & Keder · Undichte Stellen & Wasserschaden |
| DEKASEAL 8869 Butyl-Mastic, Butyl-Tape, DEKAPLAST 7303 – Butylmasse & -bänder | Abdichten | Fenster & Dachluken · Dachhauben & Kabeldurchführungen [A: Anwendungen beim Hersteller nicht genannt] |
| DEKAPUR 2K-90 – Kunststoff-Reparatur in 2 Komponenten | Reparieren & Schützen | Kunststoff & GFK reparieren · Ausgerissene Schraublöcher |
| DEKAPUR 2K-6000 A+B – Konstruktionsklebstoff für Seitenwände | Kleben & Montieren | Seitenwände & Großflächen · Undichte Stellen & Wasserschaden [A] |
| DEKAPHON 9735 – Unterbodenschutz-Spray, bitumenfrei | Reparieren & Schützen | Unterbodenschutz · Radkästen |
| DEKAPHON 958 – Unterbodenschutz auf Wasserbasis | Reparieren & Schützen | Unterbodenschutz · Radkästen |
| DEKAPHON Pro-Wax – Hohlraum- & Unterbodenwachs | Reparieren & Schützen | Hohlraumschutz · Unterbodenschutz |
| DEKACLEAN Ultra – Haftreiniger (Flasche & Tücher) | Reinigen & Zubehör | Reinigen & Entfetten + „Das brauchst du dazu“ in allen Kleben-/Abdichten-Kollektionen |
| DEKACLEAN Glass Foam – Fensterreiniger [F: nur im Handel gelistet] | Reinigen & Zubehör | Fugen glätten & Regenstreifen |
| DEKAVATOR 22 NF – Haftvermittler | Reinigen & Zubehör | Haftvermittler (Primer) + „Das brauchst du dazu“ bei Kleben & Montieren |
| DEKAFINISHER – Glättmittel, auch gegen Regenstreifen | Reinigen & Zubehör | Fugen glätten & Regenstreifen + „Das brauchst du dazu“ bei Abdichten |
| Flexsolarmodul-Klebeset (MS-1 + MS-5 + DEKACLEAN Tuch) | Reinigen & Zubehör | Klebe- & Dichtsets · Solarmodul kleben |
| Klebeset für SAT und starre Solaranlagen | Reinigen & Zubehör | Klebe- & Dichtsets · SAT-Anlage · Solarmodul kleben |
| Solar-Montage-Set (neues Shopify-Bundle, [A]) | Reinigen & Zubehör | Klebe- & Dichtsets · Solarmodul kleben |
| Kartuschenpresse, Spachtel [A: Handelsware, kein Dekalin-Produkt] | Reinigen & Zubehör | Kartuschenpressen & Werkzeug |
| Buch „Klebt nicht gibt's nicht!“ (19,99 €) [F] | Ratgeber | Promo-Kachel Ratgeber · Seite „Der Klebepapst & sein Buch“ |

**Prüfung Balance (Anzahl Produkte je Welt, eindeutig zugeordnet):** Abdichten 8 · Kleben & Montieren 3 Kernprodukte + 3 Sets · Reparieren & Schützen 5 · Reinigen & Zubehör 5 + Werkzeug. Die Welten sind über die Anzahl **Aufgaben** (je 6) balanciert, nicht über die Anzahl Produkte – das ist die richtige Größe für ein Aufgaben-Menü.

---

## 3. Mobile-Menü (Vision „header-mobile-navigation“)

```
┌──────────────────────────────┐
│ ☰   DEKALIN-Logo     🔍  🛒2 │  ← eine Zeile, Menü links, Warenkorb rechts
├──────────────────────────────┤
│ 🔍 Wonach suchst du? z. B. … │  ← Suchleiste dauerhaft ausgeklappt
└──────────────────────────────┘

Drawer (von links):
┌──────────────────────────────┐
│ ★ Bestseller               › │
│ Abdichten                  › │──► Am Dach ▸ 3 Links │ An Wänden, Türen & innen ▸ 3 Links │ Alle anzeigen
│ Kleben & Montieren   [TOP] › │
│ Reparieren & Schützen      › │
│ Reinigen & Zubehör         › │
│ ──────────────────────────── │
│ Ratgeber                   › │
│ Warum Dekalin              › │
│ ──────────────────────────── │
│ 🧭 Produktfinder starten     │  ← roter Text-Link, nicht Button (CTA-Rot bleibt dem Kauf vorbehalten)
│ 💬 Kostenlose Beratung       │
│ 👤 Anmelden                  │  ← Login ins Seitenmenü, nicht prominent im Header
└──────────────────────────────┘
```

- **Mobile Dock (neu in Vision 18) deaktivieren:** Eine zweite Navigationsleiste unten ist doppelt und verwirrend und verdeckt auf kleinen Geräten Inhalt.
- **header-secondary-menu (kleine Top-Leiste) deaktivieren:** Höchstens eine Leiste über dem Header. Die Inhalte (Beratung, Gewerbe) wandern ins Mega-Menü „Warum Dekalin“ und in den Footer.
- Mobile first: Der Großteil der Shop-Besucher kommt heute mobil, Prüfung auf 375 px und iPhone SE.

---

## 4. Suche & Produktfinder

### 4.1 Suche (Vision „Enhanced search“, predictive search)
- **Ausgeklappte Suchleiste** unter dem Header (mobil) bzw. im Header (Desktop). Das Sortiment hat über 15 Produkte (rund 22 Dekalin-Artikel plus Zubehör) → ab dieser Größe lohnt eine dauerhaft sichtbare Suche; Profis suchen gezielt nach Produktnamen.
- Platzhalter: **„Wonach suchst du? z. B. Dachluke abdichten“** – lädt zum Suchen nach Aufgabe ein.
- **Such-Drawer** (Vision zeigt „Popular searches“ + „Trending Now“-Produkte [V]): Beliebte Suchen = *Solarmodul kleben · Dachluke abdichten · SAT-Anlage kleben · Unterbodenschutz · Silikon entfernen*; Trending = MS-5, DEKASEAL 8936, DEKACLEAN Ultra, Solar-Montage-Set.
- **Synonyme** (Shopify Search & Discovery → Synonyme): Silikon, Dichtmasse, Fugenmasse, Acryl → Dichtstoff · Kraftkleber, Montagekleber, Konstruktionskleber, High Tack → DEKAsyl MS-5 · Grundierung → Haftvermittler · Solarpanel, Solarplatte, PV-Modul → Solarmodul · Wohnwagen, Caravan, Camper, Kastenwagen → Wohnmobil · Dekalin, Deklain, Dekaline → Dekalin (häufige Tippfehler, [F] Recherche 1.6). [A, rechtlich prüfen:] Wettbewerbs-Produktnamen (z. B. „Sikaflex 252/554“) nur nach Markenrechts-Prüfung als Synonym.
- Label „Suchen“, nicht „Webseite durchsuchen“ – kurz und eindeutig.

### 4.2 Produktfinder „Was hast du vor?“ (Seite `/pages/produktfinder`)
Drei Fragen (Logik wie Würth-Klebstofffinder „Material A + Material B“ [F, Recherche 5]):

| Schritt | Frage | Antworten (Kacheln) |
|---|---|---|
| 1 | Was hast du vor? | Abdichten · Kleben/Montieren · Reparieren · Schützen |
| 2 | Wo am Fahrzeug? | Dach · Außenwand · Fenster/Türen · Unterboden · Innenraum |
| 3 | Auf welchem Material? | Aluminium · GFK/Polyester · lackiertes Blech · Glas · Holz · Kunststoff (PVC/ABS) · weiß nicht |

**Ergebnis:** gefilterte Kollektions-URL, z. B. `/collections/kleben-montieren?filter.p.m.custom.einsatzort=Dach&filter.p.m.custom.untergrund=Aluminium`, plus Hinweis „Unsicher? Kostenlose Beratung“.
**Umsetzung in zwei Stufen** (erst günstig testen, dann investieren):
1. Ohne App: Vision-Seite mit Kachel-Sections (multicolumn), Links auf Filter-URLs.
2. Bei Nutzung > 2 % der Sitzungen: Quiz-App (Typeform günstig, Octane AI teuer).

---

## 5. Filter auf Kollektionsseiten (Shopify Search & Discovery)

Filter über Produkt-Metafelder (Definitionen in `05_shopify_import/metafields.md`). Vision unterstützt Filter und Swatch-Filter [V, Theme Store].

| Filter | Werte | Quelle | Anzeige |
|---|---|---|---|
| **Einsatzort** | Dach · Außenwand · Fenster & Türen · Unterboden & Radkasten · Innenraum | Metafeld `custom.einsatzort` (Liste) | Checkbox |
| **Untergrund** (ohne Primer) | Aluminium · Edelstahl · verzinkter Stahl · lackiertes Metall · Glas · GFK/Polyester · PVC · Holz (lackiert/gestrichen) | `custom.untergrund` (Liste) [F für MS-5, Recherche 2.4] | Checkbox |
| **Eigenschaft** | überlackierbar · wiederlösbar/abtupfbar · transparent · hohe Anfangsfestigkeit · silikonfrei · isocyanatfrei | `custom.eigenschaften` (Liste) | Checkbox |
| **Klebkraft** | 1–5 | `custom.klebkraft` (Ganzzahl) [A: Skala MS-1 = 1, MS-2 = 3, MS-5 = 5] | Bereich |
| **Farbe** | weiß · schwarz · grau · anthrazit · cremeweiß · transparent | Variantenoption | Swatch-Filter |
| **Gebinde** | Tube · 290–310-ml-Kartusche · 560–600-ml-Schlauchbeutel · Spray · Flasche · Set | Variantenoption | Checkbox |
| **Preis** | Bereich | Standard | Slider |
| **Verfügbarkeit** | Auf Lager | Standard | Checkbox |

Sortierung: Standard **„Bestseller“** (Orientierung für Laien); auf Aufgaben-Kollektionen manuell (Hauptprodukt zuerst, Zubehör zuletzt).

---

## 6. Footer-Menüs (Kurzfassung, Details in `02_theme_konfiguration.md`)

| Spalte | Menü-Handle | Links |
|---|---|---|
| Shop | `footer-shop` | Abdichten · Kleben & Montieren · Reparieren & Schützen · Reinigen & Zubehör · Klebe- & Dichtsets · Bestseller |
| Hilfe | `footer-hilfe` | Kostenlose Anwendungsberatung · Produktfinder · Häufige Fragen · Versand & Lieferung · Rückgabe & Widerruf · Kontakt |
| Wissen & Dekalin | `footer-dekalin` | Anleitungen & Videos · Datenblätter & SDB · Über Dekalin (seit 1907) · Schulungen nach DIN 2304 · Gewerbe & Händler · Karriere |
| Rechtliches (Fußzeile) | `footer-rechtliches` | Impressum · AGB · Datenschutz · Widerrufsbelehrung · Versand & Zahlung · Cookie-Einstellungen · Barrierefreiheit |

„Über uns“, Karriere und Rechtliches gehören in den Footer, nicht in die Hauptnavigation.

---

## 7. Begründungen kompakt (für die Präsentation)

| Entscheidung | Begründung |
|---|---|
| Menü nach Aufgabe statt Produktname | Customer-Journey-Navigation; Kunden kennen Namen nicht (Briefing); Lücke im Caravan-Handel [F, Recherche 5] |
| 4 Kauf-Welten + 2 Vertrauens-Welten, je 6 Unterpunkte | Briefing (Balance, Reihenfolge); genug Einstiege, nicht überladen |
| Text-Menü, nur 1 Promo-Kachel | Thumbnails je Menüpunkt machen das Menü unruhig und lang |
| „Alle anzeigen“ am Ende | Erst die konkreten Links, dann der Sammel-Link – lenkt nicht von den Aufgaben ab |
| Bestseller als Link/Badge, Kollektionen nach Bestseller sortiert | Laien können gleich klingende Produktnamen nicht unterscheiden – Bestseller geben Orientierung |
| Suchleiste ausgeklappt + Synonyme | Profis suchen gezielt nach Namen; > 15 Produkte |
| Kein Mobile Dock, keine Secondary-Leiste | Doppelte Leisten verwirren und kosten Platz |
| Produktfinder zuerst ohne App | Erst günstig testen, App erst bei nachgewiesener Nutzung |
| Filter Einsatzort/Untergrund/Eigenschaft | Unsicherheit „passt das auf meinem Material?“ abbauen; Würth-Logik [F] |

## 8. Offene Punkte / Unklarheiten
- **Vision Mega-Menü:** Die Doku beschreibt nur „Mega-Menu“-Block im Header + Auswahl des Hauptpunkts; die Demo zeigt zwei Layouts (Spalten mit Promo-Kacheln und eine Variante mit Sidebar-Tabs) [V]. Exakte Einstellungsnamen (Spaltenzahl, Promo-Felder) im Theme-Editor prüfen.
- **Ausgeklappte Suchleiste:** Ob Vision 18 ein Inline-Suchfeld als Option hat, ist nicht dokumentiert. Fallback: eigene Section in der Header-Gruppe mit Custom Liquid.
- Wer betreibt den Shop (DEKA oder DINOL)? Kanalkonflikt mit Fritz Berger/Reimo klären [F, Recherche 6].
- MS-6, MS-7, MS-8, Butyl-Produkte: Anwendungen teils nur auf dekalin.com, Zuordnung mit Produktmanagement bestätigen.

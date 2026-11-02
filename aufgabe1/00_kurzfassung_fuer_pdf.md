# Aufgabe 1 – Dekalin-Shop auf Shopify Vision: Kurzfassung

**Ausgangslage:** Dekalin verkauft bisher nicht an Endkunden. Die Kunden kennen keine Produktnamen, sie kennen nur ihr Vorhaben: „Solarmodul ohne Bohren aufs Dach“ oder „An der Dachluke kommt Wasser rein“.
**Leitidee:** **Einstieg nach Vorhaben, nicht nach Produktname.** Der Produktname taucht erst auf der Kollektion auf, und zwar immer mit einer Unterzeile in Klartext.
Theme: Vision 18 (Fuel Themes), Preset „Vision“. Markenfarbe Dekalin-Rot `#D42A3B`, Schrift Barlow (beides aus dem Quelltext von dekalin.de).

---

## 1. Navigationskonzept

**Hauptmenü (Mega-Menü): 6 Punkte × 2 Spalten × 3 Links, also gleichmäßig gefüllt**

| | Hauptpunkt | Spalte 1 → 3 Links | Spalte 2 → 3 Links |
|---|---|---|---|
| **Was kann ich kaufen?** | **Abdichten** | *Am Dach:* Fenster & Dachluken · Dachhauben & Durchführungen · Fugen & Nähte außen | *Wände, Türen & innen:* Serviceklappen & Türen (wiederlösbar) · Kantenleisten & Keder · Bad & Küche |
| | **Kleben & Montieren** `TOP` | *Aufs Dach:* **Solarmodul kleben** · SAT-Anlage & Antenne · Markise, Dachträger & Anbauteile | *Bauteile & Ausbau:* Fenster & Scheiben · Halter, Leisten & Innenausbau · Seitenwände (Profi) |
| | **Reparieren & Schützen** | *Reparieren:* Kunststoff & GFK · Schraublöcher · Undichte Stellen & Wasserschaden | *Schützen:* Unterbodenschutz · Hohlraumschutz · Radkästen |
| | **Reinigen & Zubehör** | *Vorbereiten & Finish:* Reinigen & Entfetten · Haftvermittler · Glätten & Regenstreifen | *Sets & Werkzeug:* Klebe- & Dichtsets · Kartuschenpressen · Bestseller |
| **Warum soll ich kaufen?** | **Ratgeber** | *Produkt finden:* Produktfinder (3 Fragen) · MS-1/MS-2/MS-5 im Vergleich · FAQ | *Anleitungen & Downloads:* Schritt-für-Schritt · Video-Akademie · Datenblätter & SDB |
| | **Warum Dekalin** | *Erfahrung:* Seit 1907 · Der „Klebepapst“ & sein Buch · HIPE & Plus X Award 2025 | *Service:* Kostenlose Beratung · Schulungen nach DIN 2304 · Gewerbe & Händler |

- **Mega-Menü** als reines Textmenü, rechts **eine** Promo-Kachel (z. B. „Solar-Montage-Set“). Der Link „Alle anzeigen“ steht am Ende. Thumbnails je Menüpunkt machen das Menü unruhig; „Alle anzeigen“ oben würde vor den eigentlichen Links ablenken.
- **Produkte stehen in mehreren Kollektionen** (automatisch über Tags). MS-5 erscheint z. B. in 7 Aufgaben-Kollektionen. Reiniger, Haftvermittler und Presse erscheinen in jeder Kleben- bzw. Abdichten-Kollektion am Ende.
- **Suche:** Die Suchleiste ist dauerhaft ausgeklappt (Platzhalter „z. B. Dachluke abdichten“), da das Sortiment mehr als 15 Produkte hat und Profis gezielt nach Produktnamen suchen. Zusätzlich gibt es Synonyme (Silikon/Dichtmasse → Dichtstoff, Kraftkleber → MS-5, „Deklain“ → Dekalin).
- **Produktfinder** mit 3 Fragen: Was hast du vor? → Wo am Fahrzeug? → Welches Material? Das Ergebnis ist eine gefilterte Kollektion. Er startet ohne App.
- **Filter** (Search & Discovery über Metafelder): Einsatzort, Untergrund, Eigenschaft (überlackierbar, wiederlösbar …), Klebkraft 1–5, Farbe, Gebinde.
- **Mobil:** Burger-Menü links, Warenkorb rechts. „Bestseller“, „Produktfinder“ und „Beratung“ stehen im Drawer. Das Mobile Dock und die Secondary-Leiste sind **aus**, weil zwei Navigationen verwirren.

---

## 2. Aufbau der Produktseite DEKAsyl MS-5 (Reihenfolge Desktop = Mobil)

| # | Vision-Section / Block | Inhalt | Warum |
|---|---|---|---|
| 1 | `breadcrumbs` | Start › Kleben & Montieren › **Solarmodul kleben** › MS-5 | Der Kunde sieht, dass er in der richtigen Aufgabe ist |
| 2 | `main-product`: **Galerie** (8 Medien) | Packshot mit 3 Callouts · Solarmodul am Dach · 6 Vorteile · Haftgrund-Ampel · 4 Schritte · Ergiebigkeit · Farben · Video | Infos stehen im Bild statt in Tabellen. Feature-Callouts wie bei Amazon. Packshot bleibt Bild 1, damit der Kunde sofort sieht, welches Produkt er kauft |
| 3 | Infobox **über** dem Titel | „Für Solarmodule, SAT-Anlage & Anbauteile – Kleben statt Bohren“ | Klartext steht vor dem unbekannten Produktnamen |
| 4 | Sterne · **Titel** · **USP-Zeile** | „DEKAsyl MS-5 High-Tack Kleb- & Dichtstoff“ / „Klebt Solarmodul, SAT-Anlage & Anbauteile ohne Bohren – und dichtet gleich mit.“ | Ein klares Hauptversprechen direkt am Produktnamen. Sie folgt der Rule of One |
| 5 | Preis + Grundpreis + Versandschwelle | 19,95 € · 68,79 €/l · ab 49 € versandkostenfrei [A] | Der Grundpreis ist Pflicht und relativiert den Preis. Die Schwelle motiviert, Zubehör dazuzunehmen |
| 6 | Varianten als **Bild-Swatches** | Weiß/Schwarz (Fugenfoto) · 290-ml-Kartusche/600-ml-Beutel. Grau gibt es nicht und wird zu MS-2 verwiesen | Bild-Swatches zeigen die echte Fugenfarbe. Die Bestseller-Variante ist vorausgewählt |
| 7 | **Lieferzeile über dem ATC** | ● Auf Lager – in 1–3 Werktagen bei dir | Wer klickt, sieht die Lieferzeit genau dort |
| 8 | **ATC** | volle Breite, 64 px, Rot, „In den Warenkorb“. Keine Menge, kein Buy-it-now, kein Sticky ATC | Ein klarer Kaufweg: Sticky ATC verdeckt mobil Inhalt, mehrere Kauf-Buttons und Werbesprache lenken ab |
| 9 | Icon-Liste + Set-Hinweis + 4 Bullets + 5 Kerndaten | Versand · Original · **kostenlose Beratung** / Solar-Montage-Set / Spezifikationstabelle | Nimmt Risiko, bringt das Bundle früh ins Blickfeld, gibt Profis die Zahlen |
| 10 | `multicolumn` Vorteile | „Klebt. Dichtet. Hält.“ mit 6 Icons | Nutzen auf einen Blick, Feature → Ergebnis |
| 11 | `media-grid` Anwendungen | 6 Bildkacheln, jede verlinkt auf ihre Aufgaben-Kollektion | Der Kunde erkennt sein Projekt wieder |
| 12 | Haftgrund-Ampel | Grün ohne Primer / Gelb mit DEKAVATOR / Rot: PE, PP, Teflon | Nimmt den größten Einwand ehrlich vorweg |
| 13 | `background-video` + `image-with-text-slideshow` | **Storytelling:** „Kleben auf Meisterniveau“ – 1907 gegründet, Automobilbau, Caravaning, Schulungen, „Klebepapst“ & Buch | Tiefe und Vertrauen ohne Superlative |
| 14 | `scrolling-content` | So klebst du ein Solarmodul in 4 Schritten (12 min Haut · 15 min fügen · 24–48 h) | Das WIE macht das Ergebnis vorstellbar |
| 15 | Vergleichstabelle | MS-1 / MS-2 / MS-5 mit Klebkraft ●○○○○ bis ●●●●● · MS-5 vs. Sikaflex-554 (nur Datenblattwerte) | Klärt die Namensverwirrung, begründet das Upgrade, grenzt fair ab |
| 16 | `promotion-blocks` + Bundles | **Solar-Montage-Set**: 2 × MS-5 + Reiniger + Haftvermittler + Presse, 69,95 € [A] | Höherer Warenkorb und sicherer Erfolg |
| 17 | `tabbed-content` | Technische Daten · Haftgründe · Verarbeitung · Downloads (TDB, SDB, Resistenz, CLP, Herstellerangaben) | Profis bekommen alles, Laien werden nicht erschlagen |
| 18 | `text-with-icons` | Beratung · Anwendungsversprechen [A] · Versand · Original | Risiko nehmen |
| 19 | `collapsible-content` | 10 FAQ (Solar ohne Bohren, Primer, Zeiten, Lackieren, MS-1/2, Silikon, Temperatur, Verbrauch, Farben, Reste) | Letzte Einwände, schließt die Datenlücken |
| 20 | `app-wrapper` Bewertungen | Proof-Block mit 3 Bewertungen und Widget mit Fotos | Social Proof, nur echte Bewertungen |
| 21 | `product-recommendations` | Passt dazu (Zubehör-Kollektion) | Cross-Sell; „Zuletzt angesehen“ bewusst weggelassen, damit der Fokus auf dem passenden Zubehör bleibt |

**Bewusst weggelassen:** Sticky ATC, Buy-it-now, Mengenwähler, Stock-Counter und Countdown, UGC-Section, Wishlist, „Made in Germany“ (nicht belegt) und Superlative.

---

## 3. Header & Footer

**Header:** Genau **eine** Announcement Bar in Anthrazit mit 3 rotierenden Trust-Texten: Versand 1–3 Tage · Direkt vom Hersteller seit 1907 · Kostenlose Beratung. Desktop: Logo links, Mega-Menü, Suchfeld, Konto und Warenkorb in einer Zeile von 72 px, beim Hochscrollen sticky. Mobil: ☰ – Logo – 🔍 – 🛒, darunter die Suchleiste. Die Secondary-Leiste und das Mobile Dock sind aus.
**Footer** (dunkel): Marke + Kontakt + Social · **Shop** · **Hilfe** · **Wissen & Dekalin** (je 6 Links) · Newsletter „Klebe-Tipps vom Profi“ mit Einwilligung · Trust-Zeile mit Zahlungsicons (hier statt auf der Produktseite) · Rechtliches inkl. Barrierefreiheit.
**Theme-Konfiguration:** Rot `#D42A3B` nur für Kauf-Aktionen (sitewide gleich, auch im Cart und Checkout), Text `#262626`, Flächen `#F5F5F5`/`#EBEBEB`, Lager-Grün `#2E7D32`. Barlow 700/400. Buttons mit 6 px Radius. Favicon: rotes Quadrat mit weißem „D“, das als Kleberaupe ausläuft.

---

## 4. Annahmen & offene Fragen

- **Preise** 19,95 € (290 ml) und 32,95 € (600 ml), Versandschwelle 49 €, Lieferzeit, Set-Preis: alles Annahmen. Die Preise orientieren sich am Handel (16,95–27,60 €) und liegen bewusst nicht unter dem Fachhandel (Kanalkonflikt).
- **Farben:** MS-5 gibt es laut Datenblatt nur in Weiß und Schwarz, Schwarz nur als 290 ml. Grau gibt es bei MS-1 und MS-2.
- **Ergiebigkeit** „≈ 7 m Raupe mit Ø 7 mm“ ist eine eigene Rechnung, keine Herstellerangabe.
- **Bewertungen:** Bewertungszahlen in Mockups sind Beispiele. Händlerbewertungen (Fritz Berger 4,96/5) sind nur mit Erlaubnis nutzbar.
- **Zu klären:** Betreiber DEKA oder DINOL (Impressum, GPSR) · Garantiebedingungen · Beratungskanal · Award-Bezug · rechtliche Freigabe des Sikaflex-Vergleichs (§ 6 UWG).
- **Vision:** Exakte Einstellungsnamen (Spezifikationstabelle, Vergleichstabelle, Inline-Suche, Mengenwähler) im Editor prüfen. Die Section- und Blocknamen stammen aus der Live-Demo v18.0.0.

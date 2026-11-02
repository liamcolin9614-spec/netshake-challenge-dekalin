# 03 – PDP-Bauplan „DEKAsyl MS-5“ (Shopify Vision 18)

Kennzeichnung: **[F]** Fakt aus `recherche/dekalin_recherche.md` (Datenblatt 07.2024, dekalin.de/.com) · **[A]** Annahme/Beispielinhalt · **[V]** Section/Block in der Vision-Demo nachgewiesen · **[?]** Name/Option im Editor prüfen.

Alle finalen Texte stehen copy-paste-fertig in `04_pdp_texte.md`; hier stehen Struktur, Ziel, Inhalt (Kurzform), Bildidee und Begründung.

---

## 0. Strategie in einem Satz

**Der Kunde kommt mit einer Aufgabe („Solarmodul ohne Bohren aufs Dach“), nicht mit einem Produktnamen.** Die Seite beantwortet deshalb in dieser Reihenfolge: *Ist das das Richtige für mein Vorhaben? → Hält es auf meinem Material? → Wie mache ich es? → Kann ich Dekalin vertrauen? → Was brauche ich noch?* – und hält den Kauf dabei mit einem Klick erreichbar.

- **Big Idea / Rule of One:** *„Kleben statt Bohren“* – MS-5 ist der Kraftkleber, mit dem Solarmodul, SAT-Anlage und Anbauteile ohne Bohrloch aufs Dach kommen und gleichzeitig abgedichtet sind. Ein Versprechen, alle übrigen Vorteile in Bullets/Icons.
- **Awareness-Stufe 3–4** (voller Markt, Sikaflex als Platzhirsch): konkreten USP erklären (hohe Anfangsfestigkeit = weniger Klemmen; −40 bis +120 °C; ohne Primer auf Alu/GFK/Glas) statt „elastisch, wetterfest“ wie alle.
- **Unsicherheit abbauen** ist der Kernjob einer technischen PDP.
- **Nur belegte Werte** aus dem Datenblatt; Lücken offen benennen (keine TÜV-/Windkanal-Nachweise, keine offizielle Ergiebigkeit) [F, Recherche 2.8].

---

## 1. Gesamtübersicht (Reihenfolge Desktop = Mobil)

| # | Vision-Section (Template `product`) | Inhalt | Verkaufspsychologisches Ziel | Farbschema |
|---|---|---|---|---|
| 0 | Header-Gruppe: `announcement-bar` + `header` (+ eigene Suchleiste mobil) | USP-Leiste, Mega-Menü, Suche | Orientierung, Trust ab Sekunde 1 | Dunkel / Standard |
| 1 | `breadcrumbs` [V] | Start › Kleben & Montieren › Solarmodul kleben › DEKAsyl MS-5 | Kontext: „Ich bin in der richtigen Aufgabe“ | Standard |
| 2 | **`main-product`** [V] (Galerie + Buybox) | Above the fold, siehe 2.1–2.2 | Passung bestätigen, Kauf mit 1 Klick | Standard |
| 3 | `multicolumn` [V] | 6 Vorteile als Icons „Klebt. Dichtet. Hält.“ | Nutzen schnell erfassen | Hell |
| 4 | `media-grid` [V] | 6 Anwendungen als Bildkacheln mit Link | Selbsterkennung „Das ist mein Projekt“ | Standard |
| 5 | `rich-text` + `multicolumn` [V] | Haftgrund-Ampel: Hält es auf meinem Material? | Größten Einwand vorwegnehmen | Hell |
| 6 | `background-video` [V] + `image-with-text-slideshow` [V, Startseite] | Storytelling „Warum MS-5? Profi-Know-how seit 1907“ | Tiefe, Marke, Vertrauen | Dunkel |
| 7 | `scrolling-content` [V] | So geht's: 4 Schritte Solarmodul kleben + Zeiten | Das WIE macht es vorstellbar | Standard |
| 8 | Vergleichstabelle (Vision-Feature „Product comparison table“ [V: fuelthemes.net], Section-Name [?]; Fallback `custom-liquid`) | MS-1 / MS-2 / MS-5 mit Klebkraft-Skala + MS-5 vs. Sikaflex-554 | Richtige Wahl absichern, Abgrenzung ohne Bashing | Hell |
| 9 | `promotion-blocks` [V] bzw. Bundle-App-Block | Solar-Montage-Set (Bundle) | Warenkorb erhöhen, Erfolg absichern | Standard |
| 10 | `tabbed-content` [V] (Demo: „Tech Specs“) | Technische Daten · Haftgründe · Verarbeitung · Downloads & Sicherheit | Profis/Skeptiker bedienen, ohne Laien zu erschlagen | Standard |
| 11 | `text-with-icons` [V, Startseite] | Beratung · Anwendungsversprechen · Versand · Original vom Hersteller | Risiko nehmen | Hell |
| 12 | `collapsible-content` [V] | FAQ (10 Fragen) | Letzte Einwände | Standard |
| 13 | `app-wrapper` [V] (Bewertungs-App) | Produktbewertungen | Social Proof | Standard |
| 14 | `product-recommendations` [V] | „Passt dazu“ | Cross-Sell | Hell |
| 15 | Footer-Gruppe | siehe 02 | Vertrauen, Rechtliches | Dunkel |

Section-Abstände über `section-spacer` [V] einheitlich (Desktop 80 px, mobil 48 px).

Reihenfolge folgt der typischen Fragenkette unter dem Kaufbereich (Benefit → Anwendung/Anleitung → Garantie → Zubehör/Bundle → Vergleich → FAQ → Bewertungen → Cross-Sell); Anwendungen und Haftgrund-Ampel stehen bewusst **vor** der Story, weil für dieses Produkt „Passt das zu meinem Vorhaben?“ die erste Frage ist.

---

## 2. Above the fold – Section `main-product`

### 2.1 Layout

**Desktop (1440 px):** Galerie links 58 % (Thumbnails links, sticky), Buybox rechts 42 %.

```
┌──────────────────────────────────────────────┬─────────────────────────────────────────┐
│ ▢   ┌──────────────────────────────────────┐ │ [Infobox: ☀ Für Solarmodule, SAT &      │
│ ▢   │                                      │ │  Anbauteile – Kleben statt Bohren]     │
│ ▢   │   BILD 1: Kartusche MS-5 weiß        │ │ ★★★★★ 4,9 · 52 Bewertungen [Beispiel]  │
│ ▢   │   + 3 Callouts                       │ │ DEKAsyl MS-5 High-Tack Kleb- &          │
│ ▢   │                                      │ │ Dichtstoff                              │
│ ▢   │                                      │ │ Klebt Solarmodul, SAT-Anlage & Anbau-   │
│     └──────────────────────────────────────┘ │ teile ohne Bohren – und dichtet gleich  │
│                                              │ mit.                                     │
│                                              │ 19,95 €   68,79 € / l · inkl. MwSt.      │
│                                              │ zzgl. Versand · ab 49 € versandkostenfrei│
│                                              │ Farbe: Weiß   [▢ weiß] [■ schwarz]       │
│                                              │ Gebinde: [290-ml-Kartusche] [600-ml-Beutel]│
│                                              │ ● Auf Lager – in 1–3 Werktagen bei dir  │
│                                              │ [██████ In den Warenkorb ██████] 64 px  │
│                                              │ 🚚 Versand 1–3 Tage  ✓ Original  💬 Beratung│
│                                              │ ┌ Für Solarmodule: Solar-Montage-Set ─┐ │
│                                              │ │ MS-5 + Reiniger + Primer + Presse  › │ │
│                                              │ └──────────────────────────────────────┘ │
│                                              │ ✓ ✓ ✓ ✓ 4 Kurz-Bullets                  │
│                                              │ ▸ Technische Kurzdaten (Spec-Tabelle)   │
└──────────────────────────────────────────────┴─────────────────────────────────────────┘
```

**Mobil (375 px):**
```
┌───────────────────────────────┐
│ Announcement · Header · Suche │
│ Start › Solarmodul kleben     │
│ ┌───────────────────────────┐ │
│ │ BILD 1 volle Breite, 1:1  │ │  ← Swipe-Galerie, Punkte
│ │ + Callouts                │ │
│ └───────────────────────────┘ │
│ ☀ Für Solarmodule, SAT & Anbauteile │
│ ★★★★★ 4,9 (52) [Beispiel]     │
│ DEKAsyl MS-5 High-Tack        │
│ Kleb- & Dichtstoff            │
│ Klebt Solarmodul, SAT-Anlage …│
│ 19,95 €  68,79 €/l            │
│ [▢ weiß] [■ schwarz]          │
│ [290 ml] [600 ml]             │
│ ● Auf Lager – 1–3 Werktage    │
│ [████ In den Warenkorb ████]  │  ← ca. 1,3 Viewports bis hier (iPhone SE prüfen)
│ 🚚 1–3 Tage ✓ Original 💬 Beratung │
│ ┌ Solar-Montage-Set ›       ┐ │
└───────────────────────────────┘
```
Ziel mobil: ATC innerhalb des ersten Viewports auf 390 × 844 (iPhone 14), auf iPhone SE spätestens nach einem kurzen Scroll. Deshalb: keine Mengenauswahl, kein Share, kein Laufband, keine Rabattbox über dem ATC.

### 2.2 Blöcke in `main-product` (Reihenfolge)

| # | Vision-Block | Inhalt (Kurz; Volltext in 04) | Ziel | Begründung |
|---|---|---|---|---|
| G | **Galerie** (Media, Thumbnails links, Zoom) [V] | 8 Medien, siehe 2.3 | Produkt + Nutzen in Bildern | Infos ins Bild statt Tabellen – auf dem Handy schneller erfasst |
| 1 | **Infobox** (kleines Icon + Text über dem Titel) [V] | Icon Sonne/Dach + „Für Solarmodule, SAT-Anlage & Anbauteile – Kleben statt Bohren“ | Klartext **vor** dem unbekannten Namen | Kunde kennt den Namen nicht; Kontext zuerst |
| 2 | **Bewertungssterne** (App-Block der Bewertungs-App) | ★ Durchschnitt + Anzahl, Link zu #bewertungen | Social Proof sofort | Produktbewertungen statt Shopbewertung (konkreter, glaubwürdiger). **[A] Start ohne Bewertungen:** Block blendet sich leer aus; Fritz-Berger-Wert 4,96/52 [F] darf **nicht** als eigene Bewertung erscheinen (UWG). In Mockups als „Beispiel“ markieren. |
| 3 | **Title** [V] | „DEKAsyl MS-5 High-Tack Kleb- & Dichtstoff“ (max. 2 Zeilen, ohne Art.-Nr.) | Produkt + Kategorie eindeutig | Kurzer Titel mit Produktart statt Artikelnummer – lesbar und eindeutig |
| 4 | **Custom Liquid: USP-Zeile** aus `custom.usp_zeile` (einzeilig, nicht farbig, `#4F4F4F`, 16 px) | „Klebt Solarmodul, SAT-Anlage & Anbauteile ohne Bohren – und dichtet gleich mit.“ | Ein Hauptversprechen | Klares Hauptversprechen direkt am Produktnamen; Ergebnis in 3. Person |
| 5 | **Price** [V] + Custom Liquid Grundpreis | 19,95 € · 68,79 € / l · inkl. MwSt. zzgl. Versand · „ab 49 € versandkostenfrei“ | Preis relativieren, Schwelle motiviert zu Zubehör | Grundpreis Pflicht (PAngV, je 1 l); Gratisversand-Schwelle neben Preis nimmt die Versandkosten-Frage vorweg; Preise [A] |
| 6 | **Variant picker** (Swatches) [V] | **Farbe:** Weiß · Schwarz (Bild-Swatch = Foto einer Fuge) · **Gebinde:** 290-ml-Kartusche · 600-ml-Schlauchbeutel (Mini-Packshot). Vorausgewählt: Weiß / 290 ml | Wahl ohne Nachdenken | Bild-Swatches zeigen die echte Fugenfarbe; Bestseller vorauswählen (ein Klick weniger). **Grau gibt es für MS-5 nicht** [F: Datenblatt nur weiß/schwarz] → Hinweis-Link „Grau? → DEKAsyl MS-2“. Schwarz nur 290 ml [F] → Kombination Schwarz/600 ml wird nicht angelegt. |
| 7 | **Inventory notice** [V] → ersetzt bzw. ergänzt durch Custom Liquid Lieferzeile | „● Auf Lager – in 1–3 Werktagen bei dir“ (grün `#2E7D32`, nur wenn verfügbar) | Sicherheit direkt vor dem Klick | Lieferzeit direkt über ATC – die Frage „Wann kommt es?“ wird am Klickpunkt beantwortet. Vision-Stock-Counter („nur noch X“) **aus** – keine künstliche Verknappung |
| 8 | **Product form** [V] | ATC „In den Warenkorb“, volle Breite, 64 px, `#D42A3B`; Menge aus; „Buy it now“ aus | Kauf so einfach wie möglich | Ein großer, klarer Button mit erwartbarem Text; keine konkurrierenden Kauf-Buttons |
| 9 | **Icon list** [V] | 🚚 Versand in 1–3 Werktagen · ✓ Original vom Hersteller · 💬 Kostenlose Anwendungsberatung (Link öffnet Kontakt) | Risiko nehmen, Beratung für Unsichere | Benefit-Zeile statt Payment-Badge; Beratungs-CTA unter ATC für alle, die noch unsicher sind |
| 10 | **Infobox** (2. Instanz, mit Link) [V] | „Für Solarmodule: **Solar-Montage-Set** – MS-5, Reiniger, Haftvermittler & Presse in einem Paket. Ansehen ›“ | Bundle früh sichtbar | Zubehör und Set früh präsent machen |
| 11 | **Short description** [V] | 4 Bullets (Rest unten) | Schnell-Scanner bedienen | Kondensierte Info |
| 12 | **Specification table** [V] (metafeldgesteuert laut fuelthemes.net) | 5 Kernwerte: Haut nach ca. 12 min · −40 bis +120 °C · ohne Primer auf Alu, GFK, Glas, PVC · überlackierbar · Shore A ca. 55 | Profis bekommen Zahlen sofort | Spezifische Zahlen schaffen Vertrauen |
| – | Deaktiviert: Scrolling text, Discount code, Share, Sticky Add-to-cart, Stock counter | | | Sticky-ATC verdeckt mobil Inhalt; Platz über ATC ist knapp |

### 2.3 Galerie mit Feature-Callouts (8 Medien)

Callouts nach Grafik-Header-Regeln: links oben, 3–7 Wörter, wünschenswerter Zustand; Packshot bleibt Bild 1, damit sofort klar ist, welches Produkt man kauft.

| # | Motiv | Headline (links oben) | Callouts / Inhalt | Begründung |
|---|---|---|---|---|
| 1 | Packshot Kartusche weiß, freigestellt, weißer Grund, daneben kleine Raupe | **Kleben statt Bohren.** | 3 Pins: „Hält sofort – weniger Klemmen“ · „−40 bis +120 °C“ · „Ohne Primer auf Alu, GFK & Glas“ | Callouts aus Kauftreibern |
| 2 | Wohnmobildach, Solarmodul mit Spoilern, Detail-Lupe auf Klebenaht | **Solarmodul ohne ein Bohrloch** | „Spoiler aufkleben, Dach bleibt dicht“ · „Klebt & dichtet in einem Schritt“ | Use-Case-Bild verkauft Emotion |
| 3 | Infografik 6 Icons (Vorteile) | **Klebt. Dichtet. Hält.** | Hohe Anfangsfestigkeit · UV- & alterungsbeständig · dauerelastisch · überlackierbar · ohne Lösemittel/Isocyanat/Silikon · geruchlos | USP-Infografik |
| 4 | Haftgrund-Raster (Ampel) mit Materialmustern | **Hält auf deinem Material?** | Grün: Alu, Edelstahl, verzinkter Stahl, Kupfer, Messing, pulverbeschichtet, lackiertes Metall, Glas, PVC, GFK, lackiertes Holz · Gelb: bei Feuchte/hoher Last → DEKAVATOR 22 NF · Rot: PE, PP, Teflon | Kompatibilitäts-Unsicherheit abbauen |
| 5 | Ablauf in 4 Bildern (Reinigen – Raupe – Fügen – fertig) mit Uhr-Icons | **In 4 Schritten fest am Dach** | 12 min Haut · 15 min fügen · 4 mm in 24 h · 24–48 h Endfestigkeit (Set-Angabe) [F] | Anleitung macht die Anwendung vorstellbar |
| 6 | Maßbild Kartusche + Raupe mit Maßstab | **Was in einer Kartusche steckt** | 290 ml · Raupe Ø 7 mm ≈ 7 m [A: Rechenwert, Hersteller bestätigen] · Klebeschicht 2 mm, SAT-Naht 3–5 mm [F] | Maße ins Bild |
| 7 | Farbvergleich weiß/schwarz auf weißem und schwarzem Dach, „überlackierbar“-Pinsel | **Weiß, Schwarz – oder in Wagenfarbe** | „Nach Hautbildung nass in nass überlackierbar“ | Farbwahl erleichtern |
| 8 | Video 30–45 s (extern gehostet, lazy) „Solarplattenhalterung kleben“ – vorhandenes Dekalin-Video [F: auf Seite MS-5 schwarz eingebunden] | – | Untertitel an, Ton aus | Video komprimiert, lazy – schont die Ladezeit |

Varianten-Bildsets: Bei Schwarz wechseln Bild 1, 2, 7 auf schwarze Kartusche/Fuge (Vision „Variant image set“ [V: Fuel-Doku]).

---

## 3. Below the fold – Section für Section

### Section 3 · `multicolumn` – Vorteile „Klebt. Dichtet. Hält.“
- **Ziel:** Nutzen in 5 Sekunden; jedes Feature in ein Ergebnis übersetzt (Feature → damit → Nutzen).
- **Inhalt:** H2 + 6 Spalten (Desktop 3 × 2, mobil 2 × 3 bzw. horizontal scrollbar), je Icon (Linien-Icon `#262626`, Akzentpunkt rot), Titel, 1 Satz:
  1. Hält sofort – hohe Anfangsfestigkeit, Klemmen oft unnötig [F]
  2. Ohne Primer auf Alu, GFK, Glas & PVC [F]
  3. −40 bis +120 °C, kurzzeitig 180 °C [F]
  4. Sehr gute UV- & Alterungsbeständigkeit [F]
  5. Nass in nass überlackierbar [F]
  6. Ohne Lösemittel, Isocyanat & PVC – geruchlos [F]
- **Bild:** keine Fotos, nur Icons (schnell, ruhig).
- **Begründung:** Benefit-/USP-Infografik; bewusst schlicht gehalten – Icons und ein Satz reichen, aufwendiges Design bringt hier keinen Mehrwert.

### Section 4 · `media-grid` – Anwendungsbereiche „Wofür Profis MS-5 nehmen“
- **Ziel:** Selbsterkennung; jede Kachel führt in die Aufgaben-Kollektion (Navigation und PDP greifen ineinander).
- **Inhalt:** 6 Bildkacheln mit Overlay-Titel + Link:
  Solarmodul & Spoiler → /collections/solarmodul-kleben · SAT-Anlage & Antenne → /collections/sat-anlage-antenne-kleben · Markise, Dachträger & Anbauteile → /collections/markise-dachtraeger-anbauteile-kleben · Fenster & Dachdurchführungen → /collections/fenster-scheiben-einkleben · Kantenprofile an Anhängern (Alu/Polyester) → /collections/kantenleisten-keder · Halter & Abdeckungen im Ausbau → /collections/halter-leisten-innenausbau-kleben [alle Anwendungen F, Recherche 2.3].
- **Bild:** echte Anwendungsfotos am Wohnmobil (Dach von oben, Detail Klebenaht), einheitlicher Look, leichte Abdunklung für weiße Schrift.
- **Begründung:** Use-Case-Bilder mit Text „geeignet für …“ – der Kunde erkennt sein Projekt wieder.

### Section 5 · `rich-text` + `multicolumn` – Haftgrund-Ampel „Hält es auf meinem Material?“
- **Ziel:** Den größten Einwand (falscher Untergrund → hält nicht) aktiv beantworten; ehrlich Grenzen nennen (nimmt dem Einwand den Wind aus den Segeln).
- **Inhalt:** 3 Spalten:
  - 🟢 **Hält ohne Primer:** Aluminium, Edelstahl, verzinkter Stahl, Zink, Kupfer, Messing, pulverbeschichtetes und lackiertes Metall, Glas, PVC, GFK/Polyester, lackiertes/gestrichenes Holz [F]
  - 🟡 **Mit Haftvermittler:** hohe thermische/physikalische Last, vor allem bei Feuchtigkeit → DEKAVATOR 22 NF [F] (Quick-Add-Link)
  - 🔴 **Hält nicht:** PE, PP, Teflon → „Ruf uns an/schreib uns, wir finden eine Lösung“ [F]
  - Unter allen: „Immer: Fläche sauber, trocken, staub- und fettfrei – mit DEKACLEAN Ultra. Im Zweifel Haftungstest.“ [F]
- **Begründung:** Rückversicherung vor dem Kauf („hält das auf meinem Material?“) – weniger Fehlkäufe und Retouren; Einwand klar beantwortet.

### Section 6 · `background-video` + `image-with-text-slideshow` – Storytelling „Warum MS-5?“
- **Ziel:** Tiefe und Vertrauen: Wer steckt dahinter, warum ist das Profi-Know-how? Abgrenzung durch Herkunft und Wissen, nicht durch Superlative.
- **Aufbau:**
  1. `background-video` (Schema Dunkel, 60 vh Desktop / 70 vh mobil, stumm, Loop 15 s): Hände tragen eine Raupe auf, Solarspoiler wird gesetzt. Overlay-Headline **„Kleben auf Meisterniveau.“** + Subline + Sekundär-Button „Unsere Geschichte“.
  2. `image-with-text-slideshow` (3 Slides, Bild links/Text rechts):
     - **1907 – Klebstoff ist unser Handwerk:** Gründung als „Deutsche Klebstoffwerke“, ab 1935 Partner des Automobilbaus [F].
     - **Vom Werkstatt-Profi zum Wohnmobil-Dach:** seit 2012 Caravaning, Klebeanleitungen für Solar, SAT, Markise [F]. Warum MS-5 an der Spitze von MS-1 (Einsteiger) und MS-2 (Fortgeschrittene) steht [F].
     - **Wir bringen Kleben bei:** Schulungen seit 2014, nach DIN 2304, Kurse zum Klebepraktiker (DVS/EWF), Buch „Klebt nicht gibt's nicht!“ von Michael Windecker, dem „Klebepapst“; HIPE Award & Plus X Award 2025 [F; Produktbezug der Awards prüfen].
- **Bild:** echte Fotos Schulungscenter, Michael Windecker mit Buch, historisches Werksfoto (falls verfügbar).
- **Begründung:** Vertrauen durch Herkunft/Expertise, „kostenloses Wissen“ als Vertrauensstufe; Herkunfts-Storytelling ist ein starkes Argument für eine Traditionsmarke. **Kein „Made in Germany“**, da nicht belegt [F: L].

### Section 7 · `scrolling-content` – „So klebst du ein Solarmodul in 4 Schritten“
- **Ziel:** Das WIE macht das Ergebnis vorstellbar und senkt die Angst vor Fehlern.
- **Inhalt:** 4 horizontale Karten (mobil swipebar) mit Foto, Schritt-Titel, 2 Sätzen, Zeit-Badge:
  1. **Reinigen** – DEKACLEAN Ultra, Fläche sauber/trocken/fettfrei; bei Feuchte/hoher Last DEKAVATOR 22 NF. *Badge: 5 min*
  2. **Raupe ziehen** – Düse auf ca. 7 mm, Raupe auf Spoiler/Halter; +5 bis +35 °C. *Badge: 7-mm-Raupe* [F]
  3. **Fügen & andrücken** – innerhalb von 15 min, bis ca. 3–5 mm Klebenaht; wärmer = schneller. *Badge: < 15 min* [F]
  4. **Aushärten lassen** – Haut nach ca. 12 min, 4 mm in 24 h; volle Belastung nach 24–48 h. *Badge: 24–48 h* [F, Set-Angabe]
  - Darunter Text-Link „Ganze Anleitung mit Video“ → dekalin-Anleitung (Seite `/pages/anleitung-solarmodul-kleben`).
- **Begründung:** Anleitungs-Slider für erklärungsbedürftige Produkte, Montage-Klarheit.

### Section 8 · Vergleich – „Welcher DEKAsyl passt?“ + „MS-5 und Sikaflex-554 im Datenblatt-Vergleich“
- **Vision:** Feature „Product comparison table“ (laut fuelthemes.net) [V]; Section-Name im Editor [?]. Fallback: `custom-liquid` mit HTML-Tabelle (Theme-Styles erben).
- **Ziel:** Kunden können Dichtstoffnamen nicht unterscheiden → klare Stufung; Upgrade-Begründung für den höheren Preis; Abgrenzung zum Platzhirsch ehrlich.
- **Tabelle A – Dekalin-Familie** [F: Positionierung/Farben/Gebinde/Anwendungen; Skala A]:

| | DEKAsyl MS-1 | DEKAsyl MS-2 | **DEKAsyl MS-5** |
|---|---|---|---|
| Für wen | Einsteiger | Fortgeschrittene | **Profis & anspruchsvolle Projekte** |
| Klebkraft-Skala [A] | ●○○○○ | ●●●○○ | **●●●●●** |
| Ideal für | Fugen, Dichtnähte, Überlappungen | Verbindungen, Dichtnähte, Solaranlagen, Überlappungen | **Solarmodule, SAT-Anlagen, Spoiler, Dachkonstruktionen, Karosseriemontage** |
| Hohe Anfangsfestigkeit (High Tack) | – | – | **✓** |
| Farben | weiß, grau, schwarz | weiß, grau, schwarz | weiß, schwarz |
| Gebinde | 290 ml | 290 ml, 600 ml | 290 ml, 600 ml (weiß) |
| | [Zum MS-1] | [Zum MS-2] | **(diese Seite)** |

- **Tabelle B – MS-5 vs. Sikaflex-554** (nur Herstellerangaben, unterschiedliche Prüfnormen möglich) [F, Recherche 4.2]:

| Datenblatt-Wert | DEKAsyl MS-5 | Sikaflex-554 |
|---|---|---|
| Basis | MS-Polymer | STP (silanterminiertes Polymer) |
| Hautbildung | ca. 12 min (20 °C) | 25 min (23 °C) |
| Shore-A-Härte | ca. 55 | 55 |
| Zugscherfestigkeit | ca. 2,5 MPa | 2,5 MPa |
| Zugfestigkeit | ca. 2,8 MPa | 3,5 MPa |
| Bruchdehnung | ca. 210 % | 500 % |
| Temperaturbeständigkeit | −40 bis +120 °C, kurz 180 °C | −50 bis +90 °C |
| Verarbeitung | +5 bis +35 °C | +5 bis +40 °C |
| Lagerfähigkeit | 18 Monate (Kartusche) | 12 Monate |
| Nachweise | keine genannt | DIN EN 45545-2, ISEGA |

  Fazit-Zeile (fair): *„Beide kleben gleich fest auf Scherung. MS-5 bildet schneller Haut und ist für höhere Dachtemperaturen ausgelegt; Sikaflex-554 ist dehnfähiger und hat Bahn-/Lebensmittel-Nachweise.“*
- **Begründung:** Vergleichstabelle; Abgrenzung ohne Bashing, zeigen, dass man die Konkurrenz kennt. **Rechtlich [A]:** vergleichende Werbung nach § 6 UWG nur mit objektiven, nachprüfbaren Werten, Quelle (Sika-Datenblatt, Stand) angeben, Marke nicht herabsetzen → vor Livegang juristisch freigeben.

### Section 9 · `promotion-blocks` / Shopify Bundles – „Solar-Montage-Set“
- **Ziel:** Warenkorb erhöhen und gleichzeitig Erfolg absichern (wer reinigt und primert, hat weniger Reklamationen).
- **Inhalt:** Bild Set flatlay (2 Kartuschen, Reiniger, Haftvermittler, Presse), H2 „Alles für ein Solarmodul in einem Paket“, Inhaltsliste, Preis 69,95 € statt 77,75 € Einzelpreis [A], ATC „Set in den Warenkorb“ (gleicher roter Button). Darunter 3 Quick-Add-Kacheln einzeln: DEKACLEAN Ultra · DEKAVATOR 22 NF · Kartuschenpresse.
- **Hinweis:** Das offizielle **Flexsolarmodul-Klebeset** (Art. 62700/62701: MS-1 + MS-5 + DEKACLEAN-Tuch [F]) wird als Alternative für flexible Module verlinkt.
- **Begründung:** Bundle-Option direkt auf der PDP (Shopify Bundles) erhöht den Warenkorb und sichert die Klebung; Quick-Add bei Zubehör.

### Section 10 · `tabbed-content` – „Technik & Downloads“ (Demo: „Tech Specs“ mit Tabs [V])
- **Ziel:** Profis und Skeptiker finden alles, Laien werden nicht erschlagen (Akkordeon/Tab statt Textwand).
- **Tabs:**
  1. **Technische Daten** – komplette Tabelle aus Datenblatt (Werte siehe 04, Abschnitt „Technische Daten“) [F, Recherche 2.5].
  2. **Haftgründe & Vorbehandlung** – Ampel als Liste [F, 2.4].
  3. **Verarbeitung** – Abdichten (glätten innerhalb 12 min mit DEKAFINISHER, nicht in die Fuge), Kleben (fügen ≤ 15 min, Schicht 2 mm), Lackieren (ab 10 min, beste Haftung nach ca. 4 h), Reinigung (DEKACLEAN Ultra) [F, 2.6].
  4. **Downloads & Sicherheit** – Technisches Datenblatt (PDF, 07.2024) [F: Link dekalin.de], Sicherheitsdatenblatt (PDF), Chemische Resistenz MS-Polymer (PDF) [F]; Kennzeichnung: nicht als gefährlich eingestuft nach CLP, EUH208 / EUH210 [F]; Herstellerangaben nach GPSR (Name, Anschrift, Kontakt) [A: Pflicht seit 13.12.2024 rechtlich prüfen; DEKA vs. DINOL klären].
- **Begründung:** Zertifikate/Normen kompakt, nicht als Hauptargument; Daten als HTML statt nur PDF ist auch SEO/KI-relevant [F, Recherche 4.4 Hebel 3].

### Section 11 · `text-with-icons` – Garantie, Service, Beratung
- **Ziel:** Risiko nehmen, bevor die letzten Einwände kommen.
- **4 Icons:**
  1. **Kostenlose Anwendungsberatung** – „Schick uns ein Foto deines Projekts – das Dekalin-Team sagt dir, welches Produkt hält.“ [A: Kanal E-Mail/WhatsApp klären; heute support@dekalin.de, Telefon nur für Gewerbe F]
  2. **Dekalin-Anwendungsversprechen** – „Hält MS-5 bei Verarbeitung nach Anleitung nicht, ersetzen wir dir das Material.“ [A: Bedingungen mit Kunde/Recht definieren; nicht überbetonen]
  3. **Versand in 1–3 Werktagen** – „mit DHL, ab 49 € versandkostenfrei“ [A]
  4. **Original vom Hersteller** – „Frische Ware direkt vom Hersteller. Kartusche ungeöffnet 18 Monate lagerfähig.“ [F: 18 Monate]
- **Begründung:** Garantie-/Service-Section senkt das gefühlte Risiko, Beratungsangebot für erklärungsbedürftige Produkte, WhatsApp wirkt persönlicher als „Live-Support“.

### Section 12 · `collapsible-content` – FAQ (10 Fragen)
- **Ziel:** Restliche Einwände in Kundensprache; schließt die Datenlücken (Ergiebigkeit, Aushärtung, Entfernen) [F, Recherche 2.8].
- **Fragen:** siehe 04. Erste Frage geöffnet. Unter der FAQ: „Deine Frage ist nicht dabei? → Beratung“.
- **Begründung:** FAQ unten auf der PDP für alle, die bis zum Schluss scrollen; Antwort-Template Ja/Nein → Warum → Wie → Grenze. FAQPage-Schema ausgeben (ohne Dummy-Einträge wie heute auf dekalin.de [F]).

### Section 13 · `app-wrapper` – Bewertungen (#bewertungen)
- **Ziel:** Beweis durch andere Kunden; mit Foto-Bewertungen (Vision: „Customer review integration with photo support“ [V: fuelthemes.net]).
- **Inhalt:** App-Widget (Judge.me/Reviews.io): Durchschnitt, Verteilung, Filter „mit Fotos“, „Solarmodul“, „SAT“. Über dem Widget 3 hervorgehobene Bewertungen (Proof-Block).
- **[A] Start:** Bewertungen über Nachkauf-Mail ca. 14–21 Tage nach Lieferung (Aushärtung + Fahrt) einsammeln, damit der Kunde das Ergebnis schon im Einsatz erlebt hat; **kein Review-Gating** (Trustpilot-Richtlinien, UWG). Händlerbewertungen (Fritz Berger 4,96/5 aus 52 [F]) nur mit Erlaubnis und Kennzeichnung der Quelle.
- **Keine UGC-Section** – lenkt ab, Bewertungen mit Fotos decken das ab.

### Section 14 · `featured-collection` – „Das brauchst du dazu“
- **Inhalt:** Ergänzende Produkte (Shopify Search & Discovery → Complementary): DEKACLEAN Ultra, DEKAVATOR 22 NF, DEKAFINISHER, Kartuschenpresse – umgesetzt als feste Kollektion „Reinigen & Zubehör“.
- **Begründung:** Cross-Sell aus anderen Kollektionen (Zubehör statt Alternativen), **kein** „Zuletzt angesehen“, damit der Fokus auf dem passenden Zubehör bleibt.

---

## 4. Bewusst weggelassen

| Element | Grund |
|---|---|
| Sticky Add-to-cart (Vision bietet es an) | Verdeckt auf kleinen Bildschirmen Inhalt und lenkt ab |
| „Buy it now“ / PayPal-Express auf der PDP | Ein klarer Kaufweg statt mehrerer Buttons; PayPal bleibt im Checkout |
| Mengenwähler | Platz über ATC; Mehrmengen über Set/Cart |
| Stock-Counter „Nur noch 3“, Countdown | künstliche Knappheit unpassend für Profi-Marke, rechtlich riskant |
| UGC-Section, Wishlist | Lenkt ab bzw. wird kaum genutzt |
| Klarna/„Auf Raten“-Hinweis | Bei rund 20 € Warenwert irrelevant, lenkt nur ab |
| „Made in Germany“, „der beste Kleber“, „hält ewig“ | nicht belegt [F: L] bzw. leere Superlative wirken unglaubwürdig |
| Fiktive Verkaufszahlen („X-mal verkauft“) | nur echte Zahlen; Abmahnrisiko – nach 60 Tagen echte Zahl einblenden |

## 5. Metafelder → Blöcke (Dynamische Quellen)

| Block/Section | Metafeld (Definition in `05_shopify_import/metafields.md`) |
|---|---|
| Infobox über Titel | `custom.infobox_text` |
| USP-Zeile | `custom.usp_zeile` |
| Lieferzeile | `custom.lieferhinweis` |
| Short description Bullets | `custom.kurz_bullets` |
| Specification table | `custom.tech_daten` (Metaobjekt-Liste) [? Vision-Datenquelle prüfen] |
| Anwendungen / Filter | `custom.anwendungen`, `custom.einsatzort`, `custom.untergrund`, `custom.eigenschaften`, `custom.klebkraft` |
| Downloads | `custom.tdb_pdf`, `custom.sdb_pdf`, `custom.resistenz_pdf` |
| FAQ | `custom.faq` (Metaobjekt-Liste `faq_eintrag`) |
| Bundle-Hinweis | `custom.set_empfehlung` (Produktreferenz) |

## 6. Annahmen & offene Punkte
- Preise (19,95 € / 32,95 €), Versandschwelle 49 €, Lieferzeit 1–3 Werktage, Set-Preis 69,95 € – alles [A].
- Ergiebigkeit „≈ 7 m bei 7-mm-Raupe“ ist eine Rechnung (290 ml ÷ 38,5 mm² Querschnitt), keine Herstellerangabe [A].
- Bewertungszahlen in Mockups sind Platzhalter.
- Anwendungsversprechen/Garantie: Bedingungen klären.
- Vergleich mit Sikaflex-554: Rechtsfreigabe (§ 6 UWG).
- Vision-Namen „Product comparison table“ und Datenquelle der „Specification table“ im Editor verifizieren.

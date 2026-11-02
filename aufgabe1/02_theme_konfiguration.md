# 02 – Theme-Konfiguration Vision (Fuel Themes) für den Dekalin-Shop

Kennzeichnung: **[F]** Fakt mit Quelle · **[A]** Annahme/Empfehlung · **[V]** in der Vision-Demo bzw. Doku geprüft · **[?]** im Theme-Editor zu verifizieren (Einstellungsname nicht öffentlich dokumentiert).

---

## 1. Theme & Preset

| Punkt | Festlegung | Begründung |
|---|---|---|
| Theme | **Vision** von Fuel Themes, aktuelle Version 18.0.0 (Demo-Store vision-main.myshopify.com meldet `schema_version 18.0.0`) [V] | Vom Kunden gewählt. Laut Theme Store: Mega menu, In-menu promos, Color swatches, Product tabs, Image hotspot, Before/after slider, Usage information, Stock counter, Trust badges, Enhanced search, Swatch filters, Recently viewed, 36+ Sections [V, themes.shopify.com/themes/vision]. |
| Preset | **„Vision“ (Standard-Preset)** als Basis; Presets laut Theme Store: Vision, Onyx, Poochy, Velocite, Solstice [V] | Das Standard-Preset ist ein Technik-/Elektronik-Shop mit klarem Weiß, Produktkarten, Spezifikationstabellen, Tabbed Content („Tech Specs“) und FAQ-Akkordeon auf der PDP – am nächsten an einem erklärungsbedürftigen Technikprodukt. Onyx (dunkel) würde das Dekalin-Rot schwächen; Poochy (verspielt, Tierbedarf) passt nicht zur Profi-Marke. |
| Anpassungsprinzip | Ein Produkt-Template `product` für alle Kleb-/Dichtstoffe, Inhalte über Metafelder („Dynamische Quelle verbinden“) | Ein Default-Template statt Template-Wildwuchs; Inhalte pflegbar ohne Theme-Code. |
| Apps | Nur: Bewertungen (Judge.me oder Reviews.io), Shopify Bundles, Shopify Search & Discovery; optional Back-in-Stock | Jede Frontend-App lädt Skripte, kleine Features als Custom Liquid – schnellere Ladezeit. |

---

## 2. Farbpalette (abgeleitet aus der Dekalin-CI)

**Quelle CI:** Quelltext von dekalin.de (01.11.2026): häufigste Markenfarbe `#D42A3B` (25×, als Text- und Hintergrundfarbe von Buttons/Links), dunklere Variante `#C4152C`, Text `#262626`, Sekundärtext `#4F4F4F`, Flächen `#EBEBEB` / `#F5F5F5`, Schrift Barlow [F, eigene Auswertung des HTML von https://dekalin.de/ und /ratgeber/do-it-yourself/].

| Token | Hex | Verwendung | Kontrast |
|---|---|---|---|
| **Dekalin-Rot (CTA)** | `#D42A3B` | Nur Kauf-Aktionen: ATC, „Zur Kasse“, Newsletter-Button, Preis im Sale, Links im Fließtext | Weiß auf Rot ≈ 5,0 : 1 (WCAG AA ✓) |
| Rot Hover | `#B0202F` [A, aus `#C4152C` abgedunkelt für sichtbaren Hover] | Hover/aktiv | |
| Anthrazit (Text, dunkle Flächen) | `#262626` | Überschriften, Fließtext, Announcement Bar, Footer | auf Weiß ≈ 15 : 1 |
| Grau (Sekundärtext) | `#4F4F4F` | Untertitel, Grundpreis, Meta-Infos | auf Weiß ≈ 8 : 1 |
| Hellgrau (Fläche) | `#F5F5F5` | Section-Hintergründe im Wechsel, Produktkarten | |
| Linie | `#EBEBEB` | Rahmen, Trenner, Akkordeons | |
| Weiß | `#FFFFFF` | Standard-Hintergrund | |
| Lager-Grün | `#2E7D32` [A] | Nur Zeile „● Auf Lager – in 1–3 Werktagen bei dir“ | auf Weiß ≈ 5,1 : 1 |
| Hinweis-Gelb | `#F2B705` [A] | Nur Ampel „mit Vorbehandlung“ im Haftgrund-Raster | (mit dunklem Text) |

**Regeln:**
- **Eine CTA-Farbe sitewide** (PDP, Side-Cart, Checkout-Branding): Dekalin-Rot. Kein Wechsel auf Grün/Schwarz im Warenkorb – der Kunde erkennt den Kaufweg überall am selben Button.
- Rot **nie** als große Fläche (Hero, Banner), damit der ATC das einzige rote Element im Viewport bleibt. Dunkle Flächen in Anthrazit.
- Gleiche Abstände, keine Sonderfarben je Section – Section-Tools vermeiden, die eigene Styles mitbringen.

### 2.1 Farbschemata in Vision (Theme-Einstellungen → Farben)
Vision nutzt Shopify-Farbschemata je Section [? Bezeichnungen im Editor prüfen]:

| Schema | Hintergrund | Text | Button | Button-Text | Sekundär-Button (Rahmen) | Einsatz |
|---|---|---|---|---|---|---|
| 1 – Standard | `#FFFFFF` | `#262626` | `#D42A3B` | `#FFFFFF` | `#262626` | Header, main-product, die meisten Sections |
| 2 – Hell | `#F5F5F5` | `#262626` | `#D42A3B` | `#FFFFFF` | `#262626` | Wechsel-Sections (Vorteile, Vergleich, FAQ) |
| 3 – Dunkel | `#262626` | `#FFFFFF` | `#D42A3B` | `#FFFFFF` | `#FFFFFF` | Announcement Bar, Storytelling-Section, Footer |
| 4 – Akzent | `#D42A3B` | `#FFFFFF` | `#FFFFFF` | `#D42A3B` | `#FFFFFF` | Nur Menü-Badge „TOP“, Rabatt-Labels in Aktionszeiten |

---

## 3. Typografie

| Rolle | Schrift | Schnitt | Größe Desktop / Mobil | Begründung |
|---|---|---|---|---|
| Überschriften | **Barlow** | 700 (Bold), Großbuchstaben nur für Eyebrow-Texte | H1 PDP 34 / 26 px · H2 Section 30 / 24 px · H3 20 / 18 px | Barlow ist die Hausschrift von dekalin.de [F]; technisch-robuster Grotesk mit DIN-Anmutung, passt zu Kleb-/Dichttechnik. Barlow ist in der Shopify-Schriftbibliothek verfügbar [? im Font-Picker bestätigen; Fallback: als Custom Font über Theme-Assets, Doku-Artikel „custom fonts“ bei Fuel Themes]. |
| Fließtext | **Barlow** | 400, Fett 600 | 16 / 16 px, Zeilenhöhe 1,55 | Eine Schriftfamilie = schnelle Ladezeit, ruhiges Bild. |
| Navigation | Barlow | 600 | 15 px | Gut lesbar bei 6 Menüpunkten. |
| Buttons | Barlow | 700, keine Versalien | 17 px | Lesbar, nicht „schreiend“. |
| Technische Werte | Barlow (Tabellenziffern) | 500 | 15 px | Spezifikationstabelle. |

Schreibweise sitewide einheitlich: **DEKAsyl MS-5**, **DEKASEAL**, **DEKACLEAN**, **DEKAVATOR**, **DEKAFINISHER**, **DEKAPHON**, **DEKAPUR** (heute uneinheitlich, inkl. Tippfehler „Deklain“ [F, Recherche 1.6]).

---

## 4. Buttons, Formen, Bilder

| Einstellung | Wert | Begründung |
|---|---|---|
| Primär-Button | Gefüllt `#D42A3B`, Text weiß, Höhe **64 px** auf der PDP (sonst 52 px), **volle Breite** in Buybox und Side-Cart, Eckenradius 6 px | Groß und volle Breite = auf dem Handy leicht zu treffen und klar die Hauptaktion; gefüllt statt Outline für maximale Sichtbarkeit. |
| Sekundär-Button | Rahmen 1,5 px `#262626`, transparent | Für „Datenblatt herunterladen“, „Anleitung ansehen“. |
| Button-Text | „In den Warenkorb“ / „Jetzt sicher zur Kasse“ | Klares, erwartbares Wording statt Werbesprache – der Kunde weiß genau, was der Klick tut. |
| Eckenradius Karten/Bilder | 8 px | Modern, aber technisch-sachlich. |
| Produktbilder | Quadratisch 1:1, weißer Hintergrund für Packshots, Hauptbild ohne Padding | Einheitliches Raster, Produkt füllt das Bild. |
| Produktkarten | Mit Untertitel (Vision-Feature „product subtitles inside product cards“ [V, Fuel-Doku]) → Klartext-Unterzeile aus Metafeld `custom.klartext_untertitel` | Produktname allein erklärt nichts. |
| Varianten-Swatches | Farb-Swatches als **Bild der Fuge** (weiß/schwarz), Gebinde als Mini-Packshot | Bild-Swatches zeigen die echte Fugenfarbe statt eines abstrakten Farbpunkts; Vision „product variant swatches“ [V, Fuel-Doku]. |
| Animation | Dezent (Einblenden beim Scrollen), keine Laufbänder | Ruhe, CLS ≈ 0. |

---

## 5. Favicon & Logo

- **Logo:** Original-Dekalin-Logo ohne Claim-Zeile im Header (Datei `Dekalin_Logo_Claim@2x.webp` auf dekalin.de hat 151 × 70 px mit Claim [F]); im Shop die Version **ohne Claim**, Breite 150 px Desktop / 120 px mobil – Logo lesbar groß, aber kein Claim im Header (spart Höhe, Claim wäre klein unlesbar).
- **Favicon (Idee):** 512 × 512 px PNG, Quadrat mit 20 % Eckenradius in Dekalin-Rot `#D42A3B`, darauf ein weißes, fettes **„D“** (Barlow ExtraBold), dessen rechter Bogen als **Kleberaupe** ausläuft (Tropfenende). Erkennbar auch bei 16 px, verbindet Marke und Produkt. Alternative: weißer Tropfen auf Rot. [A, Freigabe Markeninhaber DINOL/DEKA nötig]
- Pfad: Online Store → Themes → Anpassen → Theme-Einstellungen → Logo/Favicon [? Bezeichnung].

---

## 6. Announcement Bar (Vision „announcement-bar“, rotierend mit Pfeilen [V])

| Einstellung | Wert |
|---|---|
| Anzahl Leisten | **genau eine** (mehrere Leisten wirken unruhig und kosten Platz) |
| Farbschema | 3 – Dunkel (`#262626`, weißer Text) – kein Rot, kein Farbmix |
| Höhe | fest 36 px (CLS = 0) |
| Rotation | 3 Texte, 5 s, Pfeile aus auf Mobil [?] |
| Inhalt | USPs/Trust statt Promo: |
| Text 1 | **✓ Versand in 1–3 Werktagen · ab 49 € versandkostenfrei** [A: Werte mit Logistik klären] |
| Text 2 | **✓ Direkt vom Hersteller – Kleb- & Dichtstoffe seit 1907** [F: Gründung 1907] |
| Text 3 | **✓ Kostenlose Anwendungsberatung vom Dekalin-Team** [A: Kanal klären] |

Begründung: Die USPs stehen sitewide in der Announcement Bar und sind damit auf jeder Seite sichtbar, nicht nur auf der Startseite; Promo-Leisten und Stapel vermeiden.

---

## 7. Header (Vision Header-Gruppe)

### 7.1 Sections der Header-Gruppe [V: Demo]
| Section | Status | Grund |
|---|---|---|
| `announcement-bar` | **an** | siehe 6 |
| `header-secondary-menu` (kleine Top-Leiste mit About/Blog/Support + Länderwahl) | **aus** | Höchstens eine Leiste; Shop vorerst nur DE/EUR [A] |
| `header` | **an** | Hauptheader |
| `header-mobile-navigation` | **an** | Mobile-Drawer |
| `mobile_dock` (Shortcut-Leiste unten, neu in v18) | **aus** | Doppelte Navigation, verdeckt Inhalt |
| Custom Section „Suchleiste“ (eigene) | **an, nur ≤ 1160 px** | Ausgeklappte Suche mobil – lohnt sich bei einem Sortiment mit vielen ähnlich benannten Produkten |

### 7.2 Desktop (≥ 1160 px)
```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ ✓ Versand in 1–3 Werktagen · ab 49 € versandkostenfrei                     (36 px, #262626)   │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│ DEKALIN   Abdichten  Kleben & Montieren[TOP]  Reparieren & Schützen  Reinigen & Zubehör  │ Ratgeber  Warum Dekalin │ [🔍 Wonach suchst du? …]  👤  🛒 2 │
└──────────────────────────────────────────────────────────────────────────────────────────────┘  (≈ 72 px, sticky beim Hochscrollen)
```
| Einstellung | Wert |
|---|---|
| Logo-Position | **links** (Demo: zentriert [V]) – Logo + Menü in einer Zeile spart Höhe |
| Menü | `hauptmenue` mit 6 Mega-Menü-Blöcken („Mega-Menu“-Block je Hauptpunkt, [V: Fuel-Doku]) |
| Menü-Badge | Block „Menu Badge“: Text „TOP“, Farbe weiß auf `#D42A3B`, an „Kleben & Montieren“ [V: Fuel-Doku „badges to menu items“] |
| Mega-Menü-Promo | je Hauptpunkt 1 Promo-Kachel (Bild 3:4 + Headline + Link) [V: Demo-Klassen `mega-menu-promotion`] |
| Suche | Feld sichtbar (falls Option vorhanden [?]) sonst Icon + Drawer mit „Beliebte Suchen“ und Trending-Produkten [V] |
| Konto | kleines Icon, ohne Text (Nebenfunktion) |
| Warenkorb | Icon mit Zähler, **visuell stärkstes Icon**, öffnet Side-Cart von rechts |
| Sticky Header | an, „beim Hochscrollen einblenden“ [?] |
| Höhe | max. 72 px, Schatten klein (Demo: `header--shadow-small` [V]) |

### 7.3 Mobil (< 1160 px)
```
┌─────────────────────────────────┐
│ ✓ Versand in 1–3 Werktagen …    │ 36 px
├─────────────────────────────────┤
│ ☰      DEKALIN         🔍   🛒2 │ 56 px – Menü links, Warenkorb rechts
├─────────────────────────────────┤
│ 🔍 Wonach suchst du? z. B. …    │ 48 px – grau #F5F5F5, Radius 25 px, 14 px Text
└─────────────────────────────────┘
```
Kein „Menü“-Label neben dem Burger (Symbol ist bekannt, spart Platz); Logo zentriert (mobil), Konto im Drawer.

---

## 8. Footer (Vision Footer-Gruppe)

Aufbau laut Demo: Marken-Textblock · Link-Listen · Newsletter mit Einwilligungs-Checkbox · Länder-/Sprachwahl · Zahlungsicons · Copyright [V].

```
┌───────────────────────────────────────────────────────────────────────────────────────────────┐ Farbschema 3 – Dunkel
│ DEKALIN (Logo weiß)          SHOP                    HILFE                     WISSEN & DEKALIN      │
│ Kleben & Dichten seit 1907.  Abdichten               Kostenlose Beratung       Anleitungen & Videos  │
│ Profi-Know-how für Wohn-     Kleben & Montieren      Produktfinder             Datenblätter & SDB    │
│ mobil, Caravan & Werkstatt.  Reparieren & Schützen   Häufige Fragen            Über Dekalin          │
│ support@dekalin.de           Reinigen & Zubehör      Versand & Lieferung       Schulungen DIN 2304   │
│ [f] [ig] [yt]                Klebe- & Dichtsets      Rückgabe & Widerruf       Gewerbe & Händler     │
│                              Bestseller              Kontakt                   Karriere              │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ KLEBE-TIPPS VOM PROFI                                                                                │
│ Anleitungen, Projektideen und neue Produkte – 1–2× im Monat. [E-Mail-Adresse      ] [Anmelden]      │
│ ☐ Ich möchte den Newsletter erhalten. Abmeldung jederzeit. (Datenschutz)                             │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ ✓ Original vom Hersteller   ✓ Versand mit DHL [A]   ✓ Sicher bezahlen   [PayPal][Visa][MC][Apple Pay]│
│                                                     [Klarna][Amazon Pay]                             │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ © 2026 DEKALIN · Impressum · AGB · Datenschutz · Widerrufsbelehrung · Versand & Zahlung ·            │
│ Cookie-Einstellungen · Barrierefreiheit        Alle Preise inkl. MwSt., zzgl. Versand                 │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

| Element | Einstellung / Inhalt | Begründung |
|---|---|---|
| Spalte 1 Marke | Logo weiß, 2 Sätze Markentext, Support-Mail, Social-Icons (Facebook/Instagram `dekalinofficial`, YouTube `DEKALIN4DEKA` [F]) | Vertrauen, Absender eindeutig |
| Spalten 2–4 | Menüs `footer-shop`, `footer-hilfe`, `footer-dekalin` (je 6 Links – balanciert) | „Über uns“, Karriere, Rechtliches in den Footer – das Hauptmenü bleibt für Produkte frei |
| Newsletter | Titel „Klebe-Tipps vom Profi“, **ohne Rabatt-Versprechen** im Standard [A]; Einwilligungs-Checkbox wie in Demo [V] | Mehrwert passt zur Wissensmarke; Rabatt optional testen |
| Trust-Zeile | 3 Benefits + Zahlungsicons **im Footer statt auf der PDP** | Zahlungslogos gehören zum Abschluss, nicht in die Buybox; auf der PDP zählt der Produktnutzen |
| Länderwahl | aus (nur DE/EUR) [A] | weniger Ablenkung |
| Rechtliches | Impressum, AGB, Datenschutz, Widerrufsbelehrung, Versand & Zahlung, Cookie-Einstellungen, **Barrierefreiheitserklärung** | Pflichtseiten; BFSG gilt seit 28.06.2025 für B2C-Shops [A: rechtlich prüfen] |
| Developer-Credits | entfernen (Fuel-Doku „remove footer credits“ [V]) | professioneller Eindruck |

---

## 9. Weitere Theme-Einstellungen (Checkliste)

| Bereich | Einstellung | Wert | Begründung |
|---|---|---|---|
| Produktseite | Sticky Add-to-cart (Vision-Feature [V]) | **aus** | Verdeckt auf kleinen Bildschirmen Inhalt und lenkt ab |
| Produktseite | „Buy it now“ / dynamischer Checkout-Button | **aus** | Ein klarer Kaufweg statt mehrerer Buttons; PayPal bleibt im Checkout verfügbar |
| Produktseite | Discount-Code-Block, Share-Block, Scrolling-Text-Block | **aus** | Platz über dem ATC ist knapp |
| Produktseite | Galerie | Thumbnails links (Desktop) / Slider mit Punkten (mobil), Zoom an, Bilder volle Breite | Produkt groß zeigen, Details per Zoom |
| Produktseite | Mengenwähler | **aus** im Product form [? Option prüfen]; Menge im Side-Cart änderbar, Mehrmengen über Set/Bundle | Weniger Elemente über dem Button |
| Warenkorb | Typ | Side-Cart (Slide-out cart [V]) von rechts, Button „Jetzt sicher zur Kasse“, kein Gutscheinfeld, kein Notizfeld | Gutscheinfeld lädt zur Codesuche außerhalb des Shops ein |
| Warenkorb | Cross-Sell im Cart | 1 Produkt: DEKACLEAN Ultra („Ohne saubere Fläche hält kein Kleber“) | Vision „Cart drawer with cross-sell“ [V] |
| Kollektionen | Sortierung | Bestseller | Bewährte Produkte zuerst |
| Kollektionen | Produktkarten | Untertitel an, Quick view **aus** auf Mobil [A], Swatches an | |
| Popups | Newsletter-Popup | aus zum Start; Exit-Intent später testen | Kein Popup vor dem ersten Produktkontakt |
| Cookie-Banner | nicht-blockierend, eine Ebene | Inhalt bleibt sofort nutzbar |
| Checkout | Branding: Rot `#D42A3B` als Button, Logo, Barlow; PayPal vorausgewählt (Checkout Blocks) | Wiedererkennung vom Shop bis zur Kasse; beliebteste Zahlart vorn |
| Sprache | Deutsch, Ansprache **„du“** [A] – Caravan-Community duzt; A/B-Test „du/Sie“ einplanen | |
| SEO | Produkt-Schema mit brand, gtin13 (4046085125227 für MS-5 weiß 290 ml [F]), Preis, Verfügbarkeit, Bewertungen | Recherche 4.4 Hebel 3 |

## 10. Unklar / im Theme-Editor zu verifizieren
- Exakte Bezeichnungen der Farb-, Schrift- und Header-Einstellungen in Vision 18 (Fuel-Doku nennt nur einzelne Artikel; keine öffentliche Settings-Referenz gefunden).
- Ob der Header ein eingeblendetes Suchfeld anbietet (sonst Custom Section).
- Ob Barlow in Shopifys Font-Bibliothek liegt (sonst Custom Font, DSGVO-konform lokal hosten).
- Ob der Mengenwähler im Product-form-Block abschaltbar ist (sonst per CSS ausblenden).

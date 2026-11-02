# Kollektionen – Dekalin-Shop

Alle Kollektionen sind **automatisiert** (Produkte → Kollektionen → Kollektion erstellen → Typ „Automatisiert“). Bedingungen über Produkt-Tags aus `products.csv`. Tag-Schema:

| Präfix | Bedeutung | Beispiel |
|---|---|---|
| `welt:` | Hauptmenü-Welt | `welt:kleben-montieren` |
| `anwendung:` | Aufgabe = Handle der Aufgaben-Kollektion | `anwendung:solarmodul-kleben` |
| `zubehoer:` | Vorbereitungs-/Werkzeugprodukt, das in Aufgaben-Kollektionen am Ende mit erscheint | `zubehoer:kleben`, `zubehoer:abdichten` |
| `eigenschaft:` / `basis:` / `familie:` | Zusatzinfos (Filter laufen über Metafelder, Tags nur als Backup) | `eigenschaft:ueberlackierbar` |
| `bestseller` | redaktionelle Bestseller | |

**Bedingungslogik Aufgaben-Kollektionen:** „Produkte müssen **eine beliebige** Bedingung erfüllen“: Tag = `anwendung:<handle>` **oder** Tag = `zubehoer:<welt>`. Sortierung **manuell**: Hauptprodukt(e) oben, Zubehör unten. Welt-Kollektionen: Sortierung „Bestseller“.
Ein Template `collection` für alle; Einleitungstext über Metafeld `custom.einleitung`. Bei < 6 Produkten verwandte Kollektionen anzeigen (`custom.verwandt`), damit keine Seite leer wirkt.

SEO-Beschreibung = Shopify-Feld „Beschreibung“ (2–3 Sätze, erscheint als Einleitung); Meta-Description kann identisch gekürzt werden.

---

## 1. Welt-Kollektionen (Ebene 1) + Sonderkollektionen

| Handle | Titel | Beschreibung (SEO, 2–3 Sätze) | Bedingung |
|---|---|---|---|
| `abdichten` | Abdichten am Wohnmobil & Caravan | Hier findest du Dichtstoffe und Dichtmassen für Dachluken, Fenster, Fugen, Leisten und Durchführungen. Sortiert nach Aufgabe: wiederlösbar, überlackierbar oder dauerelastisch – du wählst, was dein Projekt braucht. Direkt vom Hersteller DEKALIN. | Tag = `welt:abdichten` |
| `kleben-montieren` | Kleben & Montieren ohne Bohren | Solarmodul, SAT-Anlage, Markise oder Halter: Mit dem richtigen Kraftkleber hält das Bauteil ohne ein einziges Bohrloch. Hier findest du Kleb- und Dichtstoffe auf MS-Polymer-Basis und alles für die Vorbereitung. | Tag = `welt:kleben-montieren` |
| `reparieren-schuetzen` | Reparieren & Schützen | Risse in Kunststoff und GFK, ausgerissene Schraublöcher oder Rost am Unterboden: Hier findest du Reparaturkleber und Unterbodenschutz für Wohnmobil, Caravan und Anhänger. | Tag = `welt:reparieren-schuetzen` |
| `reinigen-zubehoer` | Reinigen, Vorbereiten & Zubehör | Damit Kleber und Dichtstoff halten, zählt die Vorbereitung. Haftreiniger, Haftvermittler, Glättmittel, Kartuschenpressen und Komplett-Sets für dein Projekt. | Tag = `welt:reinigen-zubehoer` |
| `bestseller` | Bestseller: Was Profis immer dabeihaben | Die meistgekauften DEKALIN-Produkte für Wohnmobil und Caravan auf einen Blick. Wenn du unsicher bist, fängst du hier richtig an. | Tag = `bestseller`; Sortierung „Bestseller“ [W: OA] |
| `alle-produkte` | Alle Produkte | Das komplette DEKALIN-Sortiment zum Kleben, Dichten, Reparieren, Schützen und Reinigen. | Preis > 0 |

---

## 2. Aufgaben-Kollektionen (Ebene 3)

### Abdichten
| Handle | Titel | Beschreibung (SEO) | Bedingung (beliebige) | Produkte (aus CSV + Sortiment) |
|---|---|---|---|---|
| `fenster-dachluken-abdichten` | Fenster & Dachluken abdichten | Kommt Wasser an Dachluke oder Fenster rein? Für verdeckte Fugen unter dem Rahmen eignet sich eine abtupfbare Dichtmasse, für sichtbare Fugen eine überlackierbare Butylmasse. Hier findest du beides – plus Reiniger und Werkzeug. | `anwendung:fenster-dachluken-abdichten`, `zubehoer:abdichten` | DEKASEAL 8936, DEKASEAL 1512, MS-6, Butylbänder · Zubehör |
| `dachhauben-durchfuehrungen-abdichten` | Dachhauben & Kabeldurchführungen abdichten | Dachhaube, Kabeldurchführung, Antenne oder LTE-Haube dauerhaft dicht bekommen. Kleben und Abdichten in einem Schritt oder klassisch mit Butyl – hier findest du das passende Produkt. | `anwendung:dachhauben-durchfuehrungen-abdichten`, `zubehoer:abdichten` | DEKAsyl MS-5, MS-2, DEKASEAL 1512 · Zubehör |
| `fugen-naehte-aussen` | Fugen & Nähte außen abdichten | Dichtnähte, Überlappungen und Fugen an der Außenhaut sauber und dauerelastisch abdichten. MS-Polymer-Dichtstoffe sind überlackierbar und in Weiß, Grau und Schwarz erhältlich. | `anwendung:fugen-naehte-aussen`, `zubehoer:abdichten` | DEKAsyl MS-1, MS-2, MS-6 · DEKAFINISHER, Zubehör |
| `serviceklappen-tueren-abdichten` | Serviceklappen & Türen abdichten (wiederlösbar) | Serviceklappen, Türen und Markisenleisten müssen später wieder ab? Dann brauchst du eine Dichtmasse, die nicht aushärtet und abtupfbar bleibt. | `anwendung:serviceklappen-tueren-abdichten`, `zubehoer:abdichten` | DEKASEAL 8936, MS-6 · Zubehör |
| `kantenleisten-keder` | Kantenleisten & Keder abdichten | Kantenleisten, Keder und Abdeckprofile neu eindichten oder an Anhängern aus Alu und Polyester kleben. Hier findest du Dichtmassen und Kleber für jede Leiste. | `anwendung:kantenleisten-keder`, `zubehoer:abdichten` | DEKAsyl MS-5, MS-1, MS-2, DEKASEAL 8936, 1512 · Zubehör |
| `bad-kueche-abdichten` | Bad & Küche abdichten (innen) | Fugen in Nasszelle und Küche im Wohnmobil sauber abdichten – mit transparentem oder weißem Dichtstoff, frei von Silikon. | `anwendung:bad-kueche-abdichten`, `zubehoer:abdichten` | DEKAsyl MS-6, MS-7 · Zubehör |

### Kleben & Montieren
| Handle | Titel | Beschreibung (SEO) | Bedingung | Produkte |
|---|---|---|---|---|
| `solarmodul-kleben` | Solarmodul aufs Wohnmobil kleben | Solarmodul ohne Bohren aufs Dach: Spoiler oder Halter werden geklebt, die Klebenaht dichtet gleich mit. Hier findest du Kraftkleber, Klebesets und alles für die Vorbereitung – mit Schritt-für-Schritt-Anleitung. | `anwendung:solarmodul-kleben`, `zubehoer:kleben` | DEKAsyl MS-5, Solar-Montage-Set, Flexsolarmodul-Klebeset, SAT/Solar-Klebeset · DEKACLEAN, DEKAVATOR, Presse |
| `sat-anlage-antenne-kleben` | SAT-Anlage & Antenne kleben | SAT-Anlage und Antenne ohne Bohrloch sicher aufs Dach kleben. Mit 7-mm-Raupe und dem richtigen Kraftkleber hält die Montage auch bei Fahrtwind. | `anwendung:sat-anlage-antenne-kleben`, `zubehoer:kleben` | DEKAsyl MS-5, Klebeset SAT/Solar · Zubehör |
| `markise-dachtraeger-anbauteile-kleben` | Markise, Dachträger & Anbauteile kleben | Markise, Dachträger, Fahrradträger und andere Anbauteile kleben statt bohren. Hoher Anfangshalt, dauerelastisch und dicht. | `anwendung:markise-dachtraeger-anbauteile-kleben`, `zubehoer:kleben` | DEKAsyl MS-5 · Zubehör |
| `fenster-scheiben-einkleben` | Fenster & Scheiben einkleben | Fenster, Echtglasscheiben und Dachdurchführungen dauerhaft einkleben. Hier findest du Konstruktions- und Scheibenklebstoffe auf MS-Polymer-Basis. | `anwendung:fenster-scheiben-einkleben`, `zubehoer:kleben` | DEKAsyl MS-5, MS-8 · Zubehör |
| `halter-leisten-innenausbau-kleben` | Halter, Leisten & Innenausbau kleben | Halter, Abdeckungen, Leisten und Bodenbeläge im Ausbau kleben – auf Blech, Alu, Holz, PVC und mehr. | `anwendung:halter-leisten-innenausbau-kleben`, `zubehoer:kleben` | DEKAsyl MS-5, MS-6 · Zubehör |
| `seitenwand-grossflaechen-kleben` | Seitenwände & Großflächen kleben (Profi) | Seitenwände, Außenflächen und Chassis-Teile großflächig verkleben – mit 2K-Konstruktionsklebstoff für Werkstatt und Profi. | `anwendung:seitenwand-grossflaechen-kleben`, `zubehoer:kleben` | DEKAPUR 2K-6000 A+B · Zubehör |

### Reparieren & Schützen
| Handle | Titel | Beschreibung (SEO) | Bedingung | Produkte |
|---|---|---|---|---|
| `kunststoff-gfk-reparieren` | Kunststoff & GFK reparieren | Gebrochene Kunststoffteile, Risse in GFK oder Stoßstange: Mit 2K-Reparaturkleber werden Teile wieder belastbar. | `anwendung:kunststoff-gfk-reparieren`, `zubehoer:kleben` | DEKAPUR 2K-90 · DEKACLEAN |
| `schraubloecher-reparieren` | Ausgerissene Schraublöcher reparieren | Schraube hält nicht mehr? Ausgerissene Löcher in Kunststoff und GFK auffüllen und wieder fest verschrauben. | `anwendung:schraubloecher-reparieren`, `zubehoer:kleben` | DEKAPUR 2K-90 · DEKACLEAN [A: Anwendung beim Hersteller bestätigen] |
| `wasserschaden-reparieren` | Undichte Stellen & Wasserschaden | Wasser im Wohnmobil? Erst die Ursache finden, dann die undichte Stelle neu abdichten. Hier findest du Dichtstoffe und unseren Ratgeber zur Reparatur. | `anwendung:wasserschaden-reparieren`, `zubehoer:abdichten` | MS-2, DEKASEAL 8936, 1512, 2K-6000 · Zubehör [A] |
| `unterbodenschutz` | Unterbodenschutz für Wohnmobil & Caravan | Unterboden und Chassis gegen Rost, Steinschlag und Salz schützen – als Spray, auf Wasserbasis oder als Wachs. | `anwendung:unterbodenschutz` | DEKAPHON 9735, 958, Pro-Wax |
| `hohlraumschutz` | Hohlraumschutz | Hohlräume dauerhaft gegen Korrosion versiegeln – mit transparentem Hohlraumwachs. | `anwendung:hohlraumschutz`, `anwendung:unterbodenschutz` | DEKAPHON Pro-Wax (+ Unterbodenschutz als Ergänzung) |
| `radkaesten-schuetzen` | Radkästen schützen | Radkästen gegen Steinschlag und Rost schützen und gleichzeitig dämmen. | `anwendung:radkaesten-schuetzen` | DEKAPHON 9735, 958 |

### Reinigen & Zubehör
| Handle | Titel | Beschreibung (SEO) | Bedingung | Produkte |
|---|---|---|---|---|
| `reinigen-entfetten` | Reinigen & Entfetten vor dem Kleben | Ohne saubere Fläche hält kein Kleber. Haftreiniger entfernt Fett und Staub und löst frische Kleberreste. | `anwendung:reinigen-entfetten` | DEKACLEAN Ultra |
| `haftvermittler-primer` | Haftvermittler (Primer) | Mehr Haftung bei Hitze, Last und Feuchtigkeit: Haftvermittler vor dem Kleben auftragen. | `anwendung:haftvermittler-primer` | DEKAVATOR 22 NF |
| `glaetten-fugen-finish` | Fugen glätten & Regenstreifen entfernen | Saubere Fugen wie vom Profi und Fenster ohne Regenstreifen – mit Glättmittel und Fensterreiniger. | `anwendung:glaetten-fugen-finish`, `anwendung:regenstreifen-fenster-reinigen` | DEKAFINISHER, DEKACLEAN Glass Foam |
| `klebesets` | Klebe- & Dichtsets | Alles für ein Projekt in einem Paket: Solarmodul, SAT-Anlage oder Abdichtung. Aufeinander abgestimmt und günstiger als einzeln. | `anwendung:klebesets` | Solar-Montage-Set (Bundle), Flexsolarmodul-Klebeset, Klebeset SAT/Solar |
| `kartuschenpressen-werkzeug` | Kartuschenpressen & Werkzeug | Kartuschenpresse, Beutelpistole und Spachtel für eine gleichmäßige Raupe und saubere Fugen. | `anwendung:kartuschenpressen-werkzeug` | Kartuschenpresse [A: Handelsware] |

Gesamt: 6 Welt-/Sonderkollektionen + 24 Aufgaben-Kollektionen.

---

## 3. Noch anzulegende Produkte (nicht in `products.csv`)
| Produkt | Weg | Hinweis |
|---|---|---|
| Solar-Montage-Set | **Shopify Bundles**-App: 2 × MS-5 290 ml (Farbe wählbar) + DEKACLEAN Ultra Tücher + DEKAVATOR 22 NF 30 ml + Kartuschenpresse; Preis 69,95 € [A]; Tags `welt:reinigen-zubehoer, anwendung:klebesets, anwendung:solarmodul-kleben` | Bundle zieht Bestand der Einzelprodukte [W: App: Shopify Bundles] |
| Flexsolarmodul-Klebeset | CSV/Admin: Art. 62700 12 (schwarz), 62701 12 (weiß) [F] | MS-1 + MS-5 + DEKACLEAN-Tuch |
| MS-6, MS-7, MS-8, 2K-90, 2K-6000, DEKAPHON, Butyl, Glass Foam, Buch | Admin/CSV nach Datenlieferung | Artikelnummern, Preise fehlen |

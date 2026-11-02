# Aufgabe 2.5 – Ausgearbeitete Maßnahme: Antwortseite „Solarpanel ohne Bohren aufs Wohnmobildach kleben – mit DEKAsyl MS-5“

Stand: 01.11.2026 · Pilot von Maßnahme M1 (`03_massnahmenplan.md`) · Alle technischen Werte aus dem MS-5-Datenblatt 07.2024 bzw. `recherche/dekalin_recherche.md`; nicht belegte Inhalte sind mit **[Annahme]** gekennzeichnet und vor Livegang mit der Dekalin-Anwendungstechnik zu klären (Liste in Abschnitt 8).

---

## 1. Wahl und Begründung

**Gewählt: M1-Pilot – Antwortseite „Solarpanel ohne Bohren kleben“** statt des Caravan-FAQ-Hubs (M2).

| Kriterium | Antwortseite Solarpanel (M1-Pilot) | Caravan-FAQ-Hub (M2) |
|---|---|---|
| Größte Einzellücke im Test | **P10: Perplexity nennt nur Sikaflex (0/1), ChatGPT Sikaflex-554 auf Platz 1, MS-5 auf Platz 2 ohne Begründung** | P2/P8: Sika-FAQ als Primärquelle |
| Kaufkraft des Anlasses | hoch: Solarnachrüstung ist ein Projektkauf (Kleber + Reiniger + Haftvermittler + Set) | mittel: Wartung/Reparatur |
| Produkt | **MS-5 = Premiumprodukt und direkter Gegenspieler zu Sikaflex-554** – mit messbaren Vorteilen (+120 °C, 12 min Hautbildung, 18 Monate Lagerung) | gemischt, Schwerpunkt Butyl (dort ist Dekalin bereits sichtbar) |
| Vorhandenes Material | Datenblatt vollständig, Anleitung `/solar/` und `/sat-anlage/`, Flexsolar-Set, Video „Solarplattenhalterung“ | 27 FAQ, aber mit Platzhaltern/Dubletten; viele Antworten fehlen fachlich (Entfernen, Altreste, Ergiebigkeit) |
| Aufwand bis live | 1 Seite, 1 Freigabe, 301 von `/solar/` – **2–3 Wochen** | 40 Antworten, Freigaben über alle Produktgruppen – 4–6 Wochen |
| Wirkt zusätzlich auf | P2 (MS-5 als Sikaflex-Alternative), P3 (Kennwerte auf dekalin.de), P5 (Alu/GFK kleben), P6 (überlackierbar + UV-beständig als Attribute), P8 | P2, P4, P8 |
| Wiederverwendbarkeit | **Bauplan für alle weiteren Antwortseiten** (SAT, Markise, Alu/GFK) und liefert 12 FAQ für den Hub | – |

**Begründung in einem Satz:** Die Solarseite schließt die größte und kaufstärkste Lücke mit vorhandenem Material in der kürzesten Zeit, setzt das Premiumprodukt direkt gegen Sikaflex-554 und ist zugleich das Template für M1 und Baustein für M2.

---

## 2. Seiten-Steckbrief

| Element | Festlegung |
|---|---|
| **URL (WordPress, heute)** | `https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/` |
| URL (Shopify, nach Relaunch) | `/blogs/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren` |
| Weiterleitung | 301 von `https://dekalin.de/solar/` auf die neue URL (Inhalt wird übernommen und ersetzt) |
| **Meta-Title** (55 Zeichen) | `Solarpanel ohne Bohren aufs Wohnmobil kleben: Anleitung` |
| **Meta-Description** (152 Zeichen) | `Solarpanel ohne Bohren aufs Wohnmobildach kleben: Welcher Kleber, welche Vorbereitung, wie lange aushärten? Anleitung mit DEKAsyl MS-5, Tabelle und FAQ.` |
| H1 | Solarpanel ohne Bohren aufs Wohnmobildach kleben – so geht's mit DEKAsyl MS-5 |
| Haupt-Keyword / Prompt | „solarpanel wohnmobil kleben“ / P10 „Welchen Kleber nehme ich, um ein Solarpanel ohne Bohren aufs Wohnmobildach zu kleben?“ |
| Neben-Keywords | solarmodul wohnmobil kleben ohne bohren, kleber solarpanel wohnmobil, solarmodul spoiler kleben, flexibles solarmodul kleben, sikaflex 554 alternative |
| Seitentyp / Schema | Article + HowTo + FAQPage + Product (DEKAsyl MS-5) + BreadcrumbList + Organization |
| Autor / Prüfer | Michael Windecker (GF DEKA, Buchautor), geprüft von der Anwendungstechnik [Annahme: Freigabe der Person] · „Aktualisiert am“ sichtbar |
| Ansprache | Du (wie in Prompts und Camper-Medien) [Annahme: an Markenrichtlinie anpassen] |
| Medien | Video „Solarplattenhalterung“ (heute nur auf `/produkt/556/` eingebunden), 3 Schrittfotos, Grafik „Spoiler-Verklebung im Querschnitt“ [Annahme: neu zu erstellen]; Alt-Text-Template „Solarmodul-Spoiler mit DEKAsyl MS-5 auf Wohnmobildach kleben – Schritt X“ |

## 3. Seitenstruktur (Wireframe)

| # | Block | Zweck für KI/Nutzer |
|---|---|---|
| 1 | Breadcrumb · H1 · Autor + „Aktualisiert am“ | Thema + Aktualitäts- und Expertensignal |
| 2 | **Kurzantwort-Box** (2 Sätze) | zitierfähige Direktantwort auf P10 |
| 3 | „Das Wichtigste in Kürze“ (5 Bullets mit Zahlen) | extrahierbare Fakten |
| 4 | H2 Welcher Kleber? Warum MS-Polymer | Abgrenzung zu Butyl/Silikon |
| 5 | H2 Starres oder flexibles Modul (Tabelle) | Fallunterscheidung |
| 6 | H2 Das brauchst du (Materialliste mit Produktlinks) | Warenkorb-Logik, interne Links |
| 7 | H2 Schritt-für-Schritt (8 Schritte, Anker `#schritt-1` …) | HowTo-Passagen |
| 8 | H2 Zeiten und Temperaturen (Tabelle) | häufigste Nachfragen |
| 9 | H2 Auf welchen Dachmaterialien hält MS-5? (Tabelle) | Material-Prompts (P5) |
| 10 | H2 MS-1, MS-2 oder MS-5? (Tabelle) | Produktabgrenzung |
| 11 | H2 MS-5 im Vergleich mit Sikaflex-554 (Tabelle) | Vergleichsprompts (P2, P10) |
| 12 | H2 Häufige Fehler | Negativ-Liste |
| 13 | H2 Technische Daten (HTML-Tabelle) | Eigenschaftsprompts (P6), statt nur PDF |
| 14 | H2 FAQ (12 Fragen, je eigener Anker) | FAQPage, Passagen |
| 15 | H2 Wo kaufen? + Downloads | Händlerliste, Datenblatt, SDB, Chemische Resistenz |
| 16 | Weiterlesen (3 verwandte Ratgeber) | interne Verlinkung |

---

## 4. Fertiger Seitentext

> Formatierung entspricht der späteren HTML-Struktur (H1–H3, Tabellen als HTML-Tabellen, keine Bilder mit Text). Hinweise in eckigen Klammern sind Redaktionshinweise und werden nicht veröffentlicht.

Startseite › Ratgeber › Solarpanel kleben ohne Bohren

# Solarpanel ohne Bohren aufs Wohnmobildach kleben – so geht's mit DEKAsyl MS-5

*Von Michael Windecker, Geschäftsführer DEKA Kleben & Dichten GmbH und Autor von „Klebt nicht gibt's nicht!“ · fachlich geprüft von der DEKALIN-Anwendungstechnik · Aktualisiert am 15.11.2026* [Annahme: Person/Datum]

> **Kurz gesagt:** Ein Solarpanel klebst du ohne Bohren mit einem elastischen High-Tack-Klebstoff auf MS-Polymer-Basis wie DEKAsyl MS-5 aufs Wohnmobildach – bei starren Modulen werden die Spoiler oder Halter verklebt, halbflexible Module klebst du direkt. MS-5 haftet ohne Primer auf Aluminium, GFK, lackiertem Blech und Glas, bleibt von −40 °C bis +120 °C elastisch und hält die Teile dank hoher Anfangshaftung meist ohne Klemmen in Position.

**Das Wichtigste in Kürze**
- **Kleber:** DEKAsyl MS-5 (MS-Polymer, High Tack) – frei von Lösemitteln, Isocyanat und PVC
- **Vorbereitung:** reinigen mit DEKACLEAN ULTRA; bei hoher Belastung und Feuchtigkeit zusätzlich DEKAVATOR 22 NF
- **Verarbeitung:** bei +5 °C bis +35 °C, Teile innerhalb von 15 Minuten fügen, Klebeschicht mindestens 2 mm
- **Aushärtung:** Hautbildung nach ca. 12 Minuten, ca. 4 mm in 24 Stunden, Endfestigkeit nach 24–48 Stunden
- **Belastbarkeit:** dauerhaft elastisch von −40 °C bis +120 °C, kurzzeitig bis +180 °C; UV- und witterungsbeständig, überlackierbar

## Welcher Kleber ist der richtige für ein Solarpanel auf dem Wohnmobil?

Für die Montage auf dem Dach brauchst du einen Kleber, der zwei Dinge gleichzeitig kann: dauerhaft fest halten und elastisch bleiben. Dach, Spoiler und Modul dehnen sich bei Hitze und Kälte unterschiedlich aus, dazu kommen Vibrationen während der Fahrt. Ein starrer Kleber würde reißen, eine dauerplastische Dichtmasse würde nachgeben.

DEKAsyl MS-5 ist ein Kleb- und Dichtstoff auf Basis von MS-Polymer mit besonders hoher Anfangsfestigkeit („High Tack“). Er verbindet Spoiler und Dach elastisch, dichtet die Klebefuge gleichzeitig ab und haftet auf den typischen Dachmaterialien ohne Primer. In der DEKAsyl-Reihe ist MS-5 der Konstruktionsklebstoff für Profi-Anwendungen – für Dachkonstruktionen, SAT- und Solaranlagen.

**Nicht geeignet** sind dauerplastische Butylmassen wie DEKASEAL 8936: Sie dichten Fenster und Serviceklappen wiederlösbar ab, tragen aber keine Klebelasten. Auch Sanitärsilikon ist für Anbauteile am Fahrzeug keine Lösung. [Annahme: Silikon-Aussage fachlich freigeben]

## Starres oder flexibles Solarmodul: Was wird geklebt?

| Modultyp | Was wird geklebt? | Empfohlenes Produkt |
|---|---|---|
| Starres Modul (Aluminiumrahmen) | Spoiler oder Halter, die am Modul verschraubt sind, werden aufs Dach geklebt | DEKAsyl MS-5 bzw. Klebeset für SAT und starre Solaranlagen |
| Halbflexibles Modul | Modul wird direkt auf das Dach geklebt | DEKAsyl MS-5 |
| Flexibles Modul | Modul wird direkt auf das Dach geklebt | Flexsolarmodul-Klebeset (MS-5 + MS-1 + DEKACLEAN-Tuch), Art.-Nr. 62700 schwarz / 62701 weiß |
| Kabeldurchführung | Durchführung aufs Dach kleben und abdichten | DEKAsyl MS-5 |

## Das brauchst du

**Produkte**
- [DEKAsyl MS-5](/produkt/dekasyl-ms-5/) – 290-ml-Kartusche (weiß oder schwarz) oder 600-ml-Schlauchbeutel (weiß)
- oder das [Flexsolarmodul-Klebeset](/produkt/656/) für flexible Module
- [DEKACLEAN ULTRA](/produkt/dekaclean-ultra/) – Haftreiniger zum Reinigen und Entfetten
- [DEKAVATOR 22 NF](/produkt/dekavator-22-nf/) – Haftvermittler bei hoher Belastung und Feuchtigkeit (optional)
- [DEKAFINISHER](/produkt/dekafinisher/) – Glättmittel für saubere Abschlussnähte

**Werkzeug**
- Hand- oder Druckluftpistole (für Schlauchbeutel eine Schlauchbeutelpistole)
- Spachtel, fusselfreies Tuch, Malerkrepp
- Schutzhandschuhe [Annahme: Standardhinweis]

## Schritt-für-Schritt: Solarpanel aufs Wohnmobildach kleben

### Schritt 1: Montage planen und Bedingungen prüfen
Montiere Spoiler oder Halter nach Anleitung des Modulherstellers am Modul, lege Position und Kabelweg fest und markiere die Klebeflächen auf dem Dach. Arbeite bei +5 °C bis +35 °C auf trockenem Untergrund, am besten im Schatten.

### Schritt 2: Klebeflächen reinigen
Reinige Dach und Unterseite der Spoiler bzw. Halter mit DEKACLEAN ULTRA. Beide Flächen müssen sauber, trocken, staub- und fettfrei sein; entferne lose Dichtstoff-Altreste vorher mechanisch.

### Schritt 3: Haftung sicherstellen
Auf Aluminium, GFK, lackiertem Metall und Glas haftet MS-5 ohne Primer. Bei unbekannten Untergründen machst du einen Haftungstest; bei hoher thermischer oder physikalischer Belastung, besonders bei Feuchtigkeit, trägst du zusätzlich DEKAVATOR 22 NF auf.

### Schritt 4: Kleber auftragen
Trage MS-5 mit Hand- oder Druckluftpistole als durchgehende Raupe von ca. 7 mm auf die Unterseite der Spoiler bzw. Halter auf. Nach dem Andrücken soll die Klebeschicht mindestens 2 mm dick sein (aus 7 mm Raupe entstehen 3–5 mm); bei stark unterschiedlicher Wärmeausdehnung der Materialien wählst du sie dicker.

### Schritt 5: Teile fügen
Setze das Modul innerhalb von 15 Minuten auf und drücke es gleichmäßig an, ohne die Klebeschicht unter 2 mm zu pressen. Dank der hohen Anfangshaftung von MS-5 kann auf Klemmen meist verzichtet werden.

### Schritt 6: Kanten und Kabeldurchführung abdichten
Ziehe eine Abschlussnaht an den Klebekanten und dichte die Kabeldurchführung mit MS-5 ab. Glätte innerhalb von 12 Minuten mit einem in DEKAFINISHER getauchten Spachtel, ohne dass Finisher in die Fuge gelangt; unausgehärtete Reste entfernst du mit DEKACLEAN ULTRA.

### Schritt 7: Aushärten lassen
MS-5 härtet ca. 4 mm in 24 Stunden durch (20 °C, 50 % relative Luftfeuchte). Die Endfestigkeit ist nach 24 bis 48 Stunden erreicht – erst danach fahren.

### Schritt 8: Optional lackieren und kontrollieren
Bei Bedarf lackierst du die Naht nass in nass ab ca. 10 Minuten nach dem Auftragen; die beste Lackhaftung entsteht nach ca. 4 Stunden. Kontrolliere die Verklebung nach den ersten Fahrten und bei jeder Dichtigkeitsprüfung.

[Video „Solarplattenhalterung“ hier einbinden – aus `/produkt/556/`, mit Transkript darunter]

## Zeiten und Temperaturen auf einen Blick

| Phase | Wert (20 °C, 50 % rel. Luftfeuchte) |
|---|---|
| Verarbeitungstemperatur | +5 °C bis +35 °C |
| Hautbildung / Glätten bis | ca. 12 Minuten |
| Teile fügen bis (offene Zeit) | unter 15 Minuten |
| Überlackieren ab | ca. 10 Minuten (nass in nass), beste Lackhaftung nach ca. 4 Stunden |
| Durchhärtung | ca. 4 mm in 24 Stunden |
| Endfestigkeit / losfahren ab | 24–48 Stunden, je nach Temperatur und Luftfeuchte |
| Temperaturbeständigkeit danach | −40 °C bis +120 °C, kurzzeitig +180 °C (max. 20 Minuten) |

## Auf welchen Dachmaterialien hält DEKAsyl MS-5?

| Haftung | Untergründe |
|---|---|
| **Ohne Primer** (sauber, trocken, staub- und fettfrei) | Aluminium, Edelstahl, verzinkter Stahl, Zink, Kupfer, Messing, pulverbeschichtetes Metall, die meisten lackierten Metalle, Glas, PVC, Polyester (GFK), gestrichenes und lackiertes Holz |
| **Mit DEKAVATOR 22 NF empfohlen** | bei hoher thermischer oder physikalischer Belastung, besonders bei Feuchtigkeit |
| **Haftungstest nötig** | alle Untergründe, die oben nicht genannt sind (z. B. ABS-Kunststoffe) [Annahme: ABS als Beispiel] |
| **Keine Haftung ohne Vorbehandlung** | PE, PP, Teflon |

## DEKAsyl MS-1, MS-2 oder MS-5: Welcher ist der richtige?

| | DEKAsyl MS-1 | DEKAsyl MS-2 | **DEKAsyl MS-5** |
|---|---|---|---|
| Einordnung laut Dekalin | für Einsteiger | für Fortgeschrittene | für Profis – „Kleben und Dichten auf Meisterniveau“ |
| Typ | Dichtstoff | Dichtstoff | **Konstruktionsklebstoff, High Tack** |
| Typische Anwendungen | Fugen, Dichtnähte, Überlappungen | Verbindungen, Dichtnähte, Solaranlagen, Überlappungen | **Solarmodul-Spoiler, halbflexible Solarmodule, SAT-Anlagen, Dachkonstruktionen, Karosseriemontage, Spoiler** |
| Farben | weiß, grau, schwarz | weiß, grau, schwarz | weiß, schwarz |
| Gebinde | 290 ml | 290 ml, 600 ml Schlauchbeutel | 290 ml, 600 ml Schlauchbeutel (weiß) |
| Beim Solarpanel | Abschluss- und Dichtnähte (im Flexsolar-Set enthalten) | Verbindungen und Abdichtungen | **tragende Verklebung von Spoilern und Modulen** |

Mehr dazu: [DEKAsyl MS-1, MS-2, MS-5 – was ist der Unterschied?](/dekasyl-ms-1-dekasyl-ms-2-dekasyl-ms-5-was-ist-der-unterschied/)

## DEKAsyl MS-5 im Vergleich mit Sikaflex-554

Beide Produkte sind elastische Montageklebstoffe für Anbauteile am Caravan. Die Werte stammen aus den technischen Datenblättern der Hersteller (Stand 01.11.2026); die Prüfbedingungen unterscheiden sich teilweise.

| Merkmal | DEKAsyl MS-5 | Sikaflex-554 |
|---|---|---|
| Basis | MS-Polymer | STP (silanterminiertes Polymer) |
| Hautbildung | ca. 12 min (20 °C) | 25 min (23 °C) |
| Shore-A-Härte | ca. 55 | 55 |
| Zugfestigkeit | ca. 2,8 MPa | 3,5 MPa |
| Bruchdehnung | ca. 210 % | 500 % |
| Zugscherfestigkeit | ca. 2,5 MPa | 2,5 MPa |
| Temperaturbeständigkeit | **−40 bis +120 °C**, kurzzeitig +180 °C | −50 bis +90 °C |
| Verarbeitungstemperatur | +5 bis +35 °C | +5 bis +40 °C |
| Lagerfähigkeit | **18 Monate** (Kartusche) | 12 Monate |
| Nachweise | – | DIN EN 45545-2, ISEGA |
| Zielgruppe laut Hersteller | Endkunden und Profis | „nur für erfahrene Anwender“ |

**Fazit:** Für die Solarmontage zählt vor allem die Temperaturbeständigkeit unter dem Modul und eine schnelle Anfangshaftung – hier liegt MS-5 vorn. Sikaflex-554 ist dehnfähiger und hat Bahn- und ISEGA-Nachweise.
[Redaktion: Vergleich vor Veröffentlichung rechtlich prüfen (vergleichende Werbung, § 6 UWG); „Sikaflex“ ist eine Marke der Sika AG.]

## Häufige Fehler beim Solarpanel-Kleben

- **Butylmasse oder Silikon statt Klebstoff:** dichtet, hält aber keine Anbauteile.
- **Ungereinigte Flächen:** Staub, Fett und Altreste verhindern die Haftung – immer mit DEKACLEAN ULTRA reinigen.
- **Zu dünne Klebeschicht:** unter 2 mm kann der Kleber Wärmeausdehnung und Vibrationen nicht ausgleichen.
- **Zu spät gefügt:** nach mehr als 15 Minuten hat sich die Haut gebildet, die Haftung sinkt.
- **Finisher in der Fuge:** DEKAFINISHER nur auf den Spachtel, nie in die Klebefuge.
- **Zu früh losgefahren:** Endfestigkeit erst nach 24–48 Stunden.
- **Kleben in der prallen Sonne:** über +35 °C wird die Verarbeitungszeit zu kurz.

## Technische Daten DEKAsyl MS-5

| Merkmal | Wert |
|---|---|
| Basis / Aushärtung | MS-Polymer / durch Luftfeuchtigkeit |
| Farben | weiß, schwarz |
| Dichte | ca. 1,4 kg/l |
| Hautbildungszeit (20 °C / 50 % r. F.) | ca. 12 min |
| Offene Zeit | < 15 min |
| Durchhärtung nach 24 h | ca. 4 mm |
| Shore-A-Härte (DIN 53505) | ca. 55 |
| Volumenänderung (DIN 52451) | < 3 % |
| Standfestigkeit (Rheometer) | ca. 700 Pa |
| Zugspannung bei 100 % Dehnung | ca. 1,7 MPa |
| Zugspannung bei Bruch | ca. 2,8 MPa |
| Bruchdehnung | ca. 210 % |
| Scherspannung (DIN 53283) | ca. 2,5 MPa |
| Weiterreißfestigkeit | ca. 14 N/mm |
| Lösemittel / Isocyanat | 0 % / 0 % |
| Temperaturbeständigkeit | −40 °C bis +120 °C, kurzzeitig +180 °C (max. 20 min) |
| Verarbeitungstemperatur | +5 °C bis +35 °C |
| UV- und Witterungsbeständigkeit | hervorragend |
| Überlackierbar | ja, nach Hautbildung nass in nass |
| Lagerung (ungeöffnet, trocken, +10 bis +30 °C) | Kartusche 18 Monate, Schlauchbeutel 12 Monate |
| Gefahrstoffeinstufung | nicht als gefährlich eingestuft nach CLP; EUH208, EUH210 |
| Gebinde / Art.-Nr. | 290 ml weiß 62522 34 · 290 ml schwarz 62524 34 · 600 ml Schlauchbeutel weiß 62523 12 · Flexsolar-Set 62700 12 (schwarz) / 62701 12 (weiß) |

## Häufige Fragen zum Solarpanel-Kleben

### Welcher Kleber eignet sich, um ein Solarpanel ohne Bohren aufs Wohnmobildach zu kleben?
Ein elastischer High-Tack-Kleb- und Dichtstoff auf MS-Polymer-Basis wie DEKAsyl MS-5. Er haftet ohne Primer auf Aluminium, GFK und lackiertem Blech, bleibt von −40 °C bis +120 °C elastisch und hält Spoiler oder Halter dank hoher Anfangshaftung meist ohne Klemmen in Position. Dauerplastische Butylmassen wie DEKASEAL 8936 dichten zuverlässig, tragen aber keine Klebelasten und sind für die Montage ungeeignet.

### Muss ich bei DEKAsyl MS-5 einen Primer verwenden?
Nein, auf sauberen, trockenen, staub- und fettfreien Flächen aus Aluminium, Edelstahl, verzinktem Stahl, pulverbeschichtetem oder lackiertem Metall, Glas, PVC und Polyester (GFK) haftet MS-5 ohne Primer. Bei hoher thermischer oder physikalischer Belastung, besonders bei Feuchtigkeit, empfiehlt DEKALIN zusätzlich den Haftvermittler DEKAVATOR 22 NF. Auf PE, PP und Teflon haftet MS-5 ohne Vorbehandlung nicht.

### Wie lange muss der Kleber aushärten, bevor ich losfahren kann?
MS-5 bildet nach ca. 12 Minuten eine Haut und härtet bei 20 °C und 50 % relativer Luftfeuchte ca. 4 mm pro 24 Stunden durch. Die Endfestigkeit ist je nach Temperatur und Luftfeuchte nach 24 bis 48 Stunden erreicht – fahre erst danach. Bei Kälte und trockener Luft dauert die Aushärtung länger.

### Bei welchen Temperaturen kann ich MS-5 verarbeiten?
Zwischen +5 °C und +35 °C. Je wärmer es ist, desto kürzer ist die Verarbeitungszeit; die Teile müssen innerhalb von 15 Minuten nach dem Auftragen gefügt werden. Ein Dach in praller Sonne wird schnell wärmer als +35 °C – klebe deshalb im Schatten oder am Morgen.

### Hält die Verklebung die Hitze unter dem Solarmodul aus?
Ja. MS-5 bleibt laut technischem Datenblatt von −40 °C bis +120 °C dauerhaft elastisch und verträgt kurzzeitig bis +180 °C (maximal 20 Minuten). Die UV- und Witterungsbeständigkeit bewertet der Hersteller als hervorragend.

### Hält ein geklebtes Solarpanel auch bei Autobahnfahrt?
Die Verklebung mit MS-5 ist dauerelastisch und gleicht Vibrationen sowie die unterschiedliche Wärmeausdehnung von Modul, Halter und Dach aus; die Zugscherfestigkeit liegt bei ca. 2,5 MPa (DIN 53283). Entscheidend für den Halt sind ausreichend große Klebeflächen, eine Klebeschicht von mindestens 2 mm, eine gründliche Vorbereitung und die vollständige Aushärtung vor der ersten Fahrt.

### Kann ich flexible oder halbflexible Solarmodule direkt aufs Dach kleben?
Ja. Halbflexible Solarmodule nennt das Datenblatt ausdrücklich als Anwendung von MS-5. Für flexible Module ohne Bohren gibt es das Flexsolarmodul-Klebeset mit DEKAsyl MS-5, DEKAsyl MS-1 und DEKACLEAN-Reinigungstuch (Art.-Nr. 62700 schwarz, 62701 weiß). Beachte zusätzlich die Montagehinweise des Modulherstellers.

### Wie viel Kleber brauche ich für ein Solarpanel?
Das hängt von Anzahl und Größe der Spoiler oder Halter ab. Als Richtwert: Eine 7-mm-Raupe verbraucht rechnerisch rund 38 ml pro Meter, eine 290-ml-Kartusche reicht damit für etwa 7 Meter Raupe. Für ein Modul mit vier Spoilern genügt in der Regel eine Kartusche; plane für die Kabeldurchführung etwas Reserve ein.

### Kann ich MS-5 überlackieren?
Ja. MS-5 ist nach der Hautbildung nass in nass überlackierbar: Lackieren ist nach etwa 10 Minuten möglich, die beste Lackhaftung entsteht nach ca. 4 Stunden. MS-5 ist mit den meisten Industrielacken sowie mit Alkydharz- und Dispersionsfarben verträglich; ein Verträglichkeitstest wird empfohlen.

### Kann ich das Solarpanel später wieder abnehmen?
MS-5 ist ein Konstruktionsklebstoff für dauerhafte Verbindungen und nicht wiederlösbar ausgelegt; zum Demontieren wird die Klebefuge mechanisch durchtrennt. Soll ein Anbauteil später leicht demontierbar sein, wird es verschraubt und mit einer dauerplastischen Dichtmasse wie DEKASEAL 8936 abgedichtet.

### Was ist der Unterschied zwischen DEKAsyl MS-5 und Sikaflex-554?
Beide sind elastische Montageklebstoffe für Anbauteile mit Shore-A-Härte 55 und Zugscherfestigkeit 2,5 MPa. Laut Herstellerangaben (teils unterschiedliche Prüfbedingungen) ist MS-5 bis +120 °C temperaturbeständig (Sikaflex-554: +90 °C), bildet schneller eine Haut (ca. 12 statt 25 Minuten) und ist 18 statt 12 Monate lagerfähig. Sikaflex-554 hat die höhere Bruchdehnung (500 % statt ca. 210 %), die höhere Zugfestigkeit (3,5 statt ca. 2,8 MPa) und Nachweise nach DIN EN 45545-2 und ISEGA; Sika empfiehlt es nur für erfahrene Anwender.

### Kann ich mit MS-5 auch die Kabeldurchführung abdichten?
Ja. Dachdurchführungen gehören laut Datenblatt zu den Anwendungen von MS-5; der Kleber verbindet und dichtet in einem Arbeitsgang. Glätte die Naht innerhalb von 12 Minuten mit einem in DEKAFINISHER getauchten Spachtel – der Finisher darf nicht in die Fuge gelangen.

[Redaktion zu „Autobahnfahrt“: Liegt ein Fahrtest oder Prüfnachweis (TÜV/Windkanal) vor, als Satz ergänzen; bis dahin keine km/h-Angabe. Zu „Wie viel Kleber“: Rechenwert für eine Rundraupe ohne Verlust und „eine Kartusche für vier Spoiler“ sind **[Annahme]** – Ergiebigkeit beim Hersteller erfragen. Zu „wieder abnehmen“: Demontageverfahren **[Annahme]**, mit Anwendungstechnik abstimmen.]

## Wo bekomme ich DEKAsyl MS-5?

DEKAsyl MS-5 und die Klebesets gibt es im Caravaning-Fachhandel – unter anderem bei Campingprofi, Reimo, Movera, Fritz Berger und Frankana – sowie im Solar-Fachhandel, z. B. bei Offgridtec, Fraron und Solarkontor. Einen geschulten DEKALIN-Fachhändler in deiner Nähe findest du über die [Händlersuche](/unser-service/endkunden/).

**Downloads:** [Technisches Datenblatt DEKAsyl MS-5 (PDF)](/wp-content/uploads/2024/12/Dekalin_TDB_Dekasyl-MS-5_DE.pdf) · Sicherheitsdatenblatt · [Chemische Resistenz DEKAsyl MS-Polymer (PDF)](/dokumente//A%20DEKALIN%20Produktinfo/Chemische%20Resistenz%20Dekasyl%20MS-Polymer.pdf)

**Weiterlesen:** [SAT-Anlage aufs Wohnmobil kleben](/sat-anlage/) · [Markise, Dachträger und Anbauteile kleben](/ratgeber/markise-dachtraeger-anbauteile-kleben/) · [Alle Fragen zu Kleben & Dichten am Wohnmobil](/faq/)

---

## 5. Interne Verlinkung

**Ausgehend (von der neuen Seite)**

| Ziel | Ankertext | Position |
|---|---|---|
| Produktseite MS-5 (heute `/produkt/557/`, nach M3 `/produkt/dekasyl-ms-5/`) | „DEKAsyl MS-5“ | Kurzantwort-Box, Materialliste, Tabelle |
| Flexsolarmodul-Klebeset `/produkt/656/` | „Flexsolarmodul-Klebeset“ | Modultyp-Tabelle, Materialliste, FAQ |
| DEKACLEAN ULTRA, DEKAVATOR 22 NF, DEKAFINISHER | Produktname | Materialliste, Schritte 2/3/6 |
| `/dekasyl-ms-1-dekasyl-ms-2-dekasyl-ms-5-was-ist-der-unterschied/` | „DEKAsyl MS-1, MS-2, MS-5 – was ist der Unterschied?“ | unter Vergleichstabelle |
| `/sat-anlage/`, `/ratgeber/markise-dachtraeger-anbauteile-kleben/` | „SAT-Anlage aufs Wohnmobil kleben“, „Markise, Dachträger und Anbauteile kleben“ | Weiterlesen |
| `/faq/` (nach M2: Hub) | „Alle Fragen zu Kleben & Dichten am Wohnmobil“ | Weiterlesen |
| `/unser-service/endkunden/` | „Händlersuche“ | Wo kaufen |

**Eingehend (auf die neue Seite)**

| Quelle | Ankertext | Hinweis |
|---|---|---|
| Startseite (Teaser „Beliebte Anleitungen“) | „Solarpanel ohne Bohren kleben“ | Link von der stärksten Seite |
| Produktseiten MS-5 weiß + schwarz, MS-2, Flexsolar-Set | „Anleitung: Solarpanel aufs Wohnmobil kleben“ | oberhalb der Downloads |
| Branchenseite Caravaning `/branchen/caravaning/` | „Solarmodul aufs Wohnmobildach kleben“ | im Anwendungsblock |
| Kategorie Kleben & Dichten | „Solarpanel kleben“ | Kategorietext |
| FAQ / FAQ-Hub | „Welcher Kleber für Solarmodule?“ → `#faq` | Antwort mit Link |
| Blogartikel mit Solarbezug, `/sat-anlage/` | „Solarpanel kleben ohne Bohren“ | 3–4 Kontextlinks |
| DEKABot, YouTube-Videobeschreibung, Händler-Content-Paket (M5) | URL | externe Signale |
| 301 `/solar/` → neue URL | – | bestehende Links bleiben wirksam |

---

## 6. JSON-LD (Article + HowTo + FAQPage + Product + BreadcrumbList + Organization)

Einbau als ein `<script type="application/ld+json">` im `<head>` oder am Ende des `<body>`. JSON syntaktisch geprüft (Python `json.loads`). FAQ- und Schritttexte sind 1:1 identisch mit dem sichtbaren Seitentext.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://dekalin.de/#organization",
      "name": "DEKALIN",
      "legalName": "DEKA Kleben & Dichten GmbH",
      "url": "https://dekalin.de/",
      "logo": "https://dekalin.de/bilder/dekalin-logo.png",
      "parentOrganization": {
        "@type": "Organization",
        "name": "DINOL GmbH",
        "url": "https://www.dinol.com/"
      },
      "sameAs": [
        "https://www.dekalin.com/",
        "https://www.facebook.com/dekalinofficial",
        "https://www.instagram.com/dekalinofficial",
        "https://www.youtube.com/user/DEKALIN4DEKA"
      ]
    },
    {
      "@type": "Person",
      "@id": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#autor",
      "name": "Michael Windecker",
      "jobTitle": "Geschäftsführer DEKA Kleben & Dichten GmbH, Autor „Klebt nicht gibt's nicht!“",
      "worksFor": {
        "@id": "https://dekalin.de/#organization"
      }
    },
    {
      "@type": "Article",
      "@id": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#artikel",
      "headline": "Solarpanel ohne Bohren aufs Wohnmobildach kleben – so geht's mit DEKAsyl MS-5",
      "description": "Welcher Kleber, welche Vorbereitung, wie lange aushärten? Anleitung mit DEKAsyl MS-5, Vergleichstabelle und FAQ.",
      "image": [
        "https://dekalin.de/bilder/solarpanel-wohnmobil-kleben-ms-5.jpg"
      ],
      "datePublished": "2026-11-15",
      "dateModified": "2026-11-15",
      "inLanguage": "de-DE",
      "author": {
        "@id": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#autor"
      },
      "publisher": {
        "@id": "https://dekalin.de/#organization"
      },
      "mainEntityOfPage": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/",
      "about": {
        "@id": "https://dekalin.de/produkt/dekasyl-ms-5/#ms5-weiss-290"
      },
      "mentions": [
        {
          "@id": "https://dekalin.de/produkt/dekasyl-ms-5/#ms5-weiss-290"
        }
      ],
      "hasPart": [
        {
          "@id": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#anleitung"
        },
        {
          "@id": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#faq"
        }
      ]
    },
    {
      "@type": "HowTo",
      "@id": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#anleitung",
      "name": "Solarpanel ohne Bohren aufs Wohnmobildach kleben",
      "description": "Schritt-für-Schritt-Anleitung zum Kleben von Solarmodul-Spoilern und halbflexiblen Solarmodulen auf das Wohnmobildach mit DEKAsyl MS-5.",
      "supply": [
        {
          "@type": "HowToSupply",
          "name": "DEKAsyl MS-5 (290-ml-Kartusche oder 600-ml-Schlauchbeutel)"
        },
        {
          "@type": "HowToSupply",
          "name": "DEKACLEAN ULTRA Haftreiniger"
        },
        {
          "@type": "HowToSupply",
          "name": "DEKAVATOR 22 NF Haftvermittler (bei hoher Belastung)"
        },
        {
          "@type": "HowToSupply",
          "name": "DEKAFINISHER Glättmittel"
        }
      ],
      "tool": [
        {
          "@type": "HowToTool",
          "name": "Hand- oder Druckluftpistole"
        },
        {
          "@type": "HowToTool",
          "name": "Spachtel"
        },
        {
          "@type": "HowToTool",
          "name": "Fusselfreies Tuch"
        },
        {
          "@type": "HowToTool",
          "name": "Malerkrepp"
        }
      ],
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "name": "Montage planen und Bedingungen prüfen",
          "text": "Montiere Spoiler oder Halter nach Anleitung des Modulherstellers am Modul, lege Position und Kabelweg fest und markiere die Klebeflächen auf dem Dach. Arbeite bei +5 °C bis +35 °C auf trockenem Untergrund, am besten im Schatten.",
          "url": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#schritt-1"
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "name": "Klebeflächen reinigen",
          "text": "Reinige Dach und Unterseite der Spoiler bzw. Halter mit DEKACLEAN ULTRA. Beide Flächen müssen sauber, trocken, staub- und fettfrei sein; entferne lose Dichtstoff-Altreste vorher mechanisch.",
          "url": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#schritt-2"
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "name": "Haftung sicherstellen",
          "text": "Auf Aluminium, GFK, lackiertem Metall und Glas haftet MS-5 ohne Primer. Bei unbekannten Untergründen machst du einen Haftungstest; bei hoher thermischer oder physikalischer Belastung, besonders bei Feuchtigkeit, trägst du zusätzlich DEKAVATOR 22 NF auf.",
          "url": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#schritt-3"
        },
        {
          "@type": "HowToStep",
          "position": 4,
          "name": "Kleber auftragen",
          "text": "Trage MS-5 mit Hand- oder Druckluftpistole als durchgehende Raupe von ca. 7 mm auf die Unterseite der Spoiler bzw. Halter auf. Nach dem Andrücken soll die Klebeschicht mindestens 2 mm dick sein (aus 7 mm Raupe entstehen 3–5 mm); bei stark unterschiedlicher Wärmeausdehnung der Materialien wählst du sie dicker.",
          "url": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#schritt-4"
        },
        {
          "@type": "HowToStep",
          "position": 5,
          "name": "Teile fügen",
          "text": "Setze das Modul innerhalb von 15 Minuten auf und drücke es gleichmäßig an, ohne die Klebeschicht unter 2 mm zu pressen. Dank der hohen Anfangshaftung von MS-5 kann auf Klemmen meist verzichtet werden.",
          "url": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#schritt-5"
        },
        {
          "@type": "HowToStep",
          "position": 6,
          "name": "Kanten und Kabeldurchführung abdichten",
          "text": "Ziehe eine Abschlussnaht an den Klebekanten und dichte die Kabeldurchführung mit MS-5 ab. Glätte innerhalb von 12 Minuten mit einem in DEKAFINISHER getauchten Spachtel, ohne dass Finisher in die Fuge gelangt; unausgehärtete Reste entfernst du mit DEKACLEAN ULTRA.",
          "url": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#schritt-6"
        },
        {
          "@type": "HowToStep",
          "position": 7,
          "name": "Aushärten lassen",
          "text": "MS-5 härtet ca. 4 mm in 24 Stunden durch (20 °C, 50 % relative Luftfeuchte). Die Endfestigkeit ist nach 24 bis 48 Stunden erreicht – erst danach fahren.",
          "url": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#schritt-7"
        },
        {
          "@type": "HowToStep",
          "position": 8,
          "name": "Optional lackieren und kontrollieren",
          "text": "Bei Bedarf lackierst du die Naht nass in nass ab ca. 10 Minuten nach dem Auftragen; die beste Lackhaftung entsteht nach ca. 4 Stunden. Kontrolliere die Verklebung nach den ersten Fahrten und bei jeder Dichtigkeitsprüfung.",
          "url": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#schritt-8"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Welcher Kleber eignet sich, um ein Solarpanel ohne Bohren aufs Wohnmobildach zu kleben?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ein elastischer High-Tack-Kleb- und Dichtstoff auf MS-Polymer-Basis wie DEKAsyl MS-5. Er haftet ohne Primer auf Aluminium, GFK und lackiertem Blech, bleibt von −40 °C bis +120 °C elastisch und hält Spoiler oder Halter dank hoher Anfangshaftung meist ohne Klemmen in Position. Dauerplastische Butylmassen wie DEKASEAL 8936 dichten zuverlässig, tragen aber keine Klebelasten und sind für die Montage ungeeignet."
          }
        },
        {
          "@type": "Question",
          "name": "Muss ich bei DEKAsyl MS-5 einen Primer verwenden?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nein, auf sauberen, trockenen, staub- und fettfreien Flächen aus Aluminium, Edelstahl, verzinktem Stahl, pulverbeschichtetem oder lackiertem Metall, Glas, PVC und Polyester (GFK) haftet MS-5 ohne Primer. Bei hoher thermischer oder physikalischer Belastung, besonders bei Feuchtigkeit, empfiehlt DEKALIN zusätzlich den Haftvermittler DEKAVATOR 22 NF. Auf PE, PP und Teflon haftet MS-5 ohne Vorbehandlung nicht."
          }
        },
        {
          "@type": "Question",
          "name": "Wie lange muss der Kleber aushärten, bevor ich losfahren kann?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "MS-5 bildet nach ca. 12 Minuten eine Haut und härtet bei 20 °C und 50 % relativer Luftfeuchte ca. 4 mm pro 24 Stunden durch. Die Endfestigkeit ist je nach Temperatur und Luftfeuchte nach 24 bis 48 Stunden erreicht – fahre erst danach. Bei Kälte und trockener Luft dauert die Aushärtung länger."
          }
        },
        {
          "@type": "Question",
          "name": "Bei welchen Temperaturen kann ich MS-5 verarbeiten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Zwischen +5 °C und +35 °C. Je wärmer es ist, desto kürzer ist die Verarbeitungszeit; die Teile müssen innerhalb von 15 Minuten nach dem Auftragen gefügt werden. Ein Dach in praller Sonne wird schnell wärmer als +35 °C – klebe deshalb im Schatten oder am Morgen."
          }
        },
        {
          "@type": "Question",
          "name": "Hält die Verklebung die Hitze unter dem Solarmodul aus?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. MS-5 bleibt laut technischem Datenblatt von −40 °C bis +120 °C dauerhaft elastisch und verträgt kurzzeitig bis +180 °C (maximal 20 Minuten). Die UV- und Witterungsbeständigkeit bewertet der Hersteller als hervorragend."
          }
        },
        {
          "@type": "Question",
          "name": "Hält ein geklebtes Solarpanel auch bei Autobahnfahrt?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Die Verklebung mit MS-5 ist dauerelastisch und gleicht Vibrationen sowie die unterschiedliche Wärmeausdehnung von Modul, Halter und Dach aus; die Zugscherfestigkeit liegt bei ca. 2,5 MPa (DIN 53283). Entscheidend für den Halt sind ausreichend große Klebeflächen, eine Klebeschicht von mindestens 2 mm, eine gründliche Vorbereitung und die vollständige Aushärtung vor der ersten Fahrt."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich flexible oder halbflexible Solarmodule direkt aufs Dach kleben?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Halbflexible Solarmodule nennt das Datenblatt ausdrücklich als Anwendung von MS-5. Für flexible Module ohne Bohren gibt es das Flexsolarmodul-Klebeset mit DEKAsyl MS-5, DEKAsyl MS-1 und DEKACLEAN-Reinigungstuch (Art.-Nr. 62700 schwarz, 62701 weiß). Beachte zusätzlich die Montagehinweise des Modulherstellers."
          }
        },
        {
          "@type": "Question",
          "name": "Wie viel Kleber brauche ich für ein Solarpanel?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Das hängt von Anzahl und Größe der Spoiler oder Halter ab. Als Richtwert: Eine 7-mm-Raupe verbraucht rechnerisch rund 38 ml pro Meter, eine 290-ml-Kartusche reicht damit für etwa 7 Meter Raupe. Für ein Modul mit vier Spoilern genügt in der Regel eine Kartusche; plane für die Kabeldurchführung etwas Reserve ein."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich MS-5 überlackieren?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. MS-5 ist nach der Hautbildung nass in nass überlackierbar: Lackieren ist nach etwa 10 Minuten möglich, die beste Lackhaftung entsteht nach ca. 4 Stunden. MS-5 ist mit den meisten Industrielacken sowie mit Alkydharz- und Dispersionsfarben verträglich; ein Verträglichkeitstest wird empfohlen."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich das Solarpanel später wieder abnehmen?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "MS-5 ist ein Konstruktionsklebstoff für dauerhafte Verbindungen und nicht wiederlösbar ausgelegt; zum Demontieren wird die Klebefuge mechanisch durchtrennt. Soll ein Anbauteil später leicht demontierbar sein, wird es verschraubt und mit einer dauerplastischen Dichtmasse wie DEKASEAL 8936 abgedichtet."
          }
        },
        {
          "@type": "Question",
          "name": "Was ist der Unterschied zwischen DEKAsyl MS-5 und Sikaflex-554?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Beide sind elastische Montageklebstoffe für Anbauteile mit Shore-A-Härte 55 und Zugscherfestigkeit 2,5 MPa. Laut Herstellerangaben (teils unterschiedliche Prüfbedingungen) ist MS-5 bis +120 °C temperaturbeständig (Sikaflex-554: +90 °C), bildet schneller eine Haut (ca. 12 statt 25 Minuten) und ist 18 statt 12 Monate lagerfähig. Sikaflex-554 hat die höhere Bruchdehnung (500 % statt ca. 210 %), die höhere Zugfestigkeit (3,5 statt ca. 2,8 MPa) und Nachweise nach DIN EN 45545-2 und ISEGA; Sika empfiehlt es nur für erfahrene Anwender."
          }
        },
        {
          "@type": "Question",
          "name": "Kann ich mit MS-5 auch die Kabeldurchführung abdichten?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ja. Dachdurchführungen gehören laut Datenblatt zu den Anwendungen von MS-5; der Kleber verbindet und dichtet in einem Arbeitsgang. Glätte die Naht innerhalb von 12 Minuten mit einem in DEKAFINISHER getauchten Spachtel – der Finisher darf nicht in die Fuge gelangen."
          }
        }
      ]
    },
    {
      "@type": "Product",
      "@id": "https://dekalin.de/produkt/dekasyl-ms-5/#ms5-weiss-290",
      "name": "DEKAsyl MS-5 High Tack Kleb- und Dichtstoff weiß 290 ml",
      "description": "Elastischer High-Tack-Kleb- und Dichtstoff auf MS-Polymer-Basis mit hoher Anfangsfestigkeit, ohne Primer auf Aluminium, GFK, lackiertem Metall und Glas, dauerhaft elastisch von −40 °C bis +120 °C, überlackierbar, frei von Lösemitteln, Isocyanat und PVC. Zum Kleben von Solarmodul-Spoilern, halbflexiblen Solarmodulen, SAT-Anlagen und Dachdurchführungen.",
      "url": "https://dekalin.de/produkt/dekasyl-ms-5/",
      "image": [
        "https://dekalin.de/bilder/dekasyl-ms-5-weiss-290ml.jpg"
      ],
      "sku": "6252234",
      "mpn": "62522 34",
      "gtin13": "4046085125227",
      "brand": {
        "@type": "Brand",
        "name": "DEKALIN"
      },
      "manufacturer": {
        "@type": "Organization",
        "name": "DINOL GmbH"
      },
      "category": "Kleb- und Dichtstoffe > MS-Polymer > Konstruktionsklebstoff",
      "material": "MS-Polymer",
      "color": "weiß",
      "size": "290 ml Kartusche",
      "additionalProperty": [
        {
          "@type": "PropertyValue",
          "name": "Basis",
          "value": "MS-Polymer (silanmodifiziertes Polymer)"
        },
        {
          "@type": "PropertyValue",
          "name": "Aushärtung",
          "value": "durch Luftfeuchtigkeit"
        },
        {
          "@type": "PropertyValue",
          "name": "Dichte",
          "value": 1.4,
          "unitText": "kg/l",
          "description": "ca."
        },
        {
          "@type": "PropertyValue",
          "name": "Hautbildungszeit",
          "value": 12,
          "unitCode": "MIN",
          "description": "ca., bei 20 °C / 50 % r. F."
        },
        {
          "@type": "PropertyValue",
          "name": "Offene Zeit",
          "value": 15,
          "unitCode": "MIN",
          "description": "weniger als 15 min; Teile innerhalb von 15 min fügen"
        },
        {
          "@type": "PropertyValue",
          "name": "Durchhärtung nach 24 h",
          "value": 4,
          "unitCode": "MMT",
          "description": "ca., bei 20 °C / 50 % r. F."
        },
        {
          "@type": "PropertyValue",
          "name": "Shore-A-Härte (DIN 53505)",
          "value": 55,
          "description": "ca."
        },
        {
          "@type": "PropertyValue",
          "name": "Volumenänderung (DIN 52451)",
          "value": 3,
          "unitCode": "P1",
          "description": "kleiner 3 %"
        },
        {
          "@type": "PropertyValue",
          "name": "Standfestigkeit (Rheometer)",
          "value": 700,
          "unitCode": "PAL",
          "description": "ca."
        },
        {
          "@type": "PropertyValue",
          "name": "Zugspannung bei 100 % Dehnung",
          "value": 1.7,
          "unitCode": "MPA",
          "description": "ca."
        },
        {
          "@type": "PropertyValue",
          "name": "Zugspannung bei Bruch",
          "value": 2.8,
          "unitCode": "MPA",
          "description": "ca."
        },
        {
          "@type": "PropertyValue",
          "name": "Bruchdehnung",
          "value": 210,
          "unitCode": "P1",
          "description": "ca."
        },
        {
          "@type": "PropertyValue",
          "name": "Scherspannung (DIN 53283)",
          "value": 2.5,
          "unitCode": "MPA",
          "description": "ca."
        },
        {
          "@type": "PropertyValue",
          "name": "Weiterreißfestigkeit",
          "value": 14,
          "unitText": "N/mm",
          "description": "ca."
        },
        {
          "@type": "PropertyValue",
          "name": "Temperaturbeständigkeit",
          "minValue": -40,
          "maxValue": 120,
          "unitCode": "CEL",
          "description": "dauerhaft elastisch; kurzzeitig bis +180 °C (max. 20 min)"
        },
        {
          "@type": "PropertyValue",
          "name": "Verarbeitungstemperatur",
          "minValue": 5,
          "maxValue": 35,
          "unitCode": "CEL"
        },
        {
          "@type": "PropertyValue",
          "name": "Lösemittelgehalt",
          "value": 0,
          "unitCode": "P1"
        },
        {
          "@type": "PropertyValue",
          "name": "Isocyanatgehalt",
          "value": 0,
          "unitCode": "P1"
        },
        {
          "@type": "PropertyValue",
          "name": "UV- und Witterungsbeständigkeit",
          "value": "hervorragend (Herstellerangabe)"
        },
        {
          "@type": "PropertyValue",
          "name": "UV-beständig",
          "value": true
        },
        {
          "@type": "PropertyValue",
          "name": "Überlackierbar",
          "value": true,
          "description": "nach der Hautbildung nass in nass; beste Lackhaftung nach ca. 4 h"
        },
        {
          "@type": "PropertyValue",
          "name": "Primerlose Haftung auf",
          "value": "Aluminium, Edelstahl, verzinkter Stahl, Zink, Kupfer, Messing, pulverbeschichtetes und lackiertes Metall, Glas, PVC, Polyester (GFK), gestrichenes und lackiertes Holz"
        },
        {
          "@type": "PropertyValue",
          "name": "Keine Haftung ohne Vorbehandlung auf",
          "value": "PE, PP, Teflon"
        },
        {
          "@type": "PropertyValue",
          "name": "Anwendungen",
          "value": "Solarmodul-Spoiler, halbflexible Solarmodule, SAT-Anlagen, Fenster, Dachdurchführungen, Kantenprofile, Dachkonstruktionen, Karosseriemontage"
        },
        {
          "@type": "PropertyValue",
          "name": "Lagerfähigkeit Kartusche",
          "value": 18,
          "unitCode": "MON",
          "description": "ungeöffnet, trocken, +10 bis +30 °C"
        },
        {
          "@type": "PropertyValue",
          "name": "Gefahrstoffeinstufung",
          "value": "nicht als gefährlich eingestuft nach CLP; EUH208, EUH210"
        }
      ],
      "isSimilarTo": [
        {
          "@type": "Product",
          "name": "DEKAsyl MS-5 High Tack Kleb- und Dichtstoff schwarz 290 ml",
          "sku": "6252434",
          "mpn": "62524 34",
          "color": "schwarz",
          "brand": {
            "@type": "Brand",
            "name": "DEKALIN"
          }
        },
        {
          "@type": "Product",
          "name": "DEKAsyl MS-5 High Tack Kleb- und Dichtstoff weiß 600 ml Schlauchbeutel",
          "mpn": "62523 12",
          "color": "weiß",
          "brand": {
            "@type": "Brand",
            "name": "DEKALIN"
          }
        }
      ],
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "EUR",
        "lowPrice": "17.99",
        "highPrice": "27.60",
        "offerCount": 2,
        "availability": "https://schema.org/InStock",
        "itemCondition": "https://schema.org/NewCondition"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Startseite",
          "item": "https://dekalin.de/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Ratgeber",
          "item": "https://dekalin.de/ratgeber/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Solarpanel kleben ohne Bohren",
          "item": "https://dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/"
        }
      ]
    }
  ]
}
```

**Hinweise zum Markup**

| Punkt | Entscheidung |
|---|---|
| **Offers** | `AggregateOffer` über Händlerangebote (Fritz Berger 17,99 €, Reimo 27,60 €; MS-5 weiß 290 ml, Stichprobe 01.11.2026) – zulässig für ein Produkt, das von mehreren Verkäufern angeboten wird. **Nie wieder „0.00“.** Preise monatlich aktualisieren oder durch UVP ersetzen [Lücke: UVP fehlt]. Im Shopify-Shop stattdessen ein `Offer` mit eigenem Preis (Variante B). |
| `aggregateRating` | **bewusst weggelassen**: Die 4,96/5 aus 52 Bewertungen gehören Fritz Berger und dürfen nicht übernommen werden. Erst mit eigenen Shop-Bewertungen ergänzen. |
| `gtin13` | 4046085125227 nur für weiß 290 ml bekannt (über Fritz Berger); GTINs für schwarz und 600 ml beim Kunden anfordern. |
| `manufacturer` | DINOL GmbH laut Datenblatt („a brand of DINOL“); Herausgeber der Seite DEKA Kleben & Dichten GmbH. Rollen nach M4-Entscheidung finalisieren. |
| Varianten | über `isSimilarTo`; nach Shop-Relaunch als `ProductGroup` mit `hasVariant` + `variesBy` (color, size). |
| `additionalProperty` | alle Datenblattwerte mit UN/CEFACT-Codes (CEL °C, MIN Minute, MMT Millimeter, MPA Megapascal, PAL Pascal, P1 Prozent, MON Monat); „Überlackierbar“ und „UV-beständig“ als Boolean – genau die Attribute aus Prompt P6. |
| HowTo / FAQ Rich Results | Google zeigt beide nur noch eingeschränkt an; das Markup wird trotzdem maschinell gelesen und schadet nicht. |
| Platzhalter | Bild-URLs, Logo-URL, Produkt-Slugs, Datum, Autor – siehe Abschnitt 8. |

**Variante B – Offer im Shopify-Produkt-Template (`main-product.liquid`)**

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": {{ product.title | json }},
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  "gtin13": {{ product.selected_or_first_available_variant.barcode | json }},
  "brand": { "@type": "Brand", "name": "DEKALIN" },
  "offers": {
    "@type": "Offer",
    "url": {{ shop.url | append: product.url | json }},
    "price": {{ product.selected_or_first_available_variant.price | divided_by: 100.0 | json }},
    "priceCurrency": {{ cart.currency.iso_code | json }},
    "availability": "https://schema.org/{% if product.selected_or_first_available_variant.available %}InStock{% else %}OutOfStock{% endif %}",
    "itemCondition": "https://schema.org/NewCondition",
    "seller": { "@type": "Organization", "name": "DEKALIN" }
  },
  "additionalProperty": {{ product.metafields.custom.schema_properties.value | json }}
}
</script>
```
(`schema_properties` = JSON-Metafeld mit der `additionalProperty`-Liste aus Abschnitt 6; Versand- und Rückgabeangaben `shippingDetails` / `hasMerchantReturnPolicy` ergänzen, sobald Konditionen feststehen.)

---

## 7. Umsetzungscheckliste

### WordPress (dekalin.de, heute: WordPress + WooCommerce + Yoast + WPBakery)

- [ ] Seite unter `/ratgeber/` anlegen, Slug `solarpanel-wohnmobil-kleben-ohne-bohren`, genau eine H1
- [ ] Text aus Abschnitt 4 übernehmen; Tabellen als echte HTML-Tabellen (nicht als Bild, nicht nur im Slider/Akkordeon per JavaScript)
- [ ] FAQ-Antworten **sichtbar** ausgeben (Akkordeon nur, wenn der Text im Roh-HTML steht – per `curl` prüfen), Anker `#faq`, `#schritt-1` … setzen
- [ ] Yoast: Title und Description aus Abschnitt 2; Schema-Typ „Artikel“; Yoast-eigenes FAQ-/HowTo-Block-Schema **nicht** zusätzlich nutzen (sonst doppelte FAQPage)
- [ ] JSON-LD aus Abschnitt 6 per „Custom HTML“-Block bzw. Header-Code-Plugin nur auf dieser URL einbinden; Platzhalter ersetzen
- [ ] 301 `/solar/` → neue URL (Yoast Premium Redirects oder Plugin „Redirection“); interne Links auf `/solar/` direkt umstellen
- [ ] Video „Solarplattenhalterung“ einbinden + Transkript; Bilder mit Alt-Text-Template, WebP, < 200 KB
- [ ] Interne Links laut Abschnitt 5 setzen (eingehend und ausgehend)
- [ ] Produktseiten MS-5: Product-Schema mit Preis „0.00“ deaktivieren bzw. korrigieren (WooCommerce-Schema über Yoast WooCommerce SEO oder Filter `woocommerce_structured_data_product` anpassen) – sonst widerspricht das Produkt-Markup dieser Seite
- [ ] Meta-Description MS-5 „Dauererlastisch“ und Titles mit „Deklain“ korrigieren
- [ ] Sitemap prüfen (Seite enthalten, `/solar/` raus); robots.txt unverändert offen für OAI-SearchBot, ChatGPT-User, PerplexityBot, Bingbot, Google-Extended

### Shopify (nach Relaunch, Vision Theme)

- [ ] Blog „Ratgeber“ anlegen, Beitrag mit Handle `solarpanel-wohnmobil-kleben-ohne-bohren`; alternativ Seite mit eigenem Template `page.ratgeber.json`
- [ ] SEO-Felder (Title, Description, Handle) aus Abschnitt 2
- [ ] JSON-LD über Custom-Liquid-Abschnitt oder Metafeld `article.metafields.custom.json_ld` ausgeben; vom Theme erzeugtes Article-Schema prüfen und Dopplungen entfernen
- [ ] Produkt-Schema über Variante B; Barcode-Feld = GTIN; Metafelder für technische Daten (gleiche Werte speisen Tabelle, Filter in Search & Discovery und Schema)
- [ ] URL-Weiterleitung `/solar` → neuer Pfad (Online Store › Navigation › URL-Weiterleitungen)
- [ ] Google & YouTube App: Merchant Center verbinden (kostenlose Produkteinträge)
- [ ] Produktseite MS-5: Block „Anleitung: Solarpanel kleben“ mit Link; Upsell DEKACLEAN, DEKAVATOR, DEKAFINISHER, Flexsolar-Set

### Abnahme und Messung (beide Systeme)

- [ ] Rich Results Test + Schema Markup Validator: 0 Fehler
- [ ] GSC: URL-Prüfung, Indexierung beantragen; Bing Webmaster Tools: URL einreichen bzw. IndexNow
- [ ] Roh-HTML-Check (`curl`): Kurzantwort, Tabellen und FAQ ohne JavaScript lesbar
- [ ] Fachfreigabe Anwendungstechnik + rechtliche Prüfung Vergleich Sikaflex-554
- [ ] Re-Test P10 (und P2, P3, P6) in Perplexity und ChatGPT nach 2, 6 und 12 Wochen, 3 Läufe je Prompt; KPI aus M1 dokumentieren
- [ ] Inhalte an Händler und Solar-Partner weitergeben (M5): Kurzantwort, Schritte, Tabelle, Link

---

## 8. Offene Punkte und Annahmen (vor Livegang klären)

| # | Punkt | Status | Klären mit |
|---|---|---|---|
| A1 | Autor/Prüfer (Michael Windecker) und Veröffentlichungsdatum | [Annahme] | Dekalin Marketing |
| A2 | Ergiebigkeit (Rechenwert 38 ml/m, ~7 m je 290 ml) und „eine Kartusche für vier Spoiler“ | [Annahme] – Herstellerangabe fehlt | Anwendungstechnik |
| A3 | Prüfnachweis Fahrbelastung (TÜV/Windkanal) | [Lücke] – keine Angabe | Anwendungstechnik |
| A4 | Demontage von MS-5 | [Annahme] | Anwendungstechnik |
| A5 | Rolle von MS-1 im Flexsolar-Set (Abschluss-/Dichtnaht) | [Annahme] | Anwendungstechnik |
| A6 | Inhalt „Klebeset für SAT und starre Solaranlagen“ | [Lücke] | Produktmanagement |
| A7 | Silikon-Aussage, ABS als Haftungstest-Beispiel | [Annahme] | Anwendungstechnik |
| A8 | Bild-, Logo- und Produkt-URLs (`/bilder/…`, `/produkt/dekasyl-ms-5/`, `/produkt/dekaclean-ultra/` …) | Platzhalter – heute nummerische URLs | NETSHAKE/Web |
| A9 | GTINs schwarz 290 ml und weiß 600 ml, UVP | [Lücke] | Dekalin Vertrieb |
| A10 | Absender/Hersteller-Rollen DEKA vs. DINOL im Schema | abhängig von M4 | Geschäftsführung |
| A11 | Vergleich mit Sikaflex-554 (UWG § 6, Markenrecht) | rechtliche Prüfung | Rechtsabteilung |

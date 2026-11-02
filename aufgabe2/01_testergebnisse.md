# Aufgabe 2.1–2.2 – KI-Sichtbarkeitstest Dekalin: Methodik und Ergebnisse

Stand: 01.11.2026 · Rohdaten: `ki_tests/perplexity/P1–P10.md`, `ki_tests/chatgpt/P1–P10.md` (Antworttexte und Quellenlisten wörtlich gesichert)

---

## 1. Methodik

| Parameter | Festlegung |
|---|---|
| Testdatum | 01.11.2026 |
| Systeme | **Perplexity** (Standardmodell, Modus „Suche“) und **ChatGPT** (Standardmodell, Websuche automatisch) |
| Zustand | beide **ausgeloggt**, kein Verlauf, keine Memory, Standort DE, Sprache Deutsch |
| Session | **neue Unterhaltung je Prompt**, Prompt wörtlich wie unten, keine Nachfrage |
| Läufe | 1 Lauf je Prompt und System = **20 Antworten** (Baseline; Einschränkung siehe Abschnitt 6) |
| Prompt-Mix | 3 × Marke (P1–P3), 4 × Produkt/Problem ohne Marke (P4–P7), 3 × Empfehlung (P8–P10); Endkundensprache, Du-Form; Segmente Caravan (P1–P4, P8–P10), Material/Eigenschaft (P5, P6), Automotive (P7) |
| Sicherung | Antworttext wörtlich bzw. als wörtlicher Auszug, vollständige Quellenliste (Perplexity: URLs; ChatGPT: Zitat-Chips und Domains, ausgeloggt keine URL-Liste abrufbar) |

### Bewertungsraster je Antwort

| Kriterium | Ausprägung |
|---|---|
| Dekalin erscheint | ja/nein; **Position** = Rang unter den namentlich empfohlenen Marken/Produkten (1 = zuerst genannt) |
| Darstellung | Rolle/Etikett, das die KI vergibt („Meine Empfehlung“, „Caravan-Spezialist“ …), Tiefe (Produkte, Werte) |
| Quellen | Typ je zitierter URL: **Hersteller** (Dekalin / Sika / andere), **Händler** (inkl. Händler-Ratgeber, Marktplatz, bei Händlern gehostete Datenblätter), **Blog/Medien** (Ratgeberportale, Magazine, Podcasts), **Forum**, **Verzeichnis** |
| korrekt / vollständig | ✓ korrekt + vollständig · ◐ korrekt, aber lückenhaft · ⚠ verzerrt (Fakten stimmen, Einordnung falsch) · ✗ falsch |
| Wettbewerber | Sika und TEROSON: genannt ja/nein + Position |

Zählregel für Marken: Gezählt wird nur, wer **im Antworttext** genannt wird. Eine Marke, die nur als Quelle auftaucht (z. B. Sika in Perplexity P4), zählt nicht als Nennung, wird aber in der Spalte vermerkt.

---

## 2. Die 10 Prompts

| # | Typ | Prompt |
|---|---|---|
| P1 | Marke | Was ist Dekalin und welche Produkte gibt es für Wohnmobile? |
| P2 | Marke (Vergleich) | Dekalin oder Sikaflex – was ist besser zum Abdichten am Wohnmobil? |
| P3 | Marke/Produkt | Ist DEKAsyl MS 5 gut zum Kleben und Abdichten? |
| P4 | Produkt (Caravan) | Womit dichte ich eine Dachluke am Wohnmobil ab? |
| P5 | Produkt (Material) | Womit klebe ich Aluminium und Kunststoff dauerhaft und wetterfest? |
| P6 | Produkt (Eigenschaft) | Welcher MS-Polymer-Dichtstoff ist überlackierbar und UV-beständig? |
| P7 | Produkt (Automotive) | Womit dichte ich eine undichte Naht an der Karosserie meines Autos ab? |
| P8 | Empfehlung | Welcher ist der beste Dichtstoff für Wohnwagen und Wohnmobile? |
| P9 | Empfehlung (Profi) | Welche Marken für Kleb- und Dichtstoffe empfehlen Profis im Caravan- und Fahrzeugbau? |
| P10 | Empfehlung (Use Case) | Welchen Kleber nehme ich, um ein Solarpanel ohne Bohren aufs Wohnmobildach zu kleben? |

---

## 3. Ergebnis-Matrix (10 Prompts × 2 Systeme)

### 3.1 Perplexity

| # | Typ | Dekalin (Pos.) | Darstellung | Quellen (Typ) | korrekt / vollst. | Sika | TEROSON |
|---|---|---|---|---|---|---|---|
| P1 | Marke | **ja (1)** | Caravan-Marke; Dekaseal 8936/1512, Dekaclean, Dekavator; 2 Absätze | 9: Hersteller 1 (dekalin.de/branchen/caravaning), Händler 2, Blog/Medien 6 | ◐ korrekt; fehlen DEKAsyl/MS-Polymere, Herkunft, Industrie/Automotive | nein | nein |
| P2 | Marke | **ja (1)** | „Dekalin/Dekaseal besser für Fenster, Dachhauben“ = nur dauerplastische Dichtmasse; Sika = Kleben | 10: **Hersteller 1 (Sika-Caravan-FAQ)**, Blog 4, Forum 5; dekalin.de 0 | ⚠ DEKAsyl als Sikaflex-Alternative fehlt → Dekalin auf „nur Dichten“ reduziert | ja (2) | nein |
| P3 | Marke/Produkt | **ja (1)** | „hochhaftend“, Fenster, Luken, Solar, UV-beständig; 3 Sätze | 10: Händler 7 (Datenblatt von **reimo.com**, Fritz Berger 2, Obelink, Campingwagner, autark4ever, kleine Werft), Blog 3; dekalin.de 0 | ◐ korrekt, keine technischen Werte, keine Abgrenzung MS-1/MS-2 | nein | nein |
| P4 | Produkt | **ja (1 + 2)** | Dekaseal 1512 (sichtbare Naht) + 8936 (abtupfbar) namentlich empfohlen, Anleitung | 10: Hersteller 1 (che.sika.com, nur Primer), Blog 7 (amumot 3×), Forum 2; dekalin.de 0 | ✓ korrekt | nur Quelle | nein |
| P5 | Produkt | nein | – (empfohlen: 2K-Strukturacrylat, Epoxid; keine Marke) | 10: Hersteller 2 (Permabond), Händler 1, Blog/Portal 2, Forum 5 | – | nein | nein |
| P6 | Produkt | nein | – (empfohlen: **Ber-Fix** MS-Polymer, weil wlw-Text „überlackierbar“ + „UV-beständig“ wörtlich nennt) | 10: Verzeichnis 3 (wlw), Händler 5, Hersteller 1, Blog 1 | – (MS-5 erfüllt beides) | nein | nein |
| P7 | Produkt | nein | – (generisch „Karosserie-Nahtabdichtung“) | 10: Hersteller 2 (3M, Graco), Blog 2, Forum 6 | – | nein | nein |
| P8 | Empfehlung | **nein** | – (einzige Empfehlung: **SikaLastomer-514**) | 10: **Hersteller 3 (Sika-FAQ, che.sika, EGO)**, Händler 3, Blog 4 (davon 3 Dekalin-lastig) | – | **ja (1)** | nein |
| P9 | Empfehlung | **nein** | – (Sika, Bostik, EGO) | 10: **Hersteller 7 (Sika 4: 2 Profi-Broschüren-PDF, FAQ, Projektseite; Bostik, EGO, Axalta)**, Blog 2, Händler 1 | – | **ja (1)** | nein |
| P10 | Empfehlung | **nein** | – (Sikaflex 252i, 554, 522) | 10: Blog 5, Händler 4 (Solar-Händler, Montageanleitung PDF), Forum 1 | – | **ja (1–3)** | nein |

### 3.2 ChatGPT

| # | Typ | Dekalin (Pos.) | Darstellung | Quellen (Typ) | korrekt / vollst. | Sika | TEROSON |
|---|---|---|---|---|---|---|---|
| P1 | Marke | **ja (1)** | ausführlich: 4 Produktfamilien, 9 Produkte, Matrix „Anwendung → Produkt“, Bilder; MS-5 = High Tack für Solar | Hersteller 2 (dekalin.de, dekalin.com) | ✓ korrekt, weitgehend vollständig; keine technischen Werte | nein | nein |
| P2 | Marke | **ja (1)** | gleichwertig zu Sika; Tabelle je Bauteil; MS-5 als Sikaflex-Alternative | Hersteller 1 (dekalin.de) | ⚠ Faustregel „Dekalin = Dichten, Sika = Kleben“ unterschätzt DEKAsyl | ja (2) | nein |
| P3 | Marke/Produkt | **ja (1)** | „Gute Wahl“; −40/+120 °C, Hautbildung 12 min, 4 mm/24 h, überlackierbar, isocyanatfrei | Hersteller 1 (dekalin.com, Title „I High Tack …“) | ✓ korrekt + vollständig | nein | nein |
| P4 | Produkt | **ja (1 + 3)** | Dekaseal 8936 „Meine Empfehlung“, 1512 auf Platz 3 | keine (Modellwissen) | ✓ korrekt | ja (2) | nein |
| P5 | Produkt | nein | – (Kategorie **MS-Polymer** empfohlen, keine Marke) | Blog/Portal 1 (b2b.kleberkompass.de) | – | nein | nein |
| P6 | Produkt | nein | – (OMEGA UNI MS, WEICON Aqua-Flex, MARSTON MD-MS) | Shopping-Produktkarten mit Datenblatt-Links (Domains nicht ausgewiesen) | – (MS-5 erfüllt beides) | nein | nein |
| P7 | Produkt | nein | – | keine (Modellwissen) | – | **ja (1)** Sikaflex 221 | **ja (2)** MS 9320 SF |
| P8 | Empfehlung | **ja (2)** | Dekaseal 8936 „Beste Wahl für Fenster und Luken“; belegt über Händler campingmarkt.com | Hersteller 1 (deu.sika.com), Händler 2 (campingmarkt.com, padabo.de) | ✓ korrekt; MS-5 fehlt (Solar → Sikaflex 554) | **ja (1, 3, 4)** | nein |
| P9 | Empfehlung | **ja (2)** | „Caravan-Spezialist“, „erste Wahl für Caravan-Abdichtung“ | Hersteller 1 (deu.sika.com, Chip); dekalin.de nur als Produktlink | ◐ korrekt, aber auf Caravan verengt (Fahrzeugbau/Industrie fehlt) | **ja (1)** „Top-Empfehlung“ | ja (3) |
| P10 | Empfehlung | **ja (2)** | Dekasyl MS-5 generisch („gute Haftung“), ohne Vorteile | Hersteller 1 (deu.sika.com) | ◐ korrekt, aber ohne Belege (High Tack, Temperatur, Set) | **ja (1, 3)** Sikaflex 554 „Meine Empfehlung“ | nein |

---

## 4. Kennzahlen (exakt aus den Rohdaten)

### 4.1 Sichtbarkeitsquote (Anteil Antworten mit Nennung im Antworttext)

| Marke | Perplexity | ChatGPT | Gesamt (20) | **ohne Markenprompts P4–P10 (14)** |
|---|---|---|---|---|
| **Dekalin** | 4/10 = **40 %** | 7/10 = **70 %** | 11/20 = 55 % | **5/14 = 35,7 %** |
| Sika | 4/10 = 40 % | 6/10 = 60 % | 10/20 = 50 % | **8/14 = 57,1 %** |
| TEROSON | 0/10 = 0 % | 2/10 = 20 % | 2/20 = 10 % | 2/14 = 14,3 % |

**Nach Prompt-Typ (beide Systeme):**

| Typ | Läufe | Dekalin | Sika | TEROSON |
|---|---|---|---|---|
| Marke P1–P3 | 6 | 6/6 = 100 % | 2/6 = 33 % (nur P2, im Prompt genannt) | 0 % |
| Produkt P4–P7 | 8 | 2/8 = 25 % (nur P4) | 2/8 = 25 % | 1/8 = 12,5 % |
| Empfehlung P8–P10 | 6 | **3/6 = 50 %** (Perplexity 0/3, ChatGPT 3/3) | **6/6 = 100 %** | 1/6 = 16,7 % |

**Position (P4–P10):** Dekalin Ø Rang 1,6 (5 Antworten), davon 2 × Platz 1 (beide P4). Sika Ø Rang 1,1 (8 Antworten), davon **7 × Platz 1**.

### 4.2 Share of Voice (Produkt-/Markennennungen in Empfehlungen, Nicht-Markenprompts P4–P10)

Gezählt wird jede namentlich empfohlene Produkt- oder Markenposition (z. B. Sikaflex 554 und Sikaflex 252 in einer Antwort = 2).

| Marke | Perplexity | ChatGPT | **Gesamt** |
|---|---|---|---|
| Dekalin | 2/10 = 20,0 % | 5/21 = 23,8 % | **7/31 = 22,6 %** |
| Sika | 5/10 = 50,0 % | 8/21 = 38,1 % | **13/31 = 41,9 %** |
| TEROSON | 0/10 = 0 % | 2/21 = 9,5 % | **2/31 = 6,5 %** |
| andere (Ber-Fix, Bostik, EGO, OMEGA, WEICON, MARSTON, Würth 2×, 3M) | 3/10 | 6/21 | 9/31 = 29,0 % |

Einzelbeleg wichtigste Empfehlungsfrage (ChatGPT P8): Sika 3 von 4 Plätzen = 75 %, Dekalin 1 von 4 = 25 %.

### 4.3 Quellen

**Perplexity – 99 zitierte URLs nach Typ:**

| Typ | Anzahl | Anteil |
|---|---|---|
| **Hersteller gesamt** | 18 | **18,2 %** |
| – davon Sika (deu./che.sika.com) | 8 | 8,1 % |
| – davon **Dekalin (dekalin.de/.com)** | **1** | **1,0 %** |
| – davon andere (Permabond 2, EGO 2, 3M, Graco, Bostik, Axalta, Kingdeli) | 9 | 9,1 % |
| Händler (inkl. Händler-Ratgeber, Amazon, Datenblatt auf reimo.com) | 23 | 23,2 % |
| Blog/Medien/Ratgeberportale | 36 | 36,4 % |
| Foren | 19 | 19,2 % |
| B2B-Verzeichnis (wlw) | 3 | 3,0 % |

**ChatGPT – 10 ausgewiesene Quell-Domains in 7 Antworten** (P4, P7 ohne Websuche; P6 nur Shopping-Karten ohne Domain):

| Typ | Anzahl | Anteil |
|---|---|---|
| **Hersteller gesamt** | 7 | **70 %** |
| – davon Dekalin (dekalin.de 2, dekalin.com 2) | 4 | 40 % – **nur in Markenprompts P1–P3** |
| – davon Sika (deu.sika.com) | 3 | 30 % – in P8, P9, P10 (Empfehlung) |
| Händler (campingmarkt.com, padabo.de) | 2 | 20 % |
| Blog/Portal (kleberkompass) | 1 | 10 % |

**Citation Share (Antworten, die die eigene Domain als Quelle nutzen):**

| | Perplexity | ChatGPT | Gesamt | davon Nicht-Markenprompts |
|---|---|---|---|---|
| Dekalin-Domain | 1/10 (P1) | 3/10 (P1–P3) | **4/20 = 20 %** | **0/14 = 0 %** |
| Sika-Domain | 4/10 (P2, P4, P8, P9) | 3/10 (P8–P10) | **7/20 = 35 %** | 6/14 = 42,9 % |
| TEROSON/Henkel-Domain | 0 | 0 | 0 % | 0 % |

### 4.4 Korrektheit der Dekalin-Darstellung (11 Nennungen)

| Bewertung | Anzahl | Fälle |
|---|---|---|
| ✓ korrekt + vollständig | 5 | Perplexity P4; ChatGPT P1, P3, P4, P8 |
| ◐ korrekt, lückenhaft | 4 | Perplexity P1, P3; ChatGPT P9, P10 |
| ⚠ verzerrt | 2 | P2 in beiden Systemen („Dekalin = nur Dichten“) |
| ✗ falsch | 0 | – |

---

## 5. Kernerkenntnisse

1. **Dekalin gewinnt nur, wenn der Name schon im Prompt steht.** Markenprompts 6/6, Nicht-Markenprompts 5/14 (35,7 %) gegenüber Sika 8/14 (57,1 %). In Empfehlungsfragen liegt Sika bei 100 %, Dekalin bei 50 % – und in Perplexity bei 0/3.
2. **dekalin.de wird bei Nicht-Markenfragen nie zitiert (0/14).** Perplexity nutzt dekalin.de in 99 Quellen genau einmal; sogar das MS-5-Datenblatt kommt von reimo.com (P3). Händler und Blogs „besitzen“ die Produktinformation.
3. **Sika gewinnt mit zitierfähigen Antwortseiten, nicht mit mehr Produkten.** Die Sika-Caravan-FAQ ist in P2 und P8 die Primärquelle; zwei Profi-Broschüren-PDF tragen P9. In Perplexity P8 sind 4 von 10 Quellen Dekalin-lastig – genannt wird trotzdem nur SikaLastomer-514, weil allein Sika die Frage auf einer Seite direkt beantwortet.
4. **Dekalin wird auf „Dichten“ reduziert.** Die Stärke Butyl/Dekaseal (8936, 1512) ist gelernt; DEKAsyl MS-5 als Konstruktionskleber erscheint in Nicht-Markenprompts nur einmal (ChatGPT P10, Platz 2, ohne Begründung). Der kaufstarke Use Case Solarpanel geht an Sikaflex 554/252.
5. **Eigenschafts- und Materialfragen gewinnt, wer Attribute wörtlich und maschinenlesbar veröffentlicht** (P5, P6): Ber-Fix über einen wlw-Text, WEICON/OMEGA/MARSTON über Shopping-Karten mit Datenblatt. MS-5 erfüllt beide P6-Kriterien, dekalin.de liefert aber Product-Schema mit Preis 0,00 € ohne Marke und ohne technische Attribute.
6. **Automotive und Profi-/Industrie sind für Dekalin weiße Flecken** (P7, P9): Dort sind Sika und TEROSON die gelernten Marken; Dekalin gilt bestenfalls als „Caravan-Spezialist“.
7. **Wenn die KI die Herstellerseite findet, ist die Darstellung exzellent** (ChatGPT P3: alle Kennwerte korrekt). Der Hebel ist also nicht neue Produktkompetenz, sondern Auffindbarkeit und Zitierfähigkeit der vorhandenen Inhalte.

## 6. Was hat überrascht?

| Beobachtung | Warum überraschend |
|---|---|
| **ChatGPT zeigt Dekalin häufiger als Perplexity (70 % vs. 40 %)** | Erwartet war das Gegenteil (Perplexity durchsucht das Live-Web, wo Dekalin im Fachhandel präsent ist). ChatGPT empfiehlt Dekaseal 8936 bei P4 sogar ohne Websuche auf Platz 1 – die Community-Verankerung steckt im Modellwissen. Perplexity dagegen baut auf der Seite, die die Frage am direktesten beantwortet – und das ist fast nie dekalin.de. |
| **Die Sika-FAQ wird zitiert, obwohl sie kein FAQPage-Schema hat** – die Dekalin-FAQ hat Schema und wird nicht zitiert | Markup allein entscheidet nicht. Entscheidend sind Frage-Antwort-Struktur, direkte Antwort und Domain-Autorität. Die Dekalin-FAQ enthält zudem Platzhalter („FAQ Titel“, Lorem Ipsum) und 8 Dubletten. |
| **Ein Nischenanbieter (Ber-Fix) schlägt alle Markenhersteller bei P6** | Allein, weil sein Verzeichniseintrag die beiden gesuchten Eigenschaften wörtlich nennt. Größe der Marke ist bei Eigenschaftsfragen irrelevant. |
| **TEROSON (Henkel-Konzern) ist praktisch unsichtbar (2/20, nie als Quelle)** | Konzernreichweite ersetzt keine Endkunden-Antwortinhalte. TEROSON erscheint nur im Modellwissen bei Kfz-Fragen. |
| **Dekalin hat die passenden Seiten bereits** – `dekalin.de/solar/` (Solaranleitung mit MS-5) und `/ratgeber/dichtstoff-fuer-wohnwagen-wohnmobil/` (exakt P8) | Keine wird zitiert. Die P8-Seite trägt laut Recherche den falschen Title „Unterbodenschutz Wohnmobil“. Die Lücke ist Struktur und Technik, nicht fehlendes Wissen. |

**Einschränkungen:** ein Lauf je Prompt (KI-Antworten streuen), ChatGPT ausgeloggt ohne vollständige URL-Listen, keine Google AI Overviews getestet. Empfehlung: monatliche Wiederholung mit 3 Läufen je Prompt in einem Tracking-Tool (z. B. Finseo.ai), Werte oben als Baseline.

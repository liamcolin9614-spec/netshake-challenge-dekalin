# Aufgabe 2.4 – Maßnahmenplan KI-Sichtbarkeit Dekalin (5 Maßnahmen)

Stand: 01.11.2026 · Grundlage: Lückenliste L1–L11 (`02_wettbewerbsvergleich.md`), Baseline-Kennzahlen (`01_testergebnisse.md`)

## 1. Priorisierung: Impact/Aufwand-Matrix

Skala 1–5. **Impact** = erwarteter Effekt auf Nennung und Zitierung in den 10 Test-Prompts (Anzahl betroffener Prompts × Hebelstärke). **Aufwand** = interne Stunden, Abstimmungsbedarf (DEKA/DINOL, Anwendungstechnik, Händler), Abhängigkeiten. **Score** = Impact ÷ Aufwand.

| # | Maßnahme | Typ | Schließt Lücken | Betroffene Prompts | Impact | Aufwand | **Score** | Rang |
|---|---|---|---|---|---|---|---|---|
| **M1** | Antwortseiten für kaufstarke Use Cases (Pilot: Solarpanel ohne Bohren) | Inhalt + Schema | L1, L4, L5 | P2, P5, P8, P10 (+P3) | 5 | 2 | **2,5** | **1** |
| **M3** | Produktdaten maschinenlesbar + SEO-Hygiene | Produktdaten + Technik | L3, L11 | P3, P6, P8 (+P5) | 4 | 2 | **2,0** | **2** |
| **M2** | Caravan-FAQ-Hub als Gegenstück zur Sika-FAQ | Inhalt + Schema | L2, L4 | P2, P4, P8 | 4 | 2 | **2,0** | **3** |
| **M4** | Eine Marke, eine Quelle + Profi-Autorität | Technik/Entität + Inhalt | L8, L9, L10 | P1, P7, P9 | 4 | 3 | **1,3** | **4** |
| **M5** | Drittquellen-Programm (Händler, Solar-Partner, Community) | Off-Page | L6, L7, L10 | P3, P8, P9, P10 | 5 | 4 | **1,25** | **5** |

```
Impact
  5 |        M1                      M5
  4 |        M3 M2          M4
  3 |
  2 |
  1 |
    +----------------------------------------
        1     2      3      4      5   Aufwand
```

**Reihenfolge:** M1 → M3 → M2 → M4 → M5. Begründung: M1 und M3 nutzen vorhandene Inhalte (Solaranleitung, Datenblatt) und sind ohne Abstimmung mit Dritten umsetzbar; M2 baut auf denselben Antwortbausteinen auf. M4 braucht eine Entscheidung DEKA/DINOL, M5 externe Partner – beide haben den längsten Vorlauf und starten deshalb parallel mit der Vorbereitung ab Woche 3, wirken aber erst nach M1–M3 (die Drittquellen brauchen eine Herstellerseite, auf die sie verlinken können).

---

## 2. Die Maßnahmen im Detail

### M1 – Antwortseiten für kaufstarke Use Cases (Pilot: Solarpanel ohne Bohren)

| | |
|---|---|
| **Was wird umgesetzt?** | Je Use Case eine Antwortseite nach festem Bauplan: H1 = Nutzerfrage; die ersten 2 Sätze beantworten sie direkt mit Produktnamen; Materialliste; Schritt-für-Schritt mit Zeiten und Temperaturen aus dem Datenblatt; Vergleichstabelle (MS-1/MS-2/MS-5, ehrlich auch gegen Gattung und Sikaflex-554); 8–12 FAQ; Autor/Prüfer + Datum; JSON-LD Article + HowTo + FAQPage + Product. **Pilot: Solarpanel** (ersetzt `dekalin.de/solar/` per 301), danach SAT-Anlage, Markise/Dachträger, „Aluminium mit Kunststoff/GFK kleben“. |
| **Warum relevant für KI?** | Perplexity und ChatGPT Search zitieren kurze, eigenständige Passagen (Antwortsatz, Liste, Tabelle, FAQ). Sika gewinnt P10 mit genau solchen Seiten Dritter; `/solar/` existiert, ist aber nicht als Antwort strukturiert und wird nie zitiert. Die Tabelle „MS-5 vs. Sikaflex-554“ schließt die Begründungslücke aus P10 und die Verzerrung aus P2. |
| **Erwartetes Ergebnis** | Dekalin in P10 in beiden Systemen genannt, MS-5 mit Begründung (High Tack, +120 °C, Set); dekalin.de als zitierte Quelle in P10; MS-5 in P2/P8 als Klebe-Alternative statt „nur Dichten“. |
| **KPI (Baseline → Ziel nach 90 Tagen)** [Zielwerte = Annahme] | P10 genannt: 1/2 → 2/2 · dekalin.de zitiert in P10: 0/2 → ≥ 1/2 · Google-Ranking „solarpanel wohnmobil kleben“: Top 10 · Klicks auf MS-5-Händlerlinks (Event) |
| **Verantwortlich / Zeit** | NETSHAKE (Content, SEO, Schema) · Dekalin-Anwendungstechnik (Fachfreigabe, offene Werte) · Woche 1–3 Pilot, ab Woche 4 je Use Case 1 Seite/Woche |

### M3 – Produktdaten maschinenlesbar + SEO-Hygiene

| | |
|---|---|
| **Was wird umgesetzt?** | (a) Product-Schema korrigieren: Preis 0,00 € und „InStock“ entfernen bzw. durch echte Offers ersetzen (Shopify-Preis oder AggregateOffer der Händler), `brand` DEKALIN, `manufacturer`, `gtin13`, `mpn`, `color`, **`additionalProperty` mit allen Kennwerten** (Shore A 55, −40/+120 °C, Hautbildung 12 min …) und Eigenschafts-Booleans („überlackierbar“, „UV-beständig“, „primerlos auf …“). (b) Kennwerte als **HTML-Tabelle** auf jeder Produktseite statt nur PDF; Eigenschaften wörtlich im Text. (c) Google Merchant Center/Organic Shopping mit vollständigem Feed. (d) Hygiene: „Deklain“, „Dauererlastisch“, falsche Titles (P8-Ratgeber „Unterbodenschutz“), Duplicate `/ratgeber/`, sprechende URLs `/produkt/dekasyl-ms-5/` mit 301, robots/Sitemap-Widerspruch `/produkte/reinigen/`. |
| **Warum relevant für KI?** | P6 zeigt: Eigenschaftsfragen gewinnt, wer Attribute wörtlich und strukturiert veröffentlicht (Ber-Fix, WEICON). Shopping-Karten in ChatGPT speisen sich aus Produktfeeds/Datenblättern. Falsche Preise und fehlende Marke senken Vertrauen und verhindern Rich Results. Der falsche Title verhindert, dass die exakt passende P8-Seite rankt. |
| **Erwartetes Ergebnis** | MS-5 in P6 genannt; Kennwerte in Perplexity-P3-Antwort aus dekalin.de statt reimo.com; P8-Ratgeber rankt für „Dichtstoff Wohnwagen“. |
| **KPI** | P6 genannt: 0/2 → ≥ 1/2 · Rich-Results-Test grün auf 31 Produkt-URLs · dekalin.de unter Perplexity-Quellen P3: 0 → ≥ 1 · GSC-Impressions „ms polymer überlackierbar“ |
| **Verantwortlich / Zeit** | NETSHAKE (Technik, Schema-Template, Feed) · Dekalin (GTINs, UVP, Freigabe) · Woche 2–5 |

### M2 – Caravan-FAQ-Hub als Gegenstück zur Sika-FAQ

| | |
|---|---|
| **Was wird umgesetzt?** | Bestehende FAQ (`/faq/`) bereinigen (Lorem Ipsum, „FAQ Titel“, 8 Dubletten raus) und zu einem Hub „Kleben & Dichten am Wohnmobil – 40 Antworten“ ausbauen, gegliedert nach Bauteil (Fenster/Dachluke, Dach/Solar/SAT, Außennähte, Unterboden, Innenraum) und Grundfragen (dauerplastisch vs. elastisch, Butyl vs. MS-Polymer vs. Silikon, wiederlösbar, primerlos, Entfernen, Haftung auf Altresten, Überlackieren, Ergiebigkeit, Lagerung nach Öffnen). Jede Antwort: 2 Sätze direkt + Produktlink + Link zur Antwortseite (M1). Eine Frage je Anker-URL (`#solarpanel-kleben`). FAQPage-Schema nur mit echten Inhalten. |
| **Warum relevant für KI?** | Die Sika-FAQ ist in Perplexity P2 und P8 Primärquelle – ohne Schema, allein durch direkte Antworten auf einer URL. Ein gleichwertiger Dekalin-Hub konkurriert um genau diese Zitierposition und korrigiert „Dekalin = nur Dichten“. |
| **Erwartetes Ergebnis** | Dekalin in Perplexity P8 genannt, dekalin.de neben/anstelle sika.com zitiert; P2 ohne Verzerrung. |
| **KPI** | P8 Perplexity genannt: 0 → 1 · Citation Share dekalin.de in Nicht-Markenprompts: 0/14 → ≥ 3/14 · P2 bewertet ✓ statt ⚠ |
| **Verantwortlich / Zeit** | NETSHAKE (Struktur, Texte) · Dekalin-Support (Fragen aus DEKABot-Auswertung und E-Mail-Support) · Woche 4–7 |

### M4 – Eine Marke, eine Quelle + Profi-Autorität

| | |
|---|---|
| **Was wird umgesetzt?** | (a) Entität: Organization-Schema auf dekalin.de und dekalin.com mit identischem Namen „DEKALIN“, `parentOrganization` DINOL GmbH, Rolle DEKA (Vertrieb DE) eindeutig, `sameAs` (YouTube, Instagram, Facebook, Wikidata); eine Adresse; einheitliche Schreibweise „DEKAsyl MS-5“ überall; Wikidata-Eintrag „DEKALIN (Marke)“ + Begriffsklärung gegen „Decalin“; llms.txt; Bing Webmaster Tools + IndexNow. (b) Profi-Autorität: Branchenseite „Fahrzeug- und Caravanbau“ mit Fakten statt Slogan-H1 (seit 1907, Automobilbau seit 1935, Schulungen DIN 2304/DVS-EWF, Referenzen und Freigaben [beim Kunden klären]); Profi-Broschüre als HTML + PDF; Automotive-Antwortseite „Karosserienaht abdichten“ (nach Sortimentsprüfung). |
| **Warum relevant für KI?** | Zwei Absender, drei Ortsangaben und Wikipedia = Chemikalie erschweren die Zuordnung. P9 zeigt: Profi-Fragen werden mit Branchenseiten und Broschüren-PDF (Sika 4×, Bostik, EGO) beantwortet; Dekalin hat keine zitierfähige Profi-Quelle. |
| **Erwartetes Ergebnis** | Perplexity P9 nennt Dekalin; ChatGPT ordnet Dekalin als „Caravan- und Fahrzeugbau“ statt nur „Caravan-Spezialist“ ein; korrekte Herkunft in P1. |
| **KPI** | P9 genannt: 1/2 → 2/2 · P1 vollständig (Herkunft, DEKAsyl, Industrie) · P7 genannt: 0/2 → ≥ 1/2 (12 Monate) |
| **Verantwortlich / Zeit** | Dekalin-Geschäftsführung DEKA + DINOL (Grundsatzentscheidung Domains/Absender) · NETSHAKE (Schema, Wikidata, Seiten) · Entscheidung Woche 3, Umsetzung Woche 6–12 |

### M5 – Drittquellen-Programm

| | |
|---|---|
| **Was wird umgesetzt?** | (a) **Händler-Content-Paket** für Fritz Berger, Reimo, Obelink, Campingwagner, Movera: einheitliche Produkttexte, Kennwerttabelle, FAQ, Bilder, korrekte Schreibweise; Vorschlag eines Anwendungs-Kategorietextes für Reimo („Welcher Kleber fürs Solarmodul?“) analog zum Sika-Text. (b) **Solar-Partner**: Montageanleitungen mit MS-5 und Flexsolarmodul-Klebeset für Offgridtec, Fraron, Solarkontor (Co-Branding, Link auf M1-Seite). (c) **Medien und Community**: Vergleichs-/Listicle-Seiten aus den Test-Quellen (planmycamper, camper.help, camperstyle, PiNCAMP) mit Fakten und Testmustern versorgen; offizieller Experten-Account in wohnmobilforum.de, motor-talk, ducatoforum; 3 YouTube-Kooperationen mit Camper-DIY-Kanälen; Amazon-Präsenz prüfen. |
| **Warum relevant für KI?** | 79 % der Perplexity-Quellen sind Händler, Blogs und Foren (78/99). Empfehlungen entstehen aus Drittquellen-Konsens; in P10 nennen alle 4 Solar-Händlerquellen Sika. Modellwissen (ChatGPT P4, P7) speist sich aus genau diesen Erwähnungen. |
| **Erwartetes Ergebnis** | Dekalin in Empfehlungs-Antworten beider Systeme; mittelfristig Gleichstand mit Sika im Modellwissen. |
| **KPI** | Sichtbarkeit Empfehlungsprompts: 3/6 → ≥ 5/6 · Share of Voice P4–P10: 22,6 % → ≥ 35 % · Anzahl Drittseiten in den Testquellen, die Dekalin nennen |
| **Verantwortlich / Zeit** | Dekalin-Vertrieb/Key Account (Händler, Solar-Partner) · NETSHAKE (Paket, Outreach-Liste, Briefings) · Start Woche 3, laufend; Wirkung 3–6 Monate |

---

## 3. Fahrplan und Messung

| Woche | 1–2 | 3 | 4–5 | 6–7 | 8–12 | ab 13 |
|---|---|---|---|---|---|---|
| M1 | Pilot Solar: Text, Freigabe, Schema | Livegang + 301 | SAT, Markise | Alu/GFK kleben | weitere Use Cases | |
| M3 | | Schema-Template, Hygiene | Kennwert-Tabellen, Merchant Feed | | | |
| M2 | | | FAQ bereinigen | Hub live | | |
| M4 | | Entscheidung DEKA/DINOL | | Organization, Wikidata | Branchenseite, Broschüre HTML | |
| M5 | | Content-Paket, Outreach-Liste | Händler/Solar-Partner | Community/YouTube | laufend | laufend |
| Messung | **Baseline 01.11.** | | | Zwischentest | **Re-Test 90 Tage** | monatlich |

**Messprotokoll:** dieselben 10 Prompts, beide Systeme, ausgeloggt, 3 Läufe je Prompt (60 Antworten), ergänzend Google AI Overviews; Tracking-Tool (Finseo.ai, 25 Prompts im Starter-Plan) für die monatliche Wiederholung.

| Kern-KPI | Baseline 01.11.2026 | Ziel nach 90 Tagen [Annahme] |
|---|---|---|
| Sichtbarkeit Dekalin, Nicht-Markenprompts | 5/14 = 35,7 % | ≥ 8/14 = 57 % (Sika-Niveau) |
| Sichtbarkeit Empfehlungsprompts Perplexity | 0/3 | ≥ 2/3 |
| Share of Voice Produktnennungen P4–P10 | 22,6 % | ≥ 35 % |
| Citation Share dekalin.de, Nicht-Markenprompts | 0/14 | ≥ 4/14 |
| Anteil dekalin.de an Perplexity-Quellen | 1/99 = 1,0 % | ≥ 5 % |
| Korrektheit Dekalin-Darstellung (✓-Anteil) | 5/11 = 45 % | ≥ 80 % |

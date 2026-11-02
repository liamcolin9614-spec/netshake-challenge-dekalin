# Aufgabe 2.3 – Wettbewerbsvergleich: Dekalin vs. Sika vs. TEROSON

Stand: 01.11.2026 · Basis: 20 KI-Antworten (`01_testergebnisse.md`) + Website-, Schema- und Handelsrecherche (`recherche/dekalin_recherche.md`, Abschnitte 1, 3, 4)

## 1. Auswahl der Wettbewerber

| Wettbewerber | Warum direkt vergleichbar |
|---|---|
| **Sika** (Sikaflex, SikaLastomer) | Im Caravan-Fachhandel gleich stark wie Dekalin (Fritz Berger: Sika 27 / Dekalin 26 Artikel). Produkte fast 1:1 austauschbar: Sikaflex-554 ↔ **DEKAsyl MS-5**, Sikaflex-522 ↔ MS-2/MS-6, SikaLastomer-514 ↔ DEKASEAL 8936. ADAC-PiNCAMP nennt beide „Marktführer“. Benchmark für Sichtbarkeit. |
| **TEROSON** (Henkel) | Gleiches Regal (Fritz Berger 17 Artikel; Reimo führt Terostat/MS 9221), gleiche Technologien (MS-Polymer, Butyl), gleiche Kfz-Werkstatt-Herkunft wie Dekalin. Zeigt, dass Konzerngröße ohne Antwortinhalte nicht sichtbar macht. |

---

## 2. Wer erscheint häufiger?

| Kennzahl | Dekalin | Sika | TEROSON |
|---|---|---|---|
| Sichtbarkeit gesamt (20 Antworten) | 11 = 55 % | 10 = 50 % | 2 = 10 % |
| **Sichtbarkeit ohne Markenprompts (P4–P10, 14)** | **5 = 35,7 %** | **8 = 57,1 %** | 2 = 14,3 % |
| Empfehlungsprompts P8–P10 (6) | 3 = 50 % | **6 = 100 %** | 1 = 16,7 % |
| – davon Perplexity (3) | **0** | 3 | 0 |
| Platz 1 in Nicht-Markenprompts | 2 × (beide P4) | **7 ×** | 0 × |
| Ø Rang, wenn genannt (P4–P10) | 1,6 | 1,1 | 2,5 |
| Share of Voice Produktnennungen (P4–P10, 31) | 22,6 % | **41,9 %** | 6,5 % |
| Antworten mit eigener Domain als Quelle | 4/20 – **nur Markenprompts** | **7/20 – davon 6 Nicht-Marken** | 0/20 |
| Anteil an 99 Perplexity-Quellen | 1 (1,0 %) | 8 (8,1 %) | 0 |

**Befund:** Gesamtzahlen täuschen Gleichstand vor. Dekalin punktet nur, wenn der Nutzer die Marke schon kennt. Bei offenen Fragen – dort, wo Neukunden entstehen – ist Sika rund 1,6-mal so sichtbar, steht 7-mal auf Platz 1 und liefert selbst die Belege.

## 3. Wer wird besser dargestellt?

| Dimension | Dekalin | Sika | TEROSON |
|---|---|---|---|
| Etikett der KI | „Caravan-Spezialist“ (ChatGPT P9), „Beste Wahl für Fenster und Luken“ (P8), „Meine Empfehlung“ nur bei Dachluke (P4) | „Top-Empfehlung“ (P9), „Bester Allrounder“ (P8), „Meine Empfehlung“ für Solar (P10) | „speziell Karosserienähte“ (P7), „Fahrzeugaufbauten“ (P9) |
| Zugeschriebene Kompetenz | **Dichten** (Butyl, dauerplastisch, lösbar) | **Kleben + Dichten**, Profi, Solar, Allrounder | Kfz-Reparatur |
| Kompetenz, die fehlt | Kleben/Konstruktion (MS-5), Automotive, Industrie | – | Caravan |
| Belegtiefe | hoch nur wenn Herstellerseite gefunden (ChatGPT P3: alle Kennwerte); sonst generisch („gute Haftung“, P10) | Produktnummern je Anwendung (252i, 522, 554, Lastomer 514/710), zitiert über sika.com | Produktnummern (MS 9320 SF, MS 939, MS 9220), ohne Quelle |
| Fehlerbild | ⚠ P2 in beiden Systemen: „Dekalin = Dichten, Sika = Kleben“ – DEKAsyl als Alternative unterschlagen | keins | keins (aber kaum präsent) |

**Fazit Darstellung:** Sika wird als Systemanbieter für alle Aufgaben dargestellt, Dekalin als Butyl-Spezialist für Fenster und Luken. Das Premiumprodukt MS-5 – technisch auf Augenhöhe mit Sikaflex-554 (gleiche Shore-A 55 und Zugscherfestigkeit 2,5 MPa, höhere Temperaturbeständigkeit +120 °C statt +90 °C) – kommt in offenen Fragen nur einmal vor.

---

## 4. Warum? Was die Wettbewerber anders machen

### 4.1 Inhaltlich

| # | Sika (Beleg) | Dekalin (Beleg) | TEROSON (Beleg) | Wirkung im Test |
|---|---|---|---|---|
| I1 | **Caravan-FAQ mit 28 ausführlichen Antworten** auf einer URL (deu.sika.com/…/kleben-und-dichten-am-caravan/faq.html): Solarmodul kleben, wiederlösbar, primerlos, Entfernen, Altreste, Überlackieren, Temperatur, Wo kaufen | FAQ mit 27 echten Fragen vorhanden, aber Platzhalter „FAQ Titel“ + Lorem Ipsum, 8 Dubletten; MS-5-Fragen (Ergiebigkeit, Endfestigkeit, Entfernen) fehlen | keine Caravan-FAQ | Sika-FAQ Primärquelle in Perplexity P2 + P8; P8-Empfehlung allein SikaLastomer-514 |
| I2 | **Profi-Broschüre „Ausbau und Profi-Reparatur von Caravan und Reisemobilen“ als PDF**, DE + CH (2 URLs) | Broschüre Caravaning (3,8 MB) existiert, wird nicht zitiert; Branchenseite-H1 „Zeit, dass sie Profiprodukte verwenden“ ohne Fakten (Referenzen, Normen, OEM) | Henkel-Katalog Karosseriereparatur, nur B2B | P9: 4 von 10 Quellen Sika, Dekalin 0 |
| I3 | **Anwendungseinstieg** „Was willst du wo machen?“ (Fahrzeuggrafik → Produkt) auf DIY-Seite | Ratgeber/Anleitungen vorhanden (`/solar/`, `/sat-anlage/`, Dachluke), aber nicht als Antwortseite (direkte Antwort oben, Tabelle, FAQ) aufgebaut | keine Anwendungsseiten | P10: Perplexity nennt nur Sikaflex; `/solar/` wird nicht zitiert |
| I4 | **„Sikaflex“ als Gattungsbegriff**: Drittseiten schreiben „Sikaflex-Alternativen“, „Welches Sikaflex?“ | Dekalin wird in Drittinhalten als „Alternative zu Sikaflex“ verglichen (planmycamper, podcast.de: „MS-5 ähnlich Sikaflex-252“) | – | P2/P10: Sika ist Referenzpunkt, Dekalin die Abweichung |
| I5 | **Händler-Kategorietext** bei Reimo dreht sich um Sikaflex („Welches Sikaflex für Dachluke?“); eigene Reimo-Unterkategorie „Sika Produkte“ | kein Händler-Content-Paket; Fritz Berger schreibt „Dekaline“; MS-5-Datenblatt wird über reimo.com gefunden | Reimo schreibt „Terrostat“ | P3 Perplexity: 7 von 10 Quellen Händler, 0 Dekalin |
| I6 | **Solar-Ökosystem**: Montageanleitungen von Solar-Händlern (aceflex-PDF), Klebesets Dritter (photovoltaik4all, Büttner) nennen Sikaflex | MS-5 bei Offgridtec, Fraron, Solarkontor gelistet, aber keine Anleitungen Dritter mit Dekalin | – | P10: 4 Solar-Händlerquellen, alle Sika |
| I7 | **Reichweite im offenen Web**: Wikipedia (Sika AG), englische Foren, Reddit, YouTube-Videos | Wikipedia „Dekalin“ = Chemikalie Decalin; kein Reddit, kein Amazon.de-Treffer, YouTube 134 Abonnenten | kein Wikipedia-Artikel | Modellwissen: Sika in P7 Platz 1 ohne jede Quelle |

### 4.2 Technisch / Produktdaten

| # | Sika | Dekalin | TEROSON | Wirkung im Test |
|---|---|---|---|---|
| T1 | Produktseite Sikaflex-554: **technische Daten als HTML-Tabelle mit Prüfnormen**, Nachweise DIN EN 45545-2, ISEGA | Kennwerte stehen im Fließtext bzw. vollständig nur im **PDF**; keine Nachweise genannt | Datenblätter mehrsprachig, Seite ohne Meta-Description | P3: Perplexity ohne Kennwerte; ChatGPT nur über dekalin.com korrekt |
| T2 | kein Product-Schema (nur Breadcrumb) – kompensiert durch Autorität und Inhalt | **Product-Schema mit Preis „0.00 EUR“ + „InStock“** auf allen Produktseiten von dekalin.de, ohne brand, manufacturer, gtin, additionalProperty; MS-1 schwarz und SAT-Set ganz ohne Schema | Product-Schema dünn (brand, sku), Organization leer, Speakable vorhanden | P6: MS-5 erfüllt „überlackierbar + UV-beständig“, nennt das aber nicht maschinenlesbar → Ber-Fix/WEICON gewinnen |
| T3 | eine Marke, konsistent auf deu./che.sika.com | **zwei Domains, zwei Absender**: dekalin.de = DEKA Kleben & Dichten GmbH (Reichelsheim; Pressetexte „Ranstadt“), dekalin.com = DINOL GmbH (Lügde); Datenblatt „a brand of DINOL“ | Henkel-Dachmarke | Entität unscharf; ChatGPT nutzt wechselnd .de und .com |
| T4 | saubere Titles/Descriptions | Tippfehler „Deklain“ in Titles, „Dauererlastisch“ in MS-5-Description, **P8-Ratgeber `/ratgeber/dichtstoff-fuer-wohnwagen-wohnmobil/` mit Title „Unterbodenschutz Wohnmobil“**, dekalin.com-Title „I High Tack …“, nummerische URLs `/produkt/557/` | keine Meta-Description | Seite, die P8 exakt beantwortet, rankt/zitiert nicht |
| T5 | Organization klar (Wikipedia) | kein Organization-Schema mit sameAs, kein llms.txt, Schreibweisen „DEKASYL / DEKAsyl / Dekasyl“, „MS-5 / MS 5“ | Organization-Felder leer | Namensvarianten erschweren Zuordnung |
| T6 | robots.txt offen | robots.txt offen (gut), aber `/produkte/reinigen/` gesperrt und trotzdem in Sitemap | offen | kein Blocker, aber Hygiene |

### 4.3 Was Dekalin besser hat (und nicht ausspielt)

| Vorteil | Beleg |
|---|---|
| Größte Content-Basis der drei: ~135 Blogartikel, Akademie-Videos, Podcasts, Buch, DEKABot | Recherche 1.5 |
| MS-5 technisch konkurrenzfähig: −40 bis +120 °C (Sika-554: −50 bis +90 °C), Hautbildung 12 min (25 min), Lagerung 18 Monate (12), ohne Einschränkung für Endkunden (Sika-554: „nur für erfahrene Anwender“) | Recherche 4.2 |
| Händlerbewertung MS-5 4,96/5 aus 52 (Fritz Berger) – gleichauf mit Sikaflex-522 (4,92/5 aus 52) | Recherche 3 |
| Schulungskompetenz DIN 2304, Klebepraktiker DVS/EWF – starkes Profi-Signal, auf Branchenseiten nicht als Fakt ausgespielt | Recherche 1.5 |
| Positive Modellwahrnehmung im Caravan-Kern (ChatGPT P4 Platz 1 ohne Websuche) | Test |

---

## 5. Lückenliste für Dekalin (priorisiert)

| # | Lücke | Beleg (Test / Recherche) | Adressiert in Maßnahme |
|---|---|---|---|
| **L1** | **Keine zitierfähige Antwortseite für kaufstarke Use Cases** (Solarpanel, SAT, Markise): direkte Antwort, Schritte, Tabelle, FAQ fehlen auf einer URL | P10: Perplexity nur Sika, ChatGPT Sika Platz 1; `/solar/` nie zitiert | M1 |
| **L2** | **Kein Gegenstück zur Sika-Caravan-FAQ**; eigene FAQ mit Lorem Ipsum, Dubletten, ohne MS-5-Fragen | P2, P8 Perplexity: Sika-FAQ Primärquelle | M2 |
| **L3** | **Produktdaten nicht maschinenlesbar und fehlerhaft**: Preis 0,00 €, keine Marke/GTIN, Kennwerte nur im PDF, Eigenschaften („überlackierbar“, „UV-beständig“) nicht als Attribute | P6 beide Systeme: MS-5 fehlt; P3 Perplexity ohne Werte | M3 |
| **L4** | **Positionierung „nur Dichten“**: DEKAsyl-Kleben (MS-5 als Sikaflex-554-Alternative) nicht belegt | P2 ⚠ in beiden Systemen; P8 Solar → Sikaflex 554 | M1, M2 |
| **L5** | **Material-/Eigenschaftsfragen ohne Dekalin-Inhalt** („Alu mit Kunststoff kleben“, „GFK kleben“) | P5: Kategorie MS-Polymer empfohlen, Marke fehlt | M1 (Cluster) |
| **L6** | **Händler besitzen die Produktinformation**; kein einheitliches Content-Paket, falsche Schreibweisen bei Händlern | P3: 7/10 Händlerquellen; Reimo-Kategorietext nur Sika | M5 |
| **L7** | **Solar-Ökosystem ohne Dekalin**: Montageanleitungen und Sets Dritter nennen Sikaflex | P10: 4 Solar-Händlerquellen, alle Sika | M5 |
| **L8** | **Entität unklar**: zwei Domains/Absender (DEKA/DINOL), drei Ortsangaben, Wikipedia = Decalin, kein Organization-Schema | Recherche 0.1, 0.2, 1.1 | M4 |
| **L9** | **Kein Profi-/Industrie-Beleg**: keine zitierfähige Profi-Broschüre (HTML), keine Referenzen/Normen auf Branchenseiten | P9 Perplexity: 0 Dekalin; ChatGPT: „Caravan-Spezialist“ | M4 |
| **L10** | **Automotive unsichtbar** (Karosserienaht, Unterboden) | P7: Sika + TEROSON genannt, Dekalin 0 in beiden | M4 / M5 (Phase 2) |
| **L11** | **SEO-Hygiene verhindert Ranking der vorhandenen Seiten**: falsche Titles (P8-Seite „Unterbodenschutz“), „Deklain“, Duplicate Content `/ratgeber/`, nummerische URLs | Recherche 1.6 | M3 |

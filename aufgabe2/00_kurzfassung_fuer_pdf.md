# Aufgabe 2 – KI-Sichtbarkeit Dekalin (Kurzfassung)

**Test:** 01.11.2026 · Perplexity (Modus „Suche“) + ChatGPT (Websuche auto) · beide ausgeloggt, neue Session je Prompt, 1 Lauf · 10 Prompts × 2 Systeme = 20 Antworten · Wettbewerber: **Sika** (Benchmark, Produkte 1:1 austauschbar) und **TEROSON/Henkel** (gleiches Regal, gleiche Kfz-Herkunft)

**Bewertungsraster:** Nennung im Antworttext (ja/nein, Rang) · Darstellung (Etikett, Tiefe) · Quellentyp je URL (Hersteller/Händler/Blog/Forum/Verzeichnis) · ✓ korrekt+vollständig / ◐ lückenhaft / ⚠ verzerrt / ✗ falsch

## 1. Ergebnis-Matrix

| # | Typ | Prompt (gekürzt) | Perplexity: Dekalin · Quellen | ChatGPT: Dekalin · Quellen | Sika (P/C) | TEROSON (P/C) |
|---|---|---|---|---|---|---|
| P1 | Marke | Was ist Dekalin …? | ja (1) ◐ · dekalin.de 1, Blogs 6, Händler 2 | ja (1) ✓ · dekalin.de/.com | –/– | –/– |
| P2 | Marke | Dekalin oder Sikaflex? | ja (1) ⚠ „nur Dichten“ · **Sika-FAQ**, Foren 5 | ja (1) ⚠ · dekalin.de | 2/2 | –/– |
| P3 | Marke | Ist DEKAsyl MS 5 gut? | ja (1) ◐ ohne Werte · **Händler 7** (Datenblatt via reimo.com) | ja (1) ✓ alle Kennwerte · dekalin.com | –/– | –/– |
| P4 | Produkt | Dachluke abdichten | ja (1+2) ✓ 1512/8936 · Blogs 7, Foren 2 | ja (1+3) ✓ „Meine Empfehlung“ · Modellwissen | Quelle/2 | –/– |
| P5 | Produkt | Alu + Kunststoff kleben | nein · Foren 5, Permabond | nein (MS-Polymer generisch) · Kleberkompass | –/– | –/– |
| P6 | Produkt | MS-Polymer überlackierbar + UV-beständig | nein (**Ber-Fix** via wlw) · Verzeichnis 3, Händler 5 | nein (WEICON, OMEGA, MARSTON) · Shopping-Karten | –/– | –/– |
| P7 | Produkt | Karosserienaht abdichten | nein · Foren 6, 3M | nein · Modellwissen | –/1 | –/2 |
| P8 | Empfehlung | Bester Dichtstoff Wohnwagen | **nein** (nur SikaLastomer-514) · **Sika-FAQ** + che.sika | ja (2) ✓ 8936 · sika.com, 2 Händler | **1/1** | –/– |
| P9 | Empfehlung | Marken, die Profis empfehlen | **nein** · **Sika 4** (2 Profi-PDF), Bostik, EGO | ja (2) ◐ „Caravan-Spezialist“ · sika.com | **1/1** | –/3 |
| P10 | Empfehlung | Solarpanel ohne Bohren kleben | **nein** (nur Sikaflex 252i/554/522) · Solar-Händler 4, Blogs 5 | ja (2) ◐ MS-5 ohne Begründung · sika.com | **1/1** | –/– |

## 2. Kennzahlen

| Kennzahl | Dekalin | Sika | TEROSON |
|---|---|---|---|
| Sichtbarkeit Perplexity / ChatGPT | 40 % / 70 % | 40 % / 60 % | 0 % / 20 % |
| Sichtbarkeit gesamt (20) | 55 % | 50 % | 10 % |
| **Sichtbarkeit ohne Markenprompts (P4–P10, 14)** | **35,7 %** | **57,1 %** | 14,3 % |
| Empfehlungsprompts P8–P10 (6) | 50 % (Perplexity 0/3) | **100 %** | 16,7 % |
| Platz 1 in P4–P10 · Ø Rang | 2× · 1,6 | **7×** · 1,1 | 0× · 2,5 |
| **Share of Voice** Produktnennungen P4–P10 (31) | **22,6 %** | **41,9 %** | 6,5 % |
| Eigene Domain als Quelle (20 Antworten) | 4 – **0 bei Nicht-Markenprompts** | 7 – 6 bei Nicht-Markenprompts | 0 |
| Anteil an 99 Perplexity-Quellen | 1,0 % | 8,1 % | 0 % |

**Quellenmix Perplexity (99 URLs):** Hersteller 18,2 % · Händler 23,2 % · Blog/Medien 36,4 % · Foren 19,2 % · Verzeichnis 3,0 %. **ChatGPT (10 Domains):** Hersteller 70 % (Dekalin 4 nur in P1–P3, Sika 3 in P8–P10) · Händler 20 % · Portal 10 %.
**Korrektheit Dekalin (11 Nennungen):** ✓ 5 · ◐ 4 · ⚠ 2 · ✗ 0.

## 3. Kernerkenntnisse und Überraschungen

| # | Erkenntnis |
|---|---|
| 1 | **Dekalin gewinnt nur, wenn die Marke im Prompt steht** (6/6); bei offenen Fragen ist Sika 1,6-mal so sichtbar und 7-mal auf Platz 1. |
| 2 | **dekalin.de wird bei Nicht-Markenfragen nie zitiert (0/14)**; sogar das MS-5-Datenblatt kommt von reimo.com. Händler und Blogs besitzen die Produktinformation. |
| 3 | **Sika gewinnt mit Antwortseiten**: Caravan-FAQ (P2, P8) und Profi-Broschüren-PDF (P9) sind Primärquellen. In Perplexity P8 sind 4/10 Quellen Dekalin-lastig – genannt wird nur Sika. |
| 4 | **Dekalin = „Dichten“**: MS-5 (Gegenspieler zu Sikaflex-554) erscheint in offenen Fragen einmal, ohne Begründung; der kaufstarke Solar-Use-Case geht an Sika. |
| 5 | **Eigenschaftsfragen gewinnt, wer Attribute wörtlich und maschinenlesbar publiziert** (P6: Ber-Fix, WEICON) – dekalin.de liefert Schema mit Preis 0,00 €, ohne Marke und Kennwerte. |
| 6 | **Überraschung:** ChatGPT (70 %) > Perplexity (40 %) – die Community-Verankerung steckt im Modellwissen (P4 Platz 1 ohne Websuche); Perplexity nimmt die direkteste Antwortseite, und das ist fast nie dekalin.de. |
| 7 | **Überraschung:** Sika-FAQ ohne FAQPage-Schema wird zitiert, Dekalin-FAQ mit Schema nicht (Lorem Ipsum, 8 Dubletten). TEROSON trotz Henkel praktisch unsichtbar (2/20, nie Quelle). Dekalin hat die passenden Seiten schon (`/solar/`, P8-Ratgeber mit falschem Title „Unterbodenschutz Wohnmobil“). |

## 4. Wettbewerbsvergleich: Warum Sika vorn liegt

| Ebene | Sika | Dekalin | TEROSON |
|---|---|---|---|
| Antwortinhalte | Caravan-FAQ (28 Antworten, 1 URL), DIY-Anwendungseinstieg, Profi-Broschüre PDF (DE + CH) | viel Content (135 Blogartikel, Akademie, Anleitungen), aber nicht als Antwortseiten; FAQ mit Platzhaltern | keine Caravan-Inhalte |
| Drittquellen | „Sikaflex“ als Gattungsbegriff, Reimo-Kategorietext, Solar-Montageanleitungen und Sets Dritter, Wikipedia, Foren | Händler gleich stark (Fritz Berger 26 vs. 27 Artikel), aber ohne Content-Paket; Wikipedia „Dekalin“ = Chemikalie | Handel ja, Content nein |
| Produktdaten | Kennwerte als HTML-Tabelle mit Normen (DIN EN 45545-2, ISEGA) | Kennwerte nur PDF/Fließtext; Product-Schema Preis 0,00 €, ohne brand/gtin/Attribute | B2B-Portal, Schema dünn |
| Entität | eine Marke | zwei Domains/Absender (DEKA vs. DINOL), drei Ortsangaben, „Deklain“-Tippfehler, Schreibweisen | Henkel-Dachmarke |

**Lückenliste:** L1 keine Antwortseite für Solar/SAT/Markise · L2 kein Gegenstück zur Sika-FAQ · L3 Produktdaten nicht maschinenlesbar/fehlerhaft · L4 Positionierung „nur Dichten“ · L5 keine Material-Ratgeber (Alu/GFK) · L6 Händler besitzen Produktinfo · L7 Solar-Ökosystem ohne Dekalin · L8 Entität unklar · L9 kein Profi-/Industrie-Beleg · L10 Automotive unsichtbar · L11 SEO-Hygiene (falsche Titles, Tippfehler, nummerische URLs)

## 5. Maßnahmenplan (Impact/Aufwand 1–5, Score = I ÷ A)

| Rang | Maßnahme | Was | Warum für KI | Ergebnis / KPI (Ziel 90 Tage) | I | A | Score |
|---|---|---|---|---|---|---|---|
| 1 | **M1 Antwortseiten Use Cases** (Pilot Solar) | 2-Satz-Antwort oben, Schritte, Tabellen, 8–12 FAQ, Article/HowTo/FAQ/Product-Schema; dann SAT, Markise, Alu/GFK | KI zitiert eigenständige Passagen; schließt P10-Lücke und „nur Dichten“ | P10 2/2 genannt, dekalin.de zitiert | 5 | 2 | **2,5** |
| 2 | **M3 Produktdaten + Hygiene** | Schema ohne 0,00 €, mit brand, gtin, additionalProperty; Kennwerte als HTML; Merchant Feed; Titles/URLs fixen | Eigenschaftsfragen = Attribut-Matching (P6) | P6 ≥ 1/2; Rich Results grün | 4 | 2 | **2,0** |
| 3 | **M2 Caravan-FAQ-Hub** | FAQ bereinigen, 40 Antworten nach Bauteil, Anker je Frage | Sika-FAQ ist Primärquelle in P2/P8 | Perplexity P8 genannt; Citation Share ≥ 3/14 | 4 | 2 | **2,0** |
| 4 | **M4 Entität + Profi-Autorität** | Organization-Schema (DINOL/DEKA, sameAs), Wikidata, eine Schreibweise; Branchenseite mit Fakten, Broschüre HTML | Zuordnung der Marke; P9 wird über Profi-Quellen beantwortet | P9 2/2; P1 vollständig | 4 | 3 | 1,3 |
| 5 | **M5 Drittquellen** | Händler-Content-Paket, Solar-Partner-Anleitungen, Medien, Foren, YouTube | 79 % der Perplexity-Quellen sind Händler/Blogs/Foren | Empfehlungsprompts ≥ 5/6; SoV ≥ 35 % | 5 | 4 | 1,25 |

**Kern-KPI:** Sichtbarkeit ohne Markenprompts 35,7 % → ≥ 57 % · Citation Share dekalin.de (Nicht-Marke) 0/14 → ≥ 4/14 · Re-Test nach 90 Tagen, 3 Läufe je Prompt, monatlich per Tracking-Tool.

## 6. Ausgearbeitete Maßnahme: Antwortseite „Solarpanel ohne Bohren aufs Wohnmobildach kleben – mit DEKAsyl MS-5“

**Warum diese:** größte und kaufstärkste Einzellücke (P10: Perplexity nur Sika), Premiumprodukt MS-5 direkt gegen Sikaflex-554, Material vollständig vorhanden (Datenblatt, `/solar/`, Video, Set) → live in 2–3 Wochen; Template für alle weiteren Antwortseiten, liefert 12 FAQ für den Hub.

| Element | Umsetzung |
|---|---|
| URL / Redirect | `dekalin.de/ratgeber/solarpanel-wohnmobil-kleben-ohne-bohren/` · 301 von `/solar/` |
| Meta-Title (55) | Solarpanel ohne Bohren aufs Wohnmobil kleben: Anleitung |
| Meta-Description (152) | Solarpanel ohne Bohren aufs Wohnmobildach kleben: Welcher Kleber, welche Vorbereitung, wie lange aushärten? Anleitung mit DEKAsyl MS-5, Tabelle und FAQ. |
| Direktantwort (erste 2 Sätze) | „Ein Solarpanel klebst du ohne Bohren mit einem elastischen High-Tack-Klebstoff auf MS-Polymer-Basis wie DEKAsyl MS-5 aufs Wohnmobildach – bei starren Modulen werden Spoiler oder Halter verklebt, halbflexible Module klebst du direkt. MS-5 haftet ohne Primer auf Aluminium, GFK, lackiertem Blech und Glas, bleibt von −40 °C bis +120 °C elastisch und hält die Teile dank hoher Anfangshaftung meist ohne Klemmen in Position.“ |
| Aufbau | H1 · Kurzantwort · 5 Fakten · Welcher Kleber · Modultyp-Tabelle · Material · **8 Schritte** · Zeiten-Tabelle · Haftgründe-Tabelle · **MS-1/MS-2/MS-5** · **MS-5 vs. Sikaflex-554** · Fehler · technische Daten (HTML) · **12 FAQ** · Händler + Downloads |
| Schema (validiert) | Article + HowTo (8 Steps) + FAQPage (12) + Product MS-5 (gtin13 4046085125227, brand DEKALIN, 26 additionalProperty, **AggregateOffer 17,99–27,60 € statt 0,00 €**, kein fremdes Rating) + Breadcrumb + Organization |
| Interne Links | aus Startseite, MS-5-/MS-2-/Set-PDP, Caravaning-Branchenseite, FAQ; zu MS-5, Set, DEKACLEAN, DEKAVATOR, DEKAFINISHER, MS-Vergleich, SAT, Markise |
| Checkliste | WordPress (Yoast, Redirect, WooCommerce-Schema 0,00 € abschalten) und Shopify (Blog-Handle, Metafeld-JSON-LD, Offer-Liquid, Merchant Center) · Abnahme: Rich Results Test, Roh-HTML-Check, Re-Test P10 nach 2/6/12 Wochen |

| Schritt | Kernaussage (Werte laut Datenblatt) |
|---|---|
| 1 Planen | Spoiler am Modul montieren, Klebeflächen markieren; +5 bis +35 °C, Schatten |
| 2 Reinigen | DEKACLEAN ULTRA; sauber, trocken, staub- und fettfrei |
| 3 Haftung | primerlos auf Alu, GFK, lackiertem Metall, Glas; DEKAVATOR 22 NF bei hoher Belastung/Feuchte; PE/PP/Teflon nicht |
| 4 Auftragen | 7-mm-Raupe → 3–5 mm Naht; mind. 2 mm Klebeschicht |
| 5 Fügen | innerhalb 15 min; High Tack, meist ohne Klemmen |
| 6 Abdichten | Abschlussnaht + Kabeldurchführung; glätten mit DEKAFINISHER-Spachtel innerhalb 12 min |
| 7 Aushärten | ca. 4 mm/24 h; Endfestigkeit 24–48 h, erst dann fahren |
| 8 Lackieren | nass in nass ab ca. 10 min, beste Haftung nach 4 h |

**Vor Livegang klären [Annahmen/Lücken]:** Autor/Datum · Ergiebigkeit (Rechenwert ~7 m Raupe je 290 ml) · Prüfnachweis Fahrbelastung · Demontage · GTINs schwarz/600 ml, UVP · Rolle DEKA/DINOL im Schema · rechtliche Prüfung des Sikaflex-Vergleichs.

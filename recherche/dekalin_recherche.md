# Recherche Dekalin: Website, DEKAsyl MS-5, Wettbewerb, KI-Sichtbarkeit, Navigation

Stand der Recherche: 01.11.2026. Methode: Abruf der Seiten per HTTP (Roh-HTML, also das, was auch Crawler und KI-Bots sehen), Auswertung von Sitemaps, robots.txt und JSON-LD, Websuche, PDF-Datenblätter.

Kennzeichnung:
- **[F]** = Fakt, mit Quelle belegt
- **[A]** = Annahme, Interpretation oder Empfehlung von mir
- **[L]** = Lücke: die Information wurde gesucht und nicht gefunden

---

## 0. Die wichtigsten Erkenntnisse

1. **[F] „Dekalin“ steht für zwei Firmen.** dekalin.de wird von der DEKA Kleben & Dichten GmbH in Reichelsheim betrieben (https://dekalin.de/impressum/). dekalin.com gehört der DINOL GmbH in Lügde: „DEKALIN ist eine Marke der DINOL GmbH“ (https://www.dekalin.com/ueber-uns/unternehmen/). Laut DINOL gehört DINOL zur Würth-Gruppe (https://www.dinol.com/ueber-uns/; eine zweite Quelle dafür habe ich nicht gefunden). Das Datenblatt zu MS-5 trägt den Hinweis „a brand of DINOL“ und verweist auf die AGB der DINOL GmbH (https://dekalin.de/wp-content/uploads/2024/12/Dekalin_TDB_Dekasyl-MS-5_DE.pdf). Auf dekalin.com ist DEKA als „Distributor“ geführt (https://www.dekalin.com/distributoren/deka-kleben-dichten-gmbh/).
   **[A]** Für die KI-Sichtbarkeit ist das ein Problem: Zwei Absender, zwei Adressen, zwei Sortimente. Ein Sprachmodell kann diese Signale schwer zu einer Marke zusammenführen.
2. **[F] Der Wikipedia-Eintrag „Dekalin“ führt zur Chemikalie Decalin**, nicht zum Hersteller (Abfrage über die de.wikipedia API). Weder zur Marke noch zu DINOL, Teroson oder Dinitrol gibt es einen eigenen Artikel. „Sikaflex“ dagegen leitet auf den Artikel „Sika AG“ weiter.
   **[A]** Das erhöht die Gefahr, dass eine KI den Namen falsch zuordnet. Dekalin erklärt sogar selbst, der Name komme vom Lösungsmittel Dekahydronaphthalin (https://dekalin.de/wo-kommt-eigentlich-der-name-dekalin-her/).
3. **[F] dekalin.de basiert auf WordPress mit WooCommerce.** Es gibt einen Warenkorb und eine Kasse, kaufen kann man aber nur das Buch (19,99 €). Alle Produktseiten führen ein Product-Schema mit **Preis „0.00 EUR“ und „InStock“** (z. B. https://dekalin.de/produkt/557/).
   **[A]** Diese Daten sind falsch und wirken nach außen widersprüchlich. Ein Shopify-Shop würde das grundlegend beheben.
4. **[F] Inhaltlich ist Dekalin stark:** über 130 Blogartikel, Ratgeber, eine Akademie mit Videos, Podcasts, ein FAQ mit FAQPage-Schema, einen KI-Berater („DEKABot“), ein eigenes Buch, Schulungen nach DIN 2304 und ein komplettes 2-seitiges Datenblatt zu MS-5.
   **[F] Die Technik ist schwach:** Tippfehler „Deklain“ in Titles, Dummy-Text („Lorem Ipsum“, „FAQ Titel“) im FAQ-Schema, falsche Seitentitel, nummerische Produkt-URLs, doppelte Produkte, fehlende Meta-Descriptions (Belege in Abschnitt 1.6).
5. **[F] Im Handel ist Dekalin auf Augenhöhe mit Sika.** Bei Fritz Berger stehen in der Kategorie „Klebstoffe & Dichtmittel“ 27 Artikel von Sika, 26 von Dekalin und 17 von TEROSON. Reimo und Obelink führen ebenfalls beide Marken (Abschnitt 3).
   **[F]** Der ADAC-Ratgeber PiNCAMP nennt Dekalin und Sika „Marktführer“ (https://www.pincamp.de/magazin/ratgeber/wohnwagen/wohnwagen-dichtmasse-tipps).
6. **[F] Sika hat online klar mehr Reichweite:** einen Wikipedia-Artikel, eine eigene DIY-Caravan-Seite mit 28 FAQ, Kaufberatung im Kategorietext bei Reimo, englische Forenpräsenz und viele Marktplatz-Bewertungen. Für Dekalin habe ich keine Treffer auf Reddit und keinen Treffer auf Amazon.de gefunden (Abschnitt 4).
7. **Gewählte Wettbewerber: Sika (Sikaflex) und TEROSON (Henkel).** Die Begründung steht in Abschnitt 4.1.

---

## 1. Dekalin: Websites

### 1.1 Zwei Domains, zwei Betreiber

| | dekalin.de | dekalin.com |
|---|---|---|
| Betreiber | DEKA Kleben & Dichten GmbH, Kirchgasse 1, 61203 Reichelsheim; GF Michael Windecker; AG Friedberg HRB 4903 [F] (https://dekalin.de/impressum/) | DINOL GmbH, Pyrmonter Str. 76, 32676 Lügde; GF Frank Stentenbach; AG Lemgo HRB 5365 [F] (https://www.dekalin.com/impressum/) |
| System | WordPress 7.1.4, WooCommerce 11.2.1, WPBakery, Slider Revolution, Yoast SEO [F] (Generator-Meta-Tags im HTML der Startseite) | WordPress 7.0.2, eigenes Theme „fbnfrtg“, WP-Core-Sitemap [F] |
| Sprache | `lang="de"`, kein hreflang [F] | DE + EN (`/en/`), hreflang de/en vorhanden [F] |
| Zielgruppe | Caravaning-Endkunden + Gewerbe (Industrie, Klima/Lüftung, Raumausstatter, Sattlereien) [F] | B2B/international: Branchen „Caravan & Wohnmobile“, „Kapselklebstoff“ (Getränkeindustrie), „Tiny Houses“; Distributoren weltweit; Private Label [F] (https://www.dekalin.com/) |
| Title der Startseite | „Dekalin ➱ Spezialist für professionelles Kleben & Dichten“ [F] | „Home \| DEKALIN“ [F] |
| Meta-Description | „Dekalin ➱ Spezialist für professionelles Kleben & Dichten ➱ Ob Caravaning, Industrie, Klima und Lüftung, Raumausstatter oder Sattlereien ➱ jetzt entdecken!“ [F] | keine [F] |

[F] Die Adressen widersprechen sich. Pressetexte auf dekalin.de nennen den Ort „Ranstadt“ (https://dekalin.de/dekasyl-ms-1-dekasyl-ms-2-dekasyl-ms-5-was-ist-der-unterschied/). Branchenverzeichnisse führen DEKA unter „Gartenstraße 4, Ranstadt“ (https://www.chemie.de/firmen/11027/deka-kleben-dichten-gmbh.html). Das Impressum nennt Reichelsheim.

### 1.2 Crawlbarkeit, robots.txt, Sitemaps

- **[F] robots.txt von dekalin.de** (https://dekalin.de/robots.txt): `User-agent: *` ohne Sperre für KI-Bots. Gesperrt sind nur `/dlm_uploads/`, einige alte Messe- und Gewinnspiel-Artikel sowie **`/produkte/reinigen/`**. Die Sitemap wird verlinkt.
  - [A] Die Kategorie „Reinigen“ ist per robots.txt gesperrt, steht aber trotzdem in der Sitemap. Vermutlich ist das ein Versehen.
- **[F] Sitemaps von dekalin.de** (Yoast, https://dekalin.de/sitemap_index.xml):
  - 31 Produkt-URLs, alle unter `/produkt/<Nummer>/` (z. B. `/produkt/557/` = MS-5 weiß)
  - rund 70 Seiten und rund 135 Blogartikel
  - 28 FAQ-Einträge unter `/ufaq/`, 7 Produktkategorien, 29 Produkt-Tags (ebenfalls nur Nummern)
- **[F] Sitemap von dekalin.com** (https://www.dekalin.com/wp-sitemap.xml): 31 Seiten, 16 Produkte unter sprechenden URLs (z. B. `/produkt/dekasyl-ms-5/`) und 26 Distributoren. Die robots.txt sperrt nur `/wp-admin/`.
- **[F] Produktseiten sind serverseitig gerendert.** Beschreibung, Anwendungen, Verarbeitung und Links zu den Datenblättern stehen im Roh-HTML. Für Crawler und KI-Bots sind sie also lesbar (geprüft per curl ohne JavaScript).
- **[F] Es gibt kein `llms.txt`**, weder auf dekalin.de noch auf dekalin.com (HTTP 404).

### 1.3 Strukturierte Daten (Schema.org JSON-LD)

| Seite | JSON-LD vorhanden | Bewertung |
|---|---|---|
| Startseite dekalin.de | WebPage, WebSite + SearchAction, BreadcrumbList; **LocalBusiness** mit AggregateRating 5,0 aus 94 Reviews und einzelnen Google-Reviews [F] | [A] Selbst eingebundene Bewertungen auf dem eigenen LocalBusiness zeigt Google nicht als Rich Result an. Organization-Daten (Logo, sameAs, Kontakt) fehlen. |
| Produktseiten dekalin.de | **Product** mit name, description, image, sku, offers (price „0.00“, EUR, InStock, seller „DEKALIN Deutschland“) [F] (z. B. https://dekalin.de/produkt/557/) | [A] Preis 0 € ist fehlerhaft. Es fehlen brand, manufacturer, gtin, color und additionalProperty (technische Daten). MS-1 schwarz und das SAT-Klebeset haben gar kein Product-Schema [F]. |
| FAQ dekalin.de | **FAQPage** mit 35 Fragen [F] (https://dekalin.de/faq/) | [F] Darin stehen ein Platzhalter „FAQ Titel“ mit Lorem-Ipsum-Text und 8 doppelte Fragen. |
| Caravaning, Akademie, Kategorie „Dichten“ | FAQPage [F] | [A] Das ist gut und für KI-Antworten nützlich. |
| Blogartikel | Article + Person [F] | in Ordnung |
| Produktseite dekalin.com MS-5 | Product mit brand „DEKALIN“, manufacturer „DINOL GmbH“, category, material, color, additionalProperty (Basismaterial, Farben, Verpackung, Anwendungsbereiche) [F] (https://www.dekalin.com/produkt/dekasyl-ms-5/) | [A] Fachlich besser gepflegt als auf .de. Es fehlen offers, gtin und technische Kennwerte. |
| Unterseiten dekalin.com | meist kein JSON-LD [F] | |

### 1.4 Sortiment (dekalin.de: 31 Produkt-URLs, dekalin.com: 16 Produkte)

**[F] Kategorien auf dekalin.de**, farblich gekennzeichnet (https://dekalin.de/ratgeber/do-it-yourself/): Reinigen (und Vorbehandeln), Kleben & Dichten, Dichten, Schützen, Kleben & Reparieren. Dazu kommen „Buch“ und „Unkategorisiert“. Die Kategorie-URLs sind teils nur Nummern: `/produkt-kategorie/16/` = Kleben und Dichten, `/17/` = Kleben und Reparieren, `/18/` = Reinigen und Vorbehandeln.

**[F] Produkttabelle** (Quelle: Spezifikationen auf dekalin.com, z. B. https://www.dekalin.com/produkt/dekasyl-ms-6/, ergänzt um die Titles von dekalin.de):

| Produkt | Kategorie | Typ / Unterkategorie | Basis | Anwendungen laut Hersteller | Farben | Gebinde |
|---|---|---|---|---|---|---|
| DEKASYL MS-1 | Kleben & Dichten | Dichtstoff, „für Einsteiger“ | MS-Polymer | Fugen, Dichtnähte, Überlappungen | weiß, grau, schwarz | 290 ml |
| DEKASYL MS-2 | Kleben & Dichten | Dichtstoff, „für Fortgeschrittene“ | MS-Polymer | Verbindungen, Dichtnähte, Solaranlagen, Überlappungen | weiß, grau, schwarz | 290 ml, 600 ml Schlauchbeutel |
| **DEKASYL MS-5** | Kleben & Dichten | **Konstruktionsklebstoff, High Tack** | MS-Polymer | Dachkonstruktionen, Karosseriemontage, SAT-Anlagen, Solaranlagen, Spoiler | weiß, schwarz | 290 ml, 600 ml |
| DEKASYL MS-6 | Kleben & Dichten | Multifunktional | MS-Polymer | Fugen, Bad/Küche, Dachhauben, Dachluken, Dichtnähte, Bodenbeläge, Fenster, Spoiler, Türen | weiß, schwarz | 310 ml |
| DEKASYL MS-7 | Kleben & Dichten | Multifunktional, transparent, lebensmittelrechtlich zugelassen (laut Title auf .de) | MS-Polymer | Bad/Küche, Dichtnähte | transparent | 290 ml |
| DEKASYL MS-8 (nur auf .com) | Kleben & Dichten | Scheibenklebstoff | MS-Polymer | Scheiben, Windschutzscheiben | schwarz | 290 ml, 600 ml |
| DEKASEAL 8936 | Dichten | abtupfbare, nicht aushärtende Dichtmasse | Polyisobuten / Kunstharze | Fenster, Markisen, Radkästen, Schrauben/Leisten, Serviceklappen | anthrazit, hellgrau, schwarz | 310 ml, 560 ml |
| DEKASEAL 1512 | Dichten | überlackierbare Butyl-Dichtmasse | Butyl | Abdeckleisten, Bohrungen, Dachhauben, Dachluken, Radkästen, Türen | cremeweiß, schwarz | 310 ml, 560 ml |
| DEKASEAL 8869 Butyl-Mastic, DEKASEAL Butyl-Tape, DEKAPLAST 7303 (Butylband) | Dichten | Butylmasse / Bänder | Butyl | – | grau, schwarz | – |
| DEKAPUR 2K-90 | Kleben & Reparieren | 2K-PU Kunststoffreparatur | Isocyanat-Prepolymer + Polyol | gebrochene Kunststoffteile | schwarz | 50 ml Doppelkartusche |
| DEKAPUR 2K-6000 A+B | Kleben & Reparieren | Konstruktionsklebstoff, Seitenwand | PU | Außenflächen, Chassis, Karosseriebau | beige | 5 kg + 1 kg |
| DEKAFINISHER | Reinigen | Glättmittel (auch gegen Regenstreifen) | Tensidlösung | Fugen glätten | transparent | 500 ml Spray |
| DEKAVATOR (22) NF | Reinigen | Haftreiniger / Haftvermittler | Siloxane/Silane | – | transparent | 30 ml, 250 ml |
| DEKACLEAN Ultra (Reiniger + Tuch) | Reinigen | Haftreiniger | Alkohol | – | – | 1 l, Tücher |
| DEKAPHON 9735 | Schützen | Unterbodenschutz, sprühbar, bitumenfrei | Lösemittel | Radkästen, Unterboden | schwarz | 500 ml Spray |
| DEKAPHON 958 | Schützen | Unterbodenschutz, wasserbasiert | Dispersion | Chassis, Radkästen, Unterboden | schwarz | 1 l, 20 l |
| DEKAPHON Pro-Wax | Schützen | Hohlraum-/Unterbodenwachs | Wachs | Hohlräume, Unterboden | transparent | 500 ml |
| Flexsolarmodul-Klebeset (MS-1 + MS-5 + DEKACLEAN Tuch) | Set | – | – | flexible Solarmodule ohne Bohren | weiß, schwarz | Set (Art. 62700/62701) |
| Klebeset für SAT und starre Solaranlagen | Set | – | – | – | – | – |
| Buch „Klebt nicht gibt's nicht!“ (M. Windecker) | Buch | – | – | – | – | 19,99 € (einziger kaufbarer Artikel) |

**[F] Widerspruch:** dekalin.de schreibt: „Unsere Produkte sind frei von Isocyanaten und benötigen keinen Primer“ (Footer jeder Seite). Laut dekalin.com basiert DEKAPUR 2K-90 aber auf einem „Reaktives Isocyanat-Prepolymer“ (https://www.dekalin.com/produkt/dekapur-2k-90/).
**[A]** Diese Aussage sollte im Shop nicht pauschal stehen.

**[F]** Im Handel gibt es Artikel, die auf den Herstellerseiten fehlen:
- MS-5 als 100-ml-Tube („Dekalin Dekasyl MS 5 Kraftkleber weiß 100 ml“, Fritz-Berger-Kategorie, s. Abschnitt 3)
- DEKACLEAN Glass Foam (https://www.berger-camping.com/item/-dekalin-dekaclean-glass-foam-window-cleaner-400-ml-204191)
- Dekasyl 240/260 (https://www.fritz-berger.de/artikel/dekalin-dekasyl-240-grau-250-ml-116312)

### 1.5 Inhalte: Ratgeber, FAQ, Akademie, Service

| Bereich | Inhalt | Quelle |
|---|---|---|
| FAQ | 27 echte Fragen, nach Anwendungsfällen formuliert: „Welche Dichtmasse für Dachluken?“, „Wie dichte ich eine Antenne/LTE-Haube ab?“, „Welche Dichtmasse ist später wieder lösbar?“, „Welcher Kleber für PLA?“ | https://dekalin.de/faq/ |
| Ratgeber | Wasserschaden reparieren; Markise, Dachträger und Anbauteile kleben; Dichtstoff für Wohnwagen; Regenstreifen entfernen; DEKASEAL 8936 vs. 1512; abtupfbare Dichtmasse; MaxxFan vs. Klimaanlage | https://dekalin.de/highlight-themen/ |
| Klebeanleitungen | Solaranlage (MS-5), SAT-Anlage (MS-5), Echtglasscheiben, MaxxFan, Tipps zu 2K-6000 | https://dekalin.de/solar/, https://dekalin.de/sat-anlage/, https://dekalin.de/maxxair/ |
| Akademie | Video-Anleitungen zu Kleben & Dichten, Dichten, Kleben & Reparieren, Schützen, Reinigen | https://dekalin.de/dekalin-akademie/ |
| Blog | rund 135 Artikel (Grundlagenwissen, Caravan-Tipps, Klebstofflexikon), u. a. „DEKAsyl MS-1, MS-2, MS-5 – was ist der Unterschied?“ | https://dekalin.de/post-sitemap.xml |
| Podcasts | u. a. mit CamperStyle (Michael Windecker als „Klebepapst“) | https://dekalin.de/dekalin-podcasts/ |
| DEKABot | KI-Berater. Dekalin wertet die Anfragen nach Themen aus (z. B. „Wohnmobil Markise kleben“, „Dachträger kleben“) | https://dekalin.de/ratgeber/markise-dachtraeger-anbauteile-kleben/ |
| Downloads | Technische Datenblätter, Sicherheitsdatenblätter, Broschüren (Caravaning 3,8 MB, Klima/Lüftung 11 MB), Chemische Resistenzen | https://dekalin.de/unser-service/technische-datenblaetter/ |
| Schulungen | Anwenderschulungen, Inhouse-Schulungen, Trainingscenter, Optimierungstag. Laut Footer Schulungen nach DIN 2304-1 und zum „Klebepraktiker (European Adhesive Bonder) nach DVS/EWF“ | https://dekalin.de/unser-service/anwenderschulungen/ |
| Händlersuche | Karte mit „DEKALIN-Fachhändlern“ (laut Text klebetechnisch geschult); die Liste wird per JavaScript geladen | https://dekalin.de/unser-service/endkunden/ |
| Auszeichnungen | Blogartikel „Gewinner HIPE Award und Plus X Award 2025“ | https://dekalin.de/gewinner-hipe-award-und-plus-x-award-2025/ |

**[F] Bezugswege laut Dekalin:**
- „Endkunden können unsere Produkte über den Fachhandel beziehen, Gewerbekunden über den Großhandel“ (Footer).
- Direktbestellung ab 300 €, frei Haus ab 800 €.
- Caravaning-Handelsketten: Campingprofi, Reimo, Movera, „Friz Berger“ [sic], Frankana, Intercamp (DK) (https://dekalin.de/wo-bekommt-man-eigentlich-dekalin-produkte-zu-kaufen/).
- Die Telefonnummer gilt ausdrücklich „nur für Gewerbetreibende“; Support per E-Mail an support@dekalin.de (Footer).

**[F] Zertifikate:** Auf dekalin.com stehen nur DINOL-Zertifikate (EcoVadis Silber, ISO 9001, ISO 14001; https://www.dekalin.com/ueber-uns/standards-zertifizierungen/).
**[L]** Produktzertifikate für MS-5 (z. B. ISEGA, Bahn-Brandschutz) habe ich nicht gefunden.
**[L] „Made in Germany“** behauptet keine der Seiten (Volltextsuche in allen abgerufenen Seiten, ohne Treffer). Die Produktionsstätte ist nicht genannt.
**[A]** Auf der Kartusche im Datenblatt ist klein ein Herkunftshinweis zu erkennen. Ich lese ihn als „Made in EU“, aber unsicher. Das sollte beim Kunden geklärt werden, bevor „Made in Germany“ im Shop steht.

**[F] Unternehmensgeschichte** (https://dekalin.de/ueber-uns/):
- 1907: Gründung durch Georg Heinrich Rödiger als „Deutsche Klebstoffwerke“.
- 1914: Umwandlung in eine GmbH.
- 1935: Beginn der Zusammenarbeit mit dem Automobilbau.
- 1945: rund 80 % der Werksanlagen zerstört.
- 1999: Aus der „Dekalin Deutsche Klebstoffwerke GmbH“ entsteht per Management-Buy-out die DEKA Kleben & Dichten GmbH.
- 2012: Ausbau des Caravaning-Bereichs, Belieferung von Werkstätten und Shops, „Produkte dem Endkunden zugänglich gemacht“.
- 2014: Start des Schulungsprogramms.
- 2019: Laut Dekalin bietet die Firma als erster Klebstoffhersteller Kurse zum geprüften Klebepraktiker an.

Werte laut Website: Kundennähe, Qualität, Gesundheit (isocyanatfrei), Zuverlässigkeit, Innovation. Claim im Datenblatt: „Immer die richtige Wahl“.

**[F]** DINOL besteht laut eigener Seite seit „über sieben Jahrzehnten“, führt die Marken DINITROL und DEKALIN und hat über 50 Vertriebspartner (https://www.dinol.com/ueber-uns/).
**[L]** Wann und wie die Marke an DINOL ging, habe ich nicht gefunden. Laut US-Markenregister hat Dinol GmbH die Marke „DEKALIN“ im Januar 2023 angemeldet; registriert wurde sie im März 2025 (https://gleanmark.com/trademark/uspto-79365630).

**[F] Social Media:** Facebook /dekalinofficial, Instagram /dekalinofficial, YouTube „DEKALIN4DEKA“ mit 134 Abonnenten und 42 Videos (https://www.youtube.com/user/DEKALIN4DEKA, abgerufen am 01.11.2026).

### 1.6 SEO- und Datenqualität von dekalin.de

| Befund | Beleg |
|---|---|
| Tippfehler „Deklain“ in Titles und Meta-Descriptions | MS-1 schwarz („von Deklain“), DEKAVATOR 250 ml, Pro-Wax, 1512 schwarz, DEKAFINISHER; Blog-Title „Deklain erklärt ➱ DEKAsyl MS-1 / MS-2 / MS-5 Unterschiede“ [F] |
| „Dauererlastisch“ (Tippfehler) in der Meta-Description von MS-5 schwarz und weiß | https://dekalin.de/produkt/556/ [F] |
| Falsche Seitentitel | `/ratgeber/dichtstoff-fuer-wohnwagen-wohnmobil/` hat den Title „Unterbodenschutz Wohnmobil“; ebenso `/ratgeber/regenstreifen-wohnwagen-entfernen/`; `/unser-service/alle-downloads/` heißt „TDB für DEKACLEAN Glass Foam“ [F] |
| `/ratgeber/` zeigt den Inhalt der Startseite (gleicher Title und H1), `/branchen/` den von „Caravaning“ (Duplicate Content) | [F] |
| Viele Seiten ohne Meta-Description | Über uns, FAQ, Support, Karriere, Anwenderschulungen, Klebeanleitungen, Podcasts [F] |
| Nummerische URLs für Produkte, Kategorien und Tags | `/produkt/557/`, `/produkt-kategorie/16/` [F] |
| Doppelte Produkteinträge in der Seitenleiste | „DEKASYL MS-5 weiß“ zweimal, „DEKASEAL 8936 hellgrau“ zweimal usw. (Seitenleiste auf https://dekalin.de/wo-kommt-eigentlich-der-name-dekalin-her/) [F] |
| Uneinheitliche Schreibweise | „DEKASYL“, „DEKAsyl“, „Dekasyl“, „MS-5“, „MS 5“; Fritz Berger schreibt sogar „Dekaline“ [F] |
| H1 ist teils nur ein Werbespruch | Branchenseiten: H1 „Zeit, dass sie Profiprodukte verwenden“ [F] |
| Product-Schema mit Preis 0,00 € und „InStock“ | alle Produktseiten [F] |

---

## 2. DEKAsyl MS-5 im Detail

Quellen: Datenblatt 07.2024 (https://dekalin.de/wp-content/uploads/2024/12/Dekalin_TDB_Dekasyl-MS-5_DE.pdf), Produktseiten https://dekalin.de/produkt/557/ (weiß) und https://dekalin.de/produkt/556/ (schwarz), https://www.dekalin.com/produkt/dekasyl-ms-5/, Vergleichsartikel https://dekalin.de/dekasyl-ms-1-dekasyl-ms-2-dekasyl-ms-5-was-ist-der-unterschied/. Alle Angaben sind Herstellerangaben [F].

### 2.1 Positionierung
- „High Tack Kleb- und Dichtstoff“ auf MS-Polymer-Basis mit hoher Haftwirkung und Anfangsfestigkeit für elastische Verbindungen. Klemmzeiten verkürzen sich, Klemmen können ganz entfallen.
- MS-5 dichtet auch, wenn Materialien mit ähnlicher Steifheit verbunden werden oder zusätzlich mechanisch befestigt wird.
- In der Reihe MS-1 (Einsteiger), MS-2 (Fortgeschrittene), MS-5 (Profi) steht MS-5 oben: „Kleben und Dichten auf Meisterniveau“, „extrem reißfest“.
- dekalin.com ordnet MS-5 als „Konstruktionsklebstoff“ ein.

### 2.2 Vorteile (wörtlich laut Datenblatt)
- Frei von Lösungsmitteln, Isocyanat und PVC; laut Vergleichsartikel auch frei von Silikon und „lebensmittelunbedenklich“, „resistent gegen Schimmel“
- Sehr gute UV- und Alterungsbeständigkeit
- Hohe Anfangsfestigkeit
- Gute Haftung ohne Grundierung auf verschiedenen Untergründen
- Dauerhaft elastisch von −40 °C bis +120 °C
- Neutral, geruchlos, schnell aushärtend
- Nach der Hautbildung überlackierbar (nass in nass)
- Verträglich mit den meisten Industrielacken, mit Alkydharz- und Dispersionsfarben (Verträglichkeitstest empfohlen)

### 2.3 Anwendungen
- Elastische Verbindungen und Abdichtungen im Zug-, Wohnwagen-, Reisemobil- und Lkw-Bau
- Kleben von Fenstern, SAT-Anlagen, Solarmodul-Spoilern, halbflexiblen Solarmodulen und Dachdurchführungen
- Kleben von Kantenprofilen bei Anhängern aus Aluminium oder Polyester
- Polyesterteile mit Metallrahmen
- Laut Vergleichsartikel außerdem Verklebungen von Blech, Aluminium, PVC, Styropor und Holz; Halter und Abdeckungen „strukturell“
- dekalin.com nennt: Dachkonstruktionen, Karosseriemontage, SAT- und Solaranlagen, Spoiler
- In den Ratgebern empfiehlt Dekalin MS-5 für Solaranlage, SAT-Anlage sowie Markise und Dachträger („Kleben statt Bohren“) (https://dekalin.de/solar/, https://dekalin.de/sat-anlage/)

### 2.4 Haftgründe
Ohne Primer auf sauberen, trockenen, staub- und fettfreien Flächen aus Aluminium, Edelstahl, verzinktem Stahl, Zink, Kupfer, Messing, pulverbeschichtetem Metall, den meisten lackierten Metallen, Glas, PVC, Polyester (GFK) sowie gestrichenem und lackiertem Holz.

**Keine Haftung ohne Vorbehandlung** auf PE, PP und Teflon. Empfohlen werden die Reinigung mit DEKACLEAN ULTRA und ein Haftungstest. Bei hoher thermischer oder physikalischer Belastung, besonders bei Feuchtigkeit, empfiehlt Dekalin DEKAVATOR 22 NF.

### 2.5 Technische Daten (Datenblatt)

| Merkmal | Wert |
|---|---|
| Farben | weiß, schwarz |
| Basis / Aushärtung | MS-Polymer / durch Luftfeuchtigkeit |
| Dichte | ca. 1,4 kg/l |
| Hautbildungszeit (20 °C / 50 % r. F.) | ca. 12 min |
| Offene Zeit | < 15 min (Fügen innerhalb von 15 min) |
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
| UV- und Witterungsbeständigkeit | „hervorragend“ |
| Lagerung | ungeöffnet, trocken, +10 bis +30 °C: Kartusche 18 Monate, Schlauchbeutel 12 Monate |
| Gefahrstoffeinstufung | nicht als gefährlich eingestuft nach CLP; EUH208, EUH210 (https://www.dekalin.com/produkt/dekasyl-ms-5/) |
| Transportklassifikation | nicht zutreffend |

### 2.6 Verarbeitung
- Verarbeitung mit Hand- oder Druckluftpistole bei +5 bis 35 °C.
- **Abdichten:** innerhalb von 12 min mit einem Spachtel glätten, der in DEKAFINISHER getaucht wurde. DEKAFINISHER darf nicht in die Fuge gelangen, sonst sinkt die Haftung.
- **Kleben:** Teile innerhalb von 15 min fügen. Je wärmer es ist, desto kürzer die Verarbeitungszeit. Empfohlen ist eine Klebeschicht von 2 mm, bei stark unterschiedlicher Wärmeausdehnung dicker.
- Die SAT-Anleitung empfiehlt eine 7-mm-Raupe, daraus entsteht eine 3–5 mm dicke Klebenaht (https://dekalin.de/sat-anlage/).
- **Lackieren:** nach 10 min möglich; die beste Haftung hat die Farbe nach etwa 4 h.
- **Reinigung:** unausgehärtete Reste mit DEKACLEAN ULTRA entfernen.
- **Endfestigkeit im Flexsolar-Set:** 24–48 h, je nach Temperatur und Feuchte (https://dekalin.de/produkt/656/).

### 2.7 Gebinde, Artikelnummern, Preise

| Art.-Nr. | Größe | Verpackung | Farbe |
|---|---|---|---|
| 62522 34 | 290 ml | Kartusche | weiß |
| 62523 12 | 600 ml | Schlauchbeutel | weiß |
| 62524 34 | 290 ml | Kartusche | schwarz |
| 62700 12 | 290 ml | Set | schwarz |
| 62701 12 | 290 ml | Set | weiß |

[F] Quelle: Datenblatt. Die SKU im Shop-Schema lautet 6252234 (weiß) bzw. 6252434 (schwarz).
[F] Einen 600-ml-Schlauchbeutel in Schwarz führt das Datenblatt nicht auf; dekalin.com nennt allgemein „290 ml Kartusche, 600 ml Schlauchbeutel“.

**[F] Handelspreise (Stichprobe, 01.11.2026):**

| Händler | Artikel | Preis |
|---|---|---|
| Fritz Berger | MS-5 weiß, 290 ml (GTIN 4046085125227) | 17,99 €, Bewertung 4,96/5 aus 52 Bewertungen (https://www.fritz-berger.de/artikel/dekaline-dekasyl-ms-5-high-tack-kleb-und-dichtstoff-weiss-290-ml-20349) |
| Reimo | MS-5 weiß, 290 ml | 27,60 € (95,17 €/l) (https://www.reimo.com/camping-shop/wohnmobil-zubehoer/kleben-und-dichten/) |
| Obelink | MS-5 weiß | 16,95 € |
| Obelink | MS-5 schwarz | 36,95 € (Packungsgröße unklar) (https://www.obelink.de/wohnwagen-wohnmobil-zubehor/reinigung-instandhaltung/kleb-dichtstoffe/) |
| eBay (Induwerk) | MS-5 schwarz | 18,90 € (https://www.ebay.de/p/1554755172) |

[F] Weitere Händler: Offgridtec, Fraron, Solarkontor, Kaufland (Klebeset).
[A] Der Solar-Fachhandel ist für MS-5 ein eigener Vertriebsweg.

### 2.8 Lücken bei MS-5 [L]
- **Keine UVP und kein Preis** auf den Herstellerseiten.
- **Keine Ergiebigkeit:** wie viele Meter Raupe pro Kartusche, wie viel Kleber pro Solarmodul. Für Endkunden ist das wichtig.
- **Keine vollständige Aushärtezeit** auf der MS-5-Seite. Angegeben sind nur 4 mm in 24 h; „24–48 h Endfestigkeit“ steht nur beim Set.
- **Keine Belastungswerte für Anwendungen**, z. B. „hält ein Solarmodul bei 130 km/h“. Es gibt keine Zulassungen und keine TÜV- oder ISEGA-Nachweise für MS-5. Der Hinweis „lebensmittelunbedenklich“ im Vergleichsartikel ist nicht belegt.
- **Unbekannte Varianten:** Die 100-ml-Variante aus dem Handel und der schwarze Schlauchbeutel stehen nicht auf den Herstellerseiten.
- **Kein Herkunftsland**, keine Angabe „Made in Germany“.
- **Keine GTIN** auf den Herstellerseiten; bekannt ist nur 4046085125227 (weiß, 290 ml) über Fritz Berger.
- **Salzwasser:** Fritz Berger nennt „beständig gegen Chemikalien und Salzwasser“. Beim Hersteller steht das nur indirekt im PDF „Chemische Resistenz Dekasyl MS-Polymer“ (https://dekalin.de/dokumente//A%20DEKALIN%20Produktinfo/Chemische%20Resistenz%20Dekasyl%20MS-Polymer.pdf).
- **Keine Angaben** zu Entfernbarkeit, Wiederablösen, Haftung auf alten Klebstoffresten und Ablauf nach dem Öffnen. Sika beantwortet genau diese Fragen in seiner FAQ (Abschnitt 4.2).
- **Bewertungen** gibt es nur bei Händlern (Fritz Berger 4,96/5). Auf der Herstellerseite stehen keine Produktbewertungen.
- **Video:** Auf der Seite von MS-5 schwarz ist ein Video eingebunden („Solarplattenhalterung“); auf der Seite von MS-5 weiß fehlt es [F].

---

## 3. Präsenz bei Händlern und auf Drittseiten

| Plattform | Dekalin | Sika | TEROSON (Henkel) | Quelle |
|---|---|---|---|---|
| **Fritz Berger**, Kategorie „Klebstoffe & Dichtmittel“ (Fahrzeug > Ausbau, Umbau und Innenausbau) | 26 Artikel | 27 Artikel | 17 Artikel | Marken-Filter auf https://www.fritz-berger.de/fahrzeug/wohnwagen-und-wohnmobil-zubehoer/klebestoffe-und-dichtmittel/ |
| | MS-5: 4,96/5 aus 52 Bewertungen | Sikaflex-522 (100 ml): 4,92/5 aus 52; Sikaflex-554: 4,5/5 aus 2 | MS 939: 5/5 aus 2 | Product-JSON-LD der Fritz-Berger-Produktseiten |
| **Reimo**, Kategorie „Kleben und Dichten“ | Hersteller „DEKALIN“, mehrere Artikel | eigene Unterkategorie „Sika Produkte“; der SEO-Text der Kategorie dreht sich fast nur um Sikaflex („Welches Sikaflex für Dachluke?“) | Hersteller „HENKEL“ (Terostat RB 2759, Terostat-Bänder, MS 9221) | https://www.reimo.com/camping-shop/wohnmobil-zubehoer/kleben-und-dichten/, https://www.reimo.com/camping-shop/wohnmobil-zubehoer/sika-produkte/, https://www.reimo.com/henkel/ |
| **Obelink**, „Kleb- & Dichtstoffe“ (62 Artikel) | MS-2, MS-5, MS-7, 1512, 8936-Kit, 2K-90, DEKAFINISHER, DEKAPHON | Sikaflex-522, 554, 252, Lastomer 710 | auf Seite 1 nicht vorhanden | https://www.obelink.de/wohnwagen-wohnmobil-zubehor/reinigung-instandhaltung/kleb-dichtstoffe/ |
| **Eigenmarken der Händler** | Fritz Berger führt „Berger Kraftkleber MS-Polymer Nr. 5“, „Nr. 1-2“ und „Nr. 7“ (gleiche Nummern wie Dekalin) | | | Fritz-Berger-Kategorie |
| **Amazon.de** | Websuche ergab keinen Treffer | über eBay und Händler präsent | gewerblich (RS, Völkner) | Websuchen vom 01.11.2026 |
| **eBay.de** | mehrere Angebote | sehr viele Angebote, ein Händler mit 4,9 aus 419 Bewertungen | – | https://www.ebay.de/p/1554755172 |
| **Wikipedia (de)** | „Dekalin“ führt zur Chemikalie Decalin | Artikel „Sika AG“ (Sikaflex leitet weiter) | kein Artikel; nur im Artikel „Henkel (Unternehmen)“ | de.wikipedia API |
| **Reddit / englische Foren** | keine Treffer | sehr präsent (motorhomefun.co.uk, exploroz, t6forum: „Sikaflex 252/512/522 für Solarmodule“) | vereinzelt | https://www.motorhomefun.co.uk/forum/threads/which-sikaflex-for-holding-something-to-the-roof.226393/ |
| **Deutsche Foren** | motor-talk (Dachluken, „Dekalin 8936 als Alternative“), bauexpertenforum | motor-talk | – | https://www.motor-talk.de/forum/wohnwagen-dachluken-abdichten-t7509212.html |
| **Camping-Medien** | PiNCAMP/ADAC: Dekalin und Sika als „Marktführer“; CamperStyle mit mehreren Artikeln, Gewinnspielen und Podcast; Auto Zeitung „Praxis-Check“ MS-8 (30.08.2024) | PiNCAMP; Auto Zeitung nennt Sikaflex-522 als Alternative | – | https://www.pincamp.de/magazin/ratgeber/wohnwagen/wohnwagen-dichtmasse-tipps, https://camperstyle.de/solarmodul-oder-sat-anlage-nachruesten-so-gelingt-die-montage-dauerhaft-421047/, https://www.autozeitung.de/dekasyl-dicht-und-klebstoff-ms-8-test.html |
| **Podcasts** | podcast.de Folge 074 vergleicht: MS-2 ähnlich Sikaflex-221, MS-5 ähnlich Sikaflex-252, Dekalin „ohne Primer“ | (als Vergleichsmaßstab) | – | https://www.podcast.de/episode/624233374/074-abdichten-und-kleben-am-wohnwagen-wohnmobil |
| **YouTube** | eigener Kanal: 134 Abonnenten, 42 Videos | Videos zu Anwendungen und PowerBox, eingebunden auf sika.de/caravan | – | https://www.youtube.com/user/DEKALIN4DEKA |
| **Solar-Händler** | MS-5 und Klebesets bei Offgridtec, Fraron, Solarkontor | Sikaflex-252 in Klebesets bei photovoltaik4all; Büttner-Spoiler-Set mit Sikaflex | – | https://www.photovoltaik4all.de/caravan-modulmontage-set-spoiler-profi/pn21855 |

**[A] Bewertung:**
- Im deutschen Caravan-Fachhandel ist Dekalin so präsent wie Sika.
- Im offenen Web gewinnt Sika: Wikipedia, englische Foren, Kategorietexte der Händler, Marktplatz-Bewertungen.
- Gerade diese Quellen nutzen Sprachmodelle als Trainings- und Suchdaten. Antworten von ChatGPT oder Perplexity werden deshalb vermutlich eher „Sikaflex“ nennen.
- Das sollte man in der Challenge mit echten Testfragen prüfen, z. B. „Womit klebe ich ein Solarmodul aufs Wohnmobil?“ und „Welche Dichtmasse für Dachluke Wohnwagen?“.

---

## 4. Wettbewerber

### 4.1 Auswahl und Begründung

| Kandidat | Relevanz für Caravan-Endkunden in DE | Bewertung |
|---|---|---|
| **Sika (Sikaflex, SikaLastomer)** | Im Handel gleich stark wie Dekalin (Fritz Berger 27 Artikel, Reimo mit eigener Unterkategorie). Eigene DIY-Caravan-Seite für Privatanwender. Produkte entsprechen Dekalin fast eins zu eins: Sikaflex-522 ↔ MS-2/MS-6, Sikaflex-554 ↔ **MS-5**, SikaLastomer-514 (abtupfbar) ↔ DEKASEAL 8936. Serienlieferant der Caravan-Hersteller. | **Wettbewerber 1:** Marktführer und Maßstab, den KI-Antworten am ehesten nennen. |
| **TEROSON (Henkel)** | Fritz Berger 17 Artikel (MS 939, MS 935, MS 660, MS 9220, PU 9225, RB 2759); Reimo führt Terostat/Henkel. Ebenfalls MS-Polymer und Butyl, Kfz-Reparatur-Herkunft wie Dekalin. Website ist reines B2B (henkel-adhesives.com), ohne Caravan-Ratgeber. | **Wettbewerber 2:** Direkter Konkurrent im selben Regal und mit gleicher Herkunft (Kfz-Werkstatt). Hinter TEROSON steht ein Großkonzern, die Kommunikation an Endkunden ist aber genauso schwach wie bei Dekalin. Daran lässt sich gut zeigen, dass die Marke mit sichtbaren Antworten gewinnt. |
| Innotec (Adheseal, Easy Seal) | vor allem Werkstatt und Marktplatz (Kaufland), in den Caravan-Shops kaum präsent | geringe Relevanz |
| Soudal (Fix All), Pattex (Henkel), Fischer | Baumarkt-DIY, ohne Caravan-Fokus | Alternative für den Endkunden, aber kein Fachwettbewerb |
| Würth, Berner | Profi- und Werkstattkanal | [A] Würth ist zudem wohl Mutterkonzern von DINOL (https://www.dinol.com/ueber-uns/), also eher Schwester als Wettbewerber. |
| Eigenmarken der Händler (Berger Nr. 5, Obelink Montagekleber, Carbest) | preisaggressiv direkt neben Dekalin | als Preisdruck erwähnenswert, aber keine Marke mit eigener Website |

**Empfehlung: Sika und TEROSON.**
- Sika ist der Benchmark für Sichtbarkeit.
- TEROSON ist der Konkurrent, der Dekalin strukturell am ähnlichsten ist.
- [A] Alternativ ließe sich Fritz Berger mit seiner Eigenmarke betrachten. Der Händler steht dann aber zugleich im Wettbewerb und ist Vertriebspartner.

### 4.2 Sika: Analyse

**Website und Struktur** [F]:
- https://www.sika.de/caravan leitet auf https://deu.sika.com/de/industrie/transportation/kleben-und-dichten-am-caravan.html weiter.
- Eine Weiche fragt zuerst: „Für gewerbliche Anwender“ oder „Für Privatanwender“.
- **DIY-Seite** (https://deu.sika.com/de/industrie/kleben-und-dichten-am-caravan.html): Title „DIY – Kleben und Dichten am Caravan und Wohnmobil | Sika Deutschland“, mit Meta-Description. Inhalte:
  - Einstieg über Anwendungen am Fahrzeug („Abbildung auf unserer Startseite“, laut FAQ)
  - Vorbehandlungstabelle (PDF)
  - Produkt-Highlights Sikaflex-522, Sikaflex-554, SikaLastomer-514
  - Händlersuche, Newsletter
  - Sika Caravan PowerBox (Set für viele Anwendungen, mit Video)
- **FAQ** (https://deu.sika.com/de/industrie/kleben-und-dichten-am-caravan/faq.html): 28 ausführliche Antworten, u. a.:
  - Solarmodul kleben
  - wiederlösbare Abdichtung
  - Was bedeutet „primerlos“?
  - Entfernen von Sikaflex, Haftung auf Altresten, Überlackieren
  - Temperatur bis 90 °C
  - Styropor verkleben
  - Kartusche öffnen und wieder verschließen
  - Wo kaufen?
- **Kein FAQPage-Schema** auf der FAQ-Seite [F]; nur BreadcrumbList.
- **Produktseite Sikaflex-554** (https://deu.sika.com/de/industrie/transportation/fuer-wartung-undreparatur/sikaflex-554.html): technische Daten als HTML-Tabelle mit Prüfnormen, chemische Beständigkeit, Anleitung zur Verarbeitung, Datenblatt und SDB.
  - Hinweis auf der Seite: „nur für erfahrene Anwender geeignet“.
  - **Kein Product-Schema**, nur BreadcrumbList [F].
- **robots.txt** (https://deu.sika.com/robots.txt): offen für alle Bots; für GPTBot sind nur einzelne Kampagnenseiten gesperrt.
- **Kaufen:** Kein Online-Shop für Endkunden. Die FAQ verweist auf Fachhändler und Großhandelspartner [F].

**Technischer Vergleich mit MS-5** (Herstellerangaben, teils unterschiedliche Prüfnormen):

| | DEKAsyl MS-5 | Sikaflex-554 |
|---|---|---|
| Basis | MS-Polymer | STP (silanterminiertes Polymer) |
| Hautbildung | ca. 12 min (20 °C) | 25 min (23 °C) |
| Shore A | ca. 55 | 55 |
| Zugfestigkeit | ca. 2,8 MPa | 3,5 MPa |
| Bruchdehnung | ca. 210 % | 500 % |
| Zugscherfestigkeit | ca. 2,5 MPa | 2,5 MPa |
| Temperaturbeständigkeit | −40 bis +120 °C, kurzzeitig 180 °C | −50 bis +90 °C |
| Verarbeitung | +5 bis +35 °C | +5 bis +40 °C |
| Lagerfähigkeit | 18 Monate (Kartusche) | 12 Monate |
| Nachweise | keine genannt | DIN EN 45545-2, ISEGA |
| Gebinde | 290 ml, 600 ml | 300 ml, 600 ml, 23 l, 195 l |

[A] Diese Argumente sprechen für MS-5:
- höhere Temperaturbeständigkeit, wichtig auf dunklen Dächern und unter Solarmodulen
- schnellere Hautbildung und Anfangsfestigkeit
- längere Lagerfähigkeit
- Sika richtet MS-5-Gegenstück 554 ausdrücklich an erfahrene Anwender. Dekalin dagegen erklärt MS-5 Endkunden ohne Einschränkung.

**Präsenz außerhalb der Website:** Wikipedia, Reimo-Kategorietext, Forenpräsenz, Marktplatz-Bewertungen, Solar-Klebesets von Drittanbietern (Abschnitt 3).

### 4.3 TEROSON (Henkel): Analyse

**Website** [F]:
- Die Produkte stehen auf next.henkel-adhesives.com (B2B-Portal für Industrie und Kfz-Reparatur).
- Beispiel TEROSON MS 939 (https://next.henkel-adhesives.com/de/de/products/industrial-sealants/central-pdp.html/teroson-ms-939/000000268232-ms939.html):
  - Title „TEROSON® MS 939 | Henkel Adhesives“, **keine Meta-Description**.
  - **Product-Schema** mit brand „TEROSON“, sku und description; die Organization-Daten sind leer (telephone "", sameAs [""]). Es gibt **SpeakableSpecification**.
  - Branchen: Luft- und Raumfahrt, Energie, Automobil, Kfz-Reparatur, Industrie. **Caravan wird nicht erwähnt.**
  - Statt Preis und Händler gibt es eine „Bestellanfrage“ („Bitte kontaktieren Sie uns für Bestellmöglichkeiten“).
- robots.txt ist sehr lang (Pfadsperren für Konfigurationsseiten), keine Sperren für KI-Bots erkennbar (https://next.henkel-adhesives.com/robots.txt).
- **Kein Ratgeber und keine FAQ zum Thema Caravan gefunden.** Die Websuche ergab nur einen Henkel-Katalog zur Karosseriereparatur, in dem einzelne Produkte als „für Caravans geeignet“ markiert sind.

**Handel:**
- Fritz Berger mit 17 Artikeln; MS 939 für 17,86 €, 5/5 aus 2 Bewertungen.
- Reimo (Terostat RB 2759 Butyl, Terostat-Dichtbänder, MS 9221 Kraftkleber).
- Gewerbliche Händler (RS Components, Rubix, Völkner).
- Reimo schreibt den Namen falsch: „Terrostat“ [F].

**[A] Fazit TEROSON:** Großer Konzern, gute technische Datenblätter in vielen Sprachen. Für Endkunden, die nach einem Anwendungsfall suchen, gibt es aber keine eigene Seite. In KI-Antworten taucht TEROSON vermutlich nur auf, wenn jemand nach Werkstatt- oder Kfz-Produkten fragt.

### 4.4 Vergleichsmatrix KI-Sichtbarkeit

| Kriterium | Dekalin | Sika | TEROSON |
|---|---|---|---|
| Eigene Endkunden-Inhalte zu Caravan-Anwendungen | **stark**: Ratgeber, FAQ, Akademie, Blog, Podcasts, Buch, DEKABot | **stark**: DIY-Seite, 28 FAQ, Videos, PowerBox | **fehlt** |
| FAQ-Schema | ja, aber mit Dummy-Einträgen | nein | nein |
| Product-Schema | ja, aber Preis 0 € und keine Marke (.de); gut gepflegt auf .com | nein | ja (dünn) |
| Technische Daten im HTML | ja (Fließtext; Tabelle nur im PDF) | ja (HTML-Tabelle mit Normen) | teilweise / PDF |
| Klare Markeneinheit | **schwach** (DEKA vs. DINOL, zwei Domains, Ranstadt vs. Reichelsheim) | stark | mittel (Henkel-Dachmarke) |
| Wikipedia | Begriff ist durch die Chemikalie belegt | ja | nein |
| Foren, Reddit, international | gering (DE-Foren vereinzelt) | sehr hoch | gering |
| Händler-Bewertungen | gut (Fritz Berger 4,96/5 aus 52 für MS-5) | gut und zahlreich | wenige |
| Direktkauf beim Hersteller | nein (nur Buch) | nein | nein |
| Fachmedien | PiNCAMP, CamperStyle, Auto Zeitung | PiNCAMP, Auto Zeitung, Reimo-Texte | kaum |

**[A] Hebel für die KI-Sichtbarkeit von Dekalin (Ideen für Aufgabe 2):**
1. **Eine Marke, eine Quelle:** dekalin.de und dekalin.com zusammenführen oder eindeutig verknüpfen, z. B. über ein Organization-Schema mit sameAs, parentOrganization DINOL und gleichem Namen und gleicher Adresse.
2. **Wikidata und Wikipedia:** einen Eintrag für die Marke anlegen und eine Begriffsklärung „Dekalin (Marke)“ gegen „Decalin“.
3. **Product-Schema im Shopify-Shop:** mit brand, manufacturer, gtin13 (4046085125227), echtem Preis, Verfügbarkeit, additionalProperty (alle Werte aus dem Datenblatt) und aggregateRating aus echten Shop-Bewertungen.
4. **Anwendungsseiten mit klarer Antwort am Anfang:** etwa „Solarmodul aufs Wohnmobil kleben: Antwort in 2 Sätzen, dann Anleitung, Produkt, Mengen, Zeiten“ als HowTo und FAQ.
5. **Vergleichsseite „MS-5 vs. Sikaflex-552/554“:** sachlich, mit Daten. Sprachmodelle übernehmen gern solche Gegenüberstellungen.
6. **Datenpflege:** Tippfehler „Deklain“, Lorem Ipsum und falsche Titles beheben; ein `llms.txt` anlegen.
7. **Drittquellen ausbauen:** Händler-Kategorietexte (Reimo-Text bisher nur Sika), Produktwissen auf Amazon, Reddit und YouTube, Kooperationen mit Fachmedien.

---

## 5. Inspiration für die Navigation: Endkunden-Shops der Branche

| Shop | Einordnung der Kleber | Filter und Facetten | Erkenntnis |
|---|---|---|---|
| **Fritz Berger** | Fahrzeug > Ausbau, Umbau und Innenausbau > Klebstoffe & Dichtmittel (Breadcrumb) [F] | **Produktart:** Nahtdichter, Butylmasse, Hybrid-Klebstoff, Klebstoff, Power-Kleber, Band, Dichtmasse, Lösungsmittel; **Marke**; Filialbestand [F] | Sortiert nach Produkttyp, nicht nach Anwendung. Der Endkunde muss selbst wissen, was eine „Butylmasse“ ist. |
| **Reimo** | Camping-Shop > Wohnmobil-Zubehör > Kleben und Dichten, zusätzlich Ersatzteile > Reparaturen > Kleben und Abdichten; Marken-Unterkategorie „Sika Produkte“ [F] | Hersteller: 3M, DEKALIN, GuG, HENKEL u. a. [F] | Der Kategorietext beantwortet Fragen wie „Welches Sikaflex für Dachluke?“, also Anwendungsfragen, aber nur im Fließtext. |
| **Obelink** | Wohnwagen-/Wohnmobil-Zubehör > Reinigung & Instandhaltung > Kleb- & Dichtstoffe (62 Artikel) [F] | Farbe, Marke, Preis, Lager [F] | Ebenfalls ohne Anwendungslogik. |
| **Sika DIY** | Einstieg über eine Grafik des Fahrzeugs mit Anwendungen und passenden Produkten [F, laut FAQ Nr. 1] | – | Hier ist die Anwendungslogik umgesetzt: „Was willst du wo machen?“ |
| **Dekalin selbst** | 5 Farbkategorien nach Tätigkeit (Reinigen, Kleben & Dichten, Dichten, Schützen, Kleben & Reparieren) [F] | – | Ein guter Ausgangspunkt, aber die Begriffe sind technisch: Wer kennt den Unterschied zwischen „Dichten“ und „Kleben & Dichten“? |
| **Würth** | Online-Klebstofffinder: Auswahl der zwei Materialien, die verbunden werden sollen [F] (Broschüre https://prueflabor.wuerth-industrie.com/web/media/downloads/brochures/de_wis/anaerobe-klebstoffe.pdf) | – | Logik „Material A + Material B“ als Filter oder Produktfinder |

**[A] Kein Caravan-Shop sortiert konsequent nach Anwendungsfall.** Genau darin kann sich ein Dekalin-Shop unterscheiden.

### 5.1 Vorschlag: Kategorisierung nach Anwendungsfällen (Shopify Vision Theme) [A]

**Prinzip:** Die Hauptnavigation beantwortet die Frage „Was hast du vor?“. Filter beantworten „Wo am Fahrzeug?“ und „Auf welchem Material?“. Produktnamen erscheinen erst auf der Ergebnisebene, zusammen mit einer Klartext-Unterzeile, z. B. „DEKAsyl MS-5 – Kraftkleber für Solarmodule & Anbauteile“.

**Mega-Menü, erste Ebene:**

1. **Abdichten** – „Es kommt Wasser rein / soll dicht bleiben“
   - Fenster & Dachluken eindichten (z. B. Heki, MaxxFan)
   - Serviceklappen & Türen (wiederlösbar)
   - Fugen & Nähte außen (sichtbar, überlackierbar)
   - Kabel- & Dachdurchführungen, Antennen/LTE
   - Kantenleisten & Keder
   - Bad & Küche (innen)
2. **Kleben & Montieren** – „Etwas soll ohne Bohren halten“
   - Solarmodul kleben (starr / flexibel)
   - SAT-Anlage & Antennen
   - Markise, Dachträger, Fahrradträger & Anbauteile
   - Halter, Leisten & Innenausbau
   - Scheiben & Echtglas
   - Großflächen & Seitenwände (2K, Profi)
3. **Reparieren** – „Etwas ist kaputt“
   - Risse in Kunststoff, GFK & Stoßstange
   - Ausgerissene Schraublöcher
   - Wasserschaden beheben (Set und Ratgeber)
4. **Schützen** – „Unterboden & Rost“
   - Unterbodenschutz Wohnmobil / Wohnwagen
   - Hohlraumschutz
   - Radkästen
5. **Reinigen & Vorbereiten** – „Damit es hält“
   - Haftreiniger & Haftvermittler
   - Glätten & Fugen-Finish
   - Regenstreifen & Fensterreinigung
6. **Sets & Zubehör**
   - Klebesets (Solar, SAT, Abdichtung)
   - Kartuschenpistolen, Spachtel, Tücher
   - Buch „Klebt nicht gibt's nicht!“
7. **Hilfe & Wissen**
   - Produktfinder (3 Fragen: Was? Wo? Welches Material?)
   - Anleitungen & Videos (Akademie), FAQ, Datenblätter, Händler

**Filter** (Shopify Search & Discovery über Produkt-Metafelder):
- Einsatzort: Dach, Außenwand, Fenster/Türen, Unterboden, Innenraum
- Untergrund: Aluminium, GFK/Polyester, lackiertes Blech, Glas, Holz, PVC/ABS-Kunststoff
- Eigenschaften: überlackierbar, wiederlösbar/abtupfbar, transparent, hohe Anfangsfestigkeit
- Klebkraft-Skala 1–5: MS-1 = 1, MS-2 = 3, MS-5 = 5. [A] Diese Skala würde die Staffelung, die Dekalin selbst kommuniziert, sichtbar machen.
- Farbe, Gebinde (100 / 290 / 600 ml), Preis

**Zuordnung (Beispiele):** Ein Produkt erscheint in mehreren Kollektionen, z. B. als automatische Kollektion über Tags oder Metafelder.

| Produkt | Kollektionen |
|---|---|
| **DEKAsyl MS-5** | Solarmodul kleben; SAT-Anlage; Markise/Dachträger/Anbauteile; Kabel- & Dachdurchführungen; Kantenleisten (Kleben); Fenster kleben |
| DEKAsyl MS-1 / MS-2 / MS-6 | Fugen & Nähte; Bad & Küche (MS-6, MS-7); Kantenleisten; Fenster |
| DEKASEAL 8936 | Serviceklappen & Türen (wiederlösbar); Fenster & Dachluken (verdeckte Fuge) |
| DEKASEAL 1512 | Fenster & Dachluken (sichtbare Fuge, überlackierbar); Durchführungen |
| DEKAPUR 2K-90 | Risse in Kunststoff, Stoßstange, Schraublöcher |
| DEKAPUR 2K-6000 | Großflächen und Seitenwände |
| DEKAPHON 9735 / 958 / Pro-Wax | Unterbodenschutz, Hohlraum, Radkästen |
| DEKACLEAN, DEKAVATOR, DEKAFINISHER | Reinigen & Vorbereiten, außerdem als „Passt dazu“ auf jeder Kleber-Seite |

**Produktseite MS-5, Bausteine im Vision Theme** [A]:
- Klartext-Überschrift über dem Produktnamen
- „Ideal für“-Icons: Solarmodul, SAT-Anlage, Markise
- Ampel zu den Haftgründen
- Technische Daten als Tabelle (HTML, nicht nur PDF)
- Schritt-für-Schritt-Anleitung (aus https://dekalin.de/solar/)
- „Passt dazu“: DEKACLEAN Tuch, DEKAVATOR 22 NF, DEKAFINISHER bzw. Upsell auf das Klebeset
- FAQ-Block. Die Fragen aus Abschnitt 2.8 schließen die Lücken (Ergiebigkeit, Aushärtung, Entfernen)
- Vergleichsbox „MS-1 vs. MS-2 vs. MS-5“
- Downloads: Datenblatt, SDB, Chemische Resistenzen

---

## 6. Offene Punkte für das Briefing (beim Kunden zu klären) [L]
- Wer betreibt den Shop: DEKA oder DINOL? Welche Domain? Wie wird mit den Handelspartnern (Fritz Berger, Reimo) umgegangen, damit kein Kanalkonflikt entsteht?
- UVP und Preise, Ergiebigkeit, vollständige Aushärtezeit, Herkunftsland und Produktion, GTINs aller Varianten
- Gibt es MS-5 als 100-ml-Tube und als schwarzen Schlauchbeutel offiziell?
- Gilt die Aussage „isocyanatfrei“ für das ganze Sortiment? (Widerspruch bei 2K-90)
- Gibt es Prüfnachweise (TÜV, Windkanal, ISEGA) für die Anwendung „Solarmodul kleben“?

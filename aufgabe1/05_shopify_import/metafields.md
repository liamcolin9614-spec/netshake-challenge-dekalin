# Metafelder & Metaobjekte – Dekalin-Shop

Anlegen unter **Einstellungen → Benutzerdefinierte Daten → Produkte** (bzw. **Metaobjekte**) **vor** dem CSV-Import, damit die Metafeld-Spalten der `products.csv` (`usp_zeile`, `klartext_untertitel`, `interne_notiz`) übernommen werden. Alle Metafelder mit „Zugriff für Storefront“ aktivieren (außer `interne_notiz`) und die Filter-Metafelder für **Search & Discovery** freigeben.

Werte für MS-5 aus dem Datenblatt 07.2024 [F]; [A] = Annahme.

---

## 1. Metaobjekt-Definitionen

### 1.1 `faq_eintrag` (FAQ-Eintrag)
| Feld | Key | Typ |
|---|---|---|
| Frage | `frage` | Einzeiliger Text (Pflicht) |
| Antwort | `antwort` | Rich Text (Pflicht) |
| Thema | `thema` | Einzeiliger Text, Auswahl: Anwendung · Haftung · Zeiten · Verarbeitung · Produktwahl · Lagerung |

Einträge MS-5: 10 Stück, Texte 1:1 aus `04_pdp_texte.md`, Section 12. Handles: `ms5-solarmodul-ohne-bohren`, `ms5-primer`, `ms5-aushaertezeit`, `ms5-ueberlackieren`, `ms5-unterschied-ms1-ms2`, `ms5-silikon`, `ms5-temperaturen`, `ms5-verbrauch`, `ms5-farben`, `ms5-reste-haltbarkeit`.

### 1.2 `technische_angabe` (Zeile der Spezifikationstabelle)
| Feld | Key | Typ |
|---|---|---|
| Merkmal | `merkmal` | Einzeiliger Text |
| Wert | `wert` | Einzeiliger Text |
| Prüfnorm | `norm` | Einzeiliger Text (optional) |
| In Kurztabelle zeigen | `kurz` | Boolescher Wert |

[?] Vision bewirbt eine „metafeldgesteuerte Spezifikationstabelle“; welche Datenquelle der Block erwartet (Metaobjekt-Liste oder Key-Value-Metafeld), im Editor prüfen. Fallback: Custom-Liquid-Block, der `product.metafields.custom.tech_daten.value` als Tabelle rendert.

---

## 2. Produkt-Metafelder (namespace `custom`)

| # | Name | namespace.key | Typ | Filter | Wert DEKAsyl MS-5 |
|---|---|---|---|---|---|
| 1 | USP-Zeile | `custom.usp_zeile` | Einzeiliger Text | – | Klebt Solarmodul, SAT-Anlage & Anbauteile ohne Bohren – und dichtet gleich mit. |
| 2 | Klartext-Untertitel (Produktkarte) | `custom.klartext_untertitel` | Einzeiliger Text | – | Kraftkleber für Solarmodule & Anbauteile |
| 3 | Infobox-Text über Titel | `custom.infobox_text` | Einzeiliger Text | – | Für Solarmodule, SAT-Anlage & Anbauteile – Kleben statt Bohren |
| 4 | Lieferhinweis | `custom.lieferhinweis` | Einzeiliger Text | – | Auf Lager – in 1–3 Werktagen bei dir [A] |
| 5 | Kurz-Bullets | `custom.kurz_bullets` | Liste: einzeiliger Text | – | Hält sofort: Hohe Anfangsfestigkeit – Klemmen oft unnötig · Ohne Primer: Haftet auf Alu, GFK, Glas, PVC und lackiertem Metall · Für heiße Dächer: dauerelastisch von −40 bis +120 °C · Nach der Hautbildung nass in nass überlackierbar |
| 6 | Bild-Callouts | `custom.callouts` | Liste: einzeiliger Text | – | Hält sofort – weniger Klemmen · −40 bis +120 °C · Ohne Primer auf Alu, GFK & Glas |
| 7 | Anwendungen (Klartext) | `custom.anwendungen` | Liste: einzeiliger Text | – | Solarmodul & Spoiler · SAT-Anlage & Antenne · Markise, Dachträger & Anbauteile · Fenster & Dachdurchführungen · Kantenprofile an Anhängern (Alu/Polyester) · Halter & Abdeckungen im Ausbau · Zug-, Wohnwagen-, Reisemobil- und Lkw-Bau |
| 8 | Einsatzort | `custom.einsatzort` | Liste: einzeiliger Text, **Auswahlliste**: Dach · Außenwand · Fenster & Türen · Unterboden & Radkasten · Innenraum | **ja** | Dach · Außenwand · Fenster & Türen · Innenraum |
| 9 | Untergrund (ohne Primer) | `custom.untergrund` | Liste: einzeiliger Text, Auswahlliste: Aluminium · Edelstahl · Verzinkter Stahl · Lackiertes Metall · Glas · GFK/Polyester · PVC · Holz (lackiert/gestrichen) · Kunststoff PE/PP | **ja** | Aluminium · Edelstahl · Verzinkter Stahl · Lackiertes Metall · Glas · GFK/Polyester · PVC · Holz (lackiert/gestrichen) |
| 10 | Untergrund – nicht geeignet | `custom.untergrund_nicht` | Liste: einzeiliger Text | – | PE · PP · Teflon |
| 11 | Eigenschaften | `custom.eigenschaften` | Liste: einzeiliger Text, Auswahlliste: überlackierbar · wiederlösbar/abtupfbar · transparent · hohe Anfangsfestigkeit · silikonfrei · isocyanatfrei · lösemittelfrei · geruchlos | **ja** | überlackierbar · hohe Anfangsfestigkeit · silikonfrei · isocyanatfrei · lösemittelfrei · geruchlos |
| 12 | Klebkraft-Stufe | `custom.klebkraft` | Ganzzahl (1–5) | **ja** | 5 [A: Skala MS-1 = 1, MS-2 = 3, MS-5 = 5] |
| 13 | Stufe (Klartext) | `custom.stufe` | Einzeiliger Text | – | Profi |
| 14 | Technische Daten | `custom.tech_daten` | Liste: Metaobjekt-Referenz → `technische_angabe` | – | 21 Einträge, siehe 2.1 |
| 15 | Technisches Datenblatt | `custom.tdb_pdf` | Datei (PDF) | – | Dekalin_TDB_Dekasyl-MS-5_DE.pdf (Quelle: dekalin.de/wp-content/uploads/2024/12/…) |
| 16 | Sicherheitsdatenblatt | `custom.sdb_pdf` | Datei (PDF) | – | SDB DEKAsyl MS-5 [A: von Dekalin anfordern] |
| 17 | Chemische Resistenz | `custom.resistenz_pdf` | Datei (PDF) | – | Chemische Resistenz Dekasyl MS-Polymer.pdf [F] |
| 18 | Anleitung (Seite) | `custom.anleitung_seite` | Seitenreferenz | – | /pages/anleitung-solarmodul-kleben |
| 19 | Video | `custom.video_url` | URL | – | YouTube-Video „Solarplattenhalterung“ (Kanal DEKALIN4DEKA) [A: URL einsetzen] |
| 20 | FAQ | `custom.faq` | Liste: Metaobjekt-Referenz → `faq_eintrag` | – | 10 Einträge (1.1) |
| 21 | Set-Empfehlung | `custom.set_empfehlung` | Produktreferenz | – | solar-montage-set |
| 22 | Ergänzende Produkte | `shopify--discovery--product_recommendation.complementary_products` (Standard von Search & Discovery) | Liste: Produktreferenz | – | dekaclean-ultra-haftreiniger · dekavator-22-nf-haftvermittler · dekafinisher-glaettmittel · kartuschenpresse-290-310-ml |
| 23 | Kennzeichnung (CLP) | `custom.kennzeichnung` | Mehrzeiliger Text | – | Nicht als gefährlich eingestuft nach CLP. EUH208 [A: Stoffname aus SDB]. EUH210: Sicherheitsdatenblatt auf Anfrage erhältlich. |
| 24 | Hersteller (GPSR) | `custom.hersteller_gpsr` | Mehrzeiliger Text | – | [A: DEKA Kleben & Dichten GmbH, Kirchgasse 1, 61203 Reichelsheim ODER DINOL GmbH, Pyrmonter Str. 76, 32676 Lügde – klären] · support@dekalin.de |
| 25 | Interne Notiz | `custom.interne_notiz` | Mehrzeiliger Text, **kein** Storefront-Zugriff | – | Annahmen zu Preis/Gewicht (aus CSV) |

### 2.1 Werte `custom.tech_daten` für MS-5 (Metaobjekte `technische_angabe`)
| merkmal | wert | norm | kurz |
|---|---|---|---|
| Basis | MS-Polymer | | false |
| Aushärtung | durch Luftfeuchtigkeit | | false |
| Farben | weiß, schwarz | | false |
| Dichte | ca. 1,4 kg/l | | false |
| Hautbildungszeit (20 °C / 50 % r. F.) | ca. 12 min | | **true** |
| Offene Zeit | < 15 min | | false |
| Durchhärtung nach 24 h | ca. 4 mm | | false |
| Shore-A-Härte | ca. 55 | DIN 53505 | **true** |
| Volumenänderung | < 3 % | DIN 52451 | false |
| Standfestigkeit | ca. 700 Pa | Rheometer | false |
| Zugspannung bei 100 % Dehnung | ca. 1,7 MPa | | false |
| Zugspannung bei Bruch | ca. 2,8 MPa | | false |
| Bruchdehnung | ca. 210 % | | false |
| Scherspannung | ca. 2,5 MPa | DIN 53283 | false |
| Weiterreißfestigkeit | ca. 14 N/mm | | false |
| Lösemittel / Isocyanat | 0 % / 0 % | | false |
| Temperaturbeständigkeit | −40 °C bis +120 °C, kurzzeitig +180 °C (max. 20 min) | | **true** |
| Verarbeitungstemperatur | +5 °C bis +35 °C | | false |
| UV- und Witterungsbeständigkeit | hervorragend | | false |
| Haftung ohne Primer | Alu, Edelstahl, verz. Stahl, Glas, PVC, GFK, lackiertes Metall/Holz | | **true** |
| Lagerfähigkeit (ungeöffnet, +10 bis +30 °C) | Kartusche 18 Monate, Schlauchbeutel 12 Monate | | false |
| Überlackierbar | ja, nach Hautbildung nass in nass | | **true** |

(`kurz = true` → 5 Werte im Specification-table-Block der Buybox; alle Werte im Tab „Technische Daten“.)

---

## 3. Varianten-Metafelder (optional)

| Name | namespace.key | Typ | Wert |
|---|---|---|---|
| Swatch-Bild | `custom.swatch_bild` | Datei (Bild) | Weiß: Foto weiße Fuge · Schwarz: Foto schwarze Fuge · 600 ml: Mini-Packshot Beutel [?: Vision-Swatches können laut Fuel-Doku „product variant swatches“ über Bilder gepflegt werden; Mechanismus prüfen – alternativ Shopify-Kategorie-Metafeld „Farbe“ mit Swatch-Bild] |
| Ergiebigkeit | `custom.ergiebigkeit` | Einzeiliger Text | 290 ml: ca. 7 m Raupe Ø 7 mm [A] · 600 ml: ca. 15 m [A] |

## 4. Kollektions-Metafelder

| Name | namespace.key | Typ | Zweck |
|---|---|---|---|
| Einleitung kurz | `custom.einleitung` | Mehrzeiliger Text | 1–2 Sätze über dem Produktraster (ein Template für alle Kollektionen) |
| Anleitung | `custom.anleitung_seite` | Seitenreferenz | „So geht's“-Link im Kollektionskopf |
| Verwandte Kollektionen | `custom.verwandt` | Liste: Kollektionsreferenz | Unter Kollektionen mit < 6 Produkten |

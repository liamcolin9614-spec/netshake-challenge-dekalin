# Menüs – exakt wie in Shopify → Inhalte → Menüs (Navigation) anzulegen

Hinweise:
- Ebene 1 = Hauptpunkt, Ebene 2 = Spaltentitel im Mega-Menü, Ebene 3 = Link. Vision baut das Mega-Menü aus Menüs mit **dritter Ebene**; danach im Theme-Editor je Hauptpunkt einen Block **„Mega-Menu“** im **Header** hinzufügen und den Hauptpunkt auswählen [V: Fuel-Doku „How do I set up Mega Menus for Vision theme?“].
- Spaltentitel (Ebene 2) verlinken auf die übergeordnete Welt-Kollektion, damit ein Klick auch mobil sinnvoll ist.
- „Alle anzeigen“ jeweils als **letzter** Eintrag (Ebene 2). – erst die konkreten Aufgaben, dann der Sammel-Link.
- Menü-Badge „TOP“ an „Kleben & Montieren“: Header → Block „Menu Badge“ [V].

---

## 1. Menü „Hauptmenü“ · Handle `main-menu`

```
Abdichten                                        → /collections/abdichten
├── Am Dach                                      → /collections/abdichten
│   ├── Fenster & Dachluken abdichten            → /collections/fenster-dachluken-abdichten
│   ├── Dachhauben & Kabeldurchführungen         → /collections/dachhauben-durchfuehrungen-abdichten
│   └── Fugen & Nähte außen                      → /collections/fugen-naehte-aussen
├── An Wänden, Türen & innen                     → /collections/abdichten
│   ├── Serviceklappen & Türen (wiederlösbar)    → /collections/serviceklappen-tueren-abdichten
│   ├── Kantenleisten & Keder                    → /collections/kantenleisten-keder
│   └── Bad & Küche (innen)                      → /collections/bad-kueche-abdichten
└── Alle Produkte zum Abdichten                  → /collections/abdichten

Kleben & Montieren                               → /collections/kleben-montieren
├── Aufs Dach                                    → /collections/kleben-montieren
│   ├── Solarmodul kleben                        → /collections/solarmodul-kleben
│   ├── SAT-Anlage & Antenne kleben              → /collections/sat-anlage-antenne-kleben
│   └── Markise, Dachträger & Anbauteile         → /collections/markise-dachtraeger-anbauteile-kleben
├── Bauteile & Ausbau                            → /collections/kleben-montieren
│   ├── Fenster & Scheiben einkleben             → /collections/fenster-scheiben-einkleben
│   ├── Halter, Leisten & Innenausbau            → /collections/halter-leisten-innenausbau-kleben
│   └── Seitenwände & Großflächen (Profi)        → /collections/seitenwand-grossflaechen-kleben
└── Alle Produkte zum Kleben                     → /collections/kleben-montieren

Reparieren & Schützen                            → /collections/reparieren-schuetzen
├── Reparieren                                   → /collections/reparieren-schuetzen
│   ├── Kunststoff & GFK reparieren              → /collections/kunststoff-gfk-reparieren
│   ├── Ausgerissene Schraublöcher               → /collections/schraubloecher-reparieren
│   └── Undichte Stellen & Wasserschaden         → /collections/wasserschaden-reparieren
├── Schützen                                     → /collections/reparieren-schuetzen
│   ├── Unterbodenschutz                         → /collections/unterbodenschutz
│   ├── Hohlraumschutz                           → /collections/hohlraumschutz
│   └── Radkästen                                → /collections/radkaesten-schuetzen
└── Alle Produkte zum Reparieren & Schützen      → /collections/reparieren-schuetzen

Reinigen & Zubehör                               → /collections/reinigen-zubehoer
├── Vorbereiten & Finish                         → /collections/reinigen-zubehoer
│   ├── Reinigen & Entfetten                     → /collections/reinigen-entfetten
│   ├── Haftvermittler (Primer)                  → /collections/haftvermittler-primer
│   └── Fugen glätten & Regenstreifen            → /collections/glaetten-fugen-finish
├── Sets & Werkzeug                              → /collections/reinigen-zubehoer
│   ├── Klebe- & Dichtsets                       → /collections/klebesets
│   ├── Kartuschenpressen & Werkzeug             → /collections/kartuschenpressen-werkzeug
│   └── Bestseller                               → /collections/bestseller
└── Alles Zubehör                                → /collections/reinigen-zubehoer

Ratgeber                                         → /pages/ratgeber
├── Richtiges Produkt finden                     → /pages/produktfinder
│   ├── Produktfinder (3 Fragen)                 → /pages/produktfinder
│   ├── Welcher DEKAsyl? MS-1, MS-2, MS-5        → /pages/dekasyl-vergleich
│   └── Häufige Fragen (FAQ)                     → /pages/faq
└── Anleitungen & Downloads                      → /blogs/anleitungen
    ├── Schritt-für-Schritt-Anleitungen          → /blogs/anleitungen
    ├── Video-Akademie                           → /pages/video-akademie
    └── Datenblätter & Sicherheitsdatenblätter   → /pages/datenblaetter

Warum Dekalin                                    → /pages/ueber-dekalin
├── Erfahrung                                    → /pages/ueber-dekalin
│   ├── Seit 1907: unsere Geschichte             → /pages/ueber-dekalin
│   ├── Der „Klebepapst“ & sein Buch             → /pages/klebepapst-buch
│   └── Auszeichnungen (HIPE & Plus X 2025)      → /pages/auszeichnungen
└── Service                                      → /pages/beratung
    ├── Kostenlose Anwendungsberatung            → /pages/beratung
    ├── Schulungen nach DIN 2304                 → /pages/schulungen
    └── Für Gewerbe & Händler                    → /pages/gewerbe-haendler
```

Bilanz: 6 Hauptpunkte × 2 Spalten × 3 Links = 36 Aufgaben-Links; Welten 1–4 zusätzlich „Alle anzeigen“.

---

## 2. Menü „Mobil – Zusatzlinks“ · Handle `mobile-extra`
(Unter dem Hauptmenü im Mobile-Drawer, falls Vision ein Zusatzmenü in `header-mobile-navigation` unterstützt [?]; sonst als Ebene-1-Einträge am Ende eines separaten Mobil-Menüs `main-menu-mobile` = Kopie von `main-menu` + diese Punkte, „Bestseller“ ganz oben.)

```
★ Bestseller                    → /collections/bestseller
Produktfinder starten           → /pages/produktfinder
Kostenlose Beratung             → /pages/beratung
Anmelden                        → /account
```

## 3. Footer-Menüs

**`footer-shop` – Titel „Shop“**
```
Abdichten                → /collections/abdichten
Kleben & Montieren       → /collections/kleben-montieren
Reparieren & Schützen    → /collections/reparieren-schuetzen
Reinigen & Zubehör       → /collections/reinigen-zubehoer
Klebe- & Dichtsets       → /collections/klebesets
Bestseller               → /collections/bestseller
```

**`footer-hilfe` – Titel „Hilfe“**
```
Kostenlose Anwendungsberatung  → /pages/beratung
Produktfinder                  → /pages/produktfinder
Häufige Fragen                 → /pages/faq
Versand & Lieferung            → /policies/shipping-policy
Rückgabe & Widerruf            → /policies/refund-policy
Kontakt                        → /pages/kontakt
```

**`footer-dekalin` – Titel „Wissen & Dekalin“**
```
Anleitungen & Videos       → /blogs/anleitungen
Datenblätter & SDB         → /pages/datenblaetter
Über Dekalin (seit 1907)   → /pages/ueber-dekalin
Schulungen nach DIN 2304   → /pages/schulungen
Gewerbe & Händler          → /pages/gewerbe-haendler
Karriere                   → /pages/karriere
```

**`footer-rechtliches` – Titel „Rechtliches“ (Fußzeile, eine Zeile)**
```
Impressum                 → /policies/legal-notice
AGB                       → /policies/terms-of-service
Datenschutz               → /policies/privacy-policy
Widerrufsbelehrung        → /policies/refund-policy
Versand & Zahlung         → /policies/shipping-policy
Cookie-Einstellungen      → #cookie-settings   [A: Link der Consent-App]
Barrierefreiheit          → /pages/barrierefreiheit
```

## 4. Such-Drawer „Beliebte Suchen“ (Theme-Editor, kein Menü [?: ggf. Menü `search-popular`])
```
Solarmodul kleben     → /search?q=solarmodul
Dachluke abdichten    → /search?q=dachluke
SAT-Anlage kleben     → /search?q=sat
Unterbodenschutz      → /search?q=unterbodenschutz
Silikon entfernen     → /search?q=silikon+entfernen
```

## 5. Benötigte Seiten (Online Store → Seiten)
ratgeber · produktfinder · dekasyl-vergleich · faq · video-akademie · datenblaetter · ueber-dekalin · klebepapst-buch · auszeichnungen · beratung · schulungen · gewerbe-haendler · kontakt · karriere · barrierefreiheit · anleitung-solarmodul-kleben · Blog `anleitungen`.

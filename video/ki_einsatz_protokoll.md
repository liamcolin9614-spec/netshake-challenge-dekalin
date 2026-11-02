# KI-Einsatz in der Challenge – Protokoll (für Video-Teil 3)

Stand: 01./02.11.2026. Alles, was hier steht, ist real so abgelaufen und kann im Video gezeigt werden.

## Eingesetzte Tools
| Tool | Wofür | Ergebnis | Wo nachgebessert | Grenze |
|---|---|---|---|---|
| **Claude Code (Desktop, Opus)** als „Projektleiter“ | Briefing lesen, Aufgaben zerlegen, Agenten steuern, Dateien/PDF bauen | Projektordner mit Recherche, Testprotokollen, Konzepten | Agenten-Ergebnisse gegengeprüft (z. B. Wettbewerber-Annahmen korrigiert, MS-5-Werte nur aus Datenblatt) | Erfindet bei fehlenden Daten plausible Werte → alles mit [Annahme]/[TDB] markieren lassen |
| **Claude-Subagenten (parallel)** | 1) Dekalin-/Wettbewerbsrecherche (73 Web-Abrufe), 2) Aufgabe-2-Auswertung, 3) Aufgabe-1-Konzept | Recherche, Auswertung und Konzeptentwurf parallel statt nacheinander | Ein Agent hatte die Recherche noch nicht → nahm Wettbewerber „Innotec“ an → nachträglich auf Sika/TEROSON korrigiert | Agenten sehen nur, was man ihnen gibt; Kontext muss sauber übergeben werden |
| **Browser-Automatisierung (Claude, eingebauter Browser)** | Vision-Live-Demo analysieren (Section-/Block-Namen); Test-Shop per Skript im eingeloggten Shopify-Admin aufbauen | Echte Section-Namen für den Bauplan; Shop reproduzierbar in einem Durchlauf | Theme-Testversion sperrt Code-Editor und Asset-API → auf die Theme-Editor-API ausgewichen | Plattform-Eigenheiten (Sperren in Testversionen, CSP auf Perplexity blockiert lokales Speichern) |
| **Perplexity** (ausgeloggt) | 10 Test-Prompts, Quellen-Analyse über Tab „Links“ | Vollständige Quellenlisten je Prompt | – | Antworten variieren je Lauf; Momentaufnahme |
| **ChatGPT** (ausgeloggt) | dieselben 10 Prompts | Antworten + zitierte Domains | Quellen nur als „Chips“ sichtbar → Domains über Favicons erfasst | Ohne Login keine vollständigen Quellenlisten; teils Antwort aus Modellwissen ohne Quelle |

## 2 Beispiele fürs Video (konkret zeigen)
1. **KI-Sichtbarkeitstest systematisch:** 10 Prompts × 2 Systeme, je neue Session, Antwort + Quellen in Markdown-Protokoll; Auswertung als Matrix. *Gut:* reproduzierbar, belegbar. *Nachgebessert:* ChatGPT-Quellen-Extraktion. *Grenze:* Antworten sind nicht deterministisch → in der Praxis wöchentlich tracken (z. B. mit Finseo.ai).
2. **Recherche-Agent als Faktenprüfer:** fand Widersprüche auf dekalin.de (Preis 0,00 € im Schema, „Lorem Ipsum“ im FAQ-Schema, zwei Domains/Firmen, „isocyanatfrei“ vs. DEKAPUR 2K-90). *Gut:* Roh-HTML-Analyse wie ein Crawler. *Grenze:* Amazon/Reddit nur indirekt prüfbar.

## Learnings (Aussagen fürs Video)
- KI ersetzt nicht das Urteil: Jede Zahl auf der PDP stammt aus dem Datenblatt, nicht aus dem Modell.
- Die beste Arbeit entsteht, wenn man KI wie ein Team führt: klare Briefings, getrennte Aufgaben, Ergebnisse gegenprüfen.
- Grenzen: Halluzination bei Lücken, Plattform-Sperren (Login, CSP, Pop-ups), nicht-deterministische Antworten.

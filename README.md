# Synthetische HR-testdataset – Arvelia HR Services NV

Deze dataset is gemaakt voor een demo-app die bestanden scoort op **betrouwbaarheid** en **relevantie**. Alle documenten zijn in het Nederlands (Belgische/Vlaamse context) en **volledig fictief**. Het bedrijf *Arvelia HR Services NV* (Gent, PC 200), alle personen, klanten, adressen, ondernemingsnummers, ticketnummers en e-mailadressen zijn verzonnen. Verwijzingen naar Belgische wetgeving en instellingen (RSZ, VDAB, cao nr. 85, eenheidsstatuut ...) dienen enkel om de documenten realistisch te maken. Het zijn geen juridisch advies en ze zijn niet gecontroleerd op volledigheid.

**Referentiedatum van de dataset:** 30 september 2026 (bepaalt wat "actueel" en wat "verouderd" is).

## Inhoud

| Pad | Beschrijving |
|---|---|
| `documenten/` | 32 testdocumenten (docx, pdf, xlsx, csv, txt, md, eml) |
| `labels.csv` / `labels.json` | Grondwaarheid: eindscores, deelscores per factor en toelichting |
| `metadata.csv` / `metadata.json` | Metadata per bestand (auteur, data, status, versie, gebruik, bronnen, kernwoorden, relaties) |
| `relaties.csv` | Alle paren documenten die elkaar bevestigen of tegenspreken, met het onderwerp |

De CSV-bestanden gebruiken `;` als scheidingsteken en UTF-8 met BOM, zodat ze correct openen in een Belgische Excel. Lijsten in de CSV-bestanden staan gescheiden door ` | `. In de JSON-bestanden zijn het echte arrays.

## Twee aparte scores

Betrouwbaarheid en relevantie worden **onafhankelijk** gescoord (0–100). Een document kan relevant maar onbetrouwbaar zijn (bv. de anonieme verzuim-CSV). Het omgekeerde kan ook: betrouwbaar maar irrelevant (bv. de factuur of het lunchmenu).

### Betrouwbaarheid (gewogen gemiddelde van 7 factoren)

| Factor (kolom) | Gewicht | Wat wordt beoordeeld |
|---|---|---|
| Auteur (`b_auteur`) | 20% | Is de auteur gekend? Welke functie en autoriteit heeft die voor dit onderwerp? (HR-directeur of DPO > teamlead > extern of anoniem) |
| Bronvermelding (`b_bron`) | 15% | Verwijzingen naar wetgeving, cao's, interne beleidsdocumenten of databronnen |
| Datum (`b_datum`) | 10% | Is er een duidelijke datum van opmaak of goedkeuring? |
| Status (`b_status`) | 20% | goedgekeurd/definitief/ondertekend (hoog), gepubliceerd/verzonden, informeel, concept (laag), verouderd/gearchiveerd (zeer laag), onbekend |
| Gebruik (`b_gebruik`) | 5% | Hoe vaak het bestand geopend werd (laatste 12 maanden). Telt bewust zwak mee: populair is niet hetzelfde als juist (zie roddelmail) |
| Tegenstellingen (`b_tegenstellingen`) | 15% | 100 = geen tegenspraak. Laag bij tegenspraak door gezaghebbender documenten of bij interne tegenspraak |
| Bevestigingen (`b_bevestigingen`) | 15% | Bevestiging door andere, betrouwbare documenten. 50 = neutraal (geen verwante documenten) |

### Relevantie (gewogen gemiddelde van 3 factoren)

| Factor (kolom) | Gewicht | Wat wordt beoordeeld |
|---|---|---|
| Kernwoorden/onderwerp (`r_kernwoorden`) | 70% | In welke mate gaat het document over HR-kernthema's (arbeidsovereenkomst, verlof, verloning, verzuim, werving ...)? |
| Actualiteit (`r_actualiteit`) | 20% | Is de inhoud actueel op de referentiedatum? |
| Gebruik (`r_gebruik`) | 10% | Zelfde gebruiksscore als hierboven |

**Formules**
```
betrouwbaarheid = 0,20·auteur + 0,15·bron + 0,10·datum + 0,20·status + 0,05·gebruik + 0,15·tegenstellingen + 0,15·bevestigingen
relevantie      = 0,70·kernwoorden + 0,20·actualiteit + 0,10·gebruik
gebruik         = min(100, round(100 · ln(1 + aantal_keer_geopend) / ln(401)))     (400 keer geopend = 100)
categorie       : hoog ≥ 70 · midden 40–69 · laag < 40
```
De eindscores in `labels.csv` zijn met deze formules uit de deelscores berekend en afgerond.

## Metadata en relaties

`metadata.csv` bevat per bestand: `auteur`, `functie_auteur`, `aanmaakdatum`, `laatst_gewijzigd`, `status`, `versie`, `aantal_keer_geopend`, `aantal_bronvermeldingen`, `kernwoorden`, `bevestigd_door` en `tegengesproken_door`. Waar het formaat dat toelaat, staan auteur en data ook in de bestandseigenschappen: docx core properties, PDF-metadata, xlsx-eigenschappen en de e-mailheaders. De bestandsdatum (mtime) is gelijk aan `laatst_gewijzigd`. Bij sommige bestanden ontbreken auteur of datum bewust.

De `kernwoorden` zijn automatisch berekend: de 8 meest voorkomende inhoudswoorden na het wegfilteren van stopwoorden. Ze zijn dus niet handmatig gekozen.

### Ingebouwde tegenstellingen (selectie)
- **Verlofbeleid 2019 (v1.2)** ↔ **Verlofbeleid 2026 (v3.0)**, het arbeidsreglement en de onboarding-checklist: 4 of 6 extralegale dagen, papieren of digitale aanvraag, overdracht tot 28/2 of tot 31/3.
- **E-mail van de teamlead** (3 thuiswerkdagen, geen kerndagen, 200 EUR) ↔ **Thuiswerkbeleid v2.1**, het arbeidsreglement en de notulen van de OR (max. 2 dagen, 150 EUR, geen afspraken per team).
- **Concept-thuiswerkbeleid v0.3**: spreekt zichzelf tegen (3 dagen of max. 2; 175 of 150 EUR) en wijkt af van v2.1.
- **Duplicaat van het contract** (`_v2_kopie`: 3.650 EUR, klasse B3, start 1/10, niet ondertekend) ↔ **ondertekend contract** (3.450 EUR, B2, start 5/10), de welkomstmail, het IT-ticket en de onboarding.
- **Verzuim-CSV** (6,4%, 140 medewerkers) ↔ **Ziekteverzuimrapport Q2** en de notulen (4,6%, 138 medewerkers).
- **Anonieme roddelmail** (sluiting Antwerpen, ecocheques en thuiswerk afgeschaft) ↔ notulen van de OR, exitgesprek, thuiswerkbeleid en memo over de ecocheques.
- **Informele notities** ↔ memo over de ecocheques, loonschalen en verlofbeleid 2026.
- **Contractsjabloon 2012** (proefperiode, formule-Claeys, maaltijdcheque 6 EUR) ↔ arbeidsreglement, loonschalen en actueel contract.

### Bevestigingsclusters
- Maaltijdcheques 8 EUR en ecocheques 250 EUR: arbeidsreglement, memo, loonschalen, onboarding, notulen, welkomstmail.
- Verlof 20 + 6 dagen: verlofbeleid 2026, arbeidsreglement, onboarding, welkomstmail, vacature.
- Thuiswerk max. 2 dagen met kerndagen: thuiswerkbeleid v2.1, arbeidsreglement, onboarding, notulen, facility-mededeling, welkomstmail, vacature.
- Indiensttreding Eline Maes: contract, welkomstmail, IT-ticket, onboarding, functieomschrijving, loonschalen, opleidingsplan.
- Verder: verzuimrapport ↔ notulen, vacature ↔ cv/privacyverklaring/notulen/loonschalen, functioneringsgesprek ↔ opleidingsplan, exitgesprek ↔ notulen.
- **Zwakke bevestigingen** (valkuil): de informele notities worden "bevestigd" door het verouderde verlofbeleid van 2019 en door de roddelmail. Een goed model telt zo'n bevestiging nauwelijks mee, omdat de bevestigende bron zelf onbetrouwbaar is.

## Spreiding
- **Hoog/hoog:** arbeidsreglement, verlofbeleid 2026, thuiswerkbeleid v2.1, loonschalen, onboarding, ondertekend contract, verzuimrapport, notulen ...
- **Laag betrouwbaar, wel relevant:** verlofbeleid 2019, concept-thuiswerkbeleid, contractkopie, sjabloon 2012, teamlead-mail, verzuim-CSV, notities.
- **Betrouwbaar, deels relevant:** IT-ticket, offerte, factuur, facility-mededeling.
- **Irrelevant:** lunchmenu, recept, marketingnieuwsbrief.

De scores zijn een onderbouwde, maar subjectieve grondwaarheid voor demodoeleinden. Wie de gewichten wil aanpassen, kan de eindscores opnieuw berekenen uit de deelscores.

## Repository en scripts

De bestanden hierboven staan in de root van deze repository. Er is geen applicatiecode: de repository is de testdataset. De Python-scripts die de dataset opbouwen en controleren staan in `scripts/` (`build.py`, `verify.py`, `registry.py`, `common.py`, `g_policies.py`, `g_people.py`, `g_data.py` en `g_misc.py`). De afhankelijkheden staan in `requirements.txt`.

Vanuit de root van de repository:

```bash
pip install -r requirements.txt
python scripts/g_policies.py
python scripts/g_people.py
python scripts/g_data.py
python scripts/g_misc.py
python scripts/build.py
python scripts/verify.py
```

De `g_*.py`-scripts schrijven de documenten naar `documenten/`. `python scripts/build.py` herberekent daarna `labels.csv`, `labels.json`, `metadata.csv`, `metadata.json` en `relaties.csv`, en zet de bestandsdatum (mtime) gelijk aan `laatst_gewijzigd`. `python scripts/verify.py` controleert of elk document leesbaar is, of de labels en metadata exact dezelfde bestanden dekken, en of de scores en relaties kloppen. Een geslaagde controle eindigt met `ALLES OK`.

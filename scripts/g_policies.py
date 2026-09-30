from common import *

# 1. Arbeidsreglement (PDF, officieel)
def arbeidsreglement():
    H = f"{BEDRIJF} – Arbeidsreglement – versie 2026-01 – Status: GOEDGEKEURD"
    b = [
        ("title", "Arbeidsreglement"),
        ("pb", f"{BEDRIJF} – {ADRES} – Ondernemingsnummer {KBO}"),
        ("table", [["Documentgegevens", ""],
                   ["Versie", "2026-01 (vervangt versie 2023-02)"],
                   ["Status", "Goedgekeurd – in werking vanaf 1 januari 2026"],
                   ["Opgesteld door", "Wouter De Clercq, HR-directeur"],
                   ["Juridisch nagelezen", "Mr. Els Vandenberghe, externe raadsman arbeidsrecht"],
                   ["Goedgekeurd door", "Katrien Van Damme, gedelegeerd bestuurder, na procedure in de ondernemingsraad (vergadering 9 december 2025)"],
                   ["Neerlegging", "Afschrift neergelegd bij de Directie Toezicht op de Sociale Wetten (FOD WASO), Gent, op 18 december 2025"]],
         [5*cm, 12*cm]),
        ("h1", "Hoofdstuk 1 – Toepassingsgebied en rechtsgrond"),
        ("p", f"Dit arbeidsreglement is van toepassing op alle werknemers die met {BEDRIJF} verbonden zijn door een arbeidsovereenkomst, "
              f"ongeacht hun vestiging (Gent, Antwerpen, Hasselt). De onderneming ressorteert onder het {PC}. "
              "Het reglement werd opgesteld overeenkomstig de wet van 8 april 1965 tot instelling van de arbeidsreglementen en de "
              "wet van 3 juli 1978 betreffende de arbeidsovereenkomsten. Elke werknemer ontvangt bij indiensttreding een exemplaar en tekent voor ontvangst."),
        ("h1", "Hoofdstuk 2 – Arbeidsduur en uurregeling"),
        ("p", "De normale wekelijkse arbeidsduur bedraagt 38 uur voor voltijdse werknemers, gespreid over vijf werkdagen van maandag tot en met vrijdag. "
              "De onderneming hanteert een glijtijdregeling met stamtijden. Begin van de werkdag tussen 7u30 en 9u30; stamtijden van 9u30 tot 11u45 en van 13u45 tot 16u00. "
              "De middagpauze bedraagt minimaal 30 minuten en wordt niet als arbeidstijd beschouwd. Deeltijdse uurroosters zijn opgenomen in bijlage 2."),
        ("p", "Thuiswerk is mogelijk volgens het Thuiswerkbeleid versie 2.1: structureel maximaal 2 dagen per week, met dinsdag en donderdag als "
              "kerndagen op kantoor. Het beleid is opgesteld conform cao nr. 85 betreffende het telewerk."),
        ("h1", "Hoofdstuk 3 – Verloning en extralegale voordelen"),
        ("p", "Het loon wordt maandelijks betaald per overschrijving, uiterlijk op de laatste werkdag van de maand. De loonstrook is digitaal beschikbaar in het personeelsportaal MyArvelia. "
              "De loonschalen per functieklasse zijn vastgelegd in het document Loonschalen 2026."),
        ("bullets", ["Maaltijdcheques: 8,00 EUR per effectief gewerkte dag (werkgeversaandeel 6,91 EUR, werknemersaandeel 1,09 EUR).",
                     "Ecocheques: 250 EUR per jaar voor een voltijdse werknemer met volledige referteperiode, conform de sectorale cao van PC 200.",
                     "Groepsverzekering (vaste bijdrage 3% van het brutojaarloon) en hospitalisatieverzekering vanaf de eerste werkdag.",
                     "Thuiswerkvergoeding: 150 EUR per maand (voltijds, pro rata voor deeltijdsen) volgens het Thuiswerkbeleid."]),
        ("h1", "Hoofdstuk 4 – Vakantie en verlof"),
        ("p", "Voltijdse werknemers hebben recht op 20 wettelijke vakantiedagen en 6 extralegale verlofdagen per jaar, aangevuld met anciënniteitsdagen "
              "(1 dag per 5 jaar dienst, maximaal 4). De nadere regels staan in het Verlofbeleid versie 3.0 (2026). Omstandigheidsverlof (klein verlof) wordt toegekend "
              "overeenkomstig het koninklijk besluit van 28 augustus 1963. De wettelijke feestdagen worden gerespecteerd; valt een feestdag op een zaterdag of zondag, dan wordt een vervangdag vastgelegd in overleg met de ondernemingsraad."),
        ("h1", "Hoofdstuk 5 – Arbeidsongeschiktheid"),
        ("p", "De werknemer die arbeidsongeschikt is, verwittigt zijn leidinggevende en HR onmiddellijk en uiterlijk om 9u00 op de eerste dag van afwezigheid. "
              "Een medisch attest wordt binnen de twee werkdagen bezorgd, behoudens de wettelijke vrijstelling voor de eerste dag van arbeidsongeschiktheid (maximaal driemaal per kalenderjaar). "
              "De werkgever kan een controlearts aanstellen. Het gewaarborgd loon wordt betaald volgens de wet van 3 juli 1978."),
        ("h1", "Hoofdstuk 6 – Beëindiging van de arbeidsovereenkomst"),
        ("p", "Er geldt geen proefperiode (afgeschaft sinds 1 januari 2014 door de wet van 26 december 2013 betreffende het eenheidsstatuut). "
              "De opzeggingstermijnen worden berekend overeenkomstig artikel 37/2 van de arbeidsovereenkomstenwet, in weken, op basis van de anciënniteit. "
              "Dringende redenen tot ontslag zijn niet-limitatief opgesomd in bijlage 3."),
        ("h1", "Hoofdstuk 7 – Welzijn op het werk"),
        ("p", "Overeenkomstig de wet van 4 augustus 1996 betreffende het welzijn van de werknemers bij de uitvoering van hun werk:"),
        ("bullets", ["Interne preventieadviseur: Hilde Martens (preventie@arvelia-hr.be).",
                     "Vertrouwenspersoon: Evi Lemmens (HR-administratie).",
                     "Preventieadviseur psychosociale aspecten: Provizo Externe Dienst voor Preventie en Bescherming, Gent.",
                     "EHBO-verantwoordelijken per verdieping zijn vermeld in bijlage 4."]),
        ("h1", "Hoofdstuk 8 – Sancties en klachten"),
        ("p", "Tekortkomingen kunnen leiden tot een mondelinge verwittiging, een schriftelijke verwittiging of een geldboete van maximaal één vijfde van het dagloon. "
              "De opbrengst van boetes wordt besteed aan het sociaal fonds van de onderneming. Klachten kunnen worden gericht aan de HR-directeur of aan de werknemersvertegenwoordiging."),
        ("h1", "Bronnen"),
        ("bullets", ["Wet van 8 april 1965 tot instelling van de arbeidsreglementen.",
                     "Wet van 3 juli 1978 betreffende de arbeidsovereenkomsten, o.a. art. 37/2.",
                     "Wet van 26 december 2013 betreffende het eenheidsstatuut.",
                     "Wet van 4 augustus 1996 betreffende het welzijn van de werknemers.",
                     "Cao nr. 85 van de Nationale Arbeidsraad betreffende het telewerk.",
                     "KB van 28 augustus 1963 (omstandigheidsverlof).",
                     "Sectorale cao's PC 200 (ecocheques).",
                     "Interne documenten: Verlofbeleid v3.0 (2026), Thuiswerkbeleid v2.1 (2025), Loonschalen 2026."]),
        ("space", 10),
        ("p", "Gent, 18 december 2025. Voor de onderneming: Katrien Van Damme, gedelegeerd bestuurder (elektronisch ondertekend) – Wouter De Clercq, HR-directeur (elektronisch ondertekend)."),
    ]
    make_pdf("Arbeidsreglement_Arvelia_v2026-01.pdf", b, author="Wouter De Clercq", title="Arbeidsreglement Arvelia HR Services NV v2026-01",
             subject="Arbeidsreglement", header=H, footer="Versie 2026-01 – Goedgekeurd 18/12/2025", created=dtm(2025, 12, 18, 14), modified=dtm(2025, 12, 18, 15),
             keywords="arbeidsreglement, PC 200, verlof, thuiswerk, maaltijdcheques")

# 2. Verlofbeleid 2026 (DOCX, officieel)
def verlof2026():
    b = [
        ("title", "Verlofbeleid 2026"),
        ("table", [["Versie", "3.0"], ["Status", "Goedgekeurd"], ["In werking", "1 januari 2026"],
                   ["Auteur", "Lotte Peeters, HR Business Partner"], ["Goedgekeurd door", "Wouter De Clercq, HR-directeur – 15 januari 2026"],
                   ["Advies ondernemingsraad", "Positief advies op 9 december 2025"],
                   ["Vervangt", "Verlofbeleid versie 1.2 van 1 februari 2019 (vanaf heden verouderd)"]]),
        ("h1", "1. Doel"),
        ("p", "Dit beleid beschrijft hoe medewerkers van Arvelia HR Services NV vakantie en verlof opnemen. Het vervangt integraal de versie 1.2 uit 2019. "
              "Belangrijkste wijzigingen: het aantal extralegale verlofdagen stijgt van 4 naar 6, verlofaanvragen verlopen uitsluitend digitaal via MyArvelia, "
              "en de overdrachtstermijn voor extralegale dagen wordt verlengd tot 31 maart van het volgende jaar."),
        ("h1", "2. Vakantiedagen"),
        ("table", [["Soort", "Aantal (voltijds)", "Opmerking"],
                   ["Wettelijke vakantiedagen", "20", "Op basis van prestaties in het vakantiedienstjaar (vorig kalenderjaar)"],
                   ["Extralegale verlofdagen", "6", "Pro rata bij deeltijdse tewerkstelling of indiensttreding in de loop van het jaar"],
                   ["Anciënniteitsdagen", "+1 per 5 jaar dienst", "Maximaal 4 bijkomende dagen"],
                   ["Wettelijke feestdagen", "10", "Vervangdag bij feestdag op zaterdag of zondag"]]),
        ("p", "Nieuwe medewerkers die in de loop van het jaar starten, hebben wettelijke vakantiedagen op basis van hun prestaties bij de vorige werkgever (vakantieattest). "
              "Starters en herintreders kunnen gebruikmaken van jeugdvakantie of Europese vakantie volgens de wettelijke voorwaarden."),
        ("h1", "3. Aanvragen en goedkeuren"),
        ("bullets", ["Alle verlofaanvragen gebeuren via het personeelsportaal MyArvelia. Papieren formulieren worden niet langer aanvaard.",
                     "Verlof van meer dan 3 aaneengesloten werkdagen wordt minstens 2 weken vooraf aangevraagd.",
                     "De leidinggevende keurt goed of weigert binnen 5 werkdagen, met motivering bij weigering.",
                     "In de zomerperiode (1 juli – 31 augustus) heeft elke medewerker recht op minstens 2 aaneengesloten weken verlof, in overleg met het team."]),
        ("h1", "4. Overdracht"),
        ("p", "Wettelijke vakantiedagen moeten binnen het kalenderjaar worden opgenomen en zijn niet overdraagbaar, behalve in de wettelijk voorziene gevallen "
              "(bv. langdurige arbeidsongeschiktheid). Extralegale dagen kunnen tot 31 maart van het volgende jaar worden overgedragen; daarna vervallen ze zonder vergoeding."),
        ("h1", "5. Omstandigheidsverlof en andere verloven"),
        ("p", "Omstandigheidsverlof (klein verlof) volgt het KB van 28 augustus 1963 en de sectorale regeling van PC 200. Het geboorteverlof bedraagt 20 dagen. "
              "Voor tijdskrediet, ouderschapsverlof en andere thematische verloven gelden de regels van de RVA; HR begeleidt de aanvraag."),
        ("table", [["Gebeurtenis", "Duur"], ["Huwelijk van de werknemer", "2 dagen"], ["Overlijden echtgeno(o)t(e), kind, ouder", "3 dagen"],
                   ["Overlijden broer, zus, grootouder (inwonend)", "2 dagen"], ["Plechtige communie / lentefeest kind", "1 dag"]]),
        ("h1", "6. Collectieve sluiting"),
        ("p", "Er is geen collectieve sluiting. De vroegere sluiting tussen Kerstmis en Nieuwjaar (versie 2019) werd afgeschaft; een minimale bezetting per team wordt afgesproken."),
        ("h1", "7. Bronnen"),
        ("bullets", ["Wetgeving jaarlijkse vakantie (gecoördineerde wetten van 28 juni 1971).", "KB van 28 augustus 1963 (omstandigheidsverlof).",
                     "Arbeidsreglement Arvelia, versie 2026-01, hoofdstuk 4.", "Advies ondernemingsraad d.d. 9 december 2025."]),
        ("pi", "Vragen? hr@arvelia-hr.be – Lotte Peeters, HR Business Partner."),
    ]
    make_docx("Verlofbeleid_2026_v3.0.docx", b, author="Lotte Peeters", title="Verlofbeleid 2026 v3.0", created=dtm(2025, 11, 20), modified=dtm(2026, 1, 15, 16),
              header="Arvelia HR Services NV – Verlofbeleid – v3.0 – GOEDGEKEURD", footer="Intern document – vervangt Verlofbeleid v1.2 (2019)")

# 3. Verlofbeleid 2019 (PDF, verouderd)
def verlof2019():
    b = [
        ("title", "Verlofregeling Arvelia"),
        ("p", "Versie 1.2 – 1 februari 2019 – opgesteld door Marc Hendrickx, HR-manager"),
        ("h1", "Vakantiedagen"),
        ("p", "Elke voltijdse bediende heeft recht op 20 wettelijke vakantiedagen en 4 extralegale verlofdagen. Er zijn geen bijkomende anciënniteitsdagen. "
              "Deeltijdse medewerkers krijgen een evenredig aantal dagen."),
        ("h1", "Aanvraagprocedure"),
        ("p", "Verlof wordt aangevraagd met het papieren verlofformulier (model V-03), dat ingevuld en ondertekend door de leidinggevende aan de HR-dienst wordt bezorgd. "
              "Voor verlof langer dan een week moet het formulier één maand vooraf worden ingediend."),
        ("h1", "Overdracht"),
        ("p", "Extralegale dagen die niet werden opgenomen, kunnen worden overgedragen tot 28 februari van het volgende jaar. Wettelijke dagen zijn niet overdraagbaar."),
        ("h1", "Collectieve sluiting"),
        ("p", "Het kantoor is gesloten tussen Kerstmis en Nieuwjaar. Medewerkers zetten hiervoor 3 verlofdagen opzij."),
        ("h1", "Klein verlof"),
        ("p", "Klein verlof volgens de wettelijke regeling. Vaderschapsverlof: 10 dagen."),
        ("space", 8),
        ("small", "Vragen: Marc Hendrickx (marc.hendrickx@arvelia-hr.be)"),
    ]
    make_pdf("Verlofbeleid_2019_v1.2.pdf", b, author="Marc Hendrickx", title="Verlofregeling v1.2", subject="Verlof",
             footer="Arvelia Interim BVBA – Verlofregeling v1.2", created=dtm(2019, 2, 1, 9), modified=dtm(2019, 2, 1, 9))

# 4. Thuiswerkbeleid CONCEPT (DOCX)
def thuiswerk_concept():
    b = [
        ("red", "CONCEPT – NIET VERSPREIDEN – versie 0.3"),
        ("title", "Thuiswerkbeleid (herziening)"),
        ("pi", "Werkversie werkgroep thuiswerk. Laatste bewerking: LP. Nog niet voorgelegd aan de ondernemingsraad."),
        ("h1", "1. Inleiding"),
        ("p", "Sinds de invoering van het thuiswerkbeleid versie 2.1 in maart 2025 kregen we veel vragen over meer flexibiliteit. Deze herziening wil het beleid moderniseren."),
        ("hl", "[OPMERKING LP: inleiding herschrijven, te vaag. Verwijzen naar resultaten bevraging? Welke cijfers hebben we eigenlijk?]"),
        ("h1", "2. Aantal thuiswerkdagen"),
        ("p", "Medewerkers kunnen voortaan tot 3 dagen per week thuiswerken, met één vaste teamdag op kantoor."),
        ("hl", "[OPMERKING BW: voor payroll liefst 3 dagen, maar is dat al beslist? – LP: nee, voorstel!]"),
        ("h1", "3. Vergoeding"),
        ("p", "De maandelijkse kantoorvergoeding bedraagt 175 EUR (voltijds). Daarnaast een internetvergoeding van 20 EUR."),
        ("red", "TODO: bedrag nog checken met Filip (CFO) – fiscaal plafond? in versie 0.2 stond nog 150 EUR"),
        ("h1", "4. Uitrusting"),
        ("p", "De werkgever stelt een laptop, headset en op aanvraag een tweede scherm ter beschikking. Een ergonomische bureaustoel kan worden aangevraagd na advies van de preventieadviseur."),
        ("h1", "5. Voorwaarden"),
        ("bullets", ["Thuiswerk is mogelijk voor functies die zich ertoe lenen, na goedkeuring door de leidinggevende.",
                     "Maximaal 2 dagen per week thuiswerk, niet op kerndagen.",
                     "Bereikbaarheid tijdens de stamtijden via Teams en telefoon.",
                     "Nieuwe medewerkers werken de eerste maand volledig op kantoor."]),
        ("hl", "[?? dit spreekt sectie 2 tegen – aanpassen na beslissing directie]"),
        ("h1", "6. Evaluatie"),
        ("p", "Het beleid wordt na 6 maanden geëvalueerd. Datum inwerkingtreding: nog te bepalen."),
    ]
    make_docx("Thuiswerkbeleid_CONCEPT_v0.3.docx", b, author="Lotte Peeters", title="CONCEPT thuiswerkbeleid v0.3", created=dtm(2026, 8, 28), modified=dtm(2026, 9, 12, 17, 40),
              header="CONCEPT – werkdocument", comments="Concept, niet goedgekeurd")

# 5. Thuiswerkbeleid v2.1 (MD, intranet)
def thuiswerk_md():
    md = f"""# Thuiswerkbeleid – versie 2.1

> **Status:** Goedgekeurd · **In werking:** 1 maart 2025 · **Eigenaar:** Wouter De Clercq, HR-directeur
> **Opgesteld door:** Lotte Peeters, HR Business Partner · **Advies ondernemingsraad:** 11 februari 2025
> *Intranetpagina MyArvelia > HR > Beleid > Thuiswerk – laatst nagekeken op 2 september 2026*

## 1. Toepassingsgebied
Dit beleid geldt voor alle medewerkers van {BEDRIJF} met een functie die zich leent tot thuiswerk (structureel telewerk), in alle vestigingen.
Het beleid is opgesteld conform **cao nr. 85** van de Nationale Arbeidsraad betreffende het telewerk en is opgenomen in het arbeidsreglement (hoofdstuk 2).

## 2. Hoeveel dagen?
- Structureel maximaal **2 dagen per week** thuiswerk (pro rata voor deeltijdsen).
- **Dinsdag en donderdag zijn kerndagen** waarop iedereen op kantoor aanwezig is.
- Nieuwe medewerkers werken de **eerste maand** op kantoor om het inwerktraject te volgen.
- Occasioneel telewerk (bv. bij overmacht, werken aan de parking) kan in overleg met de leidinggevende, binnen het maximum van 2 dagen.

## 3. Vergoedingen
| Vergoeding | Bedrag | Voorwaarde |
|---|---|---|
| Forfaitaire kantoorvergoeding | 150 EUR/maand | Voltijds, structureel thuiswerk |
| Internetvergoeding | 20 EUR/maand | Idem |
| Uitrusting | laptop, headset, 2e scherm | Eigendom van de werkgever |

De bedragen blijven binnen de fiscale en RSZ-grenzen die de administratie aanvaardt (zie circulaire FOD Financiën over kosten eigen aan de werkgever).

## 4. Aanvraag
1. Aanvraag via MyArvelia (formulier "Thuiswerkafspraak").
2. Goedkeuring door de leidinggevende, registratie door HR.
3. Schriftelijke thuiswerkafspraak als bijlage bij de arbeidsovereenkomst.

## 5. Welzijn en veiligheid
De preventieadviseur (Hilde Martens) stelt een ergonomische checklist ter beschikking. Arbeidsongevallen tijdens thuiswerk vallen onder de arbeidsongevallenverzekering, conform de wettelijke vermoedens.

## 6. Herziening
Een werkgroep onderzoekt in 2026 een mogelijke herziening. **Tot een nieuwe versie formeel is goedgekeurd na advies van de ondernemingsraad, blijft deze versie 2.1 volledig van toepassing.** Afwijkende afspraken per team zijn niet toegestaan.

## Bronnen
- Cao nr. 85 NAR betreffende het telewerk
- Arbeidsreglement Arvelia v2026-01, hoofdstuk 2 en 3
- Advies ondernemingsraad 11/02/2025
- Circulaire FOD Financiën inzake thuiswerkvergoedingen

*Contact: hr@{DOMEIN}*
"""
    (OUT / "Thuiswerkbeleid_v2.1_intranet.md").write_text(md, encoding="utf-8")

# 6. Memo ecocheques (DOCX)
def memo_eco():
    b = [
        ("title", "Interne memo"),
        ("table", [["Aan", "Alle medewerkers"], ["Van", "Wouter De Clercq, HR-directeur"], ["Datum", "20 mei 2026"],
                   ["Onderwerp", "Ecocheques 2026 en herinnering maaltijdcheques"], ["Referentie", "MEMO-HR-2026-07"]]),
        ("h1", "Ecocheques 2026"),
        ("p", "Zoals elk jaar ontvangen alle medewerkers ecocheques conform de sectorale cao van het Paritair Comité 200 en cao nr. 98 van de Nationale Arbeidsraad. "
              "Voor een voltijdse medewerker met een volledige referteperiode (1 juni 2025 – 31 mei 2026) bedraagt het bedrag 250 EUR. "
              "De ecocheques worden in de loop van juni 2026 elektronisch op je e-chequekaart geladen."),
        ("bullets", ["Deeltijdse medewerkers ontvangen een bedrag in verhouding tot hun arbeidsregime.",
                     "Wie tijdens de referteperiode in dienst trad of uit dienst ging, ontvangt een pro-rata-bedrag.",
                     "Bepaalde schorsingen (bv. tijdelijke werkloosheid, ziekte na het gewaarborgd loon) kunnen het bedrag verminderen volgens de sectorale regels.",
                     "Ecocheques zijn 24 maanden geldig en enkel te besteden aan ecologische producten en diensten volgens de officiële lijst van de NAR."]),
        ("h1", "Herinnering maaltijdcheques"),
        ("p", "De waarde van de maaltijdcheques blijft ongewijzigd op 8,00 EUR per effectief gewerkte dag (werkgeversaandeel 6,91 EUR, persoonlijke bijdrage 1,09 EUR), "
              "zoals opgenomen in het arbeidsreglement (hoofdstuk 3) en de Loonschalen 2026. Geruchten dat ecocheques zouden worden afgeschaft, zijn onjuist: "
              "de sectorale verplichting blijft bestaan."),
        ("h1", "Meer informatie"),
        ("p", "Vragen over je saldo? Raadpleeg MyArvelia of contacteer payroll@arvelia-hr.be (team van Bram Wuyts)."),
        ("pi", "Bronnen: cao nr. 98 NAR; sectorale cao ecocheques PC 200; arbeidsreglement v2026-01, hoofdstuk 3."),
        ("sig", ["Wouter De Clercq\nHR-directeur\n20/05/2026"]),
    ]
    make_docx("Memo_HR_Ecocheques_2026.docx", b, author="Wouter De Clercq", title="Memo ecocheques 2026", created=dtm(2026, 5, 19, 15), modified=dtm(2026, 5, 20, 9),
              header="Arvelia HR Services NV – Interne memo MEMO-HR-2026-07", footer="Verspreid via intranet op 20/05/2026")

# 7. Privacyverklaring sollicitanten (PDF)
def privacy():
    b = [
        ("title", "Privacyverklaring voor sollicitanten"),
        ("p", f"Versie 1.4 – 1 november 2025 – Status: goedgekeurd – Verantwoordelijke: {BEDRIJF}, {ADRES}, {KBO}. "
              "Opgesteld door Jonas Verbeke, functionaris voor gegevensbescherming (DPO), dpo@arvelia-hr.be."),
        ("h1", "1. Welke gegevens verwerken wij?"),
        ("p", "In het kader van een sollicitatie verwerken wij identificatie- en contactgegevens, je cv en motivatiebrief, diploma's en getuigschriften, "
              "notities van sollicitatiegesprekken, resultaten van eventuele assessments en, met jouw toestemming, referenties van vorige werkgevers. "
              "Wij verwerken geen bijzondere categorieën van persoonsgegevens, tenzij jij die zelf spontaan meedeelt."),
        ("h1", "2. Doeleinden en rechtsgronden"),
        ("table", [["Doel", "Rechtsgrond (AVG)"],
                   ["Beoordelen van je kandidatuur voor een concrete vacature", "Precontractuele maatregelen – art. 6.1.b"],
                   ["Opnemen in onze wervingsreserve (1 jaar)", "Toestemming – art. 6.1.a"],
                   ["Verdediging bij een geschil (bv. discriminatieklacht)", "Gerechtvaardigd belang – art. 6.1.f"]], [9*cm, 8*cm]),
        ("h1", "3. Bewaartermijnen"),
        ("p", "Niet-weerhouden kandidaturen worden uiterlijk 6 maanden na het afsluiten van de procedure verwijderd, of na 1 jaar indien je toestemming gaf voor de wervingsreserve. "
              "Gegevens van aangeworven kandidaten worden opgenomen in het personeelsdossier."),
        ("h1", "4. Ontvangers"),
        ("p", "Je gegevens worden enkel gedeeld met de betrokken leidinggevenden, het HR-team en onze verwerkers (o.a. de leverancier van ons sollicitantenvolgsysteem), "
              "met wie een verwerkersovereenkomst werd gesloten. Er is geen doorgifte buiten de Europese Economische Ruimte."),
        ("h1", "5. Jouw rechten"),
        ("p", "Je hebt recht op inzage, verbetering, verwijdering, beperking, overdraagbaarheid en bezwaar, en kunt je toestemming altijd intrekken. "
              "Verzoeken richt je aan dpo@arvelia-hr.be; wij antwoorden binnen één maand. Je kunt klacht indienen bij de Gegevensbeschermingsautoriteit (GBA)."),
        ("h1", "6. Bronnen"),
        ("bullets", ["Verordening (EU) 2016/679 (AVG/GDPR), art. 6, 13 en 15-22.",
                     "Wet van 30 juli 2018 betreffende de bescherming van natuurlijke personen met betrekking tot de verwerking van persoonsgegevens.",
                     "Wet van 10 mei 2007 ter bestrijding van bepaalde vormen van discriminatie.",
                     "Intern register van verwerkingsactiviteiten, verwerking nr. HR-02 (werving en selectie)."]),
    ]
    make_pdf("Privacyverklaring_Sollicitanten_v1.4.pdf", b, author="Jonas Verbeke", title="Privacyverklaring sollicitanten v1.4", subject="GDPR",
             header="Arvelia HR Services NV – Privacyverklaring sollicitanten – v1.4", footer="Goedgekeurd 01/11/2025 – DPO",
             created=dtm(2025, 10, 28), modified=dtm(2025, 11, 1, 11))

if __name__ == "__main__":
    for f in [arbeidsreglement, verlof2026, verlof2019, thuiswerk_concept, thuiswerk_md, memo_eco, privacy]: f()
    print("policies ok")

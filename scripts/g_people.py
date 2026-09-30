from common import *

def contract_blocks(salaris, start, klasse, signed, versie_note):
    b = [
        ("title", "Arbeidsovereenkomst voor bedienden van onbepaalde duur"),
        ("pi", versie_note),
        ("h1", "Tussen"),
        ("p", f"{BEDRIJF}, met maatschappelijke zetel te {ADRES}, ondernemingsnummer {KBO}, RSZ-werkgever onder {PC}, "
              "hier vertegenwoordigd door Wouter De Clercq, HR-directeur, hierna 'de werkgever',"),
        ("p", "en mevrouw Eline Maes, wonende te Kerkstraat 17, 9050 Gentbrugge, rijksregisternummer [afgeschermd], hierna 'de werknemer',"),
        ("p", "wordt het volgende overeengekomen:"),
        ("h2", "Artikel 1 – Functie"),
        ("p", f"De werknemer wordt aangeworven als Payroll Consultant (functieklasse {klasse}) binnen het team Payroll, onder leiding van Bram Wuyts, Teamlead Payroll. "
              "De taken zijn beschreven in de functieomschrijving Payroll Consultant v2.0, die als bijlage aan deze overeenkomst wordt gehecht."),
        ("h2", "Artikel 2 – Aanvang en duur"),
        ("p", f"De overeenkomst wordt gesloten voor onbepaalde duur en gaat in op {start}. Er is geen proefperiode. De Dimona-aangifte gebeurt vóór de aanvang van de prestaties."),
        ("h2", "Artikel 3 – Arbeidsduur en plaats"),
        ("p", "De werknemer werkt voltijds, 38 uur per week, volgens de glijtijdregeling uit het arbeidsreglement. De gewone plaats van tewerkstelling is de zetel te Gent. "
              "Thuiswerk is mogelijk volgens het Thuiswerkbeleid v2.1 (maximaal 2 dagen per week, na de eerste maand)."),
        ("h2", "Artikel 4 – Loon en voordelen"),
        ("p", f"Het brutomaandloon bedraagt {salaris} EUR, geïndexeerd volgens de regels van PC 200. De werknemer heeft recht op een eindejaarspremie (13e maand) volgens de sectorale regeling, "
              "maaltijdcheques van 8,00 EUR per gewerkte dag (werknemersbijdrage 1,09 EUR), ecocheques volgens de sectorale cao, groepsverzekering en hospitalisatieverzekering."),
        ("h2", "Artikel 5 – Vakantie"),
        ("p", "De werknemer heeft recht op wettelijke vakantie en op 6 extralegale verlofdagen per jaar (pro rata in het jaar van indiensttreding), volgens het Verlofbeleid v3.0."),
        ("h2", "Artikel 6 – Vertrouwelijkheid en gegevensbescherming"),
        ("p", "De werknemer behandelt alle loon- en persoonsgegevens van klanten strikt vertrouwelijk, ook na het einde van de overeenkomst, en leeft de privacyrichtlijnen van de werkgever na (AVG)."),
        ("h2", "Artikel 7 – Beëindiging"),
        ("p", "Elke partij kan de overeenkomst beëindigen met inachtneming van de opzeggingstermijnen van artikel 37/2 van de wet van 3 juli 1978, of om dringende reden."),
        ("h2", "Artikel 8 – Slotbepalingen"),
        ("p", "De werknemer verklaart een exemplaar van het arbeidsreglement v2026-01 te hebben ontvangen. Voor al wat niet geregeld is, gelden de wet van 3 juli 1978 en de cao's van PC 200."),
    ]
    if signed:
        b += [("p", "Opgemaakt te Gent op 10 september 2026 in twee exemplaren, waarvan elke partij erkent er één te hebben ontvangen."),
              ("sig", ["Voor de werkgever\nWouter De Clercq, HR-directeur\nElektronisch ondertekend 10/09/2026 11:42",
                       "De werknemer\nEline Maes\n'Gelezen en goedgekeurd'\nElektronisch ondertekend 10/09/2026 18:05"]),
              ("pi", "Ondertekeningscertificaat: SIGN-2026-09-10-00871 (gekwalificeerde elektronische handtekening)")]
    else:
        b += [("p", "Opgemaakt te Gent op ..................... in twee exemplaren."),
              ("sig", ["Voor de werkgever\n\n\nHandtekening: ____________", "De werknemer\n\n\nHandtekening: ____________"])]
    return b

def contract_signed():
    make_docx("Arbeidsovereenkomst_Eline_Maes_ondertekend.docx",
              contract_blocks("3.450,00", "maandag 5 oktober 2026", "B2", True, "Definitieve versie – ondertekend – ref. AO-2026-0412"),
              author="Wouter De Clercq", title="Arbeidsovereenkomst Eline Maes (ondertekend)", created=dtm(2026, 9, 8, 14), modified=dtm(2026, 9, 10, 18, 5),
              header="Arvelia HR Services NV – Vertrouwelijk – Personeelsdossier E. Maes", footer="AO-2026-0412 – ondertekend 10/09/2026")

def contract_kopie():
    make_docx("Arbeidsovereenkomst_Eline_Maes_v2_kopie.docx",
              contract_blocks("3.650,00", "donderdag 1 oktober 2026", "B3", False, "versie 2"),
              author="Evi Lemmens", title="", created=dtm(2026, 9, 2, 16), modified=dtm(2026, 9, 3, 10, 12))

def template2012():
    b = [
        ("title", "Arbeidsovereenkomst voor bedienden – SJABLOON"),
        ("pi", "Arvelia Interim BVBA – modelcontract – laatst bijgewerkt maart 2012"),
        ("h2", "Artikel 1 – Functie"), ("p", "De bediende wordt aangeworven in de functie van [FUNCTIE] in de afdeling [AFDELING]."),
        ("h2", "Artikel 2 – Proefperiode"),
        ("p", "De eerste zes maanden gelden als proefperiode. Tijdens de proefperiode kan elke partij de overeenkomst beëindigen met een opzegging van zeven dagen, "
              "ten vroegste na de eerste maand."),
        ("h2", "Artikel 3 – Loon"),
        ("p", "Het brutomaandloon bedraagt [BEDRAG] EUR. De bediende ontvangt maaltijdcheques van 6,00 EUR per gewerkte dag (werknemersbijdrage 1,09 EUR)."),
        ("h2", "Artikel 4 – Arbeidsongeschiktheid"),
        ("p", "Voor arbeiders geldt een carensdag; voor bedienden wordt het gewaarborgd maandloon betaald gedurende 30 dagen."),
        ("h2", "Artikel 5 – Opzegging"),
        ("p", "Voor bedienden met een jaarloon onder de wettelijke grens bedraagt de opzeggingstermijn door de werkgever drie maanden per begonnen schijf van vijf jaar anciënniteit. "
              "Boven die grens wordt de termijn in onderling akkoord of door de rechtbank vastgesteld (formule-Claeys)."),
        ("h2", "Artikel 6 – Concurrentiebeding"),
        ("p", "De bediende verbindt zich ertoe gedurende 12 maanden na het einde van de overeenkomst geen gelijkaardige activiteit uit te oefenen in het arrondissement Gent."),
        ("sig", ["Voor de werkgever\n[NAAM]", "De bediende\n[NAAM]"]),
    ]
    make_docx("Sjabloon_Arbeidsovereenkomst_Bediende_2012.docx", b, author="Marc Hendrickx", title="Modelcontract bedienden", created=dtm(2012, 3, 14), modified=dtm(2012, 3, 20),
              footer="Arvelia Interim BVBA – sjabloon")

def functieomschrijving():
    b = [
        ("title", "Functieomschrijving – Payroll Consultant"),
        ("table", [["Functieklasse", "B2 (zie Loonschalen 2026)"], ["Afdeling", "Payroll"], ["Rapporteert aan", "Teamlead Payroll (Bram Wuyts)"],
                   ["Versie / status", "v2.0 – Goedgekeurd"], ["Opgesteld door", "Lotte Peeters, HR Business Partner, 1 juni 2026"],
                   ["Goedgekeurd door", "Wouter De Clercq, HR-directeur, 8 juni 2026"]]),
        ("h1", "Doel van de functie"),
        ("p", "De Payroll Consultant verzorgt de correcte en tijdige loonverwerking voor een portefeuille van KMO-klanten (gemiddeld 25 dossiers, ca. 900 loonbrieven per maand) "
              "en is het eerste aanspreekpunt voor hun sociaaljuridische vragen."),
        ("h1", "Kernverantwoordelijkheden"),
        ("bullets", ["Maandelijkse loonberekening en controle, inclusief variabele prestaties, ploegenpremies en loonbeslag.",
                     "Aangiftes bij de RSZ (Dimona, DmfA) en opmaak van de fiscale fiches (281.10).",
                     "Toepassing van de juiste paritaire comités en sectorale cao's (o.a. PC 200, 118, 124, 302).",
                     "Opvolging van indexeringen, ecocheques, eindejaarspremies en vakantiegeld.",
                     "Advies aan klanten over arbeidsovereenkomsten, tijdelijke werkloosheid en ontslagprocedures, in samenwerking met het erkend sociaal secretariaat.",
                     "Correcte registratie in het payrollsysteem en naleving van de AVG."]),
        ("h1", "Profiel"),
        ("bullets", ["Bachelor (bv. Office Management, Rechtspraktijk, HRM) of gelijkwaardig door ervaring.",
                     "Minstens 2 jaar ervaring in loonadministratie bij een sociaal secretariaat of payrollbureau.",
                     "Nauwkeurig, klantgericht, stressbestendig tijdens piekperiodes (eindejaar, januari).",
                     "Uitstekende kennis Nederlands; goede kennis Frans is een troef."]),
        ("h1", "KPI's"),
        ("table", [["Indicator", "Norm"], ["Loonbrieven foutloos bij eerste verwerking", "≥ 98%"], ["Tijdige RSZ-aangiftes", "100%"],
                   ["Klanttevredenheid (jaarlijkse bevraging)", "≥ 8/10"], ["Antwoordtermijn klantvragen", "≤ 2 werkdagen"]]),
        ("pi", "Bronnen: functieclassificatie Arvelia 2024 (methode analytische weging), Loonschalen 2026, competentiewoordenboek HR."),
    ]
    make_docx("Functieomschrijving_Payroll_Consultant_v2.0.docx", b, author="Lotte Peeters", title="Functieomschrijving Payroll Consultant v2.0",
              created=dtm(2026, 6, 1), modified=dtm(2026, 6, 8, 11), header="Arvelia HR Services NV – Functieomschrijving – v2.0 – Goedgekeurd")

def vacature():
    md = f"""# Vacature: HR Business Partner (m/v/x) – Gent

**Referentie:** VAC-2026-014 · **Gepubliceerd:** 25 augustus 2026 · **Solliciteren tot:** 15 oktober 2026
**Contact:** Lotte Peeters, HR Business Partner – jobs@{DOMEIN}
**Kanalen:** website Arvelia, VDAB-vacaturedatabank, LinkedIn

## Over Arvelia
{BEDRIJF} is een Vlaams HR-dienstenbedrijf met 138 medewerkers in Gent, Antwerpen en Hasselt. We ondersteunen KMO's met recruitment, payroll en HR-advies.
Door de groei van onze interne organisatie zoeken we een tweede HR Business Partner.

## Wat ga je doen?
- Je bent sparringpartner voor de teamleads van Recruitment en Sales & Accountmanagement.
- Je begeleidt functioneringsgesprekken, exitgesprekken en re-integratietrajecten.
- Je analyseert HR-cijfers (verloop, ziekteverzuim) en vertaalt die naar acties.
- Je trekt projecten zoals de herziening van het thuiswerkbeleid en het opleidingsplan.
- Je bewaakt de naleving van het arbeidsreglement en de sociale wetgeving.

## Wie ben jij?
- Master in HRM, rechten, psychologie of gelijkwaardig door ervaring.
- Minstens 5 jaar ervaring als HR-generalist of HRBP, bij voorkeur in een dienstenomgeving.
- Goede kennis van het Belgisch arbeidsrecht (PC 200, arbeidsovereenkomsten, ontslagrecht).
- Sterke communicatieve vaardigheden, discreet en oplossingsgericht.

## Wat bieden wij?
- Contract van onbepaalde duur, functieklasse C1 (zie loonschaal: 4.300 – 5.300 EUR bruto/maand).
- Maaltijdcheques van 8 EUR, ecocheques, groepsverzekering en hospitalisatieverzekering.
- 20 wettelijke + 6 extralegale verlofdagen.
- Thuiswerk tot 2 dagen per week en een thuiswerkvergoeding.
- Opleidingsbudget en minstens 5 opleidingsdagen per jaar.

## Selectieprocedure
1. Screening cv en motivatie (tot 15/10)
2. Eerste gesprek met HR (week 43)
3. Case en gesprek met de HR-directeur (week 45)
4. Aanbod en referentiecheck

*Wij selecteren op basis van competenties, ongeacht leeftijd, geslacht, afkomst of handicap. Lees onze Privacyverklaring voor sollicitanten (v1.4).*
"""
    (OUT / "Vacature_HR_Business_Partner_VAC-2026-014.md").write_text(md, encoding="utf-8")

def cv():
    b = [
        ("title", "Thomas Verhaegen"),
        ("p", "HR Business Partner | Mechelen | thomas.verhaegen@mailbox.example | +32 470 00 00 00 | augustus 2026"),
        ("h1", "Profiel"),
        ("p", "Resultaatgerichte HR-professional met meer dan 8 jaar ervaring. Ik transformeerde de HR-werking van twee organisaties en verlaagde het personeelsverloop "
              "met meer dan 40%. Passie voor mensen, data en verandering. Gekend als 'de beste HR-partner die we ooit hadden'."),
        ("h1", "Ervaring"),
        ("table", [["Periode", "Functie en organisatie", "Verwezenlijkingen"],
                   ["2022 – heden", "HR Business Partner – Logistiek Noord NV (420 medewerkers)", "Uitrol nieuw evaluatiesysteem; verloop -40% (eigen berekening); begeleiding reorganisatie magazijn"],
                   ["2019 – 2022", "HR Generalist – Brouwerij Scheldekant BV", "Opzet onboardingtraject; payrollmigratie naar nieuw sociaal secretariaat"],
                   ["2017 – 2019", "Recruiter – Talentbrug Interim", "Gemiddeld 12 plaatsingen per maand; top recruiter 2018"]], [3*cm, 6.5*cm, 7.5*cm]),
        ("h1", "Opleiding"),
        ("bullets", ["Master Human Resources Management (2017)", "Postgraduaat Sociaal Recht (2020)", "Certificaat Change Management (online, 2023)"]),
        ("h1", "Vaardigheden"),
        ("bullets", ["Belgisch arbeidsrecht, PC 200 en PC 226", "HR-analytics (Excel, Power BI)", "Coaching en conflictbemiddeling",
                     "Talen: Nederlands (moedertaal), Frans (goed), Engels (zeer goed)"]),
        ("h1", "Referenties"), ("p", "Op aanvraag."),
    ]
    make_pdf("CV_Thomas_Verhaegen.pdf", b, author="Thomas Verhaegen", title="CV Thomas Verhaegen", created=dtm(2026, 8, 29, 21), modified=dtm(2026, 8, 29, 21, 30))

def functioneringsgesprek():
    b = [
        ("title", "Verslag functioneringsgesprek 2026"),
        ("table", [["Medewerker", "Pieter Claes – Senior Recruiter (klasse C1)"], ["Leidinggevende", "Ann Sterckx – Manager Recruitment"],
                   ["Datum gesprek", "18 juni 2026"], ["Periode", "1 juli 2025 – 30 juni 2026"], ["Status", "Definitief – door beide partijen ondertekend"]]),
        ("h1", "1. Terugblik op de doelstellingen"),
        ("table", [["Doelstelling", "Norm", "Resultaat", "Beoordeling"],
                   ["Aantal plaatsingen", "30", "34", "Overtroffen"], ["Gemiddelde time-to-hire", "≤ 35 dagen", "31 dagen", "Behaald"],
                   ["Klanttevredenheid", "≥ 8,0", "8,4", "Behaald"], ["Coaching junior recruiters", "2 juniors", "2 juniors", "Behaald"]]),
        ("p", "Cijfers afkomstig uit het sollicitantenvolgsysteem (export 15/06/2026) en de klantbevraging van mei 2026."),
        ("h1", "2. Sterktes"),
        ("p", "Pieter heeft een sterk netwerk in de technische sector en weet kandidaten goed te overtuigen. Klanten waarderen zijn eerlijke communicatie. "
              "Hij nam spontaan de begeleiding van twee junior recruiters op zich."),
        ("h1", "3. Aandachtspunten"),
        ("p", "De administratieve opvolging in het systeem loopt soms achter, waardoor rapportering vertraagt. In piekperiodes delegeert Pieter te weinig."),
        ("h1", "4. Ontwikkelingsplan"),
        ("bullets", ["Opleiding 'Assessmenttechnieken en competentiegericht interviewen' (Q4 2026) – opgenomen in het Opleidingsplan 2026.",
                     "Wekelijkse administratieve blok van 2 uur inplannen.",
                     "Verkennen van doorgroei naar Teamlead Recruitment in 2027."]),
        ("h1", "5. Afspraken en handtekeningen"),
        ("p", "Opvolggesprek gepland in december 2026. De medewerker kon opmerkingen toevoegen: 'Akkoord met het verslag; vraag om extra ondersteuning bij piekperiodes.'"),
        ("sig", ["Leidinggevende\nAnn Sterckx\nondertekend 20/06/2026", "Medewerker\nPieter Claes\nondertekend 21/06/2026"]),
    ]
    make_docx("Functioneringsgesprek_2026_Pieter_Claes.docx", b, author="Ann Sterckx", title="Functioneringsgesprek 2026 – P. Claes",
              created=dtm(2026, 6, 18, 16), modified=dtm(2026, 6, 21, 9), header="Vertrouwelijk – personeelsdossier")

def exitgesprek():
    b = [
        ("title", "Verslag exitgesprek"),
        ("table", [["Medewerker", "Sofie Janssens – Accountmanager (Sales & Accountmanagement)"], ["Datum in dienst", "3 april 2023"],
                   ["Laatste werkdag", "31 augustus 2026"], ["Reden uitdiensttreding", "Ontslag door de werknemer, met opzegging"],
                   ["Gesprek gevoerd door", "Lotte Peeters, HR Business Partner"], ["Datum gesprek", "26 augustus 2026"], ["Status", "Definitief"]]),
        ("h1", "1. Redenen van vertrek"),
        ("p", "Sofie aanvaardde een functie als Key Account Manager bij een werkgever in de regio Aalst, dichter bij haar woonplaats. "
              "Ze noemt de doorgroeimogelijkheid en de kortere woon-werkverplaatsing (van 75 naar 20 minuten) als belangrijkste redenen."),
        ("p", "Gevraagd naar geruchten over een reorganisatie, geeft Sofie aan daar geen kennis van te hebben en dat dit geen rol speelde in haar beslissing."),
        ("h1", "2. Positieve punten"),
        ("bullets", ["Goede teamsfeer en collegialiteit.", "Duidelijk verlof- en thuiswerkbeleid.", "Waardering voor de ondersteuning door haar leidinggevende Kris Mertens."]),
        ("h1", "3. Verbeterpunten"),
        ("bullets", ["Hoge werkdruk tijdens de piekperiode rond jaarafsluiting.", "Weinig transparantie over het commissiesysteem voor accountmanagers.",
                     "CRM-systeem is traag en vraagt dubbele invoer."]),
        ("h1", "4. Scores (1-10)"),
        ("table", [["Aspect", "Score"], ["Algemene tevredenheid", "7"], ["Leidinggevende", "8"], ["Loon en voordelen", "6"], ["Zou Arvelia aanbevelen", "7"]]),
        ("h1", "5. Praktische afhandeling"),
        ("p", "Laptop en badge ingeleverd op 31/08. Eindafrekening en vakantiegeld bij uitdiensttreding verwerkt door payroll. C4 en attesten bezorgd. "
              "Sofie gaf toestemming om geanonimiseerde feedback te delen met de directie."),
        ("pi", "Opgesteld door Lotte Peeters op 27/08/2026 op basis van gespreksnotities; nagelezen door de medewerker per e-mail op 28/08/2026."),
    ]
    make_docx("Exitgesprek_Sofie_Janssens_2026-08.docx", b, author="Lotte Peeters", title="Exitgesprek S. Janssens",
              created=dtm(2026, 8, 27, 10), modified=dtm(2026, 8, 28, 14), header="Vertrouwelijk – HR")

if __name__ == "__main__":
    for f in [contract_signed, contract_kopie, template2012, functieomschrijving, vacature, cv, functioneringsgesprek, exitgesprek]: f()
    print("people ok")

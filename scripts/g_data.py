from common import *
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HDR = PatternFill("solid", fgColor="DCE6F1")
def sheet(ws, rows, widths=None, bold_first=True):
    for r in rows: ws.append(r)
    if bold_first:
        for c in ws[1]: c.font = Font(bold=True); c.fill = HDR
    for i, w in enumerate(widths or [], 1): ws.column_dimensions[get_column_letter(i)].width = w
def props(wb, author, title, created, modified):
    wb.properties.creator = author; wb.properties.lastModifiedBy = author; wb.properties.title = title
    wb.properties.created = created; wb.properties.modified = modified

def loonschalen():
    wb = Workbook(); ws = wb.active; ws.title = "Loonschalen 2026"
    sheet(ws, [["Klasse", "Voorbeeldfuncties", "Minimum (EUR bruto/maand)", "Midpoint", "Maximum", "Opmerking"],
               ["A1", "Onthaalmedewerker", 2450, 2675, 2900, ""],
               ["A2", "Administratief medewerker HR, Payroll officer", 2700, 2950, 3200, ""],
               ["B1", "Junior Payroll Consultant, Junior Recruiter", 2950, 3225, 3500, ""],
               ["B2", "Payroll Consultant, Recruiter, Accountmanager", 3200, 3550, 3900, "Payroll Consultant: functieomschrijving v2.0"],
               ["B3", "Senior Payroll Consultant, IT-servicedesk", 3600, 4000, 4400, ""],
               ["C1", "Senior Recruiter, HR Business Partner, Preventieadviseur", 4300, 4800, 5300, "HRBP: vacature VAC-2026-014"],
               ["C2", "Teamlead, Manager Recruitment, Sales manager", 5000, 5650, 6300, ""],
               ["D", "Directie", 6000, 7000, 8000, "Individueel bepaald binnen vork"]],
          [8, 55, 24, 12, 12, 42])
    for row in ws.iter_rows(min_row=2, min_col=3, max_col=5):
        for c in row: c.number_format = '#,##0 "EUR"'
    ws2 = wb.create_sheet("Extralegale voordelen")
    sheet(ws2, [["Voordeel", "Waarde", "Frequentie", "Bron / regeling"],
                ["Maaltijdcheques", "8,00 EUR (werkgever 6,91 / werknemer 1,09)", "per gewerkte dag", "Arbeidsreglement v2026-01, hfst. 3"],
                ["Ecocheques", "250 EUR (voltijds, volledige referteperiode)", "jaarlijks (juni)", "Sectorale cao PC 200; cao nr. 98 NAR; memo MEMO-HR-2026-07"],
                ["Eindejaarspremie", "13e maand", "december", "Sectorale regeling PC 200"],
                ["Groepsverzekering", "3% van het brutojaarloon", "maandelijks", "Pensioenreglement 2021"],
                ["Hospitalisatieverzekering", "werknemer gratis, gezinsleden tegen tarief", "jaarlijks", "Polis 2024"],
                ["Thuiswerkvergoeding", "150 EUR + 20 EUR internet", "maandelijks", "Thuiswerkbeleid v2.1"],
                ["Opleidingsrecht", "5 dagen per VTE", "jaarlijks", "Opleidingsplan 2026"]], [26, 45, 20, 55])
    ws3 = wb.create_sheet("Info")
    sheet(ws3, [["Veld", "Waarde"], ["Document", "Loonschalen 2026"], ["Versie", "2026.1"], ["Status", "Goedgekeurd"],
                ["Opgesteld door", "Filip Goossens, CFO, i.s.m. Wouter De Clercq, HR-directeur"], ["Goedgekeurd", "Directiecomité, 12 januari 2026"],
                ["Geldig vanaf", "1 januari 2026, na sectorale indexering PC 200"],
                ["Bronnen", "Sectorale barema's PC 200; interne functieclassificatie 2024; arbeidsreglement v2026-01"],
                ["Opmerking", "Individuele lonen liggen binnen de vork van de klasse; afwijkingen vereisen goedkeuring van de HR-directeur."]], [18, 90])
    props(wb, "Filip Goossens", "Loonschalen 2026", dtm(2026, 1, 8), dtm(2026, 1, 12, 17))
    wb.save(OUT / "Loonschalen_2026_v2026.1.xlsx")

def onboarding():
    wb = Workbook(); ws = wb.active; ws.title = "Checklist"
    rows = [["Fase", "Taak", "Verantwoordelijke", "Referentie / toelichting"],
            ["Vóór start", "Arbeidsovereenkomst ondertekend terug ontvangen", "HR-administratie", "Elektronische handtekening"],
            ["Vóór start", "Dimona-aangifte bij de RSZ uiterlijk op de dag vóór de start", "Payroll", "Verplicht"],
            ["Vóór start", "Laptop, accounts en MFA aanvragen via IT-servicedesk (min. 10 werkdagen vooraf)", "HR-administratie", "Ticket in servicedesk"],
            ["Vóór start", "Welkomstmail met praktische info (startuur, adres, documenten)", "HR-administratie", ""],
            ["Vóór start", "Maaltijdchequekaart aanvragen (8,00 EUR per gewerkte dag)", "Payroll", "Arbeidsreglement hfst. 3"],
            ["Dag 1", "Rondleiding, badge, EHBO en evacuatieplan", "Facility", ""],
            ["Dag 1", "Ontvangst arbeidsreglement v2026-01 – tekenen voor ontvangst", "HR-administratie", "Wet 8 april 1965"],
            ["Dag 1", "Toelichting verlofbeleid v3.0: 20 wettelijke + 6 extralegale dagen (pro rata)", "HR Business Partner", "Verlofbeleid 2026"],
            ["Dag 1", "Toelichting thuiswerkbeleid v2.1: max. 2 dagen/week, eerste maand op kantoor", "Leidinggevende", "Thuiswerkbeleid v2.1"],
            ["Week 1", "Privacyrichtlijnen en vertrouwelijkheid (AVG) – e-learning", "DPO", ""],
            ["Week 1", "Kennismaking met team en peter/meter", "Leidinggevende", ""],
            ["Week 1", "Toegang payrollsoftware en MyArvelia controleren", "IT-servicedesk", ""],
            ["Maand 1", "Opleidingsplan inwerktraject opstellen", "Leidinggevende + HR", "Opleidingsplan 2026"],
            ["Maand 1", "Ecocheques en groepsverzekering toelichten", "Payroll", "Loonschalen 2026 – extralegale voordelen"],
            ["Maand 3", "Evaluatiegesprek einde inwerkperiode", "Leidinggevende", "Geen proefperiode (eenheidsstatuut)"]]
    sheet(ws, rows, [12, 78, 22, 40])
    ws2 = wb.create_sheet("Opvolging Eline Maes")
    sheet(ws2, [["Taak", "Status", "Datum", "Opmerking"],
                ["Arbeidsovereenkomst ondertekend", "Afgerond", "10/09/2026", "AO-2026-0412, startdatum 05/10/2026, klasse B2"],
                ["Welkomstmail verstuurd", "Afgerond", "11/09/2026", "Door Evi Lemmens"],
                ["Dimona-aangifte", "Afgerond", "14/09/2026", "Ingediend door payroll"],
                ["Laptop en accounts", "In behandeling", "21/09/2026", "Ticket INC-2026-4471, levering voorzien 02/10/2026"],
                ["Maaltijdchequekaart", "Aangevraagd", "15/09/2026", ""],
                ["Peter/meter", "Afgerond", "18/09/2026", "Bram Wuyts duidt senior collega aan"],
                ["Inwerktraject payroll", "Gepland", "05/10/2026", "Zie Opleidingsplan 2026"]], [34, 16, 14, 55])
    ws3 = wb.create_sheet("Info")
    sheet(ws3, [["Veld", "Waarde"], ["Document", "Onboarding-checklist nieuwe medewerker"], ["Versie", "4.0"], ["Status", "Goedgekeurd"],
                ["Eigenaar", "Evi Lemmens, HR-administratie"], ["Gevalideerd door", "Lotte Peeters, HR Business Partner"], ["Laatste update", "20 augustus 2026 (tabblad opvolging: 21/09/2026)"]], [18, 60])
    props(wb, "Evi Lemmens", "Onboarding-checklist v4.0", dtm(2026, 8, 20), dtm(2026, 9, 21, 15))
    wb.save(OUT / "Onboarding_Checklist_v4.0.xlsx")

def opleidingsplan():
    wb = Workbook(); ws = wb.active; ws.title = "Opleidingen 2026"
    rows = [["Team", "Opleiding", "Aanbieder", "Deelnemer(s)", "Dagen", "Kost (EUR excl. btw)", "Subsidie", "Planning", "Status"],
            ["Payroll", "Update sociale wetgeving 2026", "Sociaal Juridisch Instituut (extern)", "Volledig team (42)", 1, 6300, "KMO-portefeuille", "Q1", "Afgerond"],
            ["Payroll", "Inwerktraject payroll (intern)", "Intern – Bram Wuyts", "Eline Maes", 6, 0, "–", "Okt–dec", "Gepland"],
            ["Payroll", "Loonbeslag en loonoverdracht", "Juridica Academie", "8 consultants", 1, 2400, "KMO-portefeuille", "Q2", "Afgerond"],
            ["Recruitment", "Assessmenttechnieken en competentiegericht interviewen", "Talent Assessment Academy", "Pieter Claes", 3, 1850, "–", "Q4", "Ingeschreven"],
            ["Recruitment", "Employer branding op sociale media", "Intern – Marketing", "12 recruiters", 0.5, 0, "–", "Q3", "Afgerond"],
            ["Sales", "Consultatief verkopen", "SalesLab", "Accountmanagers (6)", 2, 4200, "KMO-portefeuille", "Q2", "Afgerond"],
            ["HR", "Verzuimbeleid en re-integratie", "Provizo EDPB", "Lotte Peeters, Evi Lemmens", 1, 780, "–", "Q3", "Afgerond"],
            ["Alle", "Brandbestrijding en EHBO (bijscholing)", "Provizo EDPB", "14 EHBO'ers", 1, 2100, "–", "Q2", "Afgerond"],
            ["Alle", "AVG-bewustmaking (e-learning)", "Intern – DPO", "Alle medewerkers", 0.25, 0, "–", "Doorlopend", "Lopend"],
            ["IT", "Microsoft 365-beveiliging", "CloudSkills", "3 IT-medewerkers", 2, 2700, "VDAB-opleidingsincentive", "Q4", "Gepland"]]
    sheet(ws, rows, [12, 48, 32, 26, 7, 18, 22, 11, 13])
    ws2 = wb.create_sheet("Samenvatting")
    sheet(ws2, [["Item", "Waarde"], ["Totaal opleidingsbudget 2026", "84.000 EUR"], ["Individueel opleidingsrecht", "5 dagen per VTE per jaar (wet van 3 oktober 2022 – arbeidsdeal)"],
                ["Vlaams opleidingsverlof", "Aanvragen via HR, erkende opleidingen"], ["Subsidiekanalen", "KMO-portefeuille (VLAIO), VDAB-incentives"],
                ["Opgesteld door", "Lotte Peeters, HR Business Partner"], ["Versie", "1.3 – goedgekeurd door de HR-directeur op 10/02/2026, update 01/07/2026"],
                ["Bronnen", "Functioneringsgesprekken 2025-2026, arbeidsdeal 2022, advies ondernemingsraad"]], [32, 80])
    props(wb, "Lotte Peeters", "Opleidingsplan 2026 v1.3", dtm(2026, 2, 10), dtm(2026, 7, 1, 12))
    wb.save(OUT / "Opleidingsplan_2026_v1.3.xlsx")

AFD = [("Payroll", 42, 5.4), ("Recruitment", 36, 4.1), ("Sales & Accountmanagement", 18, 3.8), ("HR & Administratie", 12, 4.4),
       ("Finance", 9, 3.1), ("IT", 8, 6.0), ("Directie & Staf", 13, 4.8)]

def verzuim_q2():
    tot = sum(a[1] for a in AFD); gem = sum(a[1]*a[2] for a in AFD) / tot
    rows = [["Afdeling", "Gem. aantal medewerkers", "Verzuimpercentage Q2"]] + [[a, n, f"{p:.1f}%".replace(".", ",")] for a, n, p in AFD] + \
           [["Totaal / gewogen gemiddelde", tot, f"{gem:.1f}%".replace(".", ",")]]
    b = [
        ("title", "Ziekteverzuimrapport Q2 2026"),
        ("p", "Periode: 1 april – 30 juni 2026 · Versie 1.0 · Status: definitief · Opgesteld door Lotte Peeters (HR Business Partner) i.s.m. Hilde Martens (preventieadviseur) · "
              "Gevalideerd door Wouter De Clercq, HR-directeur, op 14 juli 2026"),
        ("h1", "1. Kerncijfers"),
        ("bullets", [f"Gemiddeld personeelsbestand: {tot} medewerkers (131,4 VTE).",
                     "Totaal verzuimpercentage: 4,6% (Q1 2026: 5,1%; intern streefcijfer: 4,5%).",
                     "Kort verzuim (tot 1 maand): 1,9% – middellang (1-12 maanden): 1,2% – lang (> 12 maanden): 1,5%.",
                     "Verzuimfrequentie: 0,42 meldingen per medewerker per kwartaal.",
                     "Aantal medewerkers in een re-integratietraject: 3."]),
        ("h1", "2. Verzuim per afdeling"),
        ("table", rows, [8*cm, 4.5*cm, 4.5*cm]),
        ("p", "Het hoge percentage in IT wordt verklaard door één langdurige afwezigheid in een klein team. Bij Payroll is er een piek in kort verzuim in april, samenvallend met de afsluiting van de fiscale fiches."),
        ("h1", "3. Acties"),
        ("bullets", ["Uitbreiding van het aanbod rond werkdrukbeheersing voor het payrollteam (workshop in september).",
                     "Opvolging van re-integratietrajecten volgens de regels van de codex welzijn op het werk (boek I, titel 4, hoofdstuk VI).",
                     "Terugkoppeling van de cijfers aan de ondernemingsraad (vergadering 8 september 2026) en het CPBW."]),
        ("h1", "4. Methodologie en bronnen"),
        ("p", "Verzuimpercentage = aantal kalenderdagen afwezig wegens ziekte (exclusief arbeidsongevallen en zwangerschapsverlof) gedeeld door het aantal beschikbare kalenderdagen. "
              "Bron: payrollgegevens MyArvelia (export 5 juli 2026), afwezigheidsregistratie en re-integratiedossiers van de preventieadviseur. Cijfers per afdeling zijn afgerond op één decimaal."),
    ]
    make_pdf("Ziekteverzuimrapport_Q2_2026.pdf", b, author="Lotte Peeters", title="Ziekteverzuimrapport Q2 2026", subject="Ziekteverzuim",
             header="Arvelia HR Services NV – HR-rapportering – Vertrouwelijk", footer="Ziekteverzuimrapport Q2 2026 v1.0 – definitief",
             created=dtm(2026, 7, 10), modified=dtm(2026, 7, 14, 16))
    return gem

def verzuim_csv():
    rows = ["afdeling;medewerkers;verzuim_pct;opmerking",
            "Payroll;45;7,9;veel griep??",
            "Recruitment;36;5,2;",
            "Sales;18;3,8;",
            "HR;12;4,4;",
            "Finance;9;3,1;",
            "IT;8;16;klopt dit? 1 persoon lang ziek",
            "Directie;13;4,8;",
            "TOTAAL;140;6,4;cijfers van Bram? nog na te kijken"]
    (OUT / "verzuim_cijfers_snel.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")

def notulen():
    b = [
        ("title", "Notulen ondernemingsraad"),
        ("table", [["Vergadering", "Gewone vergadering nr. 2026-07"], ["Datum", "8 september 2026, 14u00 – 16u15, vergaderzaal Schelde, Gent"],
                   ["Voorzitter", "Katrien Van Damme, gedelegeerd bestuurder"], ["Secretaris", "An Vos, werknemersvertegenwoordiger"],
                   ["Aanwezig", "Werkgeversafvaardiging: K. Van Damme, W. De Clercq, F. Goossens. Werknemersafvaardiging: A. Vos, J. Dierickx, M. Pauwels, S. Bogaert, T. Wouters."],
                   ["Verontschuldigd", "R. Coppens (werknemersafvaardiging)"],
                   ["Status", "Goedgekeurd door de leden per e-mail op 22 september 2026"]], [4*cm, 13*cm]),
        ("h1", "1. Goedkeuring notulen vorige vergadering"),
        ("p", "De notulen van de vergadering van 16 juni 2026 worden zonder opmerkingen goedgekeurd."),
        ("h1", "2. Economische en financiële informatie (H1 2026)"),
        ("p", "F. Goossens licht de halfjaarcijfers toe: omzetgroei van 4,2% ten opzichte van H1 2025, vooral in de payrollactiviteit. De rendabiliteit ligt in lijn met het budget."),
        ("h1", "3. Tewerkstelling"),
        ("p", "Het personeelsbestand bedraagt 138 medewerkers. In Q3 waren er 3 vertrekken (o.a. in accountmanagement) en 6 aanwervingen, waaronder een Payroll Consultant die start in oktober. "
              "De vacature voor een tweede HR Business Partner (VAC-2026-014) loopt."),
        ("h1", "4. Vraag van de werknemersafvaardiging over geruchten"),
        ("p", "A. Vos meldt dat er geruchten circuleren over een sluiting van het kantoor in Antwerpen en naakte ontslagen. De directie verklaart formeel dat er "
              "geen herstructurering, sluiting of collectief ontslag gepland is. Het kantoor Antwerpen verhuist in de loop van 2027 naar een nieuw pand in Berchem; "
              "alle medewerkers behouden hun functie. Bij elke toekomstige wijziging zal de procedure-Renault worden gevolgd."),
        ("h1", "5. Ziekteverzuim Q2 2026"),
        ("p", "W. De Clercq bespreekt het ziekteverzuimrapport Q2: 4,6% (Q1: 5,1%). De werknemersafvaardiging vraagt aandacht voor werkdruk in het payrollteam; een workshop werkdrukbeheersing wordt in september georganiseerd."),
        ("h1", "6. Thuiswerk"),
        ("p", "Het thuiswerkbeleid v2.1 (maximaal 2 dagen per week, kerndagen dinsdag en donderdag) blijft onverkort van toepassing. Een werkgroep bereidt een herziening voor; "
              "een concept wordt eind 2026 aan de ondernemingsraad voorgelegd. Er worden geen afwijkende afspraken per team toegestaan in afwachting daarvan."),
        ("h1", "7. Ecocheques en maaltijdcheques"),
        ("p", "De ecocheques (250 EUR voor een voltijdse medewerker met volledige referteperiode) werden in juni uitbetaald. De maaltijdcheques blijven 8,00 EUR per gewerkte dag."),
        ("h1", "8. Varia"),
        ("p", "Werken aan de parking van de zetel Gent in oktober: de facility manager communiceert de praktische regeling. Volgende vergadering: 13 oktober 2026."),
        ("space", 6),
        ("p", "Voor akkoord: Katrien Van Damme (voorzitter) – An Vos (secretaris)."),
        ("small", "Bronnen: ziekteverzuimrapport Q2 2026; halfjaarrapport Finance H1 2026; thuiswerkbeleid v2.1; memo MEMO-HR-2026-07."),
    ]
    make_pdf("Notulen_Ondernemingsraad_2026-09-08.pdf", b, author="An Vos", title="Notulen OR 8 september 2026", subject="Ondernemingsraad",
             header="Arvelia HR Services NV – Ondernemingsraad – Notulen 2026-07", footer="Goedgekeurd 22/09/2026",
             created=dtm(2026, 9, 10), modified=dtm(2026, 9, 22, 12))

if __name__ == "__main__":
    loonschalen(); onboarding(); opleidingsplan(); print("verzuim gem", verzuim_q2()); verzuim_csv(); notulen()
    print("data ok")

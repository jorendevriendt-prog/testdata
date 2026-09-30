from common import *
from email.message import EmailMessage
from email.utils import format_datetime
import datetime as dt, hashlib

TZ = dt.timezone(dt.timedelta(hours=2))
def eml(filename, frm, to, subject, date, body, cc=None, extra=None):
    m = EmailMessage()
    m["From"] = frm; m["To"] = to
    if cc: m["Cc"] = cc
    m["Subject"] = subject; m["Date"] = format_datetime(date.replace(tzinfo=TZ))
    m["Message-ID"] = f"<{hashlib.md5(filename.encode()).hexdigest()[:16]}@{frm.split('@')[-1].strip('>')}>"
    for k, v in (extra or {}).items(): m[k] = v
    m.set_content(body, charset="utf-8")
    (OUT / filename).write_bytes(bytes(m))

def mail_start():
    eml("Email_HR_Bevestiging_Startdatum_Eline_Maes.eml", "Evi Lemmens <evi.lemmens@arvelia-hr.be>", "Eline Maes <eline.maes@mailbox.example>",
        "Welkom bij Arvelia – praktische info voor je start op maandag 5 oktober", dt.datetime(2026, 9, 11, 9, 14),
        """Beste Eline,

Van harte welkom bij Arvelia HR Services! We hebben je ondertekende arbeidsovereenkomst (ref. AO-2026-0412) goed ontvangen. Hierbij de praktische informatie voor je eerste werkdag.

Startdatum: maandag 5 oktober 2026 om 9u00
Adres: Voskenslaan 214, 9000 Gent – meld je aan bij het onthaal op het gelijkvloers
Je leidinggevende: Bram Wuyts, Teamlead Payroll

Wat breng je mee?
- Je identiteitskaart (voor de badge)
- Je rekeningnummer (IBAN) voor de loonbetaling, als dat nog niet in MyArvelia staat
- Je vakantieattest van je vorige werkgever: je wettelijke vakantiedagen voor 2026 worden berekend op basis van je prestaties in 2025
- Eventuele attesten voor gezinslasten (bedrijfsvoorheffing)

Goed om te weten:
- De Dimona-aangifte wordt vóór je start ingediend door onze payrollcollega's.
- Je laptop en accounts worden door de IT-servicedesk klaargezet (je krijgt je login op dag 1).
- Je ontvangt maaltijdcheques van 8,00 EUR per gewerkte dag op een elektronische kaart.
- Voor 2026 heb je recht op 1,5 extralegale verlofdag (6 dagen pro rata voor 3 maanden), volgens het verlofbeleid v3.0.
- De eerste maand werk je op kantoor voor je inwerktraject; daarna kan je tot 2 dagen per week thuiswerken volgens het thuiswerkbeleid.

Tijdens je eerste dag krijg je een rondleiding, het arbeidsreglement en een kennismaking met je team. Heb je vragen, aarzel dan niet om me te contacteren.

Tot binnenkort!

Met vriendelijke groeten,
Evi Lemmens
HR-administratie | Arvelia HR Services NV
Voskenslaan 214, 9000 Gent | +32 9 123 45 67 | www.arvelia-hr.be
""", cc="Bram Wuyts <bram.wuyts@arvelia-hr.be>")

def mail_teamlead():
    eml("Email_Teamlead_Thuiswerk_3dagen.eml", "Bram Wuyts <bram.wuyts@arvelia-hr.be>", "team-payroll@arvelia-hr.be",
        "Goed nieuws: 3 dagen thuiswerk vanaf oktober!", dt.datetime(2026, 9, 18, 17, 52),
        """Hey team,

Kort berichtje voor het weekend: ik heb deze week mondeling met Wouter besproken dat ons team vanaf 1 oktober 3 dagen per week mag thuiswerken. De kerndagen vallen voor ons weg, we spreken gewoon af wie wanneer op kantoor is.

Ook de thuiswerkvergoeding zou naar 200 euro per maand gaan, dat staat in het nieuwe beleid dat binnenkort uitkomt. Jullie hoeven niets aan te vragen, ik regel dat wel met HR.

Tijdens de afsluiting van de maand verwacht ik wel dat iedereen bereikbaar is, uiteraard.

Nog een fijn weekend!
Bram

Verstuurd vanaf mijn iPhone
""")

def mail_roddel():
    eml("Email_Anoniem_Geruchten_Reorganisatie.eml", "Iemand die het weet <iemand.diehetweet@mailbox.example>",
        "undisclosed-recipients:;", "FW: FW: wat ze jullie NIET vertellen!!!", dt.datetime(2026, 9, 24, 23, 7),
        """Hallo allemaal,

Ik stuur dit anoniem want anders zit ik zelf in de problemen. Van iemand "van boven" heb ik gehoord dat het kantoor in Antwerpen tegen de zomer dichtgaat en dat er minstens 30 mensen op straat gaan staan. Daarom is Sofie van sales ook zo plots vertrokken, die wist het al.

Ze gaan dat natuurlijk pas zeggen als het te laat is. Let maar op: eerst verhuizen ze "tijdelijk" iedereen, en dan is het gedaan. Er komt ook een nieuw thuiswerkbeleid waarbij thuiswerk volledig wordt afgeschaft, en de ecocheques verdwijnen ook.

Iemand van payroll zegt dat de lonen van volgend jaar bevroren worden. Ik weet niet of dat klopt maar het zou me niet verbazen.

Stuur dit door naar iedereen die het moet weten. Niet naar HR natuurlijk!!

Groetjes,
een bezorgde collega

-------- Doorgestuurd bericht --------
> ik heb dit ook gehoord van iemand van Hasselt, het is echt waar
> ---
> weet iemand meer??
""")

def mail_it():
    eml("IT_Ticket_INC-2026-4471_Laptop_Nieuwe_Medewerker.eml", "Arvelia IT-servicedesk <servicedesk@arvelia-hr.be>", "Evi Lemmens <evi.lemmens@arvelia-hr.be>",
        "[INC-2026-4471] Update: laptop en accounts nieuwe medewerker E. Maes", dt.datetime(2026, 9, 21, 11, 3),
        """Beste Evi,

Er is een update voor je aanvraag.

Ticketnummer: INC-2026-4471
Categorie: Onboarding – hardware en accounts
Aangevraagd door: Evi Lemmens (HR-administratie) op 15/09/2026
Behandelaar: Stijn Dewulf (IT-servicedesk)
Prioriteit: Normaal
Status: In behandeling

Omschrijving aanvraag:
Nieuwe medewerker Eline Maes, functie Payroll Consultant, team Payroll (leidinggevende Bram Wuyts). Startdatum maandag 05/10/2026.
Benodigd: laptop standaardconfiguratie consultant, headset, tweede scherm voor thuiswerk (na eerste maand), Microsoft 365-account, MFA, toegang MyArvelia, payrollsoftware (profiel consultant), gedeelde map Payroll.

Update van Stijn Dewulf (21/09/2026 11:03):
- Laptop (Lenovo ThinkPad T14, asset ARV-LT-0388) besteld, levering bij IT voorzien op 02/10/2026.
- Microsoft 365-account aangemaakt: eline.maes@arvelia-hr.be (actief vanaf 05/10/2026 08:00).
- Licentie payrollsoftware aangevraagd bij de leverancier, bevestiging verwacht binnen 3 werkdagen.
- Tweede scherm en headset uit voorraad gereserveerd.
- MFA wordt op dag 1 samen met de medewerker geactiveerd (smartphone nodig).

Volgende stap: configuratie en test op 02/10. Je krijgt een melding zodra het ticket op "Opgelost" staat.

Je kan dit ticket opvolgen in het servicedeskportaal. Antwoord op deze mail om een opmerking toe te voegen (laat het ticketnummer in het onderwerp staan).

Met vriendelijke groeten,
Arvelia IT-servicedesk
servicedesk@arvelia-hr.be | intern 4400
""", extra={"X-Ticket-ID": "INC-2026-4471"})

def mail_newsletter():
    eml("Nieuwsbrief_CloudDesk_Pro_September.eml", "CloudDesk Pro <nieuws@clouddeskpro.example>", "info@arvelia-hr.be",
        "🚀 Nooit meer administratie? Ontdek CloudDesk Pro 7.0 – nu 50% korting!", dt.datetime(2026, 9, 16, 7, 30),
        """Bekijk deze e-mail in je browser

CLOUDDESK PRO – DE NIEUWSBRIEF VAN SEPTEMBER

Beste ondernemer,

De herfst is begonnen en dat betekent: tijd voor verandering! Met CloudDesk Pro 7.0 werkt je hele kantoor in de cloud. Onze klanten besparen gemiddeld 90% tijd op administratie*. Dat is geen belofte, dat is een garantie!**

NIEUW IN VERSIE 7.0
- Slimme agenda die zelf je vergaderingen plant
- AI-assistent "Deskie" die je e-mails beantwoordt terwijl jij koffie drinkt
- Donkere modus en 12 nieuwe kleurthema's
- Integratie met meer dan 400 apps

KLANTGETUIGENIS
"Sinds CloudDesk Pro heb ik elke vrijdag vrij!" – Karel, zaakvoerder

ACTIE: 50% korting op je eerste jaar met code HERFST50. Alleen geldig tot zondag middernacht!

WEBINAR: "Het kantoor van de toekomst", donderdag om 11u. Schrijf je nu in, de plaatsen zijn beperkt!

* Op basis van een interne enquête bij 37 enthousiaste gebruikers.
** Voorwaarden van toepassing.

Je ontvangt deze e-mail omdat je je ooit hebt ingeschreven op een van onze beurzen. Uitschrijven | Voorkeuren beheren
CloudDesk Pro – Voorbeeldlaan 1, 1000 Brussel
""")

def notities():
    txt = """notities bonus/voordelen – NIET DELEN

ok dus volgens mij:
- iedereen krijgt 13e EN 14e maand?? (Kevin zegt van wel, bij zijn vorige job was dat zo)
- ecocheques worden afgeschaft vanaf volgend jaar, heb ik gehoord in de refter
- maaltijdcheques gaan naar 10 euro, of was dat enkel bij de overheid? checken
- cao 90 bonus: 1500 netto per persoon?? (klopt denk ik niet, is waarschijnlijk bruto + hangt af van doelstellingen)
- hospitalisatie: gezinsleden gratis? -> vragen aan payroll
- groepsverzekering 5%?? of 3

vragen voor HR:
* wanneer komt de bonus
* waarom krijgt team X meer (ze zeggen dat)
* kan ik mijn verlof van vorig jaar nog opnemen (volgens mij tot eind februari???)

todo: dit eens proper uitzoeken voor het teamoverleg
"""
    (OUT / "notities_bonus_voordelen.txt").write_text(txt, encoding="utf-8")

def lunchmenu():
    txt = """BEDRIJFSRESTAURANT DE KANTINE – ZETEL GENT
Weekmenu week 40 (28 september – 2 oktober 2026)
Cateraar: Smaakmakers Catering

MAANDAG
  Soep: pompoensoep met geroosterde pitten
  Dagschotel: kip curry met basmatirijst
  Veggie: linzendahl met naanbrood

DINSDAG
  Soep: tomatensoep met balletjes
  Dagschotel: stoofvlees met frietjes en sla
  Veggie: groentelasagne

WOENSDAG
  Soep: preisoep
  Dagschotel: vol-au-vent met kroketten
  Veggie: quiche met spinazie en geitenkaas

DONDERDAG
  Soep: groentesoep
  Dagschotel: spaghetti bolognese
  Veggie: spaghetti met tomatensaus en linzen

VRIJDAG
  Soep: witloofsoep
  Dagschotel: vispannetje met puree
  Veggie: falafel met hummus en couscous

Prijzen: soep 1,50 EUR – dagschotel 6,50 EUR – broodje 3,80 EUR. Betalen met badge of Payconiq.
Allergenen: vraag ernaar aan de kassa.
Tip: op vrijdag is er verse fruitsla als dessert!
"""
    (OUT / "Lunchmenu_Week40_2026.txt").write_text(txt, encoding="utf-8")

def facility():
    md = """# Facility-mededeling: werken aan de parking – zetel Gent

**Van:** Nadia El Amrani, Facility Manager · **Datum:** 28 september 2026 · **Voor:** alle medewerkers zetel Gent

## Wat?
Van **maandag 12 oktober tot en met vrijdag 23 oktober 2026** wordt de parking aan de achterzijde van het gebouw heraangelegd (nieuwe asfaltlaag, belijning en 8 extra laadpalen voor elektrische wagens).

## Wat betekent dit voor jou?
- De achterparking (64 plaatsen) is volledig **onbeschikbaar**.
- Er zijn **30 plaatsen** voorbehouden op de parking van het naburige bedrijvencentrum (Voskenslaan 230). Reservatie via de parkeertool op het intranet, wie eerst komt, eerst maalt.
- Mindervaliden- en bezoekersplaatsen aan de voorzijde blijven beschikbaar.
- De fietsenstalling blijft bereikbaar via de zij-ingang.
- Kom indien mogelijk met het openbaar vervoer of de fiets (tramhalte op 400 m).
- Leidinggevenden kunnen in deze periode occasioneel thuiswerk toestaan, **binnen de regels van het thuiswerkbeleid v2.1 (maximaal 2 dagen per week, kerndagen dinsdag en donderdag op kantoor)**.

## Hinder
Tijdens de eerste twee dagen kunnen er geluidshinder en geurhinder zijn (asfalteren). Vergaderzalen aan de achterzijde worden best vermeden.

## Vragen?
facility@arvelia-hr.be of intern 4100.

*Aannemer: Wegenwerken Verbeke BV – opvolging door de facilitydienst. Deze regeling werd aangekondigd in de ondernemingsraad van 8 september 2026 (punt varia).*
"""
    (OUT / "Facility_Mededeling_Parkeerwerken_Oktober.md").write_text(md, encoding="utf-8")

def recept():
    b = [
        ("title", "Oma's stoofvlees met Westmalle"),
        ("pi", "voor 6 personen – het echte recept (niet dat van de kantine!)"),
        ("h1", "Ingrediënten"),
        ("bullets", ["1,5 kg runderstoofvlees (schouder of kaaklappen)", "3 grote uien", "2 flesjes donker trappistenbier", "2 sneden bruin brood",
                     "2 eetlepels mosterd", "2 laurierblaadjes en een takje tijm", "1 eetlepel bruine suiker", "1 scheutje azijn",
                     "boter, peper en zout"]),
        ("h1", "Bereiding"),
        ("num", ["Snij het vlees in blokken van ongeveer 4 cm en dep droog.",
                 "Bak het vlees in porties bruin in ruim boter. Kruid met peper en zout.",
                 "Stoof de gesneden uien glazig in dezelfde pot.",
                 "Voeg het vlees terug toe, blus met het bier en voeg laurier, tijm, suiker en azijn toe.",
                 "Besmeer de sneden brood met mosterd en leg ze bovenop het vlees.",
                 "Laat minstens 3 uur heel zachtjes stoven met het deksel op de pot. Roer af en toe.",
                 "Proef en breng op smaak. Nog beter als je het een dag op voorhand maakt!"]),
        ("h1", "Tip van oma"),
        ("p", "Serveer met verse frieten en appelmoes. Een stukje pure chocolade op het einde maakt de saus extra rond."),
    ]
    make_docx("Recept_Stoofvlees_Oma.docx", b, author="Pieter Claes", title="stoofvlees", created=dtm(2021, 11, 3, 20), modified=dtm(2021, 11, 3, 20, 30))

def ogm(n10):
    c = n10 % 97 or 97
    s = f"{n10:010d}{c:02d}"
    return f"+++{s[:3]}/{s[3:7]}/{s[7:]}+++"

def offerte():
    b = [
        ("title", "Offerte payrolldiensten"),
        ("table", [["Offertenummer", "OFF-2026-0931"], ["Datum", "22 september 2026"], ["Geldig tot", "22 oktober 2026"],
                   ["Klant", "Bakkerij De Smet BV, Industrieweg 12, 9160 Lokeren – t.a.v. mevrouw Griet De Smet, zaakvoerder"],
                   ["Opgesteld door", "Kris Mertens, Sales Manager – kris.mertens@arvelia-hr.be"]], [4*cm, 13*cm]),
        ("h1", "1. Uw situatie"),
        ("p", "Bakkerij De Smet BV stelt 45 werknemers tewerk: 31 arbeiders (PC 118, voedingsnijverheid) en 14 bedienden (PC 220). "
              "U wenst de loonverwerking uit te besteden en ondersteuning bij sociaaljuridische vragen, met name rond nachtarbeid, ploegenpremies en tijdelijke werkloosheid."),
        ("h1", "2. Ons voorstel"),
        ("bullets", ["Maandelijkse loonverwerking en loonbrieven via ons digitaal portaal, in samenwerking met ons erkend sociaal secretariaat.",
                     "Alle RSZ-aangiftes (Dimona, DmfA) en fiscale fiches.",
                     "Toepassing van de sectorale regels van PC 118 en PC 220 (premies, eindejaarspremie, ecocheques).",
                     "Vast aanspreekpunt: een Payroll Consultant met ervaring in de voedingssector.",
                     "Juridische helpdesk (antwoord binnen 2 werkdagen)."]),
        ("h1", "3. Prijzen (excl. 21% btw)"),
        ("table", [["Omschrijving", "Eenheidsprijs", "Aantal / maand", "Totaal / maand"],
                   ["Loonbrief (arbeider of bediende)", "17,50 EUR", "45", "787,50 EUR"],
                   ["Juridische helpdesk (forfait)", "150,00 EUR", "1", "150,00 EUR"],
                   ["Totaal maandelijks", "", "", "937,50 EUR"],
                   ["Eenmalige opstartkost (dossieropbouw, migratie)", "950,00 EUR", "1", "950,00 EUR"]], [7*cm, 3.3*cm, 3.2*cm, 3.5*cm]),
        ("h1", "4. Voorwaarden"),
        ("p", "Prijzen worden jaarlijks op 1 januari geïndexeerd volgens de index van de consumptieprijzen. Betaling binnen 30 dagen na factuurdatum. "
              "Opzegging van de dienstverlening met een termijn van 3 maanden. Onze algemene voorwaarden (versie 2025) zijn van toepassing. "
              "Een verwerkersovereenkomst (AVG) maakt deel uit van het contract."),
        ("p", "Voor akkoord: gelieve deze offerte ondertekend terug te bezorgen. Opstart mogelijk vanaf de loonperiode januari 2027."),
        ("small", f"{BEDRIJF} – {ADRES} – {KBO} – {IBAN}"),
    ]
    make_pdf("Offerte_OFF-2026-0931_Bakkerij_De_Smet.pdf", b, author="Kris Mertens", title="Offerte OFF-2026-0931", subject="Offerte payroll",
             header=f"{BEDRIJF} – Offerte", footer="OFF-2026-0931", created=dtm(2026, 9, 22, 10), modified=dtm(2026, 9, 22, 11))

def factuur():
    b = [
        ("title", "FACTUUR"),
        ("table", [["Factuurnummer", "2026-0917"], ["Factuurdatum", "17 september 2026"], ["Vervaldatum", "17 oktober 2026"],
                   ["Klant", "Garage Vermeulen BV, Brusselsesteenweg 88, 9090 Melle – btw BE 0698.765.432"],
                   ["Uw referentie", "Aanwerving Werkplaatschef – opdracht REC-2026-058"]], [4*cm, 13*cm]),
        ("h1", "Omschrijving"),
        ("table", [["Omschrijving", "Bedrag"],
                   ["Recruitmentfee succesvolle plaatsing Werkplaatschef (kandidaat gestart op 1 september 2026) – 18% van het bruto jaarloon van 52.000 EUR", "9.360,00 EUR"],
                   ["Subtotaal excl. btw", "9.360,00 EUR"], ["Btw 21%", "1.965,60 EUR"], ["Totaal te betalen", "11.325,60 EUR"]], [12*cm, 5*cm]),
        ("p", f"Gelieve het totaalbedrag te storten op rekening {IBAN} (BIC {BIC}) met gestructureerde mededeling {ogm(9012345678)}."),
        ("p", "Garantieregeling: indien de kandidaat binnen 3 maanden de onderneming verlaat, zoeken wij kosteloos een vervanger (zie raamovereenkomst van 12 mei 2026)."),
        ("p", "Bij laattijdige betaling zijn van rechtswege en zonder ingebrekestelling nalatigheidsinteresten verschuldigd volgens de wet van 2 augustus 2002 betreffende de bestrijding van de betalingsachterstand bij handelstransacties."),
        ("small", f"{BEDRIJF} – {ADRES} – Btw {KBO} – RPR Gent – Opgemaakt door Ines Aerts, boekhouding – boekhouding@arvelia-hr.be"),
    ]
    make_pdf("Factuur_2026-0917_Garage_Vermeulen.pdf", b, author="Ines Aerts", title="Factuur 2026-0917", subject="Factuur",
             header=f"{BEDRIJF} – Factuur 2026-0917", created=dtm(2026, 9, 17, 9), modified=dtm(2026, 9, 17, 9))

if __name__ == "__main__":
    for f in [mail_start, mail_teamlead, mail_roddel, mail_it, mail_newsletter, notities, lunchmenu, facility, recept, offerte, factuur]: f()
    print("misc ok")

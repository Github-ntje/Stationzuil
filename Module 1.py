import csv
import random
import datetime

datum = datetime.datetime.now().strftime("%Y-%m-%d")
tijd =  datetime.datetime.now().strftime("%H:%M:%S")


print('Welkom, laat uw mening en/of opmerking achter over het station waar u zich op dit moment bevindt.')
naam = input('Vul uw naam in, indien u anoniem wilt blijven vul dan niks in: ')
#Hier vult de reiziger zijn naam in. Als hij niks invult wordt er automatisch anoniem ingevuld.
if len(naam) <= 0:
    print('Anoniem')
else:
    print(naam)
#Met de if-statement heb ik ervoor gezorgt dat het mogelijk is om ook anoniem te kunnen blijven.
def station():
    stations = open('Stations.txt', 'r').readline()
    #Hier open ik het txt bestand van stations en lees ik het.
    stationSplitted = stations.split(",")
    random_station = random.choice(stationSplitted).strip()
    #Met de random functie kiest het programma zelf random een station uit het bestand.
    return random_station
def naamFunctie():
    outfile = open('feedback.NS.csv', 'a')
    if len(naam) <= 0:
        print('Anoniem')

    if len(naam) > 0:
        volledig_bericht = f"{naam}, "
    else:
         outfile.write('Anoniem')
    outfile.close()
    #Hier ben ik begonnen met het openen van de feedback txt bestand en heb ik 'a' gebruikt.
    #Op deze manier wordt er de naam (of anoniem) die is ingevoerd, toegevoegd in het txt bestand.
    return naam

def bericht():
    blijf_controleren = True
    while blijf_controleren:
        outfile = open('feedback.NS.csv', 'a')
        feedback = input('Geef uw feedback met max. 140 tekens: ')
        blijf_controleren = False
        if len(feedback) > 140:
            print('Feedback bevat te veel tekens, max. van 140 is bereikt, probeer opnieuw')
            blijf_controleren = True
        else:
            print('Bedankt voor uw bericht, die is verstuurt op: ')
        print(datum)
        print(tijd)
        #Hier doe ik het zelfde als bij de naam invoegen, maar dan met de feedback.
        #met de if-statement zorg ik ervoor dat de feedback niet langer dan 140 tekens mag bevatten.
        #Ik gebruik hier een while loop zodat de reiziger bij te veel tekens nog een poging heeft om de feedback te versturen.
    volledig_bericht = f"{naamFunctie()},{feedback},{station()},{datum},{tijd}\n"
    #Hier zorg ik ervoor dat alles netjes op een rijtje in het txt bestand feedback komt te staan.
    #Alles wordt gescheiden met komma's, zodat ik dit later nog makkelijk kan splitten indien nodig.
    #Aan het einde heb ik \n toegevoegd zodat niet alles achter elkaar komt te staan maar elk bericht een aparte regel krijgt.
    outfile.write(volledig_bericht)
    #Hier wordt het hele bericht met juiste structuur geschreven in het txt bestand.
    outfile.close()
    # Uiteindelijk sluit ik het bestand.
bericht()

import csv
import random
import datetime
import psycopg2

datum = datetime.datetime.now().strftime("%Y-%m-%d")
tijd =  datetime.datetime.now().strftime("%H:%M:%S")


print('Welkom, laat uw mening en/of opmerking achter over het station waar u zich op dit moment bevindt.')
naam = input('Vul uw naam in, indien u anoniem wilt blijven vul dan niks in: ')
if len(naam) <= 0:
    print('Anoniem')
else:
    print(naam)

def station():
    stations = open('Stations.txt', 'r').readline()

    stationSplitted = stations.split(",")
    random_station = random.choice(stationSplitted)

    #print('station' + random_station)
    return random_station
    #print(f"station {random_station}")
    #print('station' + random_station)
def naamFunctie():
    outfile = open('feedback.NS.csv', 'a')
    if len(naam) <= 0:
        print('Anoniem')

    if len(naam) > 0:
        volledig_bericht = f"{naam}, "
    else:
         outfile.write('Anoniem')
    outfile.close()
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
    volledig_bericht = f"{naamFunctie()},{feedback},station {station()},{datum},{tijd}\n"
    outfile.write(volledig_bericht)
    outfile.close()
bericht()

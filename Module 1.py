import csv
import random
import datetime

datum = datetime.datetime.now()


print('Welkom, laat uw mening en/of opmerking achter over het station waar u zich op dit moment bevindt.')
naam = input('Vul uw naam in, indien u anoniem wilt blijven vul dan niks in: ')



# naamFunctie()
def station():
    stations = open('Stations.txt', 'r').readline()

    stationSplitted = stations.split(",")
    random_station = random.choice(stationSplitted)

    print(f'station {random_station}')
    return random_station
def naamFunctie():
    outfile = open('feedback.NS.csv', 'a')
    if len(naam) <= 0:
        print('Anoniem')

    if len(naam) > 0:
        volledig_bericht = f"{naam}, "
         #outfile.write(naam)
         #outfile.write(', ')
    else:
         #volledig_bericht = f"{'Anoniem'}, "
         outfile.write('Anoniem, ')
         #volledig_bericht = f"{naam}, "
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

    volledig_bericht = f"{naamFunctie()}, {feedback}, {station()}, {datum}'\n'"
    #print(volledig_bericht)
    outfile.write(volledig_bericht)
    print(datum)
bericht()

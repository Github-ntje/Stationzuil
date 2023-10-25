#import psycopg
import datetime
datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def gecontroleerd_bericht():
    #hier open ik het txt bestand en lees ik elke regel.
    infile = open('feedback.NS.csv', 'r')
    berichten = infile.readlines()
    infile.close()


def main():
    #het menu gebruik ik zodat er structuur is, hier vraag ik de naam en a-mail van de moderator.
    berichten = gecontroleerd_bericht()
    #hier roep ik bovenstaande variabelen aan om error te voorkomen.
    naam = input('Voer uw naam in: ')
    email = input('Voer uw e-mailadres in: ')





if __name__ == "__main__":
    main()



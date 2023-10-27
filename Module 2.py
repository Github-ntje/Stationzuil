import psycopg2
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
    naam_moderator = input('Voer uw naam in: ')
    email_moderator = input('Voer uw e-mailadres in: ')

    connection_string = "host='4.234.213.225' dbname='stationszuil' user='postgres' password='Appeltaart123!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    conn.commit()
    conn.close()





if __name__ == "__main__":
    main()

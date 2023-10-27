import psycopg2
import datetime
import csv
datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def gecontroleerd_bericht():
    #hier open ik het txt bestand en lees ik elke regel.
    infile = open('feedback.NS.csv', 'r')
    #reader = csv.reader(infile)
    #return reader, infile
    berichten = infile.readlines()
    infile.close()
    return berichten

def main():
    berichten = gecontroleerd_bericht()
    # het menu gebruik ik zodat er structuur is, hier vraag ik de naam en a-mail van de moderator.
    # hier roep ik bovenstaande variabelen aan om error te voorkomen.
    naam_moderator = input('Voer uw naam in: ')
    email_moderator = input('Voer uw e-mailadres in: ')
    werknemernr = str(input('Voer werknemernummer in: '))

    connection_string = "host='4.234.213.225' dbname='stationszuil' user='postgres' password='Appeltaart123!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = """INSERT INTO moderator(werknemernr, naam, emailadres) VALUES (%s, %s, %s);"""
    data = (werknemernr, naam_moderator, email_moderator)
    cursor.execute(query, data)

    #cursor.execute("""SELECT * FROM moderator""");
    #werknemernr = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    print('Moderator: ' + str(werknemernr))

    for x in berichten:
        print('Onderstaand bericht met bijbehorende gegevens is getoond: ' + berichten[1])

        controle = input('Om dit bericht goed te keuren toets ja, om dit bericht af te keuren toets nee: ')
        if 'ja' in controle:
            print('Bericht is goedgekeurd!')
        if 'nee' in controle:
            print('Bericht is afgekeurd!')
        elif 'ja' and 'nee' not in controle:
            print('Voer ja of nee in, er is geen andere mogelijkheid. Probeer opnieuw: ')
        return x
            #blijf_controleren = False

            #print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


    #het menu gebruik ik zodat er structuur is, hier vraag ik de naam en a-mail van de moderator.
    #berichten = gecontroleerd_bericht()
    #hier roep ik bovenstaande variabelen aan om error te voorkomen.





if __name__ == "__main__":
    main()

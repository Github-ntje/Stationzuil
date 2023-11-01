import psycopg2
import datetime
datum = datetime.datetime.now().strftime("%Y-%m-%d")
tijd = datetime.datetime.now().strftime("%H:%M:%S")

def gecontroleerd_bericht():
    #hier open ik het txt bestand en lees ik elke regel.
    infile = open('feedback.NS.csv', 'r')
    volledig_bericht = infile.readlines()
    infile.close()
    return volledig_bericht

def main():
    volledig_bericht = gecontroleerd_bericht()
    # het menu gebruik ik zodat er structuur is, hier vraag ik de naam en a-mail van de moderator.
    # hier roep ik bovenstaande variabelen aan om error te voorkomen.
    naam_moderator = input('Voer uw naam in: ')
    email_moderator = input('Voer uw e-mailadres in: ')

    connection_string = "host='4.234.213.225' dbname='stationszuil' user='postgres' password='Appeltaart123!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    moderator_check_query = """SELECT werknemernr FROM moderator WHERE naam = %s AND emailadres = %s;"""
    data = (naam_moderator, email_moderator)
    cursor.execute(moderator_check_query, data)
    moderator_check = cursor.fetchone()
    if moderator_check is None:
        query = """INSERT INTO moderator(naam, emailadres) VALUES (%s, %s);"""
        data = (naam_moderator, email_moderator)
        cursor.execute(query, data)
        moderator_nummer_query = """SELECT werknemernr FROM moderator WHERE naam = %s;"""
        data = (naam_moderator,)
        cursor.execute(moderator_nummer_query, data)
        werknemernummer = cursor.fetchone()[0]
    else:
        werknemernummer = moderator_check[0]

    volledig_bericht_kopie = list(volledig_bericht)
    for x in volledig_bericht:
        print('Onderstaand bericht met bijbehorende gegevens is getoond: ' + x)

        controle = input('Om dit bericht goed te keuren toets false, om dit bericht af te keuren toets true. Als u wilt stoppen met beoordelen, toets dan exit: ')
        outfile = open('feedback.NS.csv', 'w')

        if 'true' in controle:
            print('Bericht is afgekeurd!')
        elif 'false' in controle:
            print('Bericht is goedgekeurd!')
        elif 'exit' in controle:
            return
        else:
            print('Voer true of false in, er is geen andere mogelijkheid. Probeer opnieuw: ')
        volledig_bericht_kopie.remove(x)
        for i in volledig_bericht_kopie:
            outfile.write(str(i))
        outfile.close()

        # berichten = open('feedback.NS.csv', 'r').readline()

        berichtensplitted = x.strip().split(",")

        bericht_datum = datetime.datetime.strptime(berichtensplitted[3].strip(), "%Y-%m-%d")
        bericht_tijd = datetime.datetime.strptime(berichtensplitted[4].strip(), "%H:%M:%S")

        query = """INSERT INTO bericht(bericht, naam, station, datum, tijd) VALUES (%s, %s, %s, %s, %s) RETURNING berichtnr;"""
        data = (berichtensplitted[1], berichtensplitted[0], berichtensplitted[2], bericht_datum, bericht_tijd)
        cursor.execute(query, data)
        conn.commit()
        berichtnummer = cursor.fetchone()[0]
        query = """INSERT INTO beoordeling(datum, tijd, afgekeurd, werknemernr, berichtnr) VALUES (%s, %s, %s, %s, %s);"""
        data = (datum, tijd, controle, werknemernummer, berichtnummer)
        cursor.execute(query, data)
        conn.commit()
    conn.close()
    return x
print ('Beoordeling heeft plaats gevonden op: ' + datum + tijd)



    #het menu gebruik ik zodat er structuur is, hier vraag ik de naam en a-mail van de moderator.
    #berichten = gecontroleerd_bericht()
    #hier roep ik bovenstaande variabelen aan om error te voorkomen.





if __name__ == "__main__":
    main()

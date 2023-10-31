import psycopg2
import datetime
datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
tijd =  datetime.datetime.now().strftime("%H:%M:%S")

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

    query = """INSERT INTO moderator(naam, emailadres) VALUES (%s, %s);"""
    data = (naam_moderator, email_moderator)
    cursor.execute(query, data)

    for x in volledig_bericht:
        print('Onderstaand bericht met bijbehorende gegevens is getoond: ' + x)

        controle = input('Om dit bericht goed te keuren toets true, om dit bericht af te keuren toets false. Als u wilt stoppen met beoordelen, toets dan exit: ')
        outfile = open('feedback.NS.csv', 'w')

        if 'true' in controle:
            print('Bericht is goedgekeurd!')
        elif 'false' in controle:
            print('Bericht is afgekeurd!')
        elif 'exit' in controle:
            return
        else:
            print('Voer true of false in, er is geen andere mogelijkheid. Probeer opnieuw: ')
        volledig_bericht.remove(x)
        for i in volledig_bericht:
            outfile.write(str(i))
        outfile.close()
        query = """INSERT INTO beoordeling(datum, tijd, afgekeurd) VALUES (%s, %s, %s);"""
        data = (datum, tijd, controle)
        cursor.execute(query, data)
        conn.commit()
        conn.close()
    return x
print ('Beoordeling heeft plaats gevonden op: ' + datum)



    #het menu gebruik ik zodat er structuur is, hier vraag ik de naam en a-mail van de moderator.
    #berichten = gecontroleerd_bericht()
    #hier roep ik bovenstaande variabelen aan om error te voorkomen.





if __name__ == "__main__":
    main()

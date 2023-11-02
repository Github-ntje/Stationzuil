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
    # het menu gebruik ik zodat er structuur is, hier vraag ik de naam en e-mail van de moderator.
    # hier roep ik bovenstaande variabelen aan om error te voorkomen.
    naam_moderator = input('Voer uw naam in: ')
    email_moderator = input('Voer uw e-mailadres in: ')
    #moderator moet hier naam en e-mail invoeren.

    connection_string = "host='4.234.213.225' dbname='stationszuil' user='postgres' password='Appeltaart123!'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    #de connectie wordt hier gemaakt tussen de database en pycharm.

    moderator_check_query = """SELECT werknemernr FROM moderator WHERE naam = %s AND emailadres = %s;"""
    data = (naam_moderator, email_moderator)
    cursor.execute(moderator_check_query, data)
    moderator_check = cursor.fetchone()
    if moderator_check is None:
        query = """INSERT INTO moderator(naam, emailadres) VALUES (%s, %s);"""
        data = (naam_moderator, email_moderator)
        #dit is de data die gebruikt moet worden voor desbtreffende kolommen
        cursor.execute(query, data)
        moderator_nummer_query = """SELECT werknemernr FROM moderator WHERE naam = %s;"""
        data = (naam_moderator,)
        cursor.execute(moderator_nummer_query, data)
        werknemernummer = cursor.fetchone()[0]
    else:
        werknemernummer = moderator_check[0]
        #hier wordt de gegeven info over moderator naar database geschreven.
        #Verder heb ik ook select gebruikt zodat de werknemer die meerdere keren inlogt niet steeds een andere werknemernr krijgt.
        #Als de naam en emailadres nog niet bekend is bij de database krijgt de werknemer wel een nieuwe werknemernr.
        #Dit heb ik gedaan met de if-statement.

    volledig_bericht_kopie = list(volledig_bericht)
    #Hier maak ik een kopie van volledige lijst zodat na het removen geen regels worden overgeslagen bij het lezen van het bestand.
    #Aangezien het programma steeds vanaf index 0 begint met tellen.
    #Hierdoor voegt het bestand steeds de regels terug toe vanaf index 0.
    for x in volledig_bericht:
        print('Onderstaand bericht met bijbehorende gegevens is getoond: ' + x)
        #Hier wordt de feedback getoond zodat de moderator kan beoordelen.
        # X staat hier voor 1 regel van het volledig_bericht, dus het hele feedback bestand.


        controle = input('Om dit bericht goed te keuren toets false, om dit bericht af te keuren toets true. Als u wilt stoppen met beoordelen, toets dan exit: ')
        # Hier moet de moderator het bericht goedkeuren of afgekeuren doormiddel van true en false.

        if 'true' in controle:
            print('Bericht is afgekeurd!')
        elif 'false' in controle:
            print('Bericht is goedgekeurd!')
        elif 'exit' in controle:
            return
        else:
            print('Voer true of false in, er is geen andere mogelijkheid. Probeer opnieuw: ')
        #Met de if/else-statement krijg je een reactie of het bericht juist is goedgekeurd of afgekeurd, na de beoordeling.
        #Als een moderator wilt stoppen met beoordelen teots hij exit in.

        outfile = open('feedback.NS.csv', 'w')
        volledig_bericht_kopie.remove(x)
        for i in volledig_bericht_kopie:
            outfile.write(str(i))
        outfile.close()
        #Hier open ik feedback bestand weer, maar dan met 'w' zodat er dingen kunnen worden toegevoegd of weggeschreven.
        #Eerst remove ik alle regels in het kopie van berichten.
        #Daarna write ik er weer de berichten terug in die nog NIET zijn beoordeeld.


        berichtensplitted = x.strip().split(",")
        #Hier split ik in een regel van berichten bij de komma.
        # Dit doe ik zodat ik later in dit bestand maar een deel van de regel kan weergeven.
        # Dit doe ik met berichtensplitted[...] bij de data die getoond moet worden in de database.
        #Als ik de berichten niet strip en split werkt dit niet.

        bericht_datum = datetime.datetime.strptime(berichtensplitted[3].strip(), "%Y-%m-%d")
        bericht_tijd = datetime.datetime.strptime(berichtensplitted[4].strip(), "%H:%M:%S")
        #Hier geef ik datum en tijd een nieuwe variabelen zodat ik deze kan weergeven in de data van query INSERT INTO bericht.
        #Als ik dit niet doe komt er in de database niet de tijd dat het bericht is verstuurd, maar de tijd dat het bericht is beoordeeld.
        #Datum en tijd een nieuwe variabelen geven doe ik dus om de juiste tijd en datum te kunnen schrijven naar de database van berichten.

        query = """INSERT INTO bericht(bericht, naam, station, datum, tijd) VALUES (%s, %s, %s, %s, %s) RETURNING berichtnr;"""
        data = (berichtensplitted[1], berichtensplitted[0], berichtensplitted[2], bericht_datum, bericht_tijd)
        cursor.execute(query, data)
        conn.commit()
        berichtnummer = cursor.fetchone()[0]
        query = """INSERT INTO beoordeling(datum, tijd, afgekeurd, werknemernr, berichtnr) VALUES (%s, %s, %s, %s, %s);"""
        data = (datum, tijd, controle, werknemernummer, berichtnummer)
        cursor.execute(query, data)
        conn.commit()
        #Hier wordt de gegeven info van beoordeling en bericht verstuurd naar de database.
        #In de data geef ik aan welke dingen precies moeten worden toegevoegd aan de database.
    conn.close()
    #Hier verbreek ik de connectie met de database weer.
    return x
print ('Beoordeling heeft plaats gevonden op: ' + datum + tijd)
#Uiteindelijk print ik op welke datum en tijd de beoordeling heeft plaatsgevonden.


if __name__ == "__main__":
    main()

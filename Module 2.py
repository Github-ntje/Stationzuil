import psycopg2
import datetime
import csv
datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def gecontroleerd_bericht():
    #hier open ik het txt bestand en lees ik elke regel.
    infile = open('feedback.NS.csv', 'r')
    #reader = csv.reader(infile)
    #return reader, infile
    volledig_bericht = infile.readlines()
    infile.close()
    return volledig_bericht

def main():
    volledig_bericht = gecontroleerd_bericht()
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

    for x in volledig_bericht:
        print('Onderstaand bericht met bijbehorende gegevens is getoond: ' + x)

        controle = input('Om dit bericht goed te keuren toets ja, om dit bericht af te keuren toets nee: ')
        outfile = open('feedback.NS.csv', 'w')
        if 'ja' in controle:
            print('Bericht is goedgekeurd!')
        elif 'nee' in controle:
            print('Bericht is afgekeurd!')
        elif 'exit' in controle:
            return
        else:
            print('Voer ja of nee in, er is geen andere mogelijkheid. Probeer opnieuw: ')
        volledig_bericht.remove(x)
        for i in volledig_bericht:
            outfile.write(str(i))
        outfile.close()

            #infile = open('feedback.NS.csv', 'r')
            # reader = csv.reader(infile)
            # return reader, infile
            #berichten = infile.readlines()
           # if 'ja' in controle:
           #     controle.remove(berichten[1])
          #  if 'nee' in controle:
         #       controle.remove(berichten[1])
         #   infile.close()
    return x
            #blijf_controleren = False

print ('Beoordeling heeft plaats gevonden op: ' + datum)


        #if combinatie_code in code:
          #  code.remove(combinatie_code)
            #met een if else statement laat ik het programma de kluisnummer + wachtwoord verwijderen uit het tx bestand zodat deze weer vrij komt.
          #  with open('fa kluizen.txt', 'w') as outfile:
          #      for keuze in code:
           #         outfile.write(keuze + '\n')
            #        print('Kluis is succesvol verwijderd.')


    #het menu gebruik ik zodat er structuur is, hier vraag ik de naam en a-mail van de moderator.
    #berichten = gecontroleerd_bericht()
    #hier roep ik bovenstaande variabelen aan om error te voorkomen.





if __name__ == "__main__":
    main()

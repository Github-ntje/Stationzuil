import tkinter as tk
import psycopg2
import requests
from tkinter import *

def weer(locatie_station):
    api_link = 'https://api.openweathermap.org/geo/1.0/direct'
    parameters = {'q': f'{locatie_station},NL',
        'limit': 1,
        'appid': '3ffae7ec568f5f5e97c5aed2a2c314b9'}
    #Hier voer ik de locatie in waarvan API de temperatuur laat verschijnen.
    #Verder zie je hier ook mijn API key
    #'q' staat voor

    response = requests.get(api_link, params=parameters)
    resultaten = response.json()
    lat, lon = resultaten[0]['lat'], resultaten[0]['lon']
    #lat en lon zijn de coordinaten van de plek die is gegeven.
    api_link = 'https://api.openweathermap.org/data/2.5/weather'
    parameters ={'lat': lat, 'lon': lon, 'lang': 'nl', 'units': 'metric', 'appid': '3ffae7ec568f5f5e97c5aed2a2c314b9'}

    response = requests.get(api_link, params=parameters)
    weer_data = response.json()
    temperatuur = weer_data['main']['temp']

    conn = psycopg2.connect("host='4.234.213.225' dbname='stationszuil' user='postgres' password='Appeltaart123!'")
    cur = conn.cursor()
    #Hier maak ik verbinding met de database zodat ik van daaruit informatie kan ophalen.
    query = "SELECT * FROM Bericht JOIN beoordeling ON bericht.berichtnr = beoordeling.berichtnr WHERE afgekeurd = false AND station = %s ORDER BY bericht.datum DESC, bericht.tijd DESC LIMIT 5"
    #Doormiddel van het gebruik van SELECT, JOIN en WHERE heb ik kunnen filteren dat alleen de GOEDGEKEURDE berichten worden getoond.
    #Met ORDER BY heb ik ervoor gezorg dat het op volgorde van datum en tijd komt.
    #Door het gebruik van LIMIT heb ik ervoor gezorg dat er maar 5 berichten worden getoond.
    cur.execute(query, (locatie_station,))
    volledig_bericht = cur.fetchall()
    cur.close()
    conn.close()
    #Hier sluit ik de connectie weer.

    weer_tekst.config(text=f"Het is momenteel: {temperatuur}°C in {locatie_station}")
    aankondigingen_tekstvak.delete('1.0', tk.END)

    if locatie_station == "Nijmegen":
        faciliteiten_nijmegen()
    elif locatie_station == "Amsterdam":
        faciliteiten_amsterdam()
    elif locatie_station == "Breda":
        faciliteiten_breda()

    for feedback in volledig_bericht:
        gegeven_feedback = f"\nBericht: {feedback[0]}\nNaam: {feedback[1]}\nStation: {feedback[2]}\nDatum: {feedback[3]}\nTijd: {feedback[4]}\n\n"
        aankondigingen_tekstvak.insert(tk.END, gegeven_feedback)
    #print(feedback[2])

    #Hier heb ik een tekstvak gemaakt waarin het weer komt te staan.
    #Verder heb ik hier ook een for-loop gemaakt waarbij de berichten onder elkaar worden getoond.
    #Doormiddel van een f-string heb ik ervoor gezorg dat de info op goede volgorde met de juiste deel van de gehele feedback regel wordt getoond.

beginscherm = tk.Tk()
beginscherm.title("Feedback bij stations")
beginscherm.configure(bg='gold')
beginscherm.geometry("1000x700")
beginscherm.grid_rowconfigure(0, weight=3)
beginscherm.grid_columnconfigure(0, weight=3)
beginscherm.grid_columnconfigure(1, weight=1)
#Hier heb ik het beginscherm gemaakt deze is geel is 800x700 en heeft als titel 'feedback bij stations'.


begin_tekst = tk.Label(beginscherm, text="Welkom bij informatie.NS !", font= ('Arial', 15, 'bold'), bg='SkyBlue2', fg='black')
begin_tekst.grid(column=0, pady=5, padx=5, sticky=tk.N)
#Vervolgens heb ik een label gemaakt met een welkoms bericht voor de reizigers, hier kunnen ze niet op klikken.
#Deze is blauw en matcht dus met de kleuren van NS.

info_tekst = tk.Label(beginscherm, text="Hier volgt informatie en feedback over het gekozen station:", font=('Arial, 12'), bg='SkyBlue2', fg='black')
info_tekst.grid(row=0, column=0, pady=5, padx=5)
#Hier is ook een label gemaakt met extra informatie over het scherm en de dingen die je kan doen hiermee.

weer_tekst = tk.Label(beginscherm, text="Temperatuur", font=('Arial', 11), bg='SkyBlue2', fg='black')
weer_tekst.grid(row=1, column=0, pady=10, padx=10)
#Op deze label komt de temperatuur van het gekozen station te staan.

    # Verder heb ik hier de 3 stations staan waar we informatie over kunnen krijgen.
    # Dit zijn knoppen geen labels, hier kan je op klikken om een station te kiezen waar je informatie over wilt.
    # Zodra je op 1 van deze 3 knoppen drukt zal je op de label van Temperatuur de temperatuur zien verschijnen.
    # Verder zal je ook in het witte tekstvak eronder de goedgekeurde berichten zien met de bijbehorende informatie.
aankondigingen_tekstvak = tk.Text(beginscherm, height=20, width=100, font= ('Arial', 10), bd=5, bg='snow', relief='groove')
aankondigingen_tekstvak.grid(row=2, column=0, pady=10, padx=10)

frame = Frame(beginscherm)
frame.grid()
knopframe = Frame(beginscherm, bg='black')
knopframe.grid(padx=100, pady=50, sticky=tk.W + tk.E)


plaats = ["Breda"]
knop = tk.Button(frame, text='Breda', command=lambda plaats=plaats: weer('Breda'), font=('Arial', 10, 'bold'), bg='blue2', fg='snow')
knop.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W+tk.E)

plaats = ["Nijmegen"]
knop = tk.Button(frame, text='Nijmegen', command=lambda plaats=plaats: weer('Nijmegen'), font=('Arial', 10, 'bold'), bg='blue2', fg='snow')
knop.grid(row=2, column=0, pady=5, padx=10, sticky=tk.W+tk.E)

plaats = ["Amsterdam"]
knop = tk.Button(frame, text='Amsterdam', command=lambda plaats=plaats: weer('Amsterdam'), font=('Arial', 10, 'bold'), bg='blue2', fg='snow')
knop.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W+tk.E)


#Hier heb ik de tekstvak gemaakt waar alle berichten in komen te staan.


def faciliteiten_breda():
    global img_lift, img_pr
    img_lift = tk.PhotoImage(file='img_lift.png')
    aankondigingen_tekstvak.image_create(tk.END, image=img_lift)
    img_pr = tk.PhotoImage(file='img_pr.png')
    aankondigingen_tekstvak.image_create(tk.END, image=img_pr)
    #Hier gebruik ik een functie om de bijbehorende images toe te voegen.
    #De images verschijnen in de tekstvak zodra je op dknop van desbtreffende station drukt.
    #Voor dit gedeelte heb ik video's opgezocht op het internet.

def faciliteiten_nijmegen():
    global img_toilet, img_ovfiets
    img_toilet = tk.PhotoImage(file='img_toilet.png')
    aankondigingen_tekstvak.image_create(tk.END, image=img_toilet)
    img_ovfiets = tk.PhotoImage(file='img_ovfiets.png')
    aankondigingen_tekstvak.image_create(tk.END, image=img_ovfiets)
    #Hier gebruik ik weer een functie om de images te laten verschijnen in het tekstgedeelte.
    # Dit gebeurt zodra je op de knop van desbtreffende station drukt.

def faciliteiten_amsterdam():
    global img_lift, img_pr
    img_lift = tk.PhotoImage(file='img_lift.png')
    aankondigingen_tekstvak.image_create(tk.END, image=img_lift)
    img_pr = tk.PhotoImage(file='img_pr.png')
    aankondigingen_tekstvak.image_create(tk.END, image=img_pr)
    aankondigingen_tekstvak.delete(tk.END)
    #Wederom maak ik gebruik van een functie zodat de images in het tekstvak komen te staan na het klikken op de knop.

beginscherm.mainloop()
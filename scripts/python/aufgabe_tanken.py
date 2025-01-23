# globale Liste um Autos aufzunehmen
Autos = []

# Hier die Antworten zu Aufagbe 1 eintragen
# Datentyp Autos: Liste
# Datentyp Auto[0]: Auto


# Definition der Klasse "Auto", die Blaupause für unsere Autos
class Auto:
    # Konstruktor der Klasse Autos, ermöglicht das Anlegen von neuen Autos
    # erster Parameter self, muss nie übergeben werden, enthält automatische Referenz auf eine bestimmte Instanz der Klasse Auto
    # Attribute wurden um Tankgröße(tank_max) und Füllstand(tank_aktuell) ergänzt
    # tank_aktuell wurde zwei Unterstriche vorangestellt, das Attribut ist nun privat und kann nicht mehr von außerhalb des Objekts gelesen oder verändert werden
    def __init__(self, hersteller, modell, baujahr, leistung, tank_max, tank_aktuell):
        self.hersteller = hersteller
        self.modell = modell
        self.baujahr = baujahr
        self.leistung = leistung
        self.tank_max = tank_max
        self.__tank_aktuell = tank_aktuell
    
    # Methode fahren()
    def fahren(self):
        # verringert bei jeder Fahrt den Füllstand des Tanks um 10
        self.__tank_aktuell -= 10
        print(f"{self.hersteller} {self.modell} fährt mit {self.leistung}. BRUMMBRUMM!")
    
    # Methode hupen()
    def hupen(self):
        print(f"{self.hersteller} {self.modell} hupt: TUUT TUUT!")
            
    # Methode tankanzeige(), um von außerhalb des Objekts den Füllstand abzurufen
    # unser getter für das private Attribut __tank_aktuell
    def tankanzeige(self):
        #return self.__tank_aktuell
        print(f"{self.hersteller} {self.modell} hat {self.__tank_aktuell}% Treibstoff übrig.")
    
    # Methode tanken(), um von außen den Füllstand zu verändern
    # Vorbereitung für unseren setter des privaten Attributs __tank_aktuell
    # diese Funktion soll angepasst werden für Aufgabe 3
    def tanken(self, menge):
        self.__tank_aktuell += menge

        if self.__tank_aktuell > self.tank_max:
            print("Du würdest zuviel getankt")
        else:
            print(f"Du hast {menge}% getankt")
            self.tankanzeige()

# diese Funktion soll angepasst werden für Aufgabe 2
def autos_auswerten():
    
    max_alter = 5000
    max_alter_index = -1
    min_leistung = 999999
    min_leistung_index = -1

    index = 0

    for auto in Autos:
        if (auto.baujahr < max_alter):
            max_alter = auto.baujahr
            max_alter_index = index
        
        leistung_getrennt = auto.leistung.split(" ")
        ps_zahl = int(leistung_getrennt[0])

        if (ps_zahl < min_leistung):
            min_leistung = ps_zahl
            min_leistung_index = index
        index += 1

    print(f"Das älteste Auto ist {Autos[max_alter_index].modell} und hat {Autos[max_alter_index].leistung}.")
    print(f"Das Auto mit der geringsten Leistung ist: {Autos[min_leistung_index].modell} aus dem Jahre: {Autos[min_leistung_index].baujahr}")
    

# jede Zeile erzeugt eine Instanz der Klasse Auto und speichert sie gleichzeitig in der Liste Autos
Autos.append(Auto("Mercedes", "C-Klasse", 2020, "190 PS" , 100, 100))
Autos.append(Auto("BMW", "3er", 2018, "184 PS", 100, 100))
Autos.append(Auto("Audi", "A4", 2022, "150 PS", 100, 100))
Autos.append(Auto("Volkswagen", "Golf", 2019, "140 PS", 100, 100))
Autos.append(Auto("Toyota", "Corolla", 2021, "132 PS", 100, 100))



autos_auswerten()
Autos[0].fahren()
Autos[0].fahren()
Autos[0].fahren()
Autos[0].tankanzeige()
menge = int(input("Wieviel willst du Tanken?"))
Autos[0].tanken(menge)

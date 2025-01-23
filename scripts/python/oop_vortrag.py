# globale Liste um Autos aufzunehmen
Autos = []

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
        print(f"{self.hersteller} {self.modell} hat {self.__tank_aktuell}% Treibstoff übrig.")
    
    # Methode tanken(), um von außen den Füllstand zu verändern
    # Vorbereitung für unseren setter des privaten Attributs __tank_aktuell
    def tanken(self, menge):
        self.__tank_aktuell += menge
            #eingabe tanken
            #wenn eingabe über 100% , abbruch
        if self.__tank_aktuell > self.tank_max:
            print("Du würdest zuviel getankt")
        else:
            print(f"Du hast {menge}% getankt")
            self.tankanzeige()
        pass


# jede Zeile erzeugt eine Instanz der Klasse Auto und speichert sie gleichzeitig in der Liste Autos
Autos.append(Auto("Mercedes", "C-Klasse", 2020, "190 PS", 100, 100))
Autos.append(Auto("BMW", "3er", 2018, "184 PS", 100, 100))
Autos.append(Auto("Audi", "A4", 2022, "150 PS", 100, 100))
Autos.append(Auto("Volkswagen", "Golf", 2019, "140 PS", 100, 100))
Autos.append(Auto("Toyota", "Corolla", 2021, "132 PS", 100, 100))

# Zugriffe von auußerhalb des Objekts
Autos[0].__tank_aktuell = 50
#print(Autos[0].__tank_aktuell)
# ACHTUNG BRAINFUCK!!!
# diese Zeilen scheinen zu funktionieren und erzeugen keinen Fehler
# was eigentlich passiert: es wird ein neues Attribut __tank_aktuell~ angelegt und ausgelesen
# unser prviates Attribut __tank_aktuell bleibt davon unberührt!!!

# Zugriff über getter
Autos[0].fahren()
Autos[0].fahren()
Autos[0].fahren()
Autos[0].tankanzeige()
menge = int(input("Wieviel willst du Tanken?"))
Autos[0].tanken(menge)
# hier bekommen wir den wirklichen Füllstand unseres Autos aus dem richtigen Attribut __tank_aktuell

# Schleife, die für jedes Auto in der Liste die Methoden fahren() und hupen() aufruft
#for auto in Autos:
#    auto.fahren()
#    auto.hupen()
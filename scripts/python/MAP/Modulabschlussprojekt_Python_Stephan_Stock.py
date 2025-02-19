#### Modulabschlussprojekt Stephan Stock ####

class Schiff:
    def __init__(self, Schiffname,Baujahr,Heimathafen):
        self.Schiffname = Schiffname
        self.Baujahr = Baujahr
        self.Heimathafen = Heimathafen

    def __str__(self):
        return f"Das Schiff {self.Schiffname} wurde im Jahr {self.Baujahr} gebaut und kommt aus {self.Heimathafen}."
    
class Fisch:
    def __init__(self, Fischart,Fanggebiet,Preis):
        self.Fischart = Fischart
        self.Fanggebiet = Fanggebiet
        self.Preis = Preis

    def __str__(self):
        return f"Die Fischart {self.Fischart} wurde im Gebiet {self.Fanggebiet}gefangen, und kostet {self.Preis} das Kilo"



class Fangergebnis:
    def __init__(self, fangSchiff,fangKapitän,fangDatum,fangFisch,fangFangmenge):
        self.Schiff = fangSchiff
        self.Kapitän = fangKapitän
        self.Datum = fangDatum
        self.Fisch = fangFisch
        self.Fangmenge = fangFangmenge

    def __str__(self):
        return f"Das Schiff {self.Schiff} mit dem Kapitän {self.Kapitän} hat am {self.Datum} den {self.Fisch} mit einer Menge von {self.Fangmenge} Tonnen gesammelt."

############ Listen Einlesen

liste_schiffe = list()
with open("schiffe.csv", "r", encoding="latin-1") as csv_schiffe:
    next(csv_schiffe)
    for zeile in csv_schiffe:
        Schiffname, Baujahr, Heimathafen = zeile.strip().split(";")
        liste_schiffe.append(Schiff(Schiffname,Baujahr,Heimathafen))

liste_fische = list()
with open("fische.csv", "r", encoding="latin-1") as csv_fische:
    next(csv_fische)
    for zeile in csv_fische:
        Fischart, Fanggebiet, Preis =zeile.strip().split(";")
        liste_fische.append(Fisch(Fischart,Fanggebiet,int(Preis)))

def finde_fisch(fischname):
    for fisch in liste_fische:
        if fisch.Fischart == fischname:
            return fisch

liste_fangmenge = list()
with open("fangergebnisse.csv" , "r" , encoding="latin-1") as csv_fangergebnisse:
    next(csv_fangergebnisse)
    for zeile in csv_fangergebnisse:
        Schiffname, Kapitän, Datum, Fischname, Fangmenge, = zeile.strip().split(";")
        liste_fangmenge.append(Fangergebnis(Schiffname,Kapitän,Datum,finde_fisch(Fischname), int(Fangmenge)))

############## Definitionen Definieren

# Fische die eingelesen werden automatisch in die Klassen packen


        
# Platzhalter für finde_schiffe

# Definition bester Tag wo ausgerechnet wird welcher Tag der Fänge am besten war

def bester_tag():
    dict_fangtag = dict()
    for x in liste_fangmenge:
        if x.Datum in dict_fangtag:
            dict_fangtag[x.Datum] += x.Fangmenge
        else:
            dict_fangtag[x.Datum] = x.Fangmenge

    btag = 0
    for datum, fangmenge in dict_fangtag.items():
        if fangmenge > btag:
            btag = fangmenge
            bdatum = datum
    print(f"\nDer Ergiebigste Tag war der {bdatum} mit einer Fangmenge von {btag} Tonnen.\n")

# Hier wird bearbeitet welcher Kapitän im Zeitraum die Dicksten Fische am Haken hatte.

def bester_kapitaen():

    dict_cpt = dict()

    for x in liste_fangmenge:
        if x.Kapitän in dict_cpt:
            dict_cpt[x.Kapitän] += x.Fangmenge * x.Fisch.Preis
        else:
            dict_cpt[x.Kapitän] = x.Fangmenge * x.Fisch.Preis
    
    bfang = 0
    for Kapitän, fangmenge in dict_cpt.items():
        if fangmenge > bfang:
            bfang = fangmenge
            bcpt = Kapitän
    print(f"\nDer beste Kapitän war:{bcpt}, mit einer Fangmenge von: {bfang} Tonnen.\n")

# Menübereich bearbeitung

def menu():
    print("Hauptmenü")
    print("Wähle was du machen willst:")
    print("(1) Abfrage starten")
    print("(2) Fangergebnisse bearbeiten")
    print("(3) Beenden")
    print("------------------------------------")
    auswahl=input("Bitte gebe deine Auswahl ein:\n")

    match auswahl:
        case "1":
            abfragen()
        case "2":
            fangergebnisse()
        case "3":
            exit()
        case _:
            print("Auswahl Ungültig")


def abfragen():
    print("\n### Menü: Abfragen ###")
    print("Wähle aus was du abfragen möchtest")
    print("(1) Bester Tag")
    print("(2) Bester Kapitän")
    print("(3) Hauptmenu")
    auswahl = input("Bitte gebe deine Auswahl ein: \n")

    match auswahl:
        case "1":
            bester_tag()
            abfragen()
        case "2":
            bester_kapitaen()
            abfragen()
        case "3":
            menu()
        case _:
            print("Auswahl Ungültig")

def delete_eintrag():
    print("\n### Menü: Eintrag Entfernen")

def fangergebnisse():
    print("\n### Menu: Fangergebnisse ###")
    print("Wähle aus was du machen willst:")
    print("(1) Eintrag anlegen(noch nicht implementiert)")
    print("(2) Eintrag Löschen")
    print("(3) Liste Speichern")
    print("Hauptmenü")
    auswahl = input("Bitte gebe deine Auswahl ein:")

    match auswahl:
        case "1":
            print("Noch nicht angelegt")
            fangergebnisse()
        case "2":
            delete_eintrag()
        case "3":
            save_list()
        case "4":
            menu()
        case _:
            print("Ungültige Auswahl")

######## Bereich für Probieren

# for x in liste_schiffe:
#     print(x)

# for x in liste_fische:
#     print(x)

# for x in liste_fangmenge:
#     print(x)

#bester_tag()

#bester_kapitaen()

# for x in liste_fangmenge:
#     print(x)#

##### Start des Programmes

menu()
#### Modulabschlussprojekt Stephan Stock ####

### Klassen bestimmen und für jede Klasse einen Stringoutput bestimmt.

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
    def __init__(self, Schiff,Kapitän,Datum,Fisch,Fangmenge):
        self.Schiff = Schiff
        self.Kapitän = Kapitän
        self.Datum = Datum
        self.Fisch = Fisch
        self.Fangmenge = Fangmenge

    def __str__(self):
        return f"Schiff {self.Schiff.Schiffname} Kapitän: {self.Kapitän} Datum: {self.Datum} Fisch: {self.Fisch.Fischart} Menge: {self.Fangmenge} Tonnen gesammelt."

############ Listen Einlesen mit Definitionen das die Fische und Schiffe von der Liste Fangmenge 
############ direkt richtig der Klassen zugeordnet werden.

def finde_schiff(schiffname):
    for schiff in liste_schiffe:
        if schiff.Schiffname == schiffname:
            return schiff

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
        liste_fangmenge.append(Fangergebnis(finde_schiff(Schiffname),Kapitän,Datum,finde_fisch(Fischname), int(Fangmenge)))

############## Definitionen Definieren

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

########### Menübereich Bearbeitung

# Hauptmenu was am Anfang des Programms aufgerufen wird und zudem man immer wieder zurück kommt.

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

# Untermenü für die zwei abfragen wie wir Bestimmt haben für Bester Tag und Bester Kapitän

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

# Untermenü Fangergebnisse wenn wir das Menü betreten wird uns direkt die Liste der Fangmenge und einer Index
# Zahl ausgegeben mit listebearbeiten kommen wir in das Untermenü zum Listen bearbeiten

def fangergebnisse():
    print("\n### Menu: Fangergebnisse ###")
    index = 0
    for x in liste_fangmenge:
        index +=1
        print(f"({index}) {x}")
    print("(1) Liste bearbeiten")
    print("(2) Zurück")
    auswahl = input("Bitte gebe deine Auswahl ein: \n")
    
    match auswahl:
        case "1":
            listebearbeiten()
        case "2":
            menu()
        case _:
            print("Ungültige Auswahl")

# Untermenü Liste Bearbeiten, wird aufgerufen um Einträge anzulegen (Bonusaufgabe nicht umgesetzt), Einträge zu
# Löschen und um die Liste zu speichern. Nach erfolgreicher bearbeitung oder fehlerhafter bearbeitung wird wieder
# in das Menü zurückgekehrt.

def listebearbeiten():
    print("\n### Menu: Liste Bearbeiten ###")

    print("Wähle aus was du machen willst:")
    print("(1) Eintrag anlegen(noch nicht implementiert)")
    print("(2) Eintrag Löschen")
    print("(3) Liste Speichern")
    print("(4) Hauptmenü")
    auswahl = input("Bitte gebe deine Auswahl ein: \n")

    match auswahl:
        case "1":
            print("Noch nicht angelegt")
            fangergebnisse()
        case "2":
            delete_eintrag()
            listebearbeiten()
        case "3":
            save_list()
            listebearbeiten()
        case "4":
            menu()
        case _:
            print("Ungültige Auswahl")

# Untermenü Eintrag Löschen, Hier wird angegeben welcher eintrag aus der Liste gelöscht werden soll.
# Die Liste wird von liste bearbeiten angezeigt und hier lässt sich mittels einer auswahl der Eintrag
# mittels der Indexnummer löschen.

def delete_eintrag():
    print("\n### Menü: Eintrag Entfernen")
    print("Nummer Angeben welchen eintrag du löschen willst:")
    auswahl = int(input("Auswahl treffen!\n"))
        
    if liste_fangmenge[auswahl]:
        liste_fangmenge.pop(auswahl)
        print(f"Eintrag: ({liste_fangmenge[auswahl]}) wurde Entfernt")
    else:
        print("Ungültige Auswahl")
        
# Untermenü Liste speichern, Wird benutzt um die Fangmengen Liste die wir mit der String representation ausgegeben
# bekommen in eine TextDatei mit dem Namen "Fangergebnisse.txt" zu speichern.
# Als prompt bekommen wir die aussage das die Liste im Stammverzeichniss gespeichert ist.
        
def save_list():
    print("\n### Menu : Liste speichern ###")
    print("(1) Zum Liste speichern")
    print("(2) Zurück")
    auswahl = input("Bitte gebe eine Auswahl ein: \n")

    match auswahl:
        case "1":
            with open("Fangergebnisse.txt", "w", encoding="latin-1") as txt_file:
                for x in liste_fangmenge:
                    txt_file.write(f"{x} \n")
            print("Liste im Stammverzeichniss gespeichert!\n")
        case "2":
            fangergebnisse()

##### Start des Programmes

menu()
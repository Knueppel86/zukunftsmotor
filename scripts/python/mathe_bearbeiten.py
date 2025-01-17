# importiert das Modul zur Kommunikation mit dem Betriebssystem
import os

# gibt das Menü in der Konsole aus
# fragt die Auswahl des Benutzers ab
# reagiert auf die Auswahl des Benutzers
def menue_anzeigen():
    os.system("cls")
    print("K15 - Taschenrechner")
    print("--------------------")
    print("(1) Addition")
    print("(2) Subtraktion")
    print("(3) Multiplikation")
    print("(4) Division")
    print("--------------------")    
    print("(5) Potenz")
    print("(6) Floor-Division")
    print("(7) Modulo")
    print("--------------------")
    print("(b) Beenden")
    print("--------------------")
    
    auswahl = input("Operation auswählen: ")
    match auswahl:
        case "1":
            # zahlen = zahlen_abfragen()
            # ergebnis = addition(zahlen)
            # ergebnis_anzeigen(ergebnis)
            ergebnis_anzeigen(addition(zahlen_abfragen()))
        case "b":
            exit()
        case _:
            print("Ungueltige Auswahl!")
            warten()
            menue_anzeigen()


# legt eine leere Liste an
# erfragt eine Zahl vom Benutzer und fügt sie in die Liste ein
# erfragt eine weitere Zahl vom Benutzer und fügt sie ebenfalls in die Liste ein
# gibt die Liste als Rückgabewert zurück
def zahlen_abfragen():
    zahlen = []
    zahlen.append(float(input("Zahl 1 eingeben: ")))
    zahlen.append(float(input("Zahl 2 eingeben: ")))
    return zahlen


# nimmt als Parameter eine Liste von Zahlen an
# addiert die Elemente 0 und 1 der Liste und gibt das Ergebnis als Rückgabewert zurück
def addition(zahlen):
    return zahlen[0] + zahlen[1]


# wartet auf eine Eingabe des Benutzers und ignoriert die Eingabe
# anders: pausiert die Ausführung bis der Benutzer ENTER drückt    
def warten():
    input("ENTER zum Fortfahren.")
    

# nimmt ein beliebiges Ergebnis als Parameter an
# gibt dem Benutzer das Ergebnis in der Konsole aus
# wartet bis der Benutzer ENTER drückt
# ruft wieder die Funktion zur Ausgabe des Menüs auf    
def ergebnis_anzeigen(ergebnis):
    print("Ergebnis:", ergebnis)
    warten()
    menue_anzeigen()
    

# der eigentliche Startpunkt des Skripts
# ruft zum ersten Mal die Funktion zum Anzeigen des Menüs auf    
menue_anzeigen()
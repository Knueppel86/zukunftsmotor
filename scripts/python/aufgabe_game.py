import os

#Funktionen definieren

def hauptmenue():
    print("-------------------------------------------")
    print("Wähle eines der drei Wege:")
    print("(1) Schmaler Gang nach links")
    print("(2) Hell erleuchteter Tunnel geradeaus")
    print("(3) Dunkler Gang nach rechts")
    print("-------------------------------------------")
    auswahl = input("Aktion wählen: \n")

    match auswahl:
        case "1":
            ganglinks()
        case "2":
            hellertunnel()
        case "3":
            gangrechts()
        case _:
            print("Ungueltige Auswahl!")

def ganglinks():
        print("Du hast dich für einen Schmalen Gang entschieden durch den du dich so gerade ebenso durchzwängst\nAm Ende dieses Tunnels kommst du vor einer Vorschlossenen Tür\nDu hast mehrere Optionen wie du weiter vorgehen willst. Wofür Entscheidest du dich?\n")
        
        print("(1) Klopfen")
        print("(2) Öffnen")
        print("(3) Zurückkehren")
        print("-------------------------------------------")
        auswahl = input("Aktion wählen: \n")

        match auswahl:
            case "1":
                print("(Klopfgeräusche) ... Niemand scheint sich in dem Raum hinter der Tür zu befinden\nVielleicht findest du in einen anderen Gang einen Schlüssel.\nGehe zum Start zurück!\n")
                hauptmenue()
            case "2":
                if inventar[0] == "Schlüssel":
                    print("Der Schlüssel scheint zu passen\n")
                    gutesende()
                else:
                    print("Ich brauche einen Schlüssel!\nDurchsuche die anderen gänge nach einen passenden!\nKehre zum Start zurück!\n")
                    hauptmenue()
            case "3":
                print("Ich kehre besser um, und wähle einen anderen Weg.\n")
                hauptmenue()
            case _:
                print("Ungueltige Auswahl!")

def hellertunnel():
    print("Du hast dich für einen Hell erleuchteten Tunnel entschieden.\nAm Ende dieses Tunnels siehst du ein Großes Stinkendes Monster was dir den Weg weiter blockiert. Du kannst dich entscheiden zu Kämpfen oder weg zulaufen. Was ist deine Entscheidung?\n")

    print("-------------------------------------------")
    print("(1) Angriff!")
    print("(2) Fliehen!")
    print("(3) Stein werfen!")
    print("-------------------------------------------")
    auswahl = input("Aktion wählen: \n")

    match auswahl:
        case "1":
                print("Leider ist das Monster stärker als du.\n")
                schlechtesende()
                neustart()
        case "2":
                print("Du rennst mit aller Kraft zum Start zurück.\n")
                hauptmenue()
        case "3":
            if inventar[1] == "Stein":
                print("Du triffst das Monster mit dem Stein am Kopf, es läuft heulend weg.\n")
                gutesende()
            else:
                print("Leider fehlt dir ein Stein, durchsuche die anderen Gänge ob einer zu finden ist.")
                print("Gehe zurück zum Start!\n")
                hauptmenue()
        case _:
            print("Ungueltige Auswahl!")

def gangrechts():
    print("Du hast dich für den Dunklen Gang nach Rechts entschieden\n Nach einigen Metern siehst du am Ende dieses Weges einen Schatz!\nNimmst du den Schatz und versuchst dein Glück? Oder ist es dir zu gefährlich?\nWähle Weise!\n")

    print("-------------------------------------------")
    print("Schatz gefunden")
    print("(1) Schatz nehmen")
    print("(2) Ignorieren (Zurück)")
    print("(3) Rasten")
    print("-------------------------------------------")
    auswahl = input("Aktion wählen: \n")

    match auswahl:
        case "1":
                print("Du findest in der Schatztruhe einen Schlüssel und einen Stein\nDieses legst du in dein Inventar\n")
                inventar.insert(0, "Schlüssel")
                inventar.insert(1, "Stein")
                print("Hier ist kein weiterkommen,gehe zum Start zurück!")
                hauptmenue()
        case "2":
                print("Dir ist es zu gewagt die truhe zu öffnen und gehst zum Startpunkt zurück!\n")
                hauptmenue()
        case "3":
                print("Du schläfst ein und wachst nicht mehr auf.\n")
                neustart()
        case _:
            print("Ungueltige Auswahl!")


def gutesende():
    print("Herzlichen Glückwunsch du hast es aus der Höhle rausgeschafft!\nDanke für das Spielen dieses Spieles!\n")

def schlechtesende():
    print("Du hast es leider nicht geschafft aus der Höhle zu entkommen!\n")

def neustart():
    print("Willst du es noch einmal versuchen?")
    print("(1) Ja")
    print("(2) Nein")
    auswahl = input("Aktion wählen: \n")
        
    match auswahl:
            case "1":
                inventar.insert(0, "Platzhalter1")
                inventar.insert(1, "Platzhalter2")
                hauptmenue()
            case "2":
                print("Danke fürs Spielen!\nBis zum nächsten mal!")
                exit()

inventar = ["Platzhalter1","Platzhalter2"]

#Start Programm

print("Herzlich Willkommen beim Choose your Own Adventure")
print("Eine Aufgabe von Akkan - Ruslan - Stephan aus K15\n")

print("Du öffnest deine Augen und wachst in einer Dunklen Höhle auf.\nDu weißt nicht wie du hier hergekommen bist aber es gibt mehrere Ausgänge zur Auswahl:\n")

hauptmenue()
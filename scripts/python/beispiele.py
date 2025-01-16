# Kommentar
# Durchspieltag Matchen/Schleifen/etc.


# Zahl = int(input("Ganzzahl eingeben: "))
# Ergebnis = ""

# if (Zahl > 100):
#     Ergebnis = "groeßer Null"
# elif (Zahl == 100):
#     Ergebnis = "gleich Null"
# else:
#     Ergebnis = "kleiner Null"

# print("Die Zahl", Zahl, "ist " + Ergebnis + ".")

## Match Option

# print("### Ich bin ein Menue! ###")
# print("(1) Option 1")
# print("(2) Option 2")
# print("(3) Option 3")
# print("(4) Option 4")
# print("(5) Option 5")
# print("##########################")
# print("(b) beenden")
# print("##########################")
# auswahl = input("Aktion wählen: ")

# match auswahl:
#     case "1":
#         print("Option 1 wurde ausgewählt.")
#     case "2":
#         print("Option 2 wurde ausgewählt.")
#     case "3":
#         print("Option 3 wurde ausgewählt.")
#     case "4":
#         print("Option 4 wurde ausgewählt.")
#     case "5":
#         print("Option 5 wurde ausgewählt.")
#     case "b":
#         exit()
#     case _:
#         print("Ungueltige Auswahl!")

##  For Schleifen

# for i in range(10):
#     print(i)

## Listen durchgehen

# Tiere = ["Ameise", "Baer", "Chamaeleon"]
# for tier in Tiere:
#     print(tier)

# ##Versuche Zähler

# Passwort = "1234"
# Eingabe = ""
# Versuche = 3

# for i in range(Versuche, 0, -1):
#     Eingabe = input("Passwort eingeben: ")
#     if (Eingabe == Passwort):
#         print("Passwort richtig!")
#         # login oder was auch immer
#         break
#     else:
#         print("Passwort falsch! Noch", i-1,"Versuche.")

# print("blub")

## selbeer zählrer in while schelife

# Passwort = "1234"
# Eingabe = ""
# Versuche = 3

# while (Versuche > 0):
#     Eingabe = input("Passwort eingeben: ")
#     if (Eingabe == Passwort):
#         print("Passwort richtig!")
#         # login oder was auch immer
#         break
#     else:
#         Versuche -= 1
#         print("Passwort falsch! Noch", Versuche,"Versuche.")

# print("Ende")

## While schleife bis break

# import random

# print("Zahlen raten von 1 bis 10")
# ZZahl = random.randint(1, 10)
# while True:
#     zahl = int(input("Zahl von 1 bis 10 eingeben: "))
#     if zahl == ZZahl:
#         print("Richtige Antwort!")
#         break
#     print("HAHA! Falsch, du Noob.")
# print("Spielende")

# ## while schleife mit hilfen von elif und else

# import random

# print("Zahlen raten von 1 bis 10")
# ZZahl = random.randint(1, 10)
# while True:
#     zahl = int(input("Zahl von 1 bis 10 eingeben: "))
#     if zahl == ZZahl:
#         print("Richtige Antwort!")
#         break
#     elif (zahl < ZZahl):
#         print("HAHA! Falsch, du Noob. Die gesuchte Zahl ist groeßer.")
#     else:
#         print("HAHA! Falsch, du Noob. Die gesuchte Zahl ist kleiner.")
# print("Spielende")
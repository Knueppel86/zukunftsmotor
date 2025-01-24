# for i in range(10):
#     print (i)

# namen = ["Andreas", "Bertholt", "Chantalle", "Dieter", 666]
# for element in namen:
#     print(element)

# namen = ["Andreas", "chantalle", "Bertholt", "Dieter"]
# for element in sorted(namen[1]):
#     print(element)

# zahlen = [1, 55, 7, 387, 222]
# index = 0
# for zahl in sorted(zahlen):
#     print(zahl)
#     if index > 1:
#         break

# count = 1
# while True:
#     print("Endlos", count)
#     count += 1

# recuraion error, achtung
# def katastrophe():
#     count = 1
#     while True:
#         print("Endlos", count)
#         count += 1
#         katastrophe()
# katastrophe()

# count = 0
# while True:
#     count += 1
#     if (count > 200) and (count < 300):
#         continue    
#     print("Endlos", count)
#     if count == 301:
#         break

# einInteger = 42
# einFloat = 23.666
# einString = "Eine Zeichenkette mit viel Kram, 345 und !%&/%&/%&/8"
# einBoolean = True # oder false

#eineListe = ["abc", 123, True] # frisst grundsätzlich alles
# eineListe[1] # zweites Element in der Liste
# eineListe[2] = "def" # Element 3 wird von True zu "def"

# result = eineListe.pop(1) # Löscht das zweite Element an Index 1, speichert das gelöschte Element in der Variable result
#eineListe.remove("abc") # löscht DAS ERSTE VORKOMMEN in der Liste, gibt es NICHT als Rückgabewert zurück

# einTupel = (123, "abc")
# einTupel[0] # erstes Element im Tupel
# einTupel[1] = "def" # GEHT NICHT!!!1!1!1!11 Tupel sind unveränderlich
# einTupel = (123, "def") # am besten einfach das Tupel überschreiben

einDict = {
    "ichBinEinSchlüssel" : "ichBinEinWert",
    "andererSchlüssel" : "andererWert",
    "wieder Schlüssel" : 123,
    "undNochmal" : True
} # auf der linken Seite, VOR dem Doppelpunkt sind die Schlüssel, auf der rechten Seite, NACH dem Doppelpunkt sind die damit verknüpften Werte
einDict["andererSchlüssel"] # greift auf den Wert des Schlüssels "andererSchlüssel" / Ergebnis => "andererWert"
einDict["undNochmal"] = False # ändert den Wert des Schlüssels "undNochmal" auf false
 
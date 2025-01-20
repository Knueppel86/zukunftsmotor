# zwei leere Sets als globale Variablen vorbereiten
# set, weil keine Duplikate erlaubt
Kapitaene = set()
Matrosen = set()

# öffnet die Datei "map2.csv" zum LESEN ("r" - read) und stellt sie als Variable csv_file bereit
with open("map2.csv", "r", encoding="latin-1") as csv_file:
    # erste Zeile in CSV-Datei überspringen (Spaltennamen)
    next(csv_file)
    # geht in einer Schleife, Zeile für Zeile durch den Rest der Datei
    # stellt jede Zeile als Variable line bereit
    for line in csv_file:
        # teilt die Zeile am Semikolon
        # Teil LINKS des Semikolons in kapitaen gespeichert
        # Teil RECHTS des Semikolns in matrosen
        kapitaen, matrosen = line.split(";", 1)
        # kapitean wird dem set Kapitaene hinzugefügt
        Kapitaene.add(kapitaen)        
        # erstellt die lokale Variable matrosen_getrennt
        # erstellt Liste aus Matrosen, immer am Komma getrennt
        matrosen_getrennt = matrosen.split(",")        
        # geht in einer Schleife durch alle abgetrennten Matrosen in der Variable matrosen_getrennt
        # stellt jeden Matrosen in der Variable matrose bereit
        for matrose in matrosen_getrennt:
            # löscht voran- oder nachstehende Leerzeichen
            # fügt den bereinigten Matrosen dem set Matrosen hinzu
            Matrosen.add(matrose.strip())


# öffnet die Datei "Kapitaene.txt" zum SCHREIBEN ("w" - write) und stellt sie als Variable txt_file bereit
with open("Kapitaene.txt", "w", encoding="latin-1") as txt_file:
    # geht in einer Schleife durch das alphabetisch geordnete set Kapitaene
    # stellt jeden Kapitaen als Variable kapitaen bereit
    for kapitaen in sorted(Kapitaene):
        # schreibt den Kapitaen in die Text-Datei
        # fügt nach dem Namen einen Zeilenumbruch ein (\n)
        txt_file.write(kapitaen + "\n")


# öffnet die Datei "Matrosen.txt" zum SCHREIBEN ("w" - write) und stellt sie als Variable txt_file bereit
with open("Matrosen.txt", "w", encoding="latin-1") as txt_file:
    # geht in einer Schleife durch das alphabetisch geordnete set Matrosen
    # stellt jeden Matrosen als Variable matrose bereit
    for matrose in sorted(Matrosen):
        txt_file.write(matrose + "\n")
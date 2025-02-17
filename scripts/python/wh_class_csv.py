class Prüfungsergebnis:
    def __init__(self, name, modul,punkte):
        self.name = name
        self.modul = modul
        self.punkte = punkte

    def __str__(self):
        return f"Der Teilnehmer {self.name} hat im {self.modul} {self.punkte} Punkte erzielt."
    
liste_prüfungsergebnisse = list()
with open("notenliste.csv", "r", encoding="latin-1") as csv_file:
    next(csv_file)
    for zeile in csv_file:
        # zeile = zeile.strip()
        name, modul, punkte = zeile.strip().split(";")
        liste_prüfungsergebnisse.append(Prüfungsergebnis(name, modul, int(punkte)))

# for x in liste_prüfungsergebnisse:
#     print(x)

dict_summenoten = dict()
dict_anzahlnoten = dict()

for x in liste_prüfungsergebnisse:
    if x.name in dict_summenoten:
        dict_summenoten[x.name] += x.punkte
        dict_anzahlnoten[x.name] += 1
    else:
        dict_summenoten[x.name] = x.punkte
        dict_anzahlnoten[x.name] = 1

for name, summe in dict_summenoten.items():
    durchschnitt = summe / dict_anzahlnoten[name]
    print(f"Der Teilnehmer {name} hat den Durchschnitt {durchschnitt} erzielt.")


# print(dict_summenoten)
# print(dict_anzahlnoten)
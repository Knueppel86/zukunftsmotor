#### Modulabschlussprojekt Stephan Stock ####

class Schiff:
    def __init__(self, Schiffname,Baujahr,Heimathafen):
        self.Schiffname = Schiffname
        self.Baujahr = Baujahr
        self.Heimathafen = Heimathafen

    def __str__(self):
        return f"Das Schiff {self.Schiffname} wurde im Jahr {self.Baujahr} gebaut und kommt aus {self.Heimathafen}."
    

liste_schiffe = list()
with open("schiffe.csv", "r", encoding="latin-1") as csv_schiffe:
    next(csv_schiffe)
    for zeile in csv_schiffe:
        Schiffname, Baujahr, Heimathafen = zeile.strip().split(";")
        liste_schiffe.append(Schiff(Schiffname,Baujahr,Heimathafen))

class Fisch:
    def __init__(self, Fischart,Fanggebiet,Preis):
        self.Fischart = Fischart
        self.Fanggebiet = Fanggebiet
        self.Preis = Preis

    def __str__(self):
        return f"Die Fischart {self.Fischart} wurde im Gebiet {self.Fanggebiet}gefangen, und kostet {self.Preis} das Kilo"

liste_fische = list()
with open("fische.csv", "r", encoding="latin-1") as csv_fische:
    next(csv_fische)
    for zeile in csv_fische:
        Fischart, Fanggebiet, Preis =zeile.strip().split(";")
        liste_fische.append(Fisch(Fischart,Fanggebiet,int(Preis)))

class Fangergebnis:
    def __init__(self, fangSchiff,fangKapitän,fangDatum,fangFisch,fangFangmenge):
        self.Schiff = fangSchiff
        self.Kapitän = fangKapitän
        self.Datum = fangDatum
        self.Fisch = fangFisch
        self.Fangmenge = fangFangmenge

    def __str__(self):
        return f"Das Schiff {self.Schiff} mit dem Kapitän {self.Kapitän} hat am {self.Datum} den {self.Fisch} mit einer Menge von {self.Fangmenge} Tonnen gesammelt."

# def finde_fisch():
#     for fisch in liste_fangmenge:
#         if x.fangfisch == Fischart:
#             return fisch

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
            print(f"{btag} - {bdatum}")

    print(f"Der Ergiebigste Tag war der {bdatum} mit einer Fangmenge von {btag} Tonnen.")

# def bester_kapitaen():
    # best_cpt = liste_fische[0]
    # dict_preis = dict()
    # for x in liste_fangmenge:
    #     if x.Kapitän in dict_preis:
    #         dict_preis[x.Kapitän] += x.Fisch
    #         dict_preis[x.Fisch] = best_cpt.Preis
    #     else:
    #         dict_preis[x.Kapitän] = x.Fisch
    #         dict_preis[x.Fisch] = best_cpt.Preis

    # bpreis = 0
    # for name , preis in dict_preis.items():
    #     if best_cpt.Preis > bpreis:
    #         bpreis = best_cpt.Preis
    
    # print(f"Der Beste Kapitän ist {name} mit einem gesamtwert von: {bpreis}")
    
    
    
    # Liste Fangmenge durchgehen und die Kapitäne mit den Fischen und der Anzahl zusammenrechnen

    # kapitän , datum? , fisch und die Fangmenge müssen addiert oder verglichen werden.WindowsError

    # der wert der gefangen fische muss dann mit der preistabelle errechnet werden 

    # daraus muss der erfolgreichste cpt hervorgehen und ausgegeben werden.


liste_fangmenge = list()
with open("fangergebnisse.csv" , "r" , encoding="latin-1") as csv_fangergebnisse:
    next(csv_fangergebnisse)
    for zeile in csv_fangergebnisse:
        Schiff, Kapitän, Datum, Fisch, Fangmenge, = zeile.strip().split(";")
        liste_fangmenge.append(Fangergebnis(Schiff,Kapitän,Datum,Fisch, int(Fangmenge)))


# for x in liste_schiffe:
#     print(x)

# for x in liste_fische:
#     print(x)

# for x in liste_fangmenge:
#     print(x)

bester_tag()

#bester_kapitaen()
Schiffe = list()

class Schiff:
    def __init__(self, name, baujahr, leistung):
        self.name = name
        self.baujahr = baujahr
        self.leistung = leistung
    
    def __str__(self):
        return f"{self.name} {self.baujahr} {self.leistung}"

def finde_aeltestes_schiff():

    schiff_alt = 9999
    schiff_alt_index = -1

    index = 0
    for schiff in Schiffe:
       if (schiff.baujahr < schiff_alt):
            schiff_alt = schiff.baujahr
            schiff_alt_index = index
        
    index += 1

    print(f"Das älteste Schiff ist: {Schiffe[schiff_alt_index].name} aus dem Jahr {Schiffe[schiff_alt_index].baujahr}\n")
    

def finde_staerkstes_schiff():

    schiff_leistung = 99999
    schiff_leistung_index = -1

    index = 0
    for schiff in Schiffe:
        if (schiff.leistung < schiff.leistung):
            schiff_leistung = schiff.leistung
            schiff_leistung_index = index
    index += 1

    print(f"Das stärkste Schiff ist: {Schiffe[schiff_leistung_index].name} mit einer Leistung von: {Schiffe[schiff_leistung_index].leistung} Knoten\n")

Schiffe.append(Schiff("Gringo Freedom", 1950, 2312))
Schiffe.append(Schiff("Madonna II", 1980, 4400))
Schiffe.append(Schiff("Hasso IV", 2010, 6890))

finde_aeltestes_schiff()
finde_staerkstes_schiff()

# for x in Schiffe:
#     print(x)
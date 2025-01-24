# Gringo Freedom
# Pazifischer Kabeljau:		666
# Blauflossen-Thunfisch:		3
# Heilbutt:			69

# Madonna II
# Blauflossen-Thunfisch:		7
# Gestreifter Marlin:		13
# Gelbflossen-Thunfisch:		666

# Hasso IV
# Blauflossen-Thunfisch:		111
# Humboldt-Kalmar:		777
# Pazifischer Makrelenhecht:	42



Schiffe = list()

class Schiff:
    def __init__(self, name, baujahr, leistung,):
        self.name = name
        self.baujahr = baujahr
        self.leistung = leistung
        self.fischfang = list()

    def fang_fische(self, art, menge):
        
        #fischfang = [art,menge]
        #fischfang.append("Blauflossen Thunfisch", 111)
        #print(fischfang)
        #Schiffe.extend(fischfang)
        #Schiffe.append(fischfang.art,fischfang.menge)
        #art = fischfang.art
        #menge = fischfang.menge
        #append an liste fischfang
        #wenn gringo append werte
        #wenn madonna append werte
        #wenn hasso append werte
        pass
    
    def melde_fischfang(self):
    #wenn name == gringo
        #dann melde fischfang
        #wenn name == hasso
        #melde fischfang
        pass
    
    def __str__(self):
        return f"{self.name} {self.baujahr} {self.leistung}"
    

##### Aufgabe 1 #####

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

#Fische.append(schiffang("Beispielfisch", 5))

# for x in Schiffe:
#     if x.name == "Gringo Freedom":
#         x.fang_fische("Beispielfisch", 5)

for x in Schiffe:
     print(x)

# for schiff in Schiffe:
#     schiff.melde_fischfang()

finde_staerkstes_schiff()
finde_aeltestes_schiff()


##### Musterlösung #####

Schiffe = list()

class Schiff:
    def __init__(self, name, baujahr, leistung):
        self.name = name
        self.baujahr = baujahr
        self.leistung = leistung
        self.fischfang = list()
    
    def fang_fische(self, art, menge):
        #self.fischfang.append(f"{art}: {menge}t") # einfache Variante
        self.fischfang.append([art, menge]) # vorrausschauende Variante
    
    def melde_fischfang(self):
        if self.fischfang:
            #for fang in self.fischfang:
            for fang in sorted(self.fischfang): # BONUS
                #print(f"{self.name} meldet {fang}") # einfache Variante
                print(f"{self.name} meldet {fang[0]}: {fang[1]}t") # vorrausschauende Variante
        else:
            print(f"{self.name} meldet: keine Fische gefangen.")
    
    def __str__(self):
        return f"{self.name} {self.baujahr} {self.leistung}"

Schiffe.append(Schiff("Gringo Freedom", 1950, 2312))
Schiffe.append(Schiff("Madonna II", 1980, 4400))
Schiffe.append(Schiff("Hasso IV", 2010, 6890))


for x in Schiffe:
    # if x.name == "Gringo Freedom":
    #     x.fang_fische("Pazifischer Kabeljau", 666)
    #     x.fang_fische("Blauflossen-Thunfisch", 3)
    #     x.fang_fische("Heilbutt", 69)
    if x.name == "Madonna II":
        x.fang_fische("Blauflossen-Thunfisch", 7)
        x.fang_fische("Gestreifter Marlin", 13)
        x.fang_fische("Gelbflossen-Thunfisch", 666)
    if x.name == "Hasso IV":
        x.fang_fische("Blauflossen-Thunfisch", 111)
        x.fang_fische("Humboldt-Kalmar", 777)
        x.fang_fische("Pazifischer Makrelenhecht", 42)


for schiff in Schiffe:
    schiff.melde_fischfang()
class Kurs:
    #Konstruktor
    def __init__(self, kursname, kursstart):
        self.kursname = kursname
        self.kursstart = kursstart

    #String Representation
    def __str__(self):
        return f"{self.kursname} mit Startdatum {self.kursstart}"
    
class Teilnehmer:
    def __init__(self,tnname, tnkurs, tnalter, tnort):
        self.tnname= tnname
        #das entsprechende Kursobjekt
        self.tnkurs = tnkurs
        self.tnalter = tnalter
        self.tnort = tnort

    def __str__(self):
        return f"{self.tnname} ist in Kurs {self.tnkurs.kursname} ist {self.tnalter} Jahre alt und kommt aus {self.tnort}"
    
def finde_kurs(kursname):
    for kurs in liste_kurse:
        if kurs.kursname == kursname:
            return kurs
        
def finde_altensack():
    tn_alt = liste_teilnehmer[0] # warum nicht liste_teilnehmer.tnalter[0]
    for x in liste_teilnehmer:
        if x.tnalter > tn_alt.tnalter:
            tn_alt = x
    return tn_alt


liste_kurse = list()
liste_kurse.append(Kurs("K1", "2024-01-01"))
liste_kurse.append(Kurs("K2", "2024-03-01"))
liste_kurse.append(Kurs("K3", "2024-05-01"))

# einkurs = finde_kurs("K3")
# print(einkurs)

liste_teilnehmer = list()
liste_teilnehmer.append(Teilnehmer("Andreas",finde_kurs("K1"), 24,"Berlin"))
liste_teilnehmer.append(Teilnehmer("Bernd",finde_kurs("K2"), 36,"Hamburg"))
liste_teilnehmer.append(Teilnehmer("Christoph",finde_kurs("K3"), 48,"Buxtehude"))

#print("Der Kurs des ältesten Teilnehmers: " + finde_altensack().tnkurs.kursname + " - Der Kurs startet am " + finde_altensack().tnkurs.kursstart)
print(finde_altensack())
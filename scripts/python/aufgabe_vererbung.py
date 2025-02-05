class Lebewesen:
    # Konstruktor
    def __init__(self, name, ton=None):
        self.name = name
        self.alter = 0
        self.ton = ton

    def get_name(self):
        return self.name

    def set_name(self, neuer_name):
        self.name = neuer_name

    def altern(self):
        self.alter += 1

    def get_alter(self, print_alter=False):
        if print_alter:
            print(f"{self.name} ist {self.alter} Zyklen alt.")
        else:
            return self.alter

    def gib_laut(self):
        if self.ton != None:
            print(self.name + ": " + self.ton + "!")
        else:
            print(f"{self.name}: Ich gebe keine Töne von mir.")

    def fortpflanzen(self):
        print(f"{self.name}: Sexy Time.")


# neue Klassendefinition abgeleitet (Tier)
class Saeugetier(Lebewesen):
    def fortpflanzen(self):
        print(f"{self.name}: Ich gebäre Junge.")


class Vogel(Lebewesen):
    def fortpflanzen(self):
        print(f"{self.name}: Ich lege Eier.")

class Pilz(Lebewesen):
    def fortpflanzen(self):
        print(f"{self.name}: Ich verteile Sporen")


class Hund(Saeugetier):
    def apportieren(self, gegenstand):
        print(f"{self.name}: Ich hole {gegenstand}.")

class Katze(Saeugetier):
    def kratzen(self,ziel):
        print(f"{self.name}: Ich kratze an {ziel}")


class Amsel(Vogel):
    def jagen(self, beute):
        print(f"{self.name}: Ich jage {beute}.")

class Elster(Vogel):
    def stehlen(self, ziel):
        print(f"{self.name}: Ich stehle {ziel}")

class Fliegenpilz(Pilz):
    def essen(self):
        print(f"{self.name} Mich essen ist eine schlechte Idee, Ich bin giftig!!!")
        


Tiere = list()
Tiere.append("Sabotage!")
Tiere.append(Hund("Hund", "Wuff"))
Tiere.append(Amsel("Amsel", "Piep"))
Tiere.append(Fliegenpilz("Fliegenpilz", "Pfff"))
Tiere.append(Katze("Katze", "Miau"))
Tiere.append(Elster("Elster", "Piep"))


for x in Tiere:
    if isinstance(x, Lebewesen):
        x.get_alter(True)
        x.fortpflanzen()
        x.gib_laut()
        if type(x) == Hund:
            x.apportieren("meinen Ball")
        if type(x) == Amsel:
            x.jagen("einen Wurm")
        if type(x) == Katze:
            x.kratzen("Kratzbaum")
        if type(x) == Elster:
            x.stehlen("Münze")
            x.stehlen("Perle")
        if type(x) == Fliegenpilz:
            x.essen()
        x.altern()
        print(x.get_alter())
    else:
        print(f"{x} ist kein Tier, du Noob!")

# type() prüft explizit auf den gleichen Datentyp
# isinstance() bezieht abgeleitete Klassen mit ein
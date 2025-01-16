while True:
            
        def say_hi_to(name = "KeinNameGewählt"):
            print("")
            print("Hallo " + name + "!\nDanke das du meinen Krassen Matheoperator benutzt!")
            print("")

        def ask_name():
            print("\nNenne mir deinen Namen")
            print("")
            return input()
        say_hi_to(ask_name())



        print("Bitte Wähle aus welchen Mathematischen Operator du benutzten willst")
        print("1 - Addition")
        print("2 - Subtraktion")
        print("3 - Multiplizieren")
        print("4 - Dividieren")
        print("5 - Modulus")
        print("6 - Floor Division")
        print("7 - Exponieren \n")

        def addition(a,b):
            return a + b

        def subtraktion(a,b):
            return a - b

        def multiplikation(a,b):
            return a * b

        def division(a,b):
            return a / b

        def modulus(a,b):
            return a % b

        def floor(a,b):
            return a // b

        def expo(a,b):
            return a ** b

        choose1 = int(input("Bitte Zahl eingeben: \n"))

        zahl1 = int(input("Bitte Zahl eins eingeben: \n"))
        zahl2 = int(input("Bitte Zahl zwei eingeben: \n"))

        match choose1:
            case "1":
                Ergebnis = addition(zahl1,zahl2)
                print("Das Ergebnis lautet: \n" + str(Ergebnis))
            case "2":
                    Ergebnis = zahl1 - zahl2
            case "3":
                  Ergebnis = zahl1 + zahl2

        print("Willst du noch eine Zahl ausrechnen?")
        print("1 - Ja")
        print("2 - Nein\n")
        choose2 = int(input("Bitte Zahl eingeben: \n"))

        if choose2 == 2:
            print("\nByeBye")
            exit()
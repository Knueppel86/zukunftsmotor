evaluationData = ["Zachariah", "Alexander", "Alexandra", "Alexandria", "Alexandrine", "Amelia", "Anastasia", "Ava", "Bartholomew", "Benjamin", "Catherine", "Charlotte", "Christopher", "Christopherson", "Constantine", "Elizabeth", "Ella", "Emma", "Ethan", "Eve", "Frederick", "Gabriella", "Ian", "Isabella", "Jack", "James", "Jonathan", "Leo", "Lia", "Liam", "Lily", "Lucas", "Margaret", "Mason", "Max", "Maximilian", "Maximiliana", "Nathaniel", "Nicholas", "Noah", "Olivia", "Penelope", "Sebastian", "Sophia", "Theodore", "Zoe"]

# # Verwendung von len()

# neListe = ["Eins", "Zwei", "Drei"]
# nString = "Ich bin ein string."

# print(len(neListe)) #3
# print(len(nString)) # ~ 20
# print(len(neListe[0])) #4


# # Verwendung von index()
# print(neListe.index("Zwei")) #1

#Aufgabe2
neueListe = []


for i in evaluationData:
    print("Listen Nummer evaluation Data :" , evaluationData.index(i) + 1 , i , "Anzahl der Buchstaben :" , len(i) , "\n" )
    neueListe.append(evaluationData.index(i))
    neueListe.append(i)
    neueListe.append(len(i))

#Aufgabe3
print("Einträge in der neuen Liste:      " , len(neueListe))
print("Neue Liste:                       \n" , neueListe)


#Aufgabe4
print("\nIndex Nummer:\n", evaluationData.index(max(evaluationData,key=len)), "\nAnzahl Buchstaben: \n" , len(max(evaluationData,key=len)) , "\nName : \n" , evaluationData[evaluationData.index(max(evaluationData,key=len))])
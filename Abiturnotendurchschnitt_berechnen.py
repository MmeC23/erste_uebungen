
''' Liste für Noten erzeugen. Der Name der Liste ist noten '''

''' Abfragen der Noten für Deutsch, Englisch und Mathe '''

''' Variable für den Durchschnitt anlegen. Der Name der variable ist durchschnitt. '''


''' Die Anzahl der Objekte in der Liste berechnen 
    Beispiel
    numbers = [1, 2, 3]
    avg = len(numbers)
    print(avg)
'''

''' Den Notendurchschnitt errechnen und ausdrucken
    Beispiel 
    numbers = [1,2,3,4,5]
    average = sum(numbers) / len(numbers)
    print(average)
    '''

''' Ist der Notendurchschnitt größer als 4, drucke: die Abiturprüfung muss wiederholt werden. '''

''' Ist der Notendurchnitt kleiner als 4, drucke: die Abiturprüfung wurde bestanden. '''

noten = 0 # nur das geht nicht: int object has no attribut append, man braucht noten = []
noten = []
Mathenote=int(input("Wie ist deine Mathenote? "))
Deutschnote=int(input("Wie ist deine Deutschnote? "))
Englischnote=int(input("Wie ist deine Englischnote? "))

noten.append(Mathenote)
noten.append(Deutschnote)
noten.append(Englischnote)

print(noten)
sum(noten)
len(noten)
average = sum(noten) / len(noten)
print(average)


if average >= 4:
    print("Die Abiturprüfung muss wiederholt werden.")
elif Mathenote == 6:
    print("Die Abiturprüfung muss leider wiederholt werden.")
elif Deutschnote == 6:
    print("Die Abiturprüfung muss leider wiederholt werden.")
elif Englischnote == 6:
    print("Die Abiturprüfung muss leider wiederholt werden.")
else:
    print("Du hast bestanden!")










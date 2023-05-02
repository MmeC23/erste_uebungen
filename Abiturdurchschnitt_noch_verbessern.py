
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

#noten = 0
noten = []
Mathenote=input("Wie ist deine Mathenote? ")
if Mathenote == "1":
    int(Mathenote)
if Mathenote == "2":
    int(Mathenote) 
if Mathenote == "3":
    int(Mathenote) 
if Mathenote == "4":
    int(Mathenote) 
if Mathenote == "5":
    int(Mathenote)  
if Mathenote == "6":
    int(Mathenote)  
  
else:
    print("Bitte gebe deine Note von 1 bis 6 nochmal ein. ")
    Mathenote=int(input("Wie ist deine Mathenote? "))



#if Mathenote != [1,2,3,4,5,6]: #Wie macht man das, wenn ausversehen ein Buchstabe eingegeben wurde?
   # print("Bitte gebe deine Note von 1 bis 6 nochmal ein. ")
   # Mathenote=int(input("Wie ist deine Mathenote? "))

Deutschnote=int(input("Wie ist deine Deutschnote? "))
if Deutschnote == "1":
    Deutschnote = int  
if Deutschnote == "2":
    Deutschnote = int    
if Deutschnote == "3":
    Deutschnote = int    
if Deutschnote == "4":
    Deutschnote = int    
if Deutschnote == "5":
    Deutschnote = int
if Deutschnote == "6":
    Deutschnote = int   
else:
    print("Bitte gebe deine Note von 1 bis 6 nochmal ein. ")
    Deutschnote=int(input("Wie ist deine Deutschnote? "))


Englischnote=int(input("Wie ist deine Englischnote? "))
if Englischnote == ("1", "2","3","4","5","6"):
    Englischnote = int     
else:
    print("Bitte gebe deine Note von 1 bis 6 nochmal ein. ")
    Englischnote=int(input("Wie ist deine Englischnote? "))



noten.append(int(Mathenote))
noten.append(Deutschnote)
noten.append(Englischnote)

print(noten)
sum(noten)
len(noten)
average = sum(noten) / len(noten)
print(average)


if average > 4:
    print("Die Abiturprüfung muss wiederholt werden.")
elif Mathenote == 6:
    print("Die Abiturprüfung muss leider wiederholt werden.")
elif Deutschnote == 6:
    print("Die Abiturprüfung muss leider wiederholt werden.")
elif Englischnote == 6:
    print("Die Abiturprüfung muss leider wiederholt werden.")
else:
    print("Du hast bestanden!")
    
#es wäre gut, falls sich jemand vertippt 8,9,..., dass die Abfrage nochmal beginnt
# FÜR MICH NICHT LÖSBAR










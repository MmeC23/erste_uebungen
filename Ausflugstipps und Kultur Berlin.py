

print("******************************************************\n")
print("                  BERLIN entdecken\n          ")
print("******************************************************\n")


print("Herzlich Willkommen in Berlin!\n")
print("An diesem Automaten können Sie sich über aktuelle Kultur und Ausflugstipps in Berlin informieren.")
print("Sie haben jeweils die Möglichkeit zwischen Kindern und Erwachsenen zu wählen.")
print("1 - Kultur")
print("2 - Ausflugstipps")
print()

while True:
    
            berlin = 0
            berlin = input("Bitte wählen Sie 1 für Kultur oder 2 für Ausflugstipps.")

            if berlin == "1":
                print("Sie haben Kultur ausgewählt.")
                print("Bitte wählen Sie noch aus, ob Sie an kinderfreundlichen Optionen interessiert sind: ja/nein ")
                while True:
                    kinder = input(">")
                    if kinder == "ja":
                        print("Sie haben kinderfreundliche Optionen ausgewählt. Hier kommen zwei Vorschläge. Bitte wählen Sie: ")
                        print("1 - Märchenstunde")
                        print("2 - Malen")
                        
                        while True:
                            auswahl_kinder = input(">")
                            if auswahl_kinder == "1":
                                print("Die Märchenstunde im blablabla können Sie jeden Montag nachmittag besuchen. Im Programm aktuell: Der gestiefelte Kater.  blablabla...")
                            elif auswahl_kinder == "2":
                                print("Hier können sich Kinder und Erwachsene in das Malen vertiefen. Es gibt fachkundige Anleitung zu jedem Malstil. Blablabla...")
                            else:
                                print("Ungültige Eingabe, bitte wählen Sie zwischen (1) und (2).")
                                
                    elif kinder == "nein":
                        print("Wir werden Ihnen jetzt zwei Kulturtipps für Erwachsene geben. Bitte wählen Sie: ")
                        print("1 - Theater")
                        print("2 - Lesung")
                        
                        while True:
                            auswahl_erwachsene = input(">")
                            if auswahl_erwachsene == "1":
                                print("Am kommenden Freitag können Sie sich das Theaterstück blablabla im blablabla Theater anschauen.")
                            elif auswahl_erwachsene == "2":
                                print("Die Lesung von blablabla aus seinem neuen Buch findet am nächsten Sonntag in Buchladen blablabla in der blablablastaße statt.")
                            else:
                                print("Ungültige Eingabe, bitte wählen Sie zwischen (1) und (2).")
                                
                        
                    else:
                        print("Ungültige Eingabe, bitte wählen Sie zwischen ja und nein.")
                       
                        



            elif berlin == "2":
                print("Sie haben Ausflugstipps ausgewählt.")
                print("Bitte wählen Sie noch aus, ob Sie an kinderfreundlichen Optionen interessiert sind: ja/nein ")
                while True:
                    kinder = input(">")
                    if kinder == "ja":
                        print("Sie haben kinderfreundliche Optionen ausgewählt. Hier kommen zwei Vorschläge. Bitte wählen Sie: ")
                        print("1 - Indoorspielplatz")
                        print("2 - Streichelzoo")
                        
                        while True:
                            auswahl_kinder = input(">")
                            if auswahl_kinder == "1":
                                print("Der Indoorpielplatz blablabla ist sehr beliebt. Hier können Sie blablabla...")
                            elif auswahl_kinder == "2":
                                print("Einen Streichelzoo in Berlin gibt es im Bezirk blablabla...")
                            else:
                                print("Ungültige Eingabe, bitte wählen Sie zwischen (1) und (2).")
                                
                    elif kinder == "nein":
                        print("Wir werden Ihnen jetzt zwei Kulturtipps für Erwachsene geben. Bitte wählen Sie: ")
                        print("1 - Klettern")
                        print("2 - Schlachtenseeumrundung")
                        
                        while True:
                            auswahl_erwachsene = input(">")
                            if auswahl_erwachsene == "1":
                                print("Die Kletterumgebung am ...")
                            elif auswahl_erwachsene == "2":
                                print("Bei schönem Wetter machen Sie doch einfach einen Spaziergang um den Schlachtensee.")
                            else:
                                print("Ungültige Eingabe, bitte wählen Sie zwischen (1) und (2).")
                                
                        
                    else:
                        print("Ungültige Eingabe, bitte wählen Sie zwischen ja und nein.")
                       
    
            else:
                print("Ungültige Eingabe, bitte wählen Sie zwischen Kultur (1) und Ausflugstipps (2).")
            
                





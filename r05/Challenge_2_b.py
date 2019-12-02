#Wersja druga. Zagnieżdzona lista

postac=[["pawel",30,0,0,0,0],["ewelina",10,5,5,5,5]]

choice = None

while choice != "0":
    print("""
        \n\nKreator postaci
        
        0 - zakończ
        1 - stwórz postać
        2 - wyświetl dostępne postacie
        3 - Edycja atrybutów postaci
        4 - Usuń postać
    """)
    choice = input("Wybierasz: ")

    #koniec gry
    if choice == "0":
       print("Żegnaj.")


    #Kreator postaci
    elif choice =="1":
        print("Kreator postaci")
        name = input("Podaj nazwę postaci: ")
        if name not in postac:
            pkt = 30
            print("Masz ",pkt," punktów które możesz przeznaczyć na cechy postaci")
            
            #sila
            x = int(input("Siła: "))
            if x <= pkt:
                sila = x
                pkt -= sila
                print("Pozostało Tobie ",pkt," punktów")
            else:
                print("Pozostało Tobie ",pkt," punktów")
            x = int(input("Zdrowie: "))
            if x <= pkt:
                zdrowie = x
                pkt -= zdrowie
                print("Pozostało Tobie ",pkt," punktów")
            else:
                print("Pozostało Tobie ",pkt," punktów")
            x = int(input("Mądrość: "))
            if x <= pkt:
                madrosc = x
                pkt -= madrosc
                print("Pozostało Tobie ",pkt," punktów")
            else:
                print("Pozostało Tobie ",pkt," punktów")
            x = int(input("Zręczność: "))
            if x <= pkt:
                zrecznosc = x
                pkt -= zrecznosc
                print("Pozostało Tobie ",pkt," punktów")
            else:
                print("Pozostało Tobie ",pkt," punktów")
            
            entry = name,pkt,sila,zdrowie,madrosc,zrecznosc
            postac.append(entry)
        else:
            print("Postać o takiej nazwie już istnieje")

    #Wyświetl dostepne postacie
    elif choice == "2":
        print("Dostępne postacie oraz ich atrybuty:\n")
        for entry in postac:
            name,pkt,sila,zdrowie,madrosc,zrecznosc = entry
            print(name,"Wolne pkt:",pkt," Siła:",sila,"Zdrowie:",zdrowie," Mądrość:",madrosc," Zreczność:",zrecznosc)

    #Edycja atrybutów
    elif choice == "3":
        print("Edycja atrybutów")
        imie = input("Podaj nazwę postaci, której mamy edytować atrybuty: ")

        for entry in postac:
            name,pkt,sila,zdrowie,madrosc,zrecznosc = entry
           
            if name == imie:
                #zapamiętuje pod jakim indexem jest dana postać zeby pożniej dodać ją w te same miejsce
                i=postac.index(entry)
                
                postac.remove(entry)
                pkt = 30
                print("Masz ",pkt," punktów które możesz przeznaczyć na cechy postaci")
                #sila
                x = int(input("Siła: "))
                if x <= pkt:
                    sila = x
                    pkt -= sila
                    print("Pozostało Tobie ",pkt," punktów")
                else:
                    print("Pozostało Tobie ",pkt," punktów")
                x = int(input("Zdrowie: "))
                if x <= pkt:
                    zdrowie = x
                    pkt -= zdrowie
                    print("Pozostało Tobie ",pkt," punktów")
                else:
                    print("Pozostało Tobie ",pkt," punktów")
                x = int(input("Mądrość: "))
                if x <= pkt:
                    madrosc = x
                    pkt -= madrosc
                    print("Pozostało Tobie ",pkt," punktów")
                else:
                    print("Pozostało Tobie ",pkt," punktów")
                x = int(input("Zręczność: "))
                if x <= pkt:
                    zrecznosc = x
                    pkt -= zrecznosc
                    print("Pozostało Tobie ",pkt," punktów")
                else:
                    print("Pozostało Tobie ",pkt," punktów")
                entry = name,pkt,sila,zdrowie,madrosc,zrecznosc
        postac.insert(i,entry)
    #Usuwanie postaci
    elif choice == "4":
        delete = input("Podaj nazwe uzytkownika, który chcesz usunąć: ")
        for entry in postac:
            name,pkt,sila,zdrowie,madrosc,zrecznosc = entry
            if name == delete:
                postac.remove(entry)
                print("Usunięto postać ",name)       
    else:
        print("Niestety ",choice," nie jest prawidłowym wyborem.")
        
input("\n\nAby zakończyć program, naciśnij klawisz ENTER.")

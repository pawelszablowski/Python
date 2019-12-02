#Rozdział 5,  zadanie 2
postac = []
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
        x = 0;
        pkt = 30
        sila = 0
        zdrowie = 0
        madrosc = 0
        zrecznosc = 0
        print("\nMasz do wykorzystania ",pkt," punktów na stworzenie swojej postaci")
        print("Dowolną ilość punktów możesz przeznaczyć na takie atrybuty jak: \n\nSiła \tZdrowie \tMądrość \tZręczność")
        name = input("Podaj nazwę dla Twojej postaci: ")
        print("\nPrzyznaj punkty na swoje atrybuty, masz na to ",pkt," punktów")
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
        
        entry = (name,sila,zdrowie,madrosc,zrecznosc,pkt)
        postac.append(entry)
        print("\nOto Twoja postać: ",entry)
        input("\nWciśnij ENTER aby zakończyć dodawanie postaci")

    #Wyświetl dostepne postacie
    elif choice == "2":
        print("\nOto postacie dostępnę w grze oraz jej atrybuty: ")
        for entry in postac:
            name,sila,zdrowie,madrosc,zrecznosc,pkt = entry
            print(name,"\tsila: ",sila,"\tzdrowie: ",zdrowie,"\tmadrosc: ",madrosc,"\tzrecznosc: ",zrecznosc,"\tWolne punkty: ",pkt)
    #Edycja atrybutów
    #elif choice == "3":
    #Usuwanie postaci
    elif choice == "4":
        score = input("Podaj nazwe uzytkownika, który chcesz usunąć: ")
        print(score)
        for item in postac:
            print(item)
        #if score in postac(0):
            #del postac[score]
         #   postac.remove(score)
        #else:
        #    print(score," nie ma takiej postaci na liscie")
    else:
        print("Niestety ",choice," nie jest prawidłowym wyborem.")
input("\n\nAby zakończyć program, naciśnij klawisz ENTER.")

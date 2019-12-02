#zadanie 3 rozdział 5
synojciec = {"paweł szabłowski":"janusz szabłowski"}
syn = ''
ojciec = ''
dziadek = ''
choice = None
print("Program \"Kto jest Twoim Tatą\" ")

while choice != "0":
    print("""

        0. Zakończ program
        1. Dodaj parę ojciec-syn
        2. Wyświetl bazę
        3. Wyświetl kto jest Twoim dziadkiem
        4. Edytuj dane rodzica
        5. Usuń parę syn-ojciec
    """)
    choice = input("Wybierasz: ")
    
    if choice == "0":
        print("Żegnaj")

    elif choice == "1":
        imie = input("Podaj swoje imię i nazwisko: ")
        imie = imie.lower()
        if imie not in synojciec:
            daneojca = input("Podaj imię oraz nazwisko ojca: ")
            daneojca = daneojca.lower()
            synojciec[imie] = daneojca

    #Wyświetla całą bazę ojciec - syn
    elif choice == "2":
        if synojciec == {}:
            print("\n Baza danych jest pusta. Dodaj kogoś do niej"  )
            continue
        else:
            for syn, ojciec in synojciec.items():
                print(syn.title(), " jest synem", ojciec.title())

    #Kto jest Twoim dziadkiem
    elif choice == "3":
        imie = input("Podaj swoje imię i nazwisko: ")
        imie = imie.lower()
        if imie in synojciec:
            ojciec = synojciec[imie]
            dziadek = synojciec[ojciec]

            #nazwa.title() - zamienia pierwsze litery na duże !!!
            dziadek = dziadek.title()
            print("Twoim dziadkiem jest: ", dziadek)
        else:
            print("Nie mamy Twojego dziadka w bazie danych")
            
            
    #Edycja danych rodzica        
    elif choice == "4":
        name = input("Podaj swoje imie i nazwisko: ")
        name = name.lower()
        if name in synojciec:
            daneojca = input("Podaj imie i nazwisko ojca: ")
            daneojca = daneojca.lower()
            synojciec[name] = daneojca
            print("\n Edycja danych zakończona sukcesem...")
        else:
            print("Twoje osoba nie występuje w bazie")
    #Usuwanie
    elif choice =="5":
        imie = input("Podaj swoje imie i nazwisko aby usunąć dane: ")
        imie = imie.lower()
        if imie in synojciec:
            del synojciec[imie]
            print(imie," został usunięty z bazy")
        else:
            print("Nie mamy ",imie," w bazie")
        
    else:
        print("Niestety ", choice," to niewłaściwy znak")
        
input("\n\nAby zakończyć program, naciśnij klawisz ENTER.")

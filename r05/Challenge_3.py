#zadanie 3 rozdział 5
synojciec = {"Paweł Szabłowski":"Janusz Szabłowski"}

choice = None
print("Program \"Kto jest Twoim Tatą\" ")

while choice != "0":
    print("""

        0. Zakończ program
        1. Dodaj parę ojciec-syn
        2. Wyświetl
        3. Edytuj dane rodzica
        4. Usuń parę syn-ojciec
    """)
    choice = input("Wybierasz: ")
    
    if choice == "0":
        print("Żegnaj")

    elif choice == "1":
        imie = input("Podaj swoje imię i nazwisko: ")      
        if imie not in synojciec:
            daneojca= input("Podaj imię oraz nazwisko ojca: ")
            synojciec[imie] = daneojca

    elif choice == "2":
        imie = input("Podaj swoje imię i nazwisko: ")
        print(synojciec.get(imie,"\tNie mamy Ciebie w bazie"))
            
    elif choice == "3":
        name = input("Podaj swoje imie i nazwisko: ")
        if name in synojciec:
            daneojca = input("Podaj imie i nazwisko ojca: ")
            synojciec[name] = daneojca
        else:
            print("Twoje osoba nie występuje w bazie")
    #Usuwanie
    elif choice =="4":
        imie = input("Podaj swoje imie i nazwisko aby usunąć dane: ")
        if imie in synojciec:
            del synojciec[imie]
            print(imie," został usunięty z bazy")
        else:
            print("Nie mamy ",imie," w bazie")
        
    else:
        print("Niestety ", choice," to niewłaściwy znak")
        
input("\n\nAby zakończyć program, naciśnij klawisz ENTER.")

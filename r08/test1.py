#testowy program

class Pet(object):  ## Nagłówek klasy. Dobrze jest nazywać ją z dużej litery
    """Wirtualny zwierzak"""  ## Łańcuch dokumentacyjny
    def __init__(self,name):
        print("Urodzil sie nowy zwierzak")
        self.__name = name

    @property
    def name(self):  ## Definicja metody # (self) ma być jako pierwszy prarametr instancji
        return self.__name

    @name.setter #dekorator. Poprzez użycie atrybutu setter
    def name(name, new_name): #metoda
        if (new_name == ""):
            print("Pusty łańcuch nie może byc imieniem twojego zwierzaka")
        else:
            self.__name = new_name
            print("Udało się prawidlowo zmienić nazwę zwierzaka")

    def talk(self):
        print("czesc, mam na imie", self.name)
        


#Main program
bydlak = Pet("Reksio")  ##KOnkretyzacja obiektu 
bydlak.talk()  ## Wywołanie metody

print("\nImię mojego zwierzaka to:", end= " ")
print(bydlak.name)

print("\nZmieniam nazwę zwierzaka na puste znaki")
bydlak.name = ("")
print("\nImię mojego zwierzaka to:", end= " ")
print(bydlak.name)
bydlak.talk()

print("\nImię mojego zwierzaka to:", end= " ")
print(bydlak.name)

input("\nWybierz ENTER aby zakonczyc program")





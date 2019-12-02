# Chapter 8 Challenge 4
# Utwórz program Farma zwierzaków, konkretyzując kilka obiektów klasy critter, i sledz ich stan poprzez liste
# Nasladuj program opiekun zwierzaka, lecz wymagaj od uzytkownika opieke nad cala farma
# Nadaj kazdemu zwierzakowi losowy poziom glodu i zadowolenia 
# Kazda pozycja z menu powinna umozliwic uzytkownikowi wykonanie czynnosci obejmujace wszystkie zwierzaki
import random

class Critter(object):
    """Wirtualna farma"""
    def __init__(self, name, hunger = 0, boredom = 0):  # konsstruktor klasy, ustawienie wartosći domyslnych
        self.name = name
        hunger = random.randint(0,5)
        boredom = random.randint(0,5)
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self): # prywatna metoda (dwie poziome kreski przed nazwą) wywoływana jest tylko przez inne klasy
        self.hunger += 1
        print("Głód wynośi ",self.hunger)
        self.boredom += 1
        print("Poziom zadowolenia wynosi ",self.boredom)

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m
    
    def talk(self):
        print("\nNazywam się", self.name, "i jestem", self.mood, "teraz.")
        self.__pass_time()
    
    def eat(self, food):
        print("\nMniam, mniam. ",self.name," Dziękuje.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("\nHura! ", self.name," świetnie się bawi")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def is_number(s):
    while s.isdigit() == False:
        s = raw_input("Enter only numbers: ")
    return int(s)


def main():
    farma = []
    raw_winput = 0
    print("Dodaj pierwszego zwierzaka i zacznij swoją przygodę\n")
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)
    farma.append(crit)
   
    choice = None  
    while choice != "0":
        print \
        ("""
        Opiekun farmy
    
        0 - zakończ
        1 - słuchaj wszystkich zwierzakow
        2 - nakarm wszystkie zwierzaki
        3 - pobaw się ze wszystkimi zwierzakami
        4 - dodaj zwierzaka do farmy
        """)
    
        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli 
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaka
        elif choice == "1":
            for item in farma:
                item.talk()
             
        # nakarm swojego zwierzaka
        elif choice == "2":
            food = int(input("Podaj ile jedzonka chesz dać dla zwierząt "))
            try:
                val = int(food)
            except ValueError:
                print("That's not an int!")

            for item in farma:
                item.eat(food)
         
        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            time = int(input("Ile godzin przezaczas na zabawę z zwierzętami? : "))
            for item in farma:
                item.play(time)
        
        # Dodaj zwierzaka do farmy
        elif choice == "4":
            crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
            crit = Critter(crit_name)
            farma.append(crit)
        # nieznany wybór 
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 


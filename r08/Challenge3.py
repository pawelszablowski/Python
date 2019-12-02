# Chalenge3
# Dodaj do programu "Opiekun zwierzaka" mechanizm tylnych drzwi, który dokładnie pokazuje właściwości atrubutu obiektu.
# Zrealizuj to poprzez wyświetlenie obiektu po wprowadzeniu ukrytej wartości, nie uwzględnionej w menu
# Wirtualny pupil, którym należy się opiekować

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, hunger = 0, boredom = 0):  # konsstruktor klasy, ustawienie wartosći domyslnych
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self): # prywatna metoda (dwie poziome kreski przed nazwą) wywoływana jest tylko przez inne klasy
        self.hunger += 1
        print("Głód wynośi ",self.hunger)
        self.boredom += 1
        print("Poziom zadowolenia wynosi  ",self.boredom)

    def __str__(self):
        line = "Critter object\n"
        line += "Imie: "+ self.name + "\n"
        line += "Poziom szczęścia: " + str(self.boredom) + "\n"
        line += "Poziom głodu: " + str(self.hunger) + "\n"
        line += "Poziom niezadowolenia : " + str(self.boredom + self.hunger) + "\n"
        return line
    
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
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()
    
    def eat(self, food):
        print("Mniam, mniam.  Dziękuję.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Opiekun zwierzaka
    
        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        """)
    
        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli 
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaka
        elif choice == "1":
            crit.talk()
        
        # nakarm swojego zwierzaka
        elif choice == "2":
            food = int(input("Podaj ile jedzonka chesz dać dla zwierzaka "))
            crit.eat(food)
         
        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            time = int(input("Ile godzin przezaczas na zabawę z zwierzakiem? : "))
            crit.play(time)

        # tylne drzwi
        elif choice =="4":
            print(str(crit))

        # nieznany wybór 
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 

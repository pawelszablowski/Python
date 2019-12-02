# Zwierzak z konstruktorem
# Demonstruje konstruktory

class Critter(object):
    """Wirtualny pupil""" 
    def __init__(self):   # konstruktor klasy (zwany metodą inicjalizacji). Jest wywoływana automatycznie po utworzeniu nowego obiektu
        print("Urodził się nowy zwierzak!")

    def talk(self):
        print("\nCześć! Jestem egzemplarzem klasy Critter.")

# część główna
crit1 = Critter()  # Tworzymy nowy obiekt - wywoływany jest konstruktor 
crit2 = Critter()  # Ponownie wywołany bedzie konstruktor 

crit1.talk()
crit2.talk()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

### Algorytm generuje liczby parzyste z zadanego przedzialu

class Generuj(object):
    def __init__(self, min, max):
        print("KOnstruktor klasy\n")
        self.max = max
        self.min = min

    def Parzyste(self, min, max):
        i = min
        print("Liczby parzyste z zadanego przedziału to: \n")
        while i <= max:
            if (i % 2) == 0:
                print(i, end=" ")
            i = i + 1
    def Nieparzyste(self, min, max):
        print("\nLiczby nie parzyste z zadanego przedziału to:\n")
        i = min
        while i <= max:
            if (i % 2) != 0:
                print(i, end = " ")
            i +=1
def main():
    choice = None
    print("Program wyświetla parzyste i nieparzyste liczby z podanego zakresu\n")
    while choice !=0:
        print("Wybierz dowolny klawisz żeby sprawdzić program")
        choice = input("\n0 wychodzi z programu...\n")
        liczby = Generuj(1,10)
        max = 0
        min = 0
        while 1:
            try:
                min = int(input("Podaj początkowy zakres: "))
                break
            except:
                print("Nie podałeś cyfry. Spróbuj jeszcze raz....")

        while 1:
            try:
                max = int(input("Podaj koniec zakresu: "))
                break
            except:
                print("Nie podałeś cyfry. Spróbuj jeszcze raz...")
        liczby.Parzyste(min,max)
        liczby.Nieparzyste(min,max)
           
main()
 #print(liczby.Nieparzyste,"\n")
input("Wciśniej ENTER aby wyjsć")
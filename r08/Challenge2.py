# Rozdział 8, Challenge 2
# Symulator telewizora

# Użytkownik powinien mieć możliwość wprowadzenia numeru kanału oraz regulacji głośności w właściwych zakresach 

# Stworzenie klasy telewizor.
# Atrybuty dla telewizora:
    # Numer kanału
    # Głośność (Volume)

# Metody dla telewizora:
    # Zmiana kanału z w określonym zakresie (wprowadzenie liczby).
    # Zmiana głośności w okreslonym zakresie (+ / - ).

class Tv(object):
    """Wirtualny Telewizor"""
    def __init__(self, volume, kanal):
        print("Telewizor włączony")
        self.volume = volume
        self.kanal = kanal



    def setglos(self,volume):
        if volume == "+":
            if self.volume < 100:
                self.volume += 10
            elif self.volume == 100:
                print("Głos ustawiony jest na ",self.volume)
        elif volume == "-":
            if self.volume > 0:
                self.volume -= 10
            elif self.volume == 0:
                print("Telewizor wyciszono")
        else:
            print("Wybrano nie prawidłowy znak. Wybierz \"+\" lub \"-\"")
    
    def setkanal(self, kanal):
        if self.kanal >0 and self.kanal < 100:
            self.kanal = kanal
            print("Zmieniono kanał na : ",self.kanal)
        else:
            print("Tego kanału nie ma w Twoim abonamencie")
    
    def status(self):
        print("\nWybrano kanał ", self.kanal," głos ustawiono na ",self.volume)

    def is_integer(number):
        if type(number) in (int):
            print("To jest int")
            return True
        else:
            return("To nie jest int")
            return False
        
def main():
    #sony = Tv()
    choice = None
    kan = 0
    channel = 0
    while choice != "0":
        sony.status()
        print("""
        0 - Wyłącz telewizor
        1 - Zmien kanał
        2 - Regulacja głośności
        """)
        choice = input("Wybierasz: ")
        if choice == "0":
            print("Telewizor wyłączony\n")

        elif choice == "1":
            #sony.status()
            try:
                kan = int(input("Podaj kanał : "))
            except:
                print("\nNie podałeś liczby!")
            #sony.setkanal(kan)
            sony.setkanal(kan)

        elif choice == "2":
            
            vol = input("\nWybierz \"+\" do zwiększenia glośności lub \"-\" aby przyciszyć: ")
            sony.setglos(vol)
        else:
            print("Zły wybór. Spróbuj ponownie")

# Program główny
sony = Tv(10,1)
main()

#input("Wciśnij Enter aby zakończyc")

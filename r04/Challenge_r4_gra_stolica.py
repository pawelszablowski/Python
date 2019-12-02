STOLICA = ("warszawa","londyn","moskwa","praga","lima")
import random
slowo = random.choice(STOLICA)
length = len(slowo)
print("Podpowiedz: Nazwa stolicy składa się z ",length ," znaków\n")
print("Masz 5 szans na odgadnięcię nazwy tej stolic")
szansa = 5
odpowiedz = ""
while szansa > 0 and odpowiedz != slowo:
    print("Masz jeszcze ",szansa," szans",end="")
    odpowiedz = input(" Podaj nazwę stolicy: ")
    if odpowiedz != slowo:
        print("Pudło, sprubuj jeszcze raz ")
    szansa -=1
if odpowiedz == slowo:
    print("Brawo!! Wygrałeś")
if odpowiedz != slowo:
    print("Przegrałeś")
input("\n\nWybierz Enter aby wyjść z gry")

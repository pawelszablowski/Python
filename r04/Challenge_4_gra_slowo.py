STOLICA = ("warszawa","londyn","moskwa","praga","lima")
import random
slowo = random.choice(STOLICA)
length = len(slowo)
print("Podpowiedz: Nazwa stolicy składa się z ",length ," znaków\n")
print("Masz 5 podpowiedz liter na odgadnięcię nazwy tej stolicy")
szansa = length
n = 0
odpowiedz = ""
znak = ""
odp = ""
print("Podaj literę aby sprawdzić czy wystpuje ona w wylosowanym slowie")
while n < 5 and odpowiedz != slowo:
    znak = input("Podaj literę: ")
    if znak.lower() in slowo:
        print("TAK")
    if znak.lower() not in slowo:
        print("NIE")
    n +=1
odpowiedz = input("Odgadnij wylosowane słowo: ")
if odpowiedz == slowo:
            print("Brawo!! Wygrałeś")    

if odpowiedz != slowo:
    print("Przegrałeś")
input("\n\nWybierz Enter aby wyjść z gry")

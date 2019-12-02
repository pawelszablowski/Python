#GRA - odgadnij liczbe
print("Masz 5 szans na odgadniecie cyfry wylosowanej przez komputer\n")
liczba = int(input("Podaj liczbę z zakresu 1 ...100 : "))
import random
los = random.randint(1,100)
trie = 1
while liczba != los and trie<5:

    if liczba > los:
        print("Za duża! ")
    else:
        print("Za mała")
    liczba = int(input("Podaj liczbę z zakresu 1 ...100 : "))
    trie +=1
    
if liczba == los:
    print("\nBrawo odgadłeś wylosowaną liczbę!")
    print("Udało się to tobie za", trie, " razem")

if trie == 5 and liczba != los:
    print("\a\nPrzegrałeś! Wyczerpałeś limit szans")


input("\n\nWybierz ENTER aby wyjść...")

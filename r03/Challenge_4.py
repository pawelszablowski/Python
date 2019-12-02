liczba = int(input("Podaj liczbę z zakresu 1..100 :"))
min = 1
max = 100
los = 0
import random
while los != liczba:
    los = random.randint(min,max)
    print("\nKomputer wylosował liczbe: ", los)
    if los > liczba:
        print("Za duża")
        max = los
    elif los < liczba:
        print("Za mała")
        min = los
print("Brawo, odgadłeś liczbe ")

input("\n Wcisnij dowolny klawisz...")

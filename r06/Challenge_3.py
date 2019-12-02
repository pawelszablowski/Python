#Losowanie liczby

import random

def ask_number(question, low, hight, step=1):
    response = None
    while response not in range(low,hight,step):
        print("Szukaj w zakresie",low,hight)
        response = int(input(question))
    return response

# 
def main():
    low = 1
    hight = 100
    tries = 0
    the_number = random.randrange(low,hight)

    liczba = int(input("Podaj liczbę z zakresu 1..100: "))

    while liczba != the_number:
        if liczba < the_number:
            print("Za mała")
            low = liczba
        if liczba > the_number:
            print("Za duża")
            hight = liczba
        liczba = ask_number("Podaj liczbę: ",low,hight)
        tries += 1
    print("\nBrawo! Szukana liczba to ", the_number)
    print("Udało sie odgadnąć to Tobie za ", tries," razem")

# Main program
main()




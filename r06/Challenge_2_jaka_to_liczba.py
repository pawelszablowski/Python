# Jaka to liczba?
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała,
# prawidłowa.

import random

def ask_number(question, low, high, step = 1): 
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high, step):
        print("Szukaj w zakresie ", low, "and", high)
        response = int(input(question))
    return response

print("Witaj w grze \"Odgadnij moją liczbę\" ")
print("Wymysliłem pewną liczbę od 1 do 100")
print("Spróbuj ją odgadnąć\n")

# set the initial values
the_number = random.randint(1, 100)
low = 1
high = 100
guess = ask_number("Podaj liczbę: ", low, high) 
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Niższa...")
        high = guess # player guessed too high, so high variable changed
    else:
        print("Wyższa...")
        low = guess # player guess too low, so low variable changed

    guess = ask_number("\nPodaj liczbę: ", low, high)
    tries += 1

print("\nBrawo! Tą liczbą była ", the_number)
print("Odgadłeś ją za ",tries," razem")

  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

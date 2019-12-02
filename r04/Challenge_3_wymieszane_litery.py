# Wymieszane litery
# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
# wybierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)
# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word
#podpowiedz
podpowiedz = ""
if word == "python":
    podpowiedz = "Wąż"
if word == "anagram":
    podpowiedz = "Ana.."
if word == "skomplikowany":
    podpowiedz = "Skom..."
if word == "odpowiedż":
    podpowiedz = "Odpo"
if word == "ksylofon":
    podpowiedz = "ksylo.."




# utwórz 'pomieszaną' wersję słowa
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
"""
           Witaj w grze 'Wymieszane litery'!
        
   Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print("Możesz zgarnąć 100 punktów. Każda podpowiedz = - 10p ")
print("Zgadnij, jakie to słowo:", jumble)
pomoc = ""
punkty = 100
guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    if pomoc == "":
        print("Niestety, to nie to słowo.")
    guess = input("Twoja odpowiedź: ")
    if guess != correct:
        pomoc = input("Niestety, to nie to słwo. Potrzebujesz podpowiedzi? t/n ")
        if pomoc == "t":
            print(podpowiedz)
            punkty -=10
    
if guess == correct:
    print("Zgadza się! Zgadłeś!\n")
print("Ilość Twoich punktów to: ", punkty)
print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

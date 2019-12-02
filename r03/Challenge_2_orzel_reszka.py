#Zlicza x Orzeł reszka
import random
reszka = 0
orzel = 0
licznik = 0;
while licznik <100:
    rzut = random.randint(1,2)
    if rzut == 1:
        orzel+=1
    if rzut == 2:
        reszka+=1
    licznik+=1
print("Orzeł wypadł ", orzel," razy, a reszka ",reszka, " razy")
input("\n\n Wciśnij dowolny klawisz")

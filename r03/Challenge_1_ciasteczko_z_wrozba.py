#Program "Ciasteczko z wróżbą"
print("Twoja wróżba na dziś to: ")
import random
los = random.randint(1,5)
if los == 1:
    print("Wygrasz milion")
elif los == 2:
    print("Spotka Ciebie coś miłego")
elif los == 3:
    print("Otrzymasz premie")
elif los == 4:
    print("Lodzik")
else:
    print("Wygrasz piwo")

input("\n\nWybierz Enter aby zakończyć program...")

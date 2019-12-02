komunikat = input("Podaj komunikat: ")
new_komunikat = ""
high=len(komunikat)
high-=1
n=0
while high >= 0:
    print(komunikat[high])
    new_komunikat+=komunikat[high]
    high -= 1
    n+=1
print("Nowy komunikat to " , new_komunikat)
input("Wybierz ENTER...")

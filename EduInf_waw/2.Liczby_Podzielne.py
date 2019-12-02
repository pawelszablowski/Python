#W przedziale <a, b> liczb całkowitych należy wyszukać wszystkie liczby 
# podzielne przez jedną z liczb z zadanego zbioru P.

a = int(input("Podaj początek zakresu: "))
b = int(input("\nPodaj koniec zakresu: "))
n = int(input("\nPodaj liczbę podzielników: "))
i = 0
j = 1
p = []
while i <= n:
    p.append(i)
    print(p[i],end=" ")
    i +=1
print("\n")
i = 1
while i <= b:
    while j <= n: 
        if (i % p[j]) == 0:
            print("Liczba ",i,"dzieli się przez ",p[j])
            
            break 
        
        j += 1
    i += 1
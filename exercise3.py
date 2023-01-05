#Tökéletes számok keresése
a = int(input("Írj be egy számot: "))
lista = []
for k in range(1, a+1):
    b = 0
    for i in range(1, k//2+1):
        if k % i == 0:
            b = b + i
    if b == k:
        lista.append(b)
print(f"1 és {a} között ezeket a tőkéletes számokat találtam:")
print(lista)
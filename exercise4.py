#Prím számok keresése
a = int(input("Írj be egy számot: "))
lista = []
for k in range(1, a+1):
    b = 0
    for i in range(1, k):
        if k % i == 0:
            b = b + i
    if b == 1:
        lista.append(i)
print(f"1 és {a} között ezeket a prím számokat találtam:")
print(lista)

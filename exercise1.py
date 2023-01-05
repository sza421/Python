#Kiírja egy pozitív egész szám osztóit
a = int(input("Írj be egy pozitív egész számot: "))

#Ebbe a listába kerülnek az osztók
#Az 1 már benne van, mert minden szám osztható eggyel
lista = [1]

for i in range(2, a):
    if a % i == 0 :
        lista.append(i)

lista.append(a)

print(lista)
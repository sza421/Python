#Kiírja egy pozitív egész szám osztóit
a = int(input("Írj be egy pozitív egész számot: "))

#Ebbe a listába kerülnek az osztók
lista = []

for i in range(1, a+1):
    if a % i == 0 :
        lista.append(i)

print(lista)
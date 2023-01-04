a = int(input('Elemek száma: '))

lista=[]

for i in range(a):
    if i == 0 :
        lista.append(0)
    if i == 1 :
        lista.append(1)
    if i > 1 :
        lista.append(lista[i-1]+lista[i-2])

print(lista)
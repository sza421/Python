

a = int(input('Írj be egy számot: '))
for i in range(1, a+1):
    if a % (i) == 0 and i != 1 and i != a:
        print(i)
    else:
        print('Prím szám')


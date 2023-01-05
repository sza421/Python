a = int(input("Írj be egy számot: "))

b = 0

for i in range(1, a//2+1):
    if a % i == 0:
        b = b + i

if b == a:
    print("Ez egy tökéletes szám!")
else:
    print("Ez nem egy tökéletes szám!")

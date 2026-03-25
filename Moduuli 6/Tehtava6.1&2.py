import random
tahkot = int(input("Anna nopan tahkot:"))
def heitto():
    return random.randint(1,tahkot)
tulos = 0
while tulos != tahkot:
    tulos = heitto()
    print("Nopan silmät", tulos)

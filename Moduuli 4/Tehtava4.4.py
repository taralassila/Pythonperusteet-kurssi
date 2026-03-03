import random
Luku = random.randint(1,10)
while True:
    arvaus = int(input("Arvaa luku välillä 1-10:"))
    if arvaus > Luku:
        print("Liian suuri arvaus")
    elif arvaus < Luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break

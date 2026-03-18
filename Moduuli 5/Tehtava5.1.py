import random

noppa = int(input("Anna noppien määrä:"))
summa = 0
for n in range(noppa):
    silmat = random.randint(1,6)
    summa += silmat
print(f"Noppien silmien summa:{summa}")



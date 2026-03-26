def summa():
    yht = luku1 + luku2
    return yht
def erotus():
    yht2 = luku1 - luku2
    return yht2
def tulos():
    yht3 = luku1 * luku2
    return yht3
def osamaara():
    yht4 = luku1 / luku2
    return yht4

while True:
    print("1=summa, 2=erotus, 3=tulo, 4=osamäärä, 5=lopeta")
    toiminto = input("Valitse toiminto:")
    if toiminto == "5":
        break

    luku1 = float(input("Anna ensimmäinen luku:"))
    luku2 = float(input("Anna toinen luku:"))

    if toiminto == "1":
        print("Tulos: ", summa())
    elif toiminto == "2":
        print("Tulos:", erotus())
    elif toiminto == "3":
        print("Tulos:", tulo())
    elif toiminto == "4":
        if luku2 == 0:
            print("Nollalla ei voi jakaa")
        else:
            print("Tulos:", osamaara())
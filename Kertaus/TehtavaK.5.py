
while True:
    print("1=summa, 2=erotus, 3=tulo, 4=osamäärä, 5=lopeta")
    toiminto = input("Valitse toiminto:")
    if toiminto == "5":
        break

    luku1 = float(input("Anna ensimmäinen luku:"))
    luku2 = float(input("Anna toinen luku:"))

    if toiminto == "1":
        print("Tulos:", luku1 + luku2)
    elif toiminto == "2":
        print("Tulos:", luku1 - luku2)
    elif toiminto == "3":
        print("Tulos:", luku1 * luku2)
    elif toiminto == "4":
        if luku2 == 0:
            print("Nollalla ei voi jakaa")
        else:
            print("Tulos:", luku1 / luku2)



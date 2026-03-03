eka = input("Anna luku:")
if eka == "":
    print("Ei lukua.")
else:
    pienin = suurin = eka
    while True:
        Luku = input("Anna Luku:")
        if Luku == "":
            break
        if Luku < pienin:
            pienin = Luku
        if Luku > suurin:
            suurin = Luku
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")


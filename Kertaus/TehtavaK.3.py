while True:
    luku = int(input("Anna luku: "))
    if luku == 0:
        print("Ohjelma päättyy.")
        break
    elif luku < 0:
        print("Virheellinen luku.")
    else:
        from math import sqrt
        print("Neliöjuuri:", sqrt(luku))
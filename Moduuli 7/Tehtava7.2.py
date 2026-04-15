nimet = set()
while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
for n in nimet:
    print(n)

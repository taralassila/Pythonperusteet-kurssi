luku_lista = []
while True:
    luku = int(input("Anna luku, jonka haluat lisätä listaan 0 lopettaa: "))
    if luku != 0:
        luku_lista.append(luku)
    print(luku_lista)
    luku_lista.sort()
    print(luku_lista)
    if luku == 0:
        break



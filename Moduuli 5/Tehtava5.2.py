luvut = []
while True:
    nro = input("Anna luku, tyhjä lopettaa:")
    if nro == "":
        break
    luvut.append(float(nro))
luvut.sort(reverse=True)
print("Viisi suurinta lukua:")
for l in luvut[:5]:
    print(l)
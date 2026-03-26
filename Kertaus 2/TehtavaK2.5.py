def suurin_arvo(eka,toka,kolkki):
    arvot = [eka, toka, kolkki]
    arvot.sort()
    return arvot[2]
eka1 = float(input("Anna ensimmäinen arvo: "))
toka2 = float(input("Anna toinen arvo: "))
kolkki3 = float(input("Anna kolmas arvo: "))
jarjestys = suurin_arvo(eka1,toka2,kolkki3)
print("Suurin arvo on: ", suurin_arvo(eka1,toka2,kolkki3))


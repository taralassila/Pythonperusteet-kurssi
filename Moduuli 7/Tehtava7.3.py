print("Uusi lentoasema: 1, Aiemmin haettu lentoasema: 2, Lopetus: 3")
lentoasemat = {}
while True:
    syote = input("Anna toiminto: ")
    if syote == "1":
        asema = input("Anna lentoaseman nimi: ")
        koodi = input("Anna lentoaseman ICAO: ")
        lentoasemat[koodi] = asema
    elif syote == "2":
        koodi = input("Anna lentoaseman ICAO: ")
        if koodi in lentoasemat:
            print(f"Lentoasema on {lentoasemat[koodi]}")
    elif syote == "3":
        break



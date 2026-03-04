tuntipalkka = float(input("Tuntipalkka: "))
tunnit = float(input("Tehdyt tunnit: "))
vpäivä = input("Viikonpäivä: ")
if vpäivä == "Sunnuntai" or vpäivä == "sunnuntai":
    print("Päiväpalkka:",tuntipalkka * tunnit*2)
else:
    print("Päiväpalkka:", tuntipalkka * tunnit)
sukupuoli = input("Sukupuoli:")
hemoglobiini = input("Hemoglobiini (g/l):")
if sukupuoli == "Nainen":
    if hemoglobiini <= "117":
        print("Alhainen hemoglobiini.")
    elif hemoglobiini >= "175":
        print("Korkea hemoglobiini.")
    else:
        print("Normaali hemoglobiini.")
if sukupuoli == "Mies":
    if hemoglobiini <= "134":
        print("Alhainen hemoglobiini.")
    elif hemoglobiini >= "195":
        print("Korkea hemoglobiini.")
    else:
        print("Normaali hemoglobiini.")

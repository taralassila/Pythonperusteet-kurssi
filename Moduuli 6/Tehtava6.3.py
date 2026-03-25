def litrat(gallonat):
    return gallonat * 3.785
while True:
    maara = float(input("Anna bensan määrä gallonoina: "))
    if maara < 0:
        print("Et saa bensaa")
        break
    litraat = litrat(maara)
    print(f"{maara} gallonaa on {litraat} litraa.")

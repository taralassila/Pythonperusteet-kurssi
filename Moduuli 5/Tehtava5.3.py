luku = int(input("Anna alkuluku: "))
if luku < 2:
        print("Luku ei ole alkuluku")
else:
    alkuluku = True
    for l in range(2,int(luku**0.5)+1):
        if luku % l == 0:
            alkuluku = False
            break
    if alkuluku:
        print("Luku on alkuluku")
    else:
        print("Luku ei ole alkuluku")
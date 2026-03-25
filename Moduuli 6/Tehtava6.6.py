import math
def yksikkohinta(halkaisija, hinta):
    sade = (halkaisija/2)/100
    pinta_ala = math.pi*sade**2
    return hinta/pinta_ala

pitsa1 = float(input("Ensimmäisen pitsan halkaisija:"))
hinta1 = float(input("Ensimmäisen pitsan hinta:"))

pitsa2 = float(input("Toisen pitsan halkaisija:"))
hinta2 = float(input("Toisen pitsan hinta:"))

yhinta1 = yksikkohinta(pitsa1,hinta1)
yhinta2 = yksikkohinta(pitsa2,hinta2)

if yhinta1 < yhinta2:
    print("Ensimmäisellä pitsalla on parempi vastine!")
elif yhinta2 < yhinta1:
    print("Toisella pitsalla on parempi vastine!")
else:
    print("Pitsat ovat yhtä hyviä hinnaltaan!")
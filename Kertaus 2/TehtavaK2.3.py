sanat = ["pyykkiteline","leikkuulauta","kirjahylly","terä","kani","peili"]
kirjaimet = 0
for sana in sanat:
    if len(sana)>5:
        kirjaimet+=1
print("Yli viisi kirjainta:", kirjaimet)
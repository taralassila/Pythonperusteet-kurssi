tarina = []
sana = ""
while sana != "loppu":
    sana = input("Anna sana tarinaa varten: ")
    if sana != "loppu":
        tarina.append(sana)
print(" ".join(tarina))
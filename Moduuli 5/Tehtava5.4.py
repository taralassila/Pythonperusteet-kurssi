kaupungit = []
for r in range(5):
    kaupunki = input(f"Anna kaupungin nimi {r+1}: ")
    kaupungit.append(kaupunki)
print("Antamasi kaupungit: ")
for kaupunki in kaupungit:
    print(kaupunki)
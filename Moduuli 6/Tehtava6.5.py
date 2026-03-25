def parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]
luvut = [1,2,3,4,5,6,7,8,9,10]
poistettu = parittomat(luvut)
print("Alkuperäinen lista:",luvut)
print("Lista, josta perittomat poistettu:", poistettu)
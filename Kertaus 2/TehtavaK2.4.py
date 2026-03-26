def kuusi(koko):
    print("Tämä on kuusi!")
    for k in range(1,koko + 1):
        print(" " * (koko - k)+"*" * (2*k-1))
kuusi(8)
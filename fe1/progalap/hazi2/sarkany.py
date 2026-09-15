def gondoltam():
    szam = int(input())
    print("Ennél nagyobb számra gondoltam!")
    szam2 = int(input())

    if szam2 > szam:
        print(f"Győztél, pont az {szam2} számra gondoltam!")
    else:
        print("Ó, az előbb tévedtem! Tényleg kisebb számra gondoltam! Győztél!")
if __name__=="__main__":
    gondoltam()
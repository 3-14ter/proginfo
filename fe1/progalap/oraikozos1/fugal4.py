
def koszones():
    nev = input("Adja meg a nevét! ")
    print("Üdvözlöm, tisztelt " + nev + "!")

def allatok_szama():
    allat=int(input())
    allat2=int(input())
    darabszam = (allat+allat2)*2
    print(f"Az állatok számának kétszerese: {darabszam}")
if __name__ == "__main__":
    allatok_szama()
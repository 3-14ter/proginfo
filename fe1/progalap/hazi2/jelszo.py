def szfinx(probajelszo, mainap):
    return bool("A szfinx nem arulja el a titkait")

def ajtonyitas(probajelszo, mainap):
    if szfinx(probajelszo, mainap) == True:
        return False
    else:
        return True
    

if __name__ =="__main__":
    probajelszo = input()
    mainap = int(input())
    print(szfinx(probajelszo, mainap))
    print(ajtonyitas(probajelszo, mainap))
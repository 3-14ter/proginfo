def angyal(csillagallas):
    return 3
def ordog(csillagallas):
    return 7

def valasztas(penz, csillagallas):
    jo = angyal(csillagallas)
    rossz = ordog(csillagallas)
    
    return (jo/(jo+rossz))*penz


if __name__=="__main__":
    penz=int(input())
    csillagallas = input()
    print(valasztas(penz,csillagallas))
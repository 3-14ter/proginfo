def fordul(szam):
    
    if szam >0:
        return "jobbra"
    
    if szam < 0:
        return "balra"
    else:
        return "stop"
if __name__=="__main__":
    szam = int(input())
    print(fordul(szam))
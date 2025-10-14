def tervezes(szam):
    szamlista = list(str(szam))
    if szamlista == szamlista[::-1]:
        return True
    else:
        return False

if __name__=="__main__":
    szam=int(input())
    print(tervezes(szam))
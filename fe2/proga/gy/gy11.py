def duplazas(l):
    for i in range(len(l)):
        if len(str(l[i]))==3 and str(l[i])[-1]=="3":
            l[i]=l[i]*2

def tobbszor(dict1):
    return 0

def szamjegyek(l):
    base10=set()
    for i in range(10):
        base10.add(i)
    szamok=set()
    for i in l:
        i = str(i)
        for n in i:
            szamok.add(int(n))
    szamok=base10.difference(szamok)
    return list(szamok)[0]

def statisztika(dasg):
    letters=[]
    for letter in dasg:
        letters.append(letter)
    letset=set(letters)
    for letter in letset:
        print(letters.count(letter))
    return letset

def szabalyos(l):
    betuk=[]
    c=0
    for word in l:

        print(betuk, betuk.sort())
        if betuk == betuk.sort():
            c+=1
        betuk=[]
    return c
def 
#print(szabalyos(["zug", "abrosz", "add", "so", "cica", "birs"]))


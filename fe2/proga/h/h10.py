def kep():
    with open("kepeslap.txt") as asdf:
        return asdf.read().strip()

def shillingek(tarca):
    for penz in range(len(tarca)):
        tarca[penz]=tarca[penz].split(" ")
    kontent=str(sum( int(tarca[i][0]) for i in range(len(tarca)) if tarca[i][1] == "shilling"))
    print(kontent)
    with open("penzkuldes.txt", "w") as asdf:
        if kontent =="0":
            asdf.write("0"+"\n")
            return False
        else:
            asdf.write(kontent+"\n")
            return True

def ajandek(fname, sett):
    with open(fname, encoding="utf-8") as asdf:
        a=asdf.read()
        a=a.splitlines()
        a=set(a)
        return (len(a.difference(sett)))
    
def szennyes(lost):
    with open("saros.txt","w", encoding="utf-8") as asdf:
        with open("tisztabb.txt","w", encoding="utf-8") as qwert:
            for i in range(len(lost)):
                if "sár" in lost[i]:
                    asdf.write(lost[i]+"\n")
                else:
                    qwert.write(lost[i]+"\n")
    return True

def szamlak(lost):
    osszeg = 0
    for i in range(len(lost)):
        fajlnev = lost[i] + ".txt"
        with open(fajlnev, encoding="utf-8") as asdf:
            a = asdf.read()
            sorok = a.splitlines()
            for j in range(len(sorok)):
                if sorok[j] != "":
                    osszeg += int(sorok[j])
                    
    return osszeg

#print(szamlak(['hentes', 'mosoda', 'cukraszda'])
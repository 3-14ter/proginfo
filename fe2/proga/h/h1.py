def aaaa():
    return int(input())

def nev():
    print("Mira")

def okos():
    print("Mira okos")

def tanul():
    print(input())

def mennyi():
    x=aaaa()
    y=aaaa()
    print(x+y)

def karok():
    x=aaaa()
    y=aaaa()
    print(2*x+2*y)

def kosarak():
    a=aaaa()
    aa=aaaa()
    print(f"{round(a//aa)} és {a%aa}")

def oraolvasas():
    a=aaaa()
    aa=aaaa()
    print(f"{int(a/30)}:{int(aa/6)}")

def kismutato():
    a=aaaa()
    print(f"{a//30}:{a%30*2}")  

def navigacio():
    ora=aaaa()
    perc=aaaa()
    oraszog=ora*30+perc*0.5
    percszog=perc*6
    if oraszog-percszog > 0:
        print(360-oraszog + percszog)
    else:
        print(percszog-oraszog)

def koratlag():
    a=aaaa()
    aa=aaaa()
    print((a*60+aa)/(12*60))

def lavafolyam():
    a=aaaa()
    aa=aaaa()
    print(aa/a)

def elveszett_muvelet():
    a=aaaa()
    aa=aaaa()
    print((3*a)-(2*aa))

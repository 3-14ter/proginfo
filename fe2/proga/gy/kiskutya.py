def kezdet():
    return int(1923)

def kutymuty():
    return int(input())

def gondozo_arany(a,aa):
    return a/aa

def szokas(e):
    return e

def megfigyeles(a):
    a=kutymuty()
    return kutymuty()*2+1

def pajta_meret(a):
    return True if a <10 else False

def mindenki_elegedett(a,aa,aaa):
    return True if a == True and aa==True and aaa==True else False

#def probalkozas(a):
#    int(a)
#def otlet(aa): 
#    int(aa)=probalkozas()


def jerry(problema):
    return len(str(problema)) < 5
def kollega(problema):
    return str(problema).startswith("1")
def problemamegoldas(problema):
    if jerry(problema)==True:
        return True
    elif kollega(problema)==True:
        return True
    else:
        return False

def hatalomatvetel(a,aa):
    return "OK" if a == aa else "KIUZVE!"

def cicca():
    return int(input())
def osboszorkany (a):
    b=cicca()
    bb=cicca()
    bbb=cicca()
    return True if (b!=0 and a%b==0) or (bb!=0 and a%bb==0) or (bbb!= 0 and a%bbb==0) else False

def harc(a,aa):
    a = str(a)
    aa= str (aa)
    jwin=0
    bwin=0
    for i in range(len(a)):
        if a[i]>aa[i]:
            jwin+=1
        if a[i]<aa[i]:
            bwin+=1
    if jwin == 0 and osboszorkany<0:
        return "osboszorkany"
    if bwin == 0 and jwin<0:
        return "Jerry"
    
    if jwin>bwin:
        return "Jerry"
    if jwin<bwin:
        return "osboszorkany"
    else:
        return "senki"

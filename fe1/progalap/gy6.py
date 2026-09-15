def reggeli(a):
    l = a.split(",")
    if len(l)!=1:
        return len(l)
    else:
        return l[0].upper()
    
def megnyirbalas(a,torolnivalo):
    for char in torolnivalo:
        a = a.strip(torolnivalo)
    return a

def megtisztit(kupac):
    return kupac.replace("*", "")
def mennyiseg(kupac):
    return len(kupac)
def kavic_szamlalas():  
    pass
#rrfdddprint(megnyirbalas(a="--**---||--/*",torolnivalo="*-"))
def kulonleges_aktak(l,n1,n2):
    return [l[i] for i in range(n1, n2-1)]

def veszelyes_emberek(l1,l2):
    return [l1[i] for i in range(len(l1)) if l1[i] in l2] 

def ekszerrablas(l1, l2):
    return [i+1 for i in range(len(l1)) if l1[i] not in l2]

def napidij_kifizetes(l1,l2):
    x=sum(1 for i in range(len(l1)) if i+1 in l2 and l1[i] != "verekedős")
    for i in range(len(l1)):
        if i+1 in l2 and l1[i] != "verekedős":
            l1[i]=l1[i].replace(l1[i],"verekedős")
    print(l1)
    return x

def verekedes(l1,l2):
    l1=dict(enumerate(l1,start=1))
    for i in list(l1.keys()):
        if i in set(l2):
            del l1[i]
    list(l1.values())
    return len(l1)


def rejtekhely(l1, l2):
    P = -1
    place = ""
    for i in range(len(l1)):
        l3 = l2[i].split(";")
        p = sum([int(i) for i in l3])
        if p > P:
            P = p
            place = l1[i]
    return place

def logikai_lanc(s, l):
    while len(l) > 0:
        m=False
        for i in l:
            if s[-1] == i[0]:    
                l.remove(i)
                s=i
                m=True
        if not m:
            return "logikai ellentmondás"
    return s

def nyomozas(l1, l2):
    for i in l1:
        r=logikai_lanc(i,l2)
        if r != "logikai ellentmondás":
            return i+"->"+r

def munka(s):
    if "válás" in s:
        return 0
    l=s.split()
    for i in l:
        if i[-1] =="$":
            return int(i[:-1])

def pancser(l):
    if len(l)== 0:
        return 0
    m = -1
    for i in l[1:]:
        r = munka(i)
        if r!=0 and m == -1:
            m=r
            continue
        if r<m:
            m=r
    return m if m != -1 else 0
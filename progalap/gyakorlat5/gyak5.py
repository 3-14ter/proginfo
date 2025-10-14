def idogep_osszeszereles(x):
    return len(x)
def kijelzo(x,y,z):
    a=[x,y,z]
    return a
def utazas(x):
    return x.count("idogorbites")
def veszelyes (x):
    if x.count("T-Rex"):
        return True
    else: 
        return False
def husevo(dino):
    return len(dino) % 2 == 0
def etetes(x):
    y = []
    for i in range(0, len(x)):
        if not husevo(x[i]):
            y.append(x[i])
    return y
def latnivalok(x):
    if x.count("ember"):
        x.remove("ember")
    return x
def raktarozas(x):
    y =[]
    for i in range (0, len(x)):
        if (x[i].split(":"))[1] =="elviszem":
            y.append((x[i].split(":"))[0])
    return y
def uldozes(x):
    fo ri print(len(max(x)))
    return x
def taska_falatozas(x):
    y=[]
    for i in range(0,len(x)):
        if (x[i])[1] !="@" or (x[i])[-2] !="@":
            y.append(x[i])
    return y
#print(uldozes(x= ["***", "*||**", "--|--|--", "-----", "~~~~~~"]))

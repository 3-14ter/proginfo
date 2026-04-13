def tabla(a):
    return(str(a.upper()))

def nevsorolvasas(a,b):
    c = a.split(';')
    print(c)
    if str(b) in c:
        return True
    else:
        return False
def uregek(a):
    return a.count("*")
def fegyverkezes(a):
     b = str(a)
     c = []
     for i in range(len(b)):
        c.append("|"+b[i])
     return "".join(c)
def javitas(a):
    x =a
    y:str
    while x.count("sérült")>0:
        x=a.replace("sérült","javított")
    y=x
    while y.count("hibás") > 0:
        y=x.replace("hibás","javított")
    return str(y)
def leltar():
    x = input()
    y = 0
    while x != "o": 
        y += int(x)
        x = input()
    return y
def orjarat():
    a=input()
    x=0
    y=0
    while a != "vege":
        if a[0]==a[-1]:
            x+=1
        else:
            y+=1
        a = input()
    return x/y if y>0 else None
def meneteles(x):
    print("Most "+str(x)+" bogár menetel")
def kikepzes(x):
    a = str(x)
    y=0
    z=0
    for i in range (len(a)) :
        y=int(a[i])
        z+=y
        meneteles(a[i])
    return z
def valogatas(x):
    y=""
    for i in range(0, len(x), 2):
        if int(x[i+1])>=5:
            y+=x[i]
    return y



def edzes(x):
    if x>10:
        return x*2
    elif x==10:
        return x*2
    else:
        return x*3
def trening():
    x=input()
    p = ""
    y=0
    while x != "":
        for i in range(0,len(x)):
            if x[i].count("("):            
                break
            p+=x[i]
        if x.count("szorgalmas"):
            y+=int(edzes(int(p)))
            print(y)
        else:
            y+=int(p)
            print(y)
        p=""
        x=input()
    return y



def tisztit(a):
    return a[0:-1]
def haditerv(a):
    b=""
    x=input()
    signs=[]
    for i in range(len(a)):
        signs.append(a[i])
    while x !="STOP":
        if x[-1] in signs:
            b+=tisztit(x)+";"
        x=input()
    return b[::-1]

def arokasas():
    a = input()
    r = 0
    while a!="(0;0)":
        x, y = a[1:-1].split(";")  
        d = (int(x)**2 + int(y)**2)**0.5
        if d > r:
            r=d

        a=input()
    return r
#print(arokasas())

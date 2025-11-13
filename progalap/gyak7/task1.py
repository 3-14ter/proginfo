def madarak_szama(x):
    for szam in range(x):
        print(f"{szam+1}. madár")


def tamadas(x,y):
    if len(x)<=len(y):
        return False    
    else:
        return True

def ugralas(x):
    xp=0
    for i in range(len(x)):
        xp+=int(x[i])
    return xp

def haboru(x,y):
    x.sort()
    y.sort(reverse=True)
    print(x[0], y[0])
    if int(x[0]) > int(y[0]):
        return True
    return False
def helyszin(x,y):
    z=[]
    for i in range(len(x)):
        if int(x[i])>int(y[i]):
            z.append(i)
    return z


def kardgyujtes(x):
    y=0
    for i in range(len(x)):
        if int(x[i])>0:
            y+=1
    return y


def mergesgomba(x):
    y=[]
    for i in range(len(x)):
        y.append(x[i].split(","))
    for i in range(len(y)):
        y[i] = list(map(int, y[i]))
    print(y)
    for i in range(len(y)):
        if sum(y[i])%2 !=0:
            return False
        else:
            return True
print(mergesgomba(x=["1,2,3,", "5","1,6,3,2,5,"]))
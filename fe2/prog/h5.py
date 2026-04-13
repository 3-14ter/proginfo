def megertes(a):
    return [x for x in a.split("*") if x != '']

def jatt(l):
    if len(l)%3 ==0:
        return l[-(len(l)//3)::]
    else:
        return l[-(len(l)//3-1)::]

def kicsomagolas(a):
    return a.split(";")[1:-1]

def elfogyott(l):
    return [i for i in l if '*' not in i]

def plakat(a, l):
    for i in l:
        if i in a:
            st = "***" + i + "***"
            a = a.replace(i, st)
    return a

def szomszedok(l,a1,a2):
    return True if l[l.index(a1)+1 % len(l)]==a2 or l[l.index(a1)-1 % len(l)]==a2 else False

def ulesrend(l):
    n = len(l)
    
    # 1. Szabály: Lucky és Lola Lux egymás mellett ülnek
    if "Lucky" in l and "Lola Lux" in l:
        if not szomszedok(l, "Lucky", "Lola Lux"):
            return False

    # 2. Szabály: Mina Luigi és Ököl Tony között ül
    if "Mina" in l:
        # Mindkettőnek a szomszédjának kell lennie
        if not (szomszedok(l, "Mina", "Luigi, a concierge") and szomszedok(l, "Mina", "Ököl Tony")):
            return False

    # 3. és 4. Szabály: Minetti és Georgio viszonya
    m = "Minetti, a pénztáros"
    g = "Georgio, a főpincér"
    joe = "az öreg Joe"

    if m in l and g in l:
        # 3. Nem ülhetnek egymás mellett
        if szomszedok(l, m, g):
            return False
            
        # 4. Ha pontosan egy ember van közöttük, az nem lehet az öreg Joe
        i_m = l.index(m)
        
        # Ellenőrizzük a "jobb" irányt (2 hellyel arrébb)
        if l[(i_m + 2) % n] == g:
            if l[(i_m + 1) % n] == joe: # A köztük lévő (1 hellyel arrébb)
                return False
                
        # Ellenőrizzük a "bal" irányt (2 hellyel vissza)
        if l[(i_m - 2) % n] == g:
            if l[(i_m - 1) % n] == joe: # A köztük lévő (1 hellyel vissza)
                return False

    return True

def ulesrend2_javitott(l):
    return not (
        ("Lucky" in l and "Lola Lux" in l and not szomszedok(l, "Lucky", "Lola Lux")) or
        ("Mina" in l and not (szomszedok(l, "Mina", "Luigi, a concierge") and szomszedok(l, "Mina", "Ököl Tony"))) or
        ("Minetti, a pénztáros" in l and "Georgio, a főpincér" in l and (
            szomszedok(l, "Minetti, a pénztáros", "Georgio, a főpincér") or
            (l[(l.index("Minetti, a pénztáros") + 2) % len(l)] == "Georgio, a főpincér" and l[(l.index("Minetti, a pénztáros") + 1) % len(l)] == "az öreg Joe") or
            (l[(l.index("Minetti, a pénztáros") - 2) % len(l)] == "Georgio, a főpincér" and l[(l.index("Minetti, a pénztáros") - 1) % len(l)] == "az öreg Joe")
        ))
    )


def ovadek(s): 
    c=0
    for i in range(len(s)):
        if s[i]=="$":
            ch=1
            x=""
            while s[i-ch].isdigit():
                x+=s[i-ch]
                ch+=1
            c+=int(x[::-1])
    return c


def kicsomagolas(a):
    return a.split(";")[1:-1]
def kave(x):
    x = x.replace("whiskey", "kávé")
    x = x.replace("whisky", "kávé")
    return x
def mindennapok(a):
    return kicsomagolas(kave(a))

def targetselector(guards):
    minDist = 999 
    target = guards[0]
    for i in range(len(guards)):
        dist = abs(guards[i][0]) + abs(guards[i][1])
        if dist < minDist:
            minDist = dist
            target = guards[i]
    return target
def intercept(pos, guard):
    pass
def coords(x):
    x=x.split(";")
    return [int(x[0]), int(x[1])]
def vedekezes(pos, guards, nRelic):
    pos=coords(pos)
    for i in range(len(guards)):
        guards[i]=coords(guards[i]) 
    if not guards:
        if pos == [0,0]:
            return "j"
        else:
            return "adsf"
    target=targetselector(guards)

    moveX = ""
    moveY = ""
    nextX = pos[0]
    nextY = pos[1]
    
    if target[0] > pos[0]:
        moveX = "j"
        nextX += 1
    elif target[0] < pos[0]:
        moveX = "b"
        nextX -= 1
    if target[1] > pos[1]:
        moveY = "f"
        nextY += 1
    elif target[1] < pos[1]:
        moveY = "l"
        nextY -= 1
    step = moveX + moveY
    if nextX == 0 and nextY == 0:
        if moveX and moveY:
            step = moveX
        elif moveX:
            step = moveX + "f" 
        elif moveY:
            step = "j" + moveY
    if step == "":
        return "asdf"
    return step
#print(vedekezes("3;2", ['0;2', '2;0', '-1;0'], 9))
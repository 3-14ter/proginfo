def bemutatkozas():
    print("Miriam")

def cipogyartas():
    print("Elokeszites\n")
    print("Gyartas\n")
    print("Utomunka")

def ujitas():
    print(input())

def tervezes():
    x=int(input())
    y = int(input())
    z=int(input())
    print(x+y+z)

def idobecsles():
    a=float(input())
    b=float(input())
    c=float(input())
    print(int((a**2*b)/(0.8*c)))

def tavozas():
    x=int(input())
    print(x//12)

def atlagos_elegedettseg():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    print((a+b+c+d)/4)

def szavazatok():
    x=int(input())
    y=int(input())
    print((x-(x-y))*"+"+"\n"+(x-y)*"-")

def hasznalat():
    x=input()
    aaaaaaa=0
    for i in range(len(x)):
        aaaaaaa+=int(x[i])
    print(aaaaaaa)

def visszatancolas():
    asd=input()
    print(int(asd[::-1]))

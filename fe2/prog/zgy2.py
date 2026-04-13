def str_alapok(a):
    return '' if a=='' else a.replace("a","e") if a[0]=="a" else a[4] if len(a)>4 else a.upper()

def seged1(x):
    return x + 3
def seged2(x):
    return 2 * x
def ismetles(n1,n2):
    x=0
    for i in range(n1,n2+1):
        if i%2==0:
            x+=seged1(i+1)
        else:
            x+=seged2(i*2)
    return seged1(x)

def ismetles2(n1,n2):
    return seged1(sum(seged1(i+1) if i%2==0 else seged2(i*2) for i in range(n1,n2+1)))

def beolvasas():
    n1=int(input())
    n2=int(input())
    b=True
    while True:
        n3=input()
        if n3 == "VEGE":
            break
        if int(n3) != n1+n2+1:
            b=False
        n1=n2
        n2=int(n3)
    return b

def buborek01(iksz):
    print(iksz*"o")
def buborek02(iksz, ipszilon):
    rem = 0
    if iksz > ipszilon:
        rem = iksz-ipszilon
        print(ipszilon*"oO"+rem*"o")
    elif iksz < ipszilon:
        rem = ipszilon-iksz
        print(iksz*"oO"+rem*"O")
    else:
        print(iksz*"oO")
def viragfuzer():
    alist = []
    while True:
        a = input()
        if a == "":
            break
        else:
            alist.append(a)

    return "+".join(alist)
def hopp(iksz, ipszilon, zé):
    div = zé // iksz
    couonter=0
    mult="Potty!"
    simp = "Hopp!"
    out = []
    for i in range(div):
        couonter += iksz
        if couonter > zé:
            break
        if couonter%ipszilon == 0:
            out.append(mult)
        else:
            out.append(simp)
    print("\n".join(out))
    return out.count("Potty!")

def godorben(iksz):
    progress = 0
    ugri = 10
    iter = 0
    while progress < iksz:
        iter +=1
        progress += ugri
        if progress >= iksz:
            break
        progress*=0.9
        ugri +=2         
    return iter

if __name__=="__main__":
    iksz = int(input())
#    ipszilon = int(input())
#    zé = int(input())
    print(godorben(iksz))
#    print(hopp(iksz, ipszilon, zé))
#    buborek01(iksz)
#    buborek02(iksz,ipszilon)
#    print(viragfuzer())
def gyongyok_ara(p,z,k):
    zcount= 100//z
    zfin=z*zcount
    pcount = 0
    pfin=0
    kcount = 0
    kfin = 0
    if p <= z:
        pfin=(zcount+2)*p
        pcount = zcount+2
    else:
        pcount = max(zcount - 2,0)
        pfin=pcount*p
        
    if pfin+zfin < 200:
        kcount = pcount + zcount
        kfin = kcount*k
    else:
        kfin = zcount*k
    return pfin+zfin+kfin
if __name__=="__main__":
    p = int(input())
    z = int(input())
    k = int(input())
    print(gyongyok_ara(p,z,k)) 
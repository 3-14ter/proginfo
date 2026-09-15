def valasztas(x,y):
    nulla = 0
    if x>0 and y>0:
        return 1
    elif x>0 and y<0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x<0 and y>0:
        return 4
    else:
        return nulla
if __name__=="__main__":
    x = int(input())
    y = int(input())
    print(valasztas(x,y))
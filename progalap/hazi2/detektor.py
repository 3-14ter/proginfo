def kerites(range, keriteshossz):
    if keriteshossz%range == 0:
        return 0
    else:
        return range-(keriteshossz%range)  
if __name__=="__main__":
    range = int(input())
    keriteshossz = int(input())
    print(kerites(range,keriteshossz))
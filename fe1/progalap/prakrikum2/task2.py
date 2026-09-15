def bazis_epites():
    s = input()
    l = ["A felhasznált modulok: "]
    while True:
        if s=="VÉGE":
            break
        l.append(s)
    return str(l)
if __name__=="__main__":
    print(bazis_epites())  
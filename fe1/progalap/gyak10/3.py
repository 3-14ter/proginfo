def szamjegyek(l):
    sz = {"0","1","2","3","4","5","6","7","8","9"}
    for i in range(len(l)):
        for j in range(len(str(l[i]))):
            if str(l[i][j]) in sz:
                sz.pop()
    return sz
print(szamjegyek([1073, 9240, 5, 80]))
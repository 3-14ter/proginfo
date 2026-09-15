def szotar(dic1, set1):
    retl =[]
    for key, item in dic1.items():
        if item in set1:
            retl.append(key)
    for key in retl:
        dic1.pop(key)
    return retl

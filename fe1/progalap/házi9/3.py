def lehallgatas(dic, sett):
    c = set()
    for a, b, in dic.items():
        for i in sett:
            if b == i:
                c.add(a)
    return c

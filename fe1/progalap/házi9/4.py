def kaszino(dic, dicc):
    s=set()
    for geng, kartyak in dic.items():
        for kartya, jelentes in dicc.items():
            if kartya in kartyak:
                s.add(jelentes)
    return s

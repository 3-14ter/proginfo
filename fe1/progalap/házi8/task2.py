def penzosztas(a):
    if not a:
        return ""
    else:
        a = a.split(';')
        a = sorted(a, key=int)
    return ";".join(a)

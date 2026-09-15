def eladas(a,b=set()):
    s = set(a.split(";"))
    return len(s & b)

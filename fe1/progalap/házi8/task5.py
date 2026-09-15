def titkosiras(a):
    if not a:
        return str(0)
    a = a.split()
    b = [str(len(s)) for s in a]
    c = [s[::-1] for s in a]
    return "".join(b) + "".join(c)


def kezeles(gy, b):
    cont = set()
    for d in b:
        for g in gy:
            if d % g == 0:
                cont.add(d)
                break
    b -= cont
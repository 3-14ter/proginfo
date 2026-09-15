def orjaratok(a,b,c):
    d=b+c-1
    for d in a:
        e=((b+d-1)//c)*c
        if e<d:
            return False
    return True
print(orjaratok([5, 8], 17, 4))
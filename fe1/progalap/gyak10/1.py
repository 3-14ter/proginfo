def duplazas(l):
    for i in range(len(l)):
        if str(l[i])[-1] == '3' and len(str(l[i])) == 3:
            l[i]*=2
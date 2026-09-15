def foci(x):
    a=len(x)
    if len(x)%2 != 0:
        return False 
    for i in range(len(x)):
        x[i]=x[i].split("-")
    b=[]
    c=[]
    for i in range(a):
        if len(b)<=a/2:
            for j in range (len(x[i])):
                if x[i][1:] in (b):
                    c.append(x[i][0])
                else:
                    b.append(x[i][0])
        else:
            c.append(x[i][0])
    d=set(c) & set(c)
    if len(d)>0:
        return False
    else:
        return True
print(foci(x=['Mazsola-Tádé-Manócska-Rókakoma', 'Rókakoma', 'Tádé', 'Manócska']))
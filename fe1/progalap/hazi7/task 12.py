def legrosszabb_hazszam(x):
    y=[]
    for i in range(len(x)):
        if x[i]==min(x):
            y.append(i+1)
    return y

def legjobb_hazszam(x):
    y=[]
    for i in range(len(x)):
        if x[i]==max(x):
            y.append(i+1)
    return y

def ijaszverseny(a,b):
    for i in range(len(a)):
        if a[i]+b[i] in a and a[i]+b[i] != a[i]:
            return True
    return False 

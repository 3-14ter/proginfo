def kilepes(s):
    r=[]
    for i in range(len(s)):
        if s[i]=="*":
            r.append(i)
    return r

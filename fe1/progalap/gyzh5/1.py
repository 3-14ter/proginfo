def szotarkeszites(l1, l2):
    dic={}
    for i in range(len(l1)):
        if l1[i] == l1[i].lower() and int(l2[i]%2) == 0:
            dic[l1[i]]=l2[i]
    return dic

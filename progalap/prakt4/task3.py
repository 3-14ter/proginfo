def zsebek(li):
    li_2=[]
    if len(li) != 0:
        for i in range(0,len(li)):
            if "fegyverként használható" in li[i]:
                li_2.append(li[i])
        return li_2
    else: return li_2
#print(zsebek(li=[]))

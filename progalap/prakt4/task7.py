def eszrevetel(li1, li2): 
    for i in li2:
        while i in  li1:
            li1.remove(i)
    return li1
def noi_nevek(linevek):
    count=0
    for nev in range(len(linevek)):
        if linevek[nev][-1] == "a":
            count +=1
    return count
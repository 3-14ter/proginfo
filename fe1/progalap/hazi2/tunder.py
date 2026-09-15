def milyen(ferfi, noi):
    if ferfi>noi:
        return "n"
    if noi>ferfi:
        return "f"
    else:
        return "s"
    
def mennyi(ferfi, noi):
    if ferfi>noi:
        return ferfi-noi
    if noi>ferfi:
        return noi-ferfi
    else:
        return 0
    

if __name__=="__main__":
    ferfi = int(input())
    noi = int(input())
    print(milyen(ferfi,noi), mennyi(ferfi,noi))
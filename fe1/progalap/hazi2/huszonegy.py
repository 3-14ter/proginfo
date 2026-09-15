def milyen_XXI(ferfi, noi, mindegy):
    if ferfi > noi:
        if ferfi - noi > mindegy:
            return "n"
        else:
            return "s"
    if noi > ferfi:
        if noi - ferfi > mindegy:
            return "f"
        else:
            return "s"
    else:
        return "s"
    

def mennyi_XXI(ferfi, noi, mindegy):
    if ferfi > noi:
        diff = ferfi - noi
        if diff > mindegy:
            return diff - mindegy
        else:
            return 0
    if noi > ferfi:
        diff = noi - ferfi
        if diff > mindegy:
            return diff - mindegy
        else:
            return 0
    else:
        return 0


if __name__ == "__main__":
    ferfi = int(input())
    noi = int(input())
    mindegy = int(input())
    print(milyen_XXI(ferfi, noi, mindegy), mennyi_XXI(ferfi, noi, mindegy))
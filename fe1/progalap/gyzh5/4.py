def csv_kezeles(filename):
    sums=[]
    with open(filename, "r", encoding="utf-8") as csv:
        readcsv = csv.readlines()
    for lines in readcsv[1:]:
        var = lines.strip().split(",")
        name, x, y = var
        if name and name[0].isupper() and name[1:].islower():
            sums.append(int(x)+int(y))
    return sums
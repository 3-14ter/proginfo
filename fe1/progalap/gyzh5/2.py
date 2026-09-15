def fajlba_iras(l1, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(len(l1)):
            f.write(f":{l1[i]}:\n")

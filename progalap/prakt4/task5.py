def korbenjaras(li1,elhaladt):
    for i in elhaladt:
        if li1.count(i)<2:
            return False
    return True

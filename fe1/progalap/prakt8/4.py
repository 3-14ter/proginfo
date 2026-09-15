def szelvihar(dic, hely):
    if hely not in dic:
        return dic
    dic.pop(hely)
    return dic
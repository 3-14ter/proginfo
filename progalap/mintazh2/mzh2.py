def str_alapok(text):
    if len(text) == 0:
        return text
    if text[0]=="a":
        text = text.replace("a","e")
        return text
    if len(text)>4 and text[0]!="a":
        return text[4]
    else:
        text=text.upper()
    return text

def seged1(x):
    return x + 3

def seged2(x):
    return 2 * x

def ismetles(x,y):
    for i in range(y-x):
        if i%2 ==0:
            pass
        else:
            i+=seged2(x)


#print(str_alapok(text=""))
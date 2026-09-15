def utazas(s):
    r = set()
    ind = None
    collected = []
    for i, ch in enumerate(s):
        if ch == "+":
            if ind is None:
                ind = i
                collected = []
        elif ch == "*":
            if ind is None:
                return {i} 
            r.add("".join(collected))
            ind = None
            collected = []
        else:
            if ind is not None:
                collected.append(ch)
    return r

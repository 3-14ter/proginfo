def atlagfelett(x):
    return sum(1 for i in x if i >(sum(x)/len(x)))
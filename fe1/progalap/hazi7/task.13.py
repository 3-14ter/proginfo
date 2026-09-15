def ermek_szama(x):
    return [(sum(1 for i in x if i<=30)), (sum(1 for i in x if 31<=i<=80)), (sum(1 for i in x if 81<=i<101))]

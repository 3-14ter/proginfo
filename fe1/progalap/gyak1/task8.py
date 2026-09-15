def szavazatok():
    all=int(input())
    plus=int(input())
    print('+'*plus, '\n', '-'*(all-plus), sep='')

if __name__=="__main__":
    szavazatok()
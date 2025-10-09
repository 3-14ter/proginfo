def csata(thezi, loserek1, loserek2, loserek3):
    teams = [loserek1,loserek2,loserek3]
    teams.sort(reverse=True)
    definer = 0 
    if teams[0]-teams[1] == 0:
        definer = teams[2]
    else: 
        definer = teams[0]-teams[1]-teams[2]
    if definer >= thezi:
        return False
    else:
        return True
if __name__=="__main__":
    thezi = int(input())
    loserek1 = int(input())
    loserek2 = int(input())
    loserek3 = int(input())
    print(csata(thezi, loserek1,loserek2,loserek3))
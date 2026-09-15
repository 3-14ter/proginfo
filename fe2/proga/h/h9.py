def erkezes(dict1, str1):
    return dict1.get(str1) if str1 in dict1 else 0

def beszivargas(dict1):
    a =""
    for key, value in dict1.items():
        if value == "takarító":
            a = key
    return a  

def lehallgatas(dict1, hidingplace):
    fhgfd=set()
    for k, v in dict1.items():
        if v in hidingplace:
            fhgfd.add(k)
    return fhgfd

def kaszino(geng,info):
    ans=set()
    for k, l in geng.items():
        for i in range(len(l)):
            print(l[i])
            if l[i] in info.keys():
                ans.add(info.get(l[i]))
    return ans

def percent(num):
    return int(num[:-1])/100
def ugras(jump, land):
    best=[]
    for action, jumpodd in jump.items():
       for landing, landodd in land.items():
           best.append(percent(jumpodd) * percent(landodd))
    return int(max(best)*100)

def menekules(all_locations, From, to):
    if From not in all_locations or to not in all_locations: 
        return -1
    return ((all_locations.get(From).get("GPS_X") - all_locations.get(to).get("GPS_X"))**2 + (all_locations.get(From).get("GPS_Y") - all_locations.get(to).get("GPS_Y"))**2)**(1/2)

def hajo():

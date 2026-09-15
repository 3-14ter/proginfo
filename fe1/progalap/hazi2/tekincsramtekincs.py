def sarkany(date):
    return len("A sarkany nem fecseg feleslegesen")

def kincs(date, request):
    penz = sarkany(date)
    if penz > request:
        return request
    else:
        return penz

if __name__=="__main__":
    date = int(input())
    request = int(input()) 
    print(kincs(date, request))
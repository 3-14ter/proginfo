def navigacio():
    kor = 360
    ora=int(input())
    perc=int(input())
    oraszog=(30)*ora + 0.5*perc
    percszog=(6)*perc

    if percszog-oraszog>=0:
        print(percszog-oraszog)
    else:
        print(percszog-oraszog+kor)


if __name__ == "__main__":
    navigacio()
    
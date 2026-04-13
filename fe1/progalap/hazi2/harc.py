def harc(jobb, bal, kozep):
    attack = []
    if not jobb:
        attack.append("1")
    if not bal:
        attack.append("2")
    if not kozep:
        attack.append("3")
    
    return ";".join(attack)


if __name__ == "__main__":
    jobb = input() == "True"
    bal = input() == "True"
    kozep = input() == "True"
    print(harc(jobb, bal, kozep))
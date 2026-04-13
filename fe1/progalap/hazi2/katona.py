def szerencse():
    háború = input("Lesz háború? ")
    if háború == "igen":
        nemtartalekos = input("Tartalékos lesz? ")
        if nemtartalekos == "nem":
            front = input("Kiküldik a frontra? ")
            if front == "igen":
                damaged = input("Megsebesül? ")
                if damaged == "igen":
                    sulyosan = input("Könnyen sebesül meg? ")
                    if sulyosan == "nem":
                        gyogyul = input("Meggyógyul? ")
                        if gyogyul == "nem":
                            temetes = input("Rendesen eltemetik? ")
                            if temetes == "nem":
                                return False
    return True 


if __name__ == "__main__":
    print(szerencse())

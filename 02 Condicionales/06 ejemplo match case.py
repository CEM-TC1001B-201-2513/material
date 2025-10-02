n = int(input("Ingresa un número de 1 a 3: "))
match n:
    case 1:
        print("n vale uno")
    case 2:
        print("n vale dos")
    case 3:
        print("n vale tres")
    case _:
        print("n no está entre 1 y 3")
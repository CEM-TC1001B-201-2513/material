edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
    mes_nacimiento = int(input("Indica tu mes de nacimiento en número:"))
    if mes_nacimiento > 6:
        print("Naciste en el segundo semestre")
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    faltante = 18 - edad
    print(f"Te faltan {faltante} años para ser mayor de edad.")

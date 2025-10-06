import random

aleatorio = random.randint(1,100)
selección = int(input("Ingresa un número del 1 al 100: "))
intentos = 1
while selección != aleatorio:
    if selección > aleatorio:
        print("El número que buscas es menor.")
    else:
        print("El número que buscas es mayor.")
    selección = int(input("Ingresa un número del 1 al 100: "))
    intentos += 1
print(f"Has atinado, te tomó {intentos} intentos.")
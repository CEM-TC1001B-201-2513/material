# for i in range(5)
i = 0 # inicio
while i <= 4: # final -> condición de paro o de salida
    print(f"El valor de i es: {i}")
    # i = i + 1
    i += 1 # paso
print("-"*30)

lista = [1,2,"hola",True,[1,2]]
# lista[posición] -> De izquierda a derecha e inicia en 0
print(lista[2])
# len(lista) -> Longitud de la lista
print(len(lista))
i = 0
while i < len(lista):
    print(f"lista[{i}] -> {lista[i]}")
    i += 1
print("-"*30)

opción = input("Ingresa 1)Sí o 2)No: ").strip()
while opción != "1" and opción != "2":
    print("Debes escribir 1 para sí o 2 para no...")
    opción = input("Ingresa 1)Sí o 2)No: ").strip()











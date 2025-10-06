# Tabla de multiplicar
# Preguntar por un valor entero n
# Imprimir la tabla de multiplicar de 1 a 10 del valor n
# Ejemplo 5:
# 1 x 5 = 5
# 2 x 5 = 10
# ...
# 10 x 5 = 50
n = int(input("Ingrese un número: "))
for i in range(1,11):
    multiplicación = n * i
    print(f"{i} x {n} = {multiplicación}")
    
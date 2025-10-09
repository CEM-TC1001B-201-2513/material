# parámetros -> entradas
# valor de retorno -> salida

# sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    resultado = x + y
    print(f"El resultado es: {resultado}")
    
# suma1()

# Con parámetros y sin valor de retorno
def suma2(x : float, y : float) -> None:
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")
    
# suma2(5, 10)
#a = float(input("Ingresa el valor de x: "))
#b = float(input("Ingresa el valor de y: "))
#suma2(a, b)

# Con parámetros y con valor de retorno
def suma3(x : float, y : float) -> float:
    resultado = x + y
    return resultado

res = suma3(5, 10)
print(res)
res = suma3(1,2) * 10
print(res)


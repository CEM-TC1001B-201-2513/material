precio = 0
cuenta = 0
while precio >= 0:
    cuenta += precio
    precio = float(input("Ingresa el precio del producto: "))
print(f"El total de la cuenta es: ${cuenta:,.2f}")
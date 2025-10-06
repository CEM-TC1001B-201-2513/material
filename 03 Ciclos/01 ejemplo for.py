# range(final) -> Una secuencia de números enteros
# que empieza en 0, avanza de 1 en 1 y
# termina antes de final
for i in range(5):
    print(f"El valor de i es: {i}")

print("-"*30)

# range(inicio, final) -> Una secuencia de números enteros
# que empieza en inicio, avanza de 1 en 1 y
# termina antes de final
for i in range(5, 10):
    print(f"El valor de i es: {i}")

print("-"*30)

# range(inicio, final, paso) -> Una secuencia de números enteros
# que empieza en inicio, avanza de paso en paso y
# termina antes de final
for i in range(10, 5, -1):
    print(f"El valor de i es: {i}")
    
print("-"*30)

texto = "hola mundo"
for i in texto:
    print(f"El valor de i es: {i}")

print("-"*30)

lista = [1,2,True,"hola",[7,4],False]
for i in lista:
    print(f"El valor de i es: {i}")

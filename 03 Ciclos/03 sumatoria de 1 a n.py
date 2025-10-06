# Sumatoria de 1 hasta n
# Ingresar un número entero n
# Calcular la sumatoria de 1 hasta n
# Ejemplo n = 5
# 1+2+3+4+5=15
n = int(input("Ingrese el valor de n: "))
sumatoria = 0
for i in range(1,n+1):
    sumatoria = sumatoria + i
print(f"Sumatoria de 1 hasta {n} es: {sumatoria}")



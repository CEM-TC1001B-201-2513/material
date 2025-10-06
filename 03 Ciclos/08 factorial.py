# Factorial
# Ingresen un número entero n
# Ejemplo n = 5
# 5! -> 5*4*3*2*1 -> 120
n = int(input("Ingrese el valor de n: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"{n}! = {factorial}")


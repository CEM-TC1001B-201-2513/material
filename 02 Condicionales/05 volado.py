# Simular un volado
# Preguntar al usuario si la moneda caerá en Águila o Sol
# Indicar al usuario si ganó o perdió
import random

# 1 -> Águila, 2 -> Sol
moneda = random.randint(1,2)

# .strip() -> Elimina los espacios del inicio y del final
# .lower() -> Convierte todo a minúsculas
# adivina = input("Adivina águila o sol: ").strip().lower()
#if adivina == "águila" or adivina == "aguila":

adivina = int(input("Escribe 1 para Águila o 2 para Sol: "))

if adivina == moneda:
    print("¡Felicidades, atinaste!")
else:
    print("No has atinado, suerte para la próxima.")


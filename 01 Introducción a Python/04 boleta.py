mat1 = float(input("Ingresa calificación de materia 1: "))
mat2 = float(input("Ingresa calificación de materia 2: "))
mat3 = float(input("Ingresa calificación de materia 3: "))
mat4 = float(input("Ingresa calificación de materia 4: "))
mat5 = float(input("Ingresa calificación de materia 5: "))
mat6 = float(input("Ingresa calificación de materia 6: "))
mat7 = float(input("Ingresa calificación de materia 7: "))
promedio = (mat1 + mat2 + mat3 + mat4 + mat5 + mat6 + mat7) / 7
# f-strings
print(f"El promedio de tu semestre es: {promedio}")
# : -> aplicar un formato especial
# , -> separador de miles
# .n -> redondear a n decimales
# f -> mostrar el resultado como float
print(f"El promedio de tu semestre es: {promedio:,.2f}")
# Maneras antiguas (no usar)
print("El promedio de tu semestre es:", promedio)
print("El promedio de tu semestre es: " + str(promedio))
print("El promedio de tu semestre es: {0:,.2f}".format(promedio))
número_materias = int(input("¿Cuántas materias cursaste?: "))
promedio = 0
for i in range(1, número_materias+1):
    calificación = float(input(f"Calificación de materia {i}: "))
    # promedio = promedio + calificación
    promedio += calificación
# promedio = promedio / número_materias
promedio /= número_materias
print(f"Tu promedio es: {promedio}")
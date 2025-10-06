alumnos = ["Héctor", "Mateo", "Romina", "Obama", "Bolillo"]
nombre = input("Ingresa el nombre a buscar: ")
condición = False
for alumno in alumnos:
    if nombre == alumno:
        condición = True
if condición == True:
    print("El alumno está en la lista.")
else:
    print("El nombre no está en la lista")
# --------------------------------------------

# break -> detiene por completo el ciclo
# continue -> detiene la repetición actual y pasa a la
# siguiente
for alumno in alumnos:
    if nombre == alumno:
        print("El alumno está en la lista.")
        break
else: # Si no se ejecutó un break, entonces haz:
    print("El nombre no está en la lista")




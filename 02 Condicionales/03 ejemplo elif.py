# Recibir como entrada una calificación
# Más de 90 -> A
# Más de 80 hasta 90 -> B
# Más de 70 hasta 80 -> C
# Más de 60 hasta 70 -> D
# De 60 hacia abajo -> F

calificación = float(input("Ingresa tu calificación: "))
if calificación > 90:
    print("A")
else:
    if calificación > 80:
        print("B")
    else:
        if calificación > 70:
            print("C")
        else:
            if calificación > 60:
                print("D")
            else:
                print("F")
                
# ----------------------------------

if calificación > 90:
    print("A")
elif calificación > 80:
    print("B")
elif calificación > 70:
    print("C")
elif calificación > 60:
    print("D")
else:
    print("F")
        
    
    
    
    
import pandas as pd
import streamlit as st
from datetime import date

st.header("Instrumento de medición")

form = st.form("formulario")

# Evitar lo más posible
nombre = form.text_input("Nombre")

edad = form.number_input("Edad",
                         min_value=0,
                         max_value=120,
                         value=18)

calificación = form.slider("Calificación",
                           min_value=0,
                           max_value=100,
                           value=50,
                           step=10)

colores = [
    "Azul",
    "Amarillo",
    "Verde",
    "Rojo"
    ]
#color = form.radio("Color favorito", colores)
color = form.radio("Color favorito",
                   colores,
                   horizontal=True, # Aparecen uno junto al otro
                   index=0) # Posición seleccionada por default

estados_mexico = [
    "Aguascalientes",
    "Baja California",
    "Baja California Sur",
    "Campeche",
    "Chiapas",
    "Chihuahua",
    "Coahuila",
    "Colima",
    "Durango",
    "Guanajuato",
    "Guerrero",
    "Hidalgo",
    "Jalisco",
    "México",
    "Michoacán",
    "Morelos",
    "Nayarit",
    "Nuevo León",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Quintana Roo",
    "San Luis Potosí",
    "Sinaloa",
    "Sonora",
    "Tabasco",
    "Tamaulipas",
    "Tlaxcala",
    "Veracruz",
    "Yucatán",
    "Zacatecas",
    "Ciudad de México"
]

estado = form.selectbox("Estado de la república",
                        estados_mexico,
                        index=0)

form.write("Idiomas que manejas")

español = form.checkbox("Español")
inglés = form.checkbox("Inglés")
francés = form.checkbox("Frances")
chino_simplificado = form.checkbox("Chino simplificado")

notificaciones = form.toggle("Recibir notificaciones")

fecha = form.date_input("Fecha de nacimiento",
                        min_value=date(1990, 1, 1),
                        max_value=date(2030, 12, 31))

guardar = form.form_submit_button("Guardar")

if guardar:
    df = pd.read_csv("datos/resultados.csv")
    # "Nombre de la columna en el csv": nombre_variable
    nueva_fila = pd.DataFrame([{
        "Nombre": nombre,
        "Edad": edad,
        "Calificación": calificación,
        "Color favorito": color,
        "Estado de la república": estado,
        "Español": español,
        "Inglés": inglés,
        "Francés": francés,
        "Chino simplificado": chino_simplificado,
        "Recibir notificaciones": notificaciones,
        "Fecha de nacimiento": fecha
        }])
    df = pd.concat([df, nueva_fila], ignore_index=True)
    df.to_csv("datos/resultados.csv", index=False)
    st.success("Resultados guardados")








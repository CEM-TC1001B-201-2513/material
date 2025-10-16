import pandas as pd
import streamlit as st

@st.cache_data
def cargar_datos_csv(nombre_archivo):
    df = pd.read_csv(nombre_archivo)
    return df

@st.cache_data
def cargar_datos_excel(nombre_archivo):
    df = pd.read_excel(nombre_archivo)
    return df

evaluadores_df = cargar_datos_csv("datos/base_evaluadores_2024.csv")

st.header("Estudios consultados")

# Si su archivo tiene pocas filas
st.dataframe(evaluadores_df)
st.caption("Tomado de https://datos.gob.mx/dataset/registro_evaluadores_acreditados_rcea")
st.write("Una descripción de los datos y por qué son relevantes para la solución de la problemática")

# Si su archivo tiene muchas filas (miles)
st.dataframe(evaluadores_df.head(10))
st.caption("Tomado de https://datos.gob.mx/dataset/registro_evaluadores_acreditados_rcea")
st.write("Una descripción de los datos y por qué son relevantes para la solución de la problemática")

import pandas as pd
import streamlit as st

df = pd.read_csv("datos/resultados.csv")

st.header("Resultados del instrumento")

st.dataframe(df)

st.write("Explicación sobre los datos recopilados")
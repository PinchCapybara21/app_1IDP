import streamlit as st
import pandas as pd

import plotly.express as px
import geopandas as gpd
import numpy as np

data = pd.read_csv('final.csv')
st.title("Indicadores Económicos de Colombia")
st.markdown('Acá puedes ver la evolución del PIB, desempleo e inflación en Colombia a del 2010 al 2024.') 

color_2 = st.selectbox('Selecciona el color de la gráfica:', ["blue", "red", "gray"])

mostrar_todas = st.checkbox('Mostrar todas las variables')

if mostrar_todas:
    fig = px.line(data, x="anio", y = ["pib", "desempleo", "inflacion"], 
        title="Evolución de las variables en el tiempo",
        color_discrete_map = {"pib": "blue", "desempleo": "red", "inflacion": "gray"})
else: 
    opcion = st.selectbox("Selecciona la variable a graficar:", ["pib", "desempleo", "inflacion"]) 
    fig = px.line(data, x="anio", y=opcion, title=f"Evolución de {opcion} en el tiempo") 
    fig.update_traces(line=dict(color=color_2))
    fig.update_traces(
    hovertemplate="anio: %{x}<br>Valor: %{y:.2f}")

fig.update_layout(
    xaxis_title="Tiempo (años)",
   ## yaxis_title="Valor (%)",
    font=dict(size=14),
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1a", step="year", stepmode="backward"),
                dict(count=5, label="5a", step="year", stepmode="backward"),
                dict(step="all", label="Todo")
            ])
        ),
        rangeslider=dict(visible=True),
        type="date"
    )
)
fig.uptaded_layout(yaxis = dict(dtick=2))
st.plotly_chart(fig, use_container_width=True)



st.markdown('Hecho en Colombia por: Juan, Sebas y Oscar')

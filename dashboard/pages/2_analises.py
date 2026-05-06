import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.api_client import get_artilheiros, get_equipes

st.title("Análises")

# --- Filtro de temporada ---
temporada = st.slider("Temporada:", min_value=1950, max_value=2024, value=2023)

st.divider()

# --- Artilheiros ---
st.subheader("Top 10 Pilotos por Pontos")

try:
    artilheiros = get_artilheiros(temporada=temporada)
    df_art = pd.DataFrame(artilheiros)

    df_art["piloto"] = df_art["nome"] + " " + df_art["sobrenome"]

    fig = px.bar(
        df_art,
        x="total_pontos",  
        y="piloto",        
        orientation="h",
        title=f"Top 10 artilheiros — {temporada}",
        color="total_pontos",
        color_continuous_scale="reds"
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao buscar artilheiros: {e}")

st.divider()

# --- Equipes ---
st.subheader("Evolução de Pontos por Temporada")

try:
    equipes = get_equipes()  
    df_eq = pd.DataFrame(equipes)

    fig2 = px.line(
        df_eq,
        x="temporada",
        y="total_pontos",
        title="Pontuação total por temporada (histórico)",
        markers=True
    )
    st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao buscar equipes: {e}")

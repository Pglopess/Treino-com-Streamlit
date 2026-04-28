import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.api_client import get_pilotos

st.title("👥 Visão Geral — Pilotos")

# --- Busca os dados ---
try:
    pilotos = get_pilotos()
    df = pd.DataFrame(pilotos)
except Exception as e:
    st.error(f"Erro ao conectar na API: {e}")
    st.stop()

# --- Métricas no topo ---
col1, col2 = st.columns(2)
col1.metric("Total de pilotos", len(df))
col2.metric("Nacionalidades distintas", df["nacionalidade"].nunique())

st.divider()

# --- Filtro por nacionalidade ---
nacionalidades = sorted(df["nacionalidade"].dropna().unique().tolist())
selecionada = st.selectbox("Filtrar por nacionalidade:", ["Todas"] + nacionalidades)

if selecionada != "Todas":
    df = df[df["nacionalidade"] == selecionada]

st.subheader(f"Pilotos ({len(df)} encontrados)")
st.dataframe(df, use_container_width=True)
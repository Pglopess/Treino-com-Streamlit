import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.api_client import get_pilotos, get_artilheiros

st.title("🔍 Detalhes do Piloto")

# --- Busca lista de pilotos para o selectbox ---
try:
    pilotos = get_pilotos()
    df = pd.DataFrame(pilotos)
    df["nome_completo"] = df["nome"] + " " + df["sobrenome"]
except Exception as e:
    st.error(f"Erro ao carregar pilotos: {e}")
    st.stop()

# --- Seleção do piloto ---
piloto_selecionado = st.selectbox("Selecione um piloto:", df["nome_completo"].tolist())

piloto = df[df["nome_completo"] == piloto_selecionado].iloc[0]

# --- Card com informações ---
col1, col2, col3 = st.columns(3)
col1.metric("Nome completo", piloto["nome_completo"])
col2.metric("Nacionalidade", piloto["nacionalidade"])
col3.metric("Data de nascimento", piloto["nascimento"])

st.divider()

# --- Aparições no top 10 histórico ---
st.subheader("Aparições no Top 10 histórico")

try:
    artilheiros = get_artilheiros()  # sem filtro = histórico completo
    df_art = pd.DataFrame(artilheiros)
    df_art["nome_completo"] = df_art["nome"] + " " + df_art["sobrenome"]

    aparicoes = df_art[df_art["nome_completo"] == piloto_selecionado]

    if aparicoes.empty:
        st.info("Este piloto não aparece no top 10 histórico.")
    else:
        st.metric("Total de pontos (carreira)", aparicoes["total_pontos"].sum())
        st.dataframe(aparicoes[["nome_completo", "total_pontos"]], use_container_width=True)

except Exception as e:
    st.error(f"Erro ao buscar histórico: {e}")
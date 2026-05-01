import streamlit as st
import pandas as pd
import sys
import os

# Ajuste do path para importar o api_client
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.api_client import get_pilotos

st.title("Pilotos por Nacionalidade")

# Lista de nacionalidades
nacionalidades = [
    "British", "German", "Brazilian", "Spanish",
    "French", "Italian", "Dutch", "Finnish"
]

# Selectbox
nacionalidade = st.selectbox("Selecione a nacionalidade", nacionalidades)

# Chamada da API com tratamento de erro
try:
    pilotos = get_pilotos(nacionalidade=nacionalidade)
    df = pd.DataFrame(pilotos)
except Exception as e:
    st.error(f"Erro ao conectar na API: {e}")
    st.stop()

# Métrica
st.metric("Quantidade de pilotos", len(df))

# Tabela
if df.empty:
    st.warning("Nenhum piloto encontrado.")
else:
    st.dataframe(df)
import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("API_URL", "http://localhost:8000")

@st.cache_data(ttl=60)
def get_pilotos(nacionalidade: str = None):
    params = {}
    if nacionalidade:
        params["nacionalidade"] = nacionalidade
    resposta = requests.get(f"{BASE_URL}/pilotos", params=params)
    resposta.raise_for_status()
    return resposta.json()

@st.cache_data(ttl=60)
def get_artilheiros(temporada: int = None):
    params = {}
    if temporada:
        params["temporada"] = temporada
    resposta = requests.get(f"{BASE_URL}/analises/artilheiros", params=params)
    resposta.raise_for_status()
    return resposta.json()

@st.cache_data(ttl=60)
def get_equipes(temporada: int = None):
    params = {}
    if temporada:
        params["temporada"] = temporada
    resposta = requests.get(f"{BASE_URL}/analises/equipes", params=params)
    resposta.raise_for_status()
    return resposta.json()
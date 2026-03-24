import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Conexão
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("👤 Cadastro de Clientes")

with st.form("form_cliente"):
    nome = st.text_input("Nome do Cliente")
    email = st.text_input("Email")
    submit = st.form_submit_button("Cadastrar")

    if submit:
        supabase.table("clientes").insert({"nome": nome, "email": email}).execute()
        st.success("Cliente cadastrado!")

# Relatório simples
st.subheader("Clientes Cadastrados")
response = supabase.table("clientes").select("*").execute()
df = pd.DataFrame(response.data)
st.dataframe(df)

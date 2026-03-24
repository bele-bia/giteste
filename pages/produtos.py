import streamlit as st
from supabase import create_client
import pandas as pd

supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

st.title("📦 Cadastro de Produtos")

with st.form("form_prod"):
    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço", min_value=0.0)
    submit = st.form_submit_button("Salvar Produto")

    if submit:
        supabase.table("produtos").insert({"nome": nome, "preco": preco}).execute()
        st.success("Produto salvo!")

# Listagem
response = supabase.table("produtos").select("*").execute()
st.dataframe(pd.DataFrame(response.data))

import streamlit as st
from supabase import create_client
import pandas as pd
import plotly.express as px

supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

st.title("📊 Relatórios Financeiros")

# Buscar dados
prod_res = supabase.table("produtos").select("*").execute()
df = pd.DataFrame(prod_res.data)

if not df.empty:
    st.subheader("Produtos por Preço")
    fig = px.bar(df, x="nome", y="preco", title="Preço dos Produtos")
    st.plotly_chart(fig)
else:
    st.warning("Nenhum dado encontrado.")

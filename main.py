import streamlit as st

st.set_page_config(page_title="Sistema Comercial", page_icon="🏢")

st.title("🏢 Painel Comercial Principal")
st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("Clientes", "150", "+12%")
col2.metric("Produtos", "45", "0")
col3.metric("Vendas (Mês)", "R$ 15.000", "+5%")

st.info("Utilize o menu lateral para navegar entre Cadastro e Relatórios.")

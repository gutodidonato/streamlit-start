import streamlit as st
from components.utils import format_number, df_rec_diario

def display(df):
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        # Exibir Receita Diária como uma label
        dia_especifico = st.selectbox('Escolha um Dia', df_rec_diario['Data da Compra'].dt.strftime('%Y-%m-%d').unique())
        receita_dia = df_rec_diario[df_rec_diario['Data da Compra'].dt.strftime('%Y-%m-%d') == dia_especifico]['Preço'].sum()
        
        st.markdown(f"### Receita do Dia: {format_number(receita_dia, prefix='R$')}")
        

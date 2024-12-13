import streamlit as st
from components.utils import df_vendedores_mais_dinheiro, df_vendedores_mais_vendas

def display(df):
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Vendedor de maior receita:', df_vendedores_mais_dinheiro['Vendedor'].iloc[0])
        st.write(df_vendedores_mais_dinheiro)
    with coluna2:
        st.metric('Vendedor de mais produtos:', df_vendedores_mais_vendas['Vendedor'].iloc[0])
        st.write(df_vendedores_mais_vendas)
import streamlit as st
from components.utils import format_number, df_rec_mensal
from components.charts import grafico_rec_mensal

def display(df):
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Venda neste mês:', format_number(df_rec_mensal['Preço'].iloc[-1], prefix='R$'))
        st.write(df_rec_mensal.set_index('Mes'))
    with coluna2:
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
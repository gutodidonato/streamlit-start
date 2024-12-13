import streamlit as st
from components.utils import format_number, df_rec_estado
from components.charts import create_pydeck_map, grafico_barra_estado, grafico_rec_categoria

def display(df):
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), prefix='R$'))
        st.plotly_chart(grafico_barra_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.write(df_rec_estado)
        grafico_map_estado = create_pydeck_map(df_rec_estado)
        st.pydeck_chart(grafico_map_estado)
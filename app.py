import streamlit as st
from components.dataset import df 
from components.utils import format_number, df_rec_estado, df_rec_diario, df_rec_mensal, df_vendedores_mais_vendas, df_vendedores_mais_dinheiro
from components.charts import grafico_rec_mensal, grafico_barra_estado, grafico_rec_categoria

import components.abas.aba1
import components.abas.aba2
import components.abas.aba3
import components.abas.aba4
import components.abas.aba5

st.set_page_config(layout='wide')

st.title("Dashboard de Vendas: ")
st.sidebar.title('Filtro Vendedores')
filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique()
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

aba1, aba2, aba3, aba4, aba5 = st.tabs(['Dataset', 'Receita Total', 'Receita Mensal', 'Receita Diária', 'Vendedores'])

with aba1:
    components.abas.aba1.display(df)
    
with aba2:
    components.abas.aba2.display(df)
          
with aba3:
    components.abas.aba3.display(df)
        
with aba4:
    components.abas.aba4.display(df)

with aba5:
    components.abas.aba5.display(df)
    
        
        


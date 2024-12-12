import streamlit as st
from components.dataset import df 
from components.utils import format_number, df_rec_estado, df_rec_diario, df_rec_mensal, df_vendedores_mais_vendas, df_vendedores_mais_dinheiro
from components.charts import grafico_rec_mensal, grafico_barra_estado, grafico_rec_categoria
import components.windows.aba1
import components.windows.aba2

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
    components.windows.aba1.display(df)
    
with aba2:
    components.windows.aba2.display(df)
        
        
        
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Venda neste mês:', format_number(df_rec_mensal['Preço'].iloc[-1], prefix='R$'))
        st.write(df_rec_mensal.set_index('Mes'))
    with coluna2:
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        
with aba4:
    pass

with aba5:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Vendedor de maior receita:', df_vendedores_mais_dinheiro['Vendedor'].iloc[0])
        st.write(df_vendedores_mais_dinheiro)
    with coluna2:
        st.metric('Vendedor de maior receita:', df_vendedores_mais_vendas['Vendedor'].iloc[0])
        st.write(df_vendedores_mais_vendas)
    
        
        


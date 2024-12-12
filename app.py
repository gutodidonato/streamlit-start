import streamlit as st
from dataset import df 
from utils import format_number, df_rec_estado, df_rec_diario, df_rec_mensal, df_vendedores_mais_vendas, df_vendedores_mais_dinheiro
from grafico import grafico_map_estado, grafico_rec_mensal, grafico_barra_estado, grafico_rec_categoria

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
    st.write(df)
    
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), prefix='R$'))
        st.plotly_chart(grafico_barra_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.write(df_rec_estado)
        
        largura = st.slider("Largura do gráfico", 400, 800, 400)
        altura = st.slider("Altura do gráfico", 400, 600, 400)
        
        grafico_map_estado.update_layout(width=largura, height=altura)
        st.plotly_chart(grafico_map_estado, use_container_width=False)
        
        
        
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
    
        
        


import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso

st.title('Dataframe')
with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as Colunas',
        list(df.columns),
        list(df.columns)
    )
st.sidebar.title('Filtros')
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Selecione as Categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
    )
with st.sidebar.expander('Preço do Produto'):
    precos = st.slider(
        'Selecione o Preço',
        df['Preço'].min(), df['Preço'].max(),
        (df['Preço'].min(), df['Preço'].max())
    )
with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input(
        'Selecione a Data',
        (df['Data da Compra'].min(),
         df['Data da Compra'].max())
    )
    
query = '''
            `Categoria do Produto` in @categorias and \
            @precos[0] <= Preço <= @precos[1] and \
            @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]
st.dataframe(filtro_dados)
st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas')
st.markdown('Escreva o nome do arquivo ')
coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input('Nome do Arquivo', label_visibility='collapsed')
    if nome_arquivo == '':
        nome_arquivo = 'data'
    nome_arquivo += '.csv'
with coluna2:
    st.download_button(
        label="Download CSV",
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso
    )
    
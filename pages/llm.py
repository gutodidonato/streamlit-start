import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks import StreamlitCallbackHandler

# Configurar a chave da API OpenAI
import os
os.environ["OPENAI_API_KEY"] = "---"

# Streamlit app
st.title("DataChat: Your AI Lecture Assistant")

# Carregador de arquivos para CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Ler o arquivo CSV em um DataFrame pandas
    df = pd.read_csv(uploaded_file)
    st.write("Pré-visualização dos Dados:")
    st.dataframe(df.head())

    # Criar uma instância do modelo de linguagem OpenAI
    llm = OpenAI(temperature=0)

    # Criar um agente de DataFrame pandas
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)

    # Criar um template de prompt para análise de dados
    analysis_template = PromptTemplate(
        input_variables=["question", "df_info"],
        template="""
        Você é um assistente de IA que ajuda a analisar dados.
        Dadas as seguintes informações sobre um DataFrame:
        
        {df_info}
        
        Por favor, responda à seguinte pergunta:
        {question}
        
        Forneça uma resposta clara e concisa com base nas informações fornecidas.
        """
    )

    # Criar uma LLMChain para análise de dados
    analysis_chain = LLMChain(llm=llm, prompt=analysis_template)

    # Função para obter informações do DataFrame
    def get_df_info(df):
        return f"""
        Colunas: {', '.join(df.columns)}
        Tipos de dados: {df.dtypes.to_dict()}
        Estatísticas resumidas:
        {df.describe().to_string()}
        """

    # Interface de chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("O que você gostaria de saber sobre os dados?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            st_callback = StreamlitCallbackHandler(st.container())
            df_info = get_df_info(df)
            # Usar tanto o agente quanto a cadeia para flexibilidade
            try:
                response = agent.run(prompt, callbacks=[st_callback])
            except Exception:
                response = analysis_chain.run(question=prompt, df_info=df_info, callbacks=[st_callback])
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

else:
    st.write("Por favor, carregue um arquivo CSV para começar.")

# Adicionar uma seção para gerar palestras
st.header("Gerar uma Palestra")
lecture_topic = st.text_input("Digite um tópico para a palestra com base nos dados:")
if lecture_topic and st.button("Gerar Palestra"):
    with st.spinner("Gerando palestra..."):
        df_info = get_df_info(df)
        lecture_prompt = f"""
        Gere uma palestra curta sobre o tópico '{lecture_topic}' com base nas seguintes informações sobre o dataframe:
        
        {df_info}
        
        Inclua pontos-chave e insights dos dados em sua palestra.
        """
        try:
            lecture = agent.run(lecture_prompt)
        except Exception:
            lecture = llm(lecture_prompt)
        st.subheader(f"Palestra sobre {lecture_topic}")
        st.write(lecture)

# Instruções para os usuários
st.sidebar.header("Como usar o DataChat")
st.sidebar.markdown("""
1. Carregue um arquivo CSV contendo seus dados.
2. Faça perguntas sobre os dados na interface de chat.
3. Gere palestras sobre tópicos específicos com base nos dados.
4. Explore insights e aprenda com seus dados!
""")
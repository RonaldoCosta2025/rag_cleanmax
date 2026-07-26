# Importa o Streamlit para criar a interface web.
import streamlit as st

# Importa os caminhos centralizados do projeto.
from src.config import INDEX_FILE, CHUNKS_FILE


# Importa funções para carregar o banco vetorial.
from src.vectorstore.faiss_store import (
    carregar_indice,
    carregar_chunks
)


# Importa o agente RAG.
from src.rag.agent import AgenteRAG



# Define o título da aplicação.
st.title("Assistente Corporativo CleanMax")


indice = carregar_indice(
    INDEX_FILE
)

chunks = carregar_chunks(
    CHUNKS_FILE
)



# Cria o agente.
agente = AgenteRAG(
    indice,
    chunks
)



# Campo para o usuário digitar a pergunta.
pergunta = st.text_input(
    "Digite sua pergunta:"
)



# Botão para enviar.
if st.button("Perguntar"):

    # Verifica se existe uma pergunta.
    if pergunta:

        # Executa o agente.
        resultado = agente.perguntar(
            pergunta
        )


        # Mostra a resposta.
        # st.subheader("Resposta")

        # st.write(
        #     resultado["resposta"]
        # )


        # Mostra as fontes.
        st.subheader("Fontes utilizadas")

        for fonte in resultado["fontes"]:

            st.write(
                f"- {fonte}"
            )


        # Mostra quantidade de chunks.
        # st.subheader("Informações técnicas")

        # st.write(
        #     f"Chunks utilizados: {resultado['quantidade_chunks']}"
        # )

        # Exibe o título da resposta.
        st.subheader("Resposta")

        # Verifica se a resposta indica que a cota da API foi excedida.
        if "limite de utilização da API Gemini" in resultado["resposta"]:

            # Exibe um aviso em destaque.
            st.warning(resultado["resposta"])

        # # Caso contrário, exibe normalmente.
        # else:

        #     st.write(resultado["resposta"])
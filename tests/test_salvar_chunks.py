# Importa as funções do banco vetorial.
from src.vectorstore.faiss_store import (
    carregar_indice,
    carregar_chunks,
    buscar
)


# Importa a função que gera embeddings.
from src.embeddings.embedding_generator import gerar_embedding


# Importa o pipeline RAG.
from src.rag.pipeline import responder


# Caminhos dos arquivos salvos.
caminho_indice = "vectorstore/index.faiss"
caminho_chunks = "vectorstore/chunks.pkl"


# Carrega o índice FAISS.
indice = carregar_indice(caminho_indice)


# Carrega os chunks.
chunks = carregar_chunks(caminho_chunks)


# Pergunta do usuário.
pergunta = "Quais são os valores da empresa?"


# Gera o vetor da pergunta.
embedding_consulta = gerar_embedding(pergunta)


# Busca os chunks mais relevantes.
distancias, indices = buscar(
    indice,
    embedding_consulta,
    quantidade=3
)


# Lista que armazenará os chunks encontrados.
chunks_encontrados = []


# Recupera os objetos Chunk.
for indice_chunk in indices[0]:

    chunk = chunks[indice_chunk]

    chunks_encontrados.append(chunk)


# Envia pergunta + chunks para o RAG.
resposta = responder(
    pergunta,
    chunks_encontrados
)


# Exibe a resposta final.
print(resposta)
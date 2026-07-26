# Importa as funções do banco vetorial.
from src.vectorstore.faiss_store import (
    carregar_indice,
    carregar_chunks,
    buscar
)


# Importa a função que gera embeddings.
from src.embeddings.embedding_generator import gerar_embedding


# Caminhos dos arquivos salvos.
caminho_indice = "vectorstore/index.faiss"
caminho_chunks = "vectorstore/chunks.pkl"


# Carrega o índice FAISS.
indice = carregar_indice(caminho_indice)


# Carrega os chunks originais.
chunks = carregar_chunks(caminho_chunks)


# Pergunta para testar.
pergunta = "Qual o estoque do Detergente Neutro?"


# Cria o vetor da pergunta.
embedding_consulta = gerar_embedding(pergunta)


# Busca os 3 chunks mais próximos.
distancias, indices = buscar(
    indice,
    embedding_consulta,
    quantidade=5
)


# Percorre os resultados encontrados.
# Percorre simultaneamente as similaridades e os índices encontrados.
for similaridade, indice_chunk in zip(
    distancias[0],
    indices[0]
):

    # Ignora resultados pouco relevantes.
    if similaridade < 0.35:
        continue

    # Recupera o chunk correspondente.
    chunk = chunks[indice_chunk]

    # Adiciona o texto do chunk ao contexto.
    # contextos.append(chunk.texto)

    # Adiciona o nome do arquivo às fontes.
    # fontes.append(chunk.arquivo)

    # Recupera o chunk correspondente.
    chunk = chunks[indice_chunk]


    print("\n------------------------")
    print("CHUNK ENCONTRADO")

    # Mostra a origem do documento.
    # print("Arquivo:", chunk.metadata["arquivo"])

    print("Arquivo:", chunk.arquivo)

    print(chunk.texto)

    # Mostra a distância encontrada.
    # print("Similaridade:", distancia)

    # Mostra o conteúdo recuperado.
    # print(chunk.page_content)
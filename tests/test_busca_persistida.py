# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa a função que transforma a pergunta em um vetor.
from src.embeddings.embedding_generator import gerar_embedding

# Importa as funções que carregam o FAISS e os chunks salvos.
from src.vectorstore.faiss_store import carregar_indice, carregar_chunks, buscar


# Define o caminho do índice FAISS salvo.
caminho_indice = Path("vectorstore/index.faiss")

# Define o caminho dos chunks salvos.
caminho_chunks = Path("vectorstore/chunks.pkl")

# Carrega o índice FAISS para a memória.
indice = carregar_indice(caminho_indice)

# Carrega os chunks salvos para a memória.
chunks = carregar_chunks(caminho_chunks)

# Define a pergunta que queremos pesquisar.
pergunta = "O que é a CleanMax?"

# Transforma a pergunta em um vetor.
embedding_pergunta = gerar_embedding(pergunta)

# Procura os dois chunks mais próximos da pergunta.
distancias, indices = buscar(
    indice,
    embedding_pergunta,
    quantidade=2
)

# Percorre os resultados encontrados pelo FAISS.
for distancia, indice_chunk in zip(distancias[0], indices[0]):

    # Recupera o Chunk correspondente ao índice encontrado.
    chunk = chunks[indice_chunk]

    # Exibe uma identificação do resultado.
    print("\nCHUNK ENCONTRADO")

    # Exibe o arquivo de origem do chunk.
    print(f"Arquivo: {chunk.arquivo}")

    # Exibe a distância entre a pergunta e o chunk.
    print(f"Distância: {distancia}")

    # Exibe o texto do chunk.
    print(chunk.texto)
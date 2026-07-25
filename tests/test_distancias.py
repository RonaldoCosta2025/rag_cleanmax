# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa a função que transforma textos em embeddings.
from src.embeddings.embedding_generator import gerar_embedding

# Importa as funções que carregam o FAISS, os chunks e realizam a busca.
from src.vectorstore.faiss_store import carregar_indice, carregar_chunks, buscar


# Define o caminho do índice FAISS salvo.
caminho_indice = Path("vectorstore/index.faiss")

# Define o caminho dos chunks salvos.
caminho_chunks = Path("vectorstore/chunks.pkl")

# Carrega o índice FAISS para a memória.
indice = carregar_indice(caminho_indice)

# Carrega os chunks para a memória.
chunks = carregar_chunks(caminho_chunks)


# Cria uma lista com perguntas para testar a relevância.
perguntas = [
    "O que é a CleanMax?",
    "Qual é o salário do diretor da CleanMax?"
]


# Percorre cada pergunta da lista.
for pergunta in perguntas:

    # Transforma a pergunta em um vetor numérico.
    embedding_pergunta = gerar_embedding(pergunta)

    # Procura os dois chunks mais próximos da pergunta.
    distancias, indices = buscar(
        indice,
        embedding_pergunta,
        quantidade=2
    )

    # Mostra qual pergunta está sendo analisada.
    print(f"\nPERGUNTA: {pergunta}")

    # Percorre as distâncias e os índices encontrados.
    for distancia, indice_chunk in zip(distancias[0], indices[0]):

        # Recupera o chunk correspondente ao índice.
        chunk = chunks[indice_chunk]

        # Mostra a distância encontrada pelo FAISS.
        print(f"Distância: {distancia}")

        # Mostra qual arquivo contém o chunk.
        print(f"Arquivo: {chunk.arquivo}")

        # Mostra o início do texto para identificarmos o resultado.
        print(f"Texto: {chunk.texto[:150]}...")
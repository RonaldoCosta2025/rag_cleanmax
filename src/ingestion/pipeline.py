# Importa Path para trabalhar com caminhos de arquivos e pastas.
from pathlib import Path

# Importa a função que carrega automaticamente todos os documentos.
from src.ingestion.loader import carregar_documentos

# Importa a função responsável por dividir os documentos em chunks.
from src.ingestion.chunker import criar_chunks

# Importa a função que gera os embeddings.
from src.embeddings.embedding_generator import gerar_embeddings

# Importa as funções responsáveis por criar e salvar o índice FAISS.
from src.vectorstore.faiss_store import (
    criar_indice,
    salvar_indice,
    salvar_chunks,
)

# Importa os caminhos centralizados do projeto.
from src.config import (
    VECTORSTORE_DIR,
    INDEX_FILE,
    CHUNKS_FILE,
)

# Define a função principal da ingestão.
def ingestir_documentos(pasta_documentos: Path):

    # Mostra que a ingestão foi iniciada.
    print("Carregando documentos...")

    # Carrega todos os documentos encontrados na pasta.
    documentos = carregar_documentos(pasta_documentos)

    # Mostra quantos documentos foram encontrados.
    print(f"Documentos encontrados: {len(documentos)}")

    # Mostra que o processo de chunking começou.
    print("\nCriando chunks...")

    # Cria os chunks de todos os documentos.
    chunks = criar_chunks(documentos)

    # Mostra quantos chunks foram gerados.
    print(f"Chunks criados: {len(chunks)}")

    # Cria uma lista contendo apenas o texto de cada chunk.
    textos = [
        chunk.texto
        for chunk in chunks
    ]

    # Mostra que os embeddings serão gerados.
    print("\nGerando embeddings...")

    # Gera um embedding para cada chunk.
    embeddings = gerar_embeddings(textos)

    # Mostra que o índice FAISS será criado.
    print("\nCriando índice FAISS...")

    # Cria o índice vetorial.
    indice = criar_indice(embeddings)

    # Garante que a pasta do banco vetorial exista.
    VECTORSTORE_DIR.mkdir(exist_ok=True)

    # Salva o índice FAISS.
    salvar_indice(
        indice,
        INDEX_FILE
    )

    salvar_chunks(
        chunks,
        CHUNKS_FILE
    )

    # Mostra uma mensagem de sucesso.
    print("\nIngestão finalizada com sucesso!")

    # Retorna o índice e os chunks caso sejam necessários.
    return indice, chunks
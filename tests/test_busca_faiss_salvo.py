# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa a função que transforma uma pergunta em embedding.
from src.embeddings.embedding_generator import gerar_embedding

# Importa a função que carrega o índice FAISS salvo.
from src.vectorstore.faiss_store import carregar_indice, buscar

# Importa a função que carrega o documento PDF.
from src.ingestion.pdf_loader import carregar_pdf

# Importa a função que cria os chunks do documento.
from src.ingestion.chunker import criar_chunks


# Define o caminho do índice FAISS salvo anteriormente.
caminho_indice = Path("vectorstore/index.faiss")

# Carrega o índice FAISS para a memória.
indice = carregar_indice(caminho_indice)

# Define o caminho do PDF utilizado para criar os chunks.
arquivo = Path("docs/01_Apresentacao_Empresa.pdf")

# Carrega o documento PDF.
documento = carregar_pdf(arquivo)

# Recria os chunks do documento.
chunks = criar_chunks(documento)

# Define a pergunta que será pesquisada.
pergunta = "O que é a CleanMax?"

# Transforma a pergunta em um vetor.
embedding_pergunta = gerar_embedding(pergunta)

# Pesquisa no FAISS os dois chunks mais próximos da pergunta.
distancias, indices = buscar(
    indice,
    embedding_pergunta,
    quantidade=2
)

# Percorre os resultados encontrados pelo FAISS.
for distancia, indice_chunk in zip(distancias[0], indices[0]):

    # Recupera o chunk correspondente ao índice retornado pelo FAISS.
    chunk = chunks[indice_chunk]

    # Exibe uma identificação do resultado.
    print("\nCHUNK ENCONTRADO")

    # Exibe o arquivo de origem do chunk.
    print(f"Arquivo: {chunk.arquivo}")

    # Exibe a distância entre a pergunta e o chunk.
    print(f"Distância: {distancia}")

    # Exibe o conteúdo do chunk encontrado.
    print(chunk.texto)
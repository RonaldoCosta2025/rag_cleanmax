from pathlib import Path

from src.ingestion.pdf_loader import carregar_pdf
from src.ingestion.chunker import criar_chunks
from src.embeddings.embedding_generator import gerar_embeddings, gerar_embedding
from src.vectorstore.faiss_store import criar_indice, busca


arquivo = Path("docs/01_Apresentacao_Empresa.pdf")

documento = carregar_pdf(arquivo)

chunks = criar_chunks(documento)

textos = [chunk.texto for chunk in chunks]

embeddings = gerar_embeddings(textos)

indice = criar_indice(embeddings)


pergunta = "O que é a CleanMax?"

embedding_pergunta = gerar_embedding(pergunta)

distancias, indices = busca(
    indice,
    embedding_pergunta,
    quantidade=2
)


for distancia, indice_chunk in zip(distancias[0], indices[0]):

    chunk = chunks[indice_chunk]

    print("\nCHUNK ENCONTRADO")
    print(f"Arquivo: {chunk.arquivo}")
    print(f"Distância: {distancia}")
    print(chunk.texto)
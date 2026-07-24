from pathlib import Path

from src.ingestion.pdf_loader import carregar_pdf
from src.ingestion.chunker import criar_chunks
from src.embeddings.embedding_generator import gerar_embeddings
from src.vectorstore.faiss_store import criar_indice


arquivo = Path("docs/01_Apresentacao_Empresa.pdf")

documento = carregar_pdf(arquivo)

chunks = criar_chunks(documento)

textos = [chunk.texto for chunk in chunks]

embeddings = gerar_embeddings(textos)

indice = criar_indice(embeddings)

print(indice.ntotal)
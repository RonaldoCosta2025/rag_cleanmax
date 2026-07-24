from pathlib import Path

from src.ingestion.pdf_loader import carregar_pdf
from src.ingestion.text_splitter import dividir_texto
from src.embeddings.embedder import gerar_embeddings


arquivos = Path("docs").glob("*.pdf")


chunks = []


for arquivo in arquivos:

    documento = carregar_pdf(arquivo)

    documentos_chunks = dividir_texto(documento)

    chunks.extend(documentos_chunks)


print("Quantidade de chunks:", len(chunks))


textos = [
    chunk.texto
    for chunk in chunks
]


vetores = gerar_embeddings(textos)


print("\nQuantidade de vetores:", len(vetores))


print("\nTamanho do vetor:")
print(len(vetores[0]))


print("\nPrimeiro vetor:")
print(vetores[0][:10])


print("\nPrimeira origem:")
print(chunks[0].arquivo)
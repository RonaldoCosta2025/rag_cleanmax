from pathlib import Path

from src.ingestion.chunker import criar_chunks
from src.ingestion.pdf_loader import carregar_pdf


arquivo = Path("docs/01_Apresentacao_Empresa.pdf")

documento = carregar_pdf(arquivo)

chunks = criar_chunks(documento)

print(f"Arquivo: {documento.arquivo}")
print(f"Quantidade de chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks):

    print(f"Chunk {i+1}")
    print(chunk.arquivo)
    print(chunk.texto[:150])
    print("-" * 60)
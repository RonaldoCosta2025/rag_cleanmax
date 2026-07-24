from pathlib import Path
from pypdf import PdfReader

# importando os arquivos e seus metodos
from src.ingestion.pdf_loader import carregar_pdf
from src.ingestion.text_splitter import dividir_texto
from src.embeddings.embedding_generator import gerar_embeddings

arquivo = Path('docs/02_Catalogo_Produtos.pdf')

texto = carregar_pdf(arquivo)

chunks = dividir_texto(texto)

embeddings = gerar_embeddings(chunks)

print(f'Quantidade de chunks: {len(chunks)}')

print(f'Quantidade de embeddings: {len(embeddings)}')

print(f'\nPrimeiro chunk: \n{chunks[0][:200]}')

print(f'\nDimensão do primeiro embedding: {len(embeddings[0])}')
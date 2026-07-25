# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa a função que carrega o PDF.
from src.ingestion.pdf_loader import carregar_pdf

# Importa a função que cria os chunks.
from src.ingestion.chunker import criar_chunks

# Importa as funções que geram embeddings.
from src.embeddings.embedding_generator import gerar_embeddings

# Importa as funções responsáveis pelo FAISS e pelos chunks.
from src.vectorstore.faiss_store import criar_indice, salvar_indice, salvar_chunks


# Define o caminho do PDF utilizado no teste.
arquivo = Path("docs/01_Apresentacao_Empresa.pdf")

# Carrega o documento PDF.
documento = carregar_pdf(arquivo)

# Divide o documento em chunks.
chunks = criar_chunks(documento)

# Extrai o texto de cada chunk.
textos = [chunk.texto for chunk in chunks]

# Gera os embeddings dos textos.
embeddings = gerar_embeddings(textos)

# Cria o índice FAISS.
indice = criar_indice(embeddings)

# Define a pasta onde os dados serão armazenados.
pasta_vectorstore = Path("vectorstore")

# Cria a pasta caso ela ainda não exista.
pasta_vectorstore.mkdir(exist_ok=True)

# Define o caminho do índice FAISS.
caminho_indice = pasta_vectorstore / "index.faiss"

# Define o caminho onde os chunks serão armazenados.
caminho_chunks = pasta_vectorstore / "chunks.pkl"

# Salva o índice FAISS.
salvar_indice(indice, caminho_indice)

# Salva os chunks junto com seus metadados.
salvar_chunks(chunks, caminho_chunks)

# Mostra onde o índice foi salvo.
print(f"Índice salvo em: {caminho_indice}")

# Mostra onde os chunks foram salvos.
print(f"Chunks salvos em: {caminho_chunks}")

# Mostra a quantidade de chunks armazenados.
print(f"Quantidade de chunks: {len(chunks)}")
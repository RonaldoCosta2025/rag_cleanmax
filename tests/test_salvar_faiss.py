# Importa Path para trabalhar com caminhos de arquivos e pastas.
from pathlib import Path

# Importa a função responsável por carregar o PDF.
from src.ingestion.pdf_loader import carregar_pdf

# Importa a função responsável por criar os chunks.
from src.ingestion.chunker import criar_chunks

# Importa as funções responsáveis pelos embeddings.
from src.embeddings.embedding_generator import gerar_embeddings

# Importa as funções do nosso armazenamento FAISS.
from src.vectorstore.faiss_store import criar_indice, salvar_indice


# Define o caminho do PDF que será utilizado no teste.
arquivo = Path("docs/01_Apresentacao_Empresa.pdf")

# Carrega o documento PDF.
documento = carregar_pdf(arquivo)

# Divide o documento em chunks.
chunks = criar_chunks(documento)

# Extrai somente o texto de cada chunk.
textos = [chunk.texto for chunk in chunks]

# Gera um embedding para cada texto.
embeddings = gerar_embeddings(textos)

# Cria o índice FAISS utilizando os embeddings.
indice = criar_indice(embeddings)

# Define a pasta onde o índice será armazenado.
pasta_vectorstore = Path("vectorstore")

# Cria a pasta caso ela ainda não exista.
pasta_vectorstore.mkdir(exist_ok=True)

# Define o caminho completo do arquivo FAISS.
caminho_indice = pasta_vectorstore / "index.faiss"

# Salva o índice FAISS no disco.
salvar_indice(indice, caminho_indice)

# Mostra uma mensagem informando onde o índice foi salvo.
print(f"Índice salvo em: {caminho_indice}")

# Mostra quantos vetores foram armazenados no índice.
print(f"Quantidade de vetores: {indice.ntotal}")

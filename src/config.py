# Importa a classe Path para trabalhar com caminhos de arquivos e pastas.
from pathlib import Path


# Obtém a pasta raiz do projeto.
BASE_DIR = Path(__file__).resolve().parent.parent


# Define a pasta onde ficam os documentos.
DOCS_DIR = BASE_DIR / "docs"


# Define a pasta onde fica o banco vetorial.
VECTORSTORE_DIR = BASE_DIR / "vectorstore"


# Define o caminho do índice FAISS.
INDEX_FILE = VECTORSTORE_DIR / "index.faiss"


# Define o caminho do arquivo de chunks.
CHUNKS_FILE = VECTORSTORE_DIR / "chunks.pkl"
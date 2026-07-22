# Esse arquivo centralizará configurações

# IMPORTANDO A CLASSE PATH, VAI TRABALHAR COM CAMINHOS DE ARQUIVOS
from pathlib import Path

# PASTA RAIZ DO PROJETO
BASE_DIR = Path(__file__).resolve().parent

# PASTA QUE CONTÉM OS DOCUMENTOS
DOCS_DIR = BASE_DIR / "docs"

# PASTA ONDE FICARÁ O BANCO VETORIAL
VECTORSTORE_DIE = BASE_DIR / "vectorstore"


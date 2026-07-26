# Importa a função que carrega todos os documentos.
from src.ingestion.loader import carregar_documentos

# Importa o caminho da pasta de documentos.
from src.config import DOCS_DIR

# Define a pasta de documentos.
pasta_docs = DOCS_DIR

# Carrega todos os documentos encontrados.
documentos = carregar_documentos(pasta_docs)

# Mostra a quantidade de documentos carregados.
print("Quantidade de documentos:", len(documentos))

# Percorre todos os documentos encontrados.
for documento in documentos:

    # Mostra o nome do arquivo.
    print(f"\nArquivo: {documento.arquivo}")

    # Mostra a quantidade de caracteres.
    print("Caracteres:", len(documento.texto))
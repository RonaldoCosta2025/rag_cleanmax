# Importa Path para trabalhar com o caminho da pasta.
from pathlib import Path

# Importa a função que carrega todos os documentos.
from src.ingestion.loader import carregar_documentos


# Define o caminho da pasta onde estão os documentos.
pasta_docs = Path("docs")

# Carrega todos os documentos suportados encontrados na pasta.
documentos = carregar_documentos(pasta_docs)


# Mostra a quantidade de documentos carregados.
print("Quantidade de documentos:", len(documentos))

# Percorre todos os documentos encontrados.
for documento in documentos:

    # Mostra o nome do arquivo.
    print(f"\nArquivo: {documento.arquivo}")

    # Mostra a quantidade de caracteres do documento.
    print("Caracteres:", len(documento.texto))
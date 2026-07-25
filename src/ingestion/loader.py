# Importa Path para trabalhar com pastas e caminhos de arquivos.
from pathlib import Path

# Importa o carregador que identifica automaticamente o tipo do documento.
from src.ingestion.document_loader import carregar_documento


# Define os formatos de arquivos que o projeto aceita neste momento.
EXTENSOES_SUPORTADAS = {
    ".pdf",
    ".csv",
}


# Define a função que carrega todos os documentos de uma pasta.
def carregar_documentos(pasta: Path):

    # Cria uma lista vazia para armazenar os documentos carregados.
    documentos = []

    # Percorre todos os arquivos encontrados dentro da pasta.
    for arquivo in pasta.iterdir():

        # Ignora qualquer item que não seja um arquivo.
        if not arquivo.is_file():
            continue

        # Obtém a extensão do arquivo em letras minúsculas.
        extensao = arquivo.suffix.lower()

        # Verifica se o formato do arquivo é suportado.
        if extensao not in EXTENSOES_SUPORTADAS:
            continue

        # Carrega o documento usando o loader geral.
        documento = carregar_documento(arquivo)

        # Adiciona o documento carregado à lista.
        documentos.append(documento)

    # Retorna todos os documentos encontrados.
    return documentos
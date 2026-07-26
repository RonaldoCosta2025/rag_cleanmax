# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa a biblioteca responsável por ler arquivos Word.
from docx import Document

# Importa a estrutura padrão usada pelo projeto.
from src.ingestion.document import Documento


# Define a função responsável por carregar arquivos DOCX.
def carregar_docx(caminho: Path):

    # Abre o arquivo Word.
    documento = Document(caminho)

    # Cria uma lista para armazenar os textos encontrados.
    textos = []

    # Percorre todos os parágrafos do documento.
    for paragrafo in documento.paragraphs:

        # Verifica se o parágrafo possui conteúdo.
        if paragrafo.text.strip():

            # Adiciona o texto na lista.
            textos.append(paragrafo.text)


    # Junta todos os parágrafos em um único texto.
    texto = "\n".join(textos)


    # Retorna o documento no padrão usado pelo projeto.
    return Documento(
        texto=texto,
        arquivo=caminho.name
    )
from pathlib import Path

import fitz

from src.ingestion.document import Documento


def carregar_pdf(caminho: Path):

    texto = ""

    with fitz.open(caminho) as pdf:

        for pagina in pdf:

            texto += pagina.get_text()


    documento = Documento(
        texto=texto,
        arquivo=caminho.name
    )


    return documento
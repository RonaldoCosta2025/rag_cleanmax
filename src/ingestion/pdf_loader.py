from pathlib import Path
from pypdf import PdfReader

# funcao para carregaro pdf
def carregar_pdf(caminho_pdf: Path) -> str:

    leitor = PdfReader(caminho_pdf)

    texto_completo = ''

    for pagina in leitor.pages:
        texto = pagina.extract_text()

        if texto:
            texto_completo += texto + '\n'
    return texto_completo
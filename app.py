# importando pastas para acessar os pdfs
# DOCS_DIR = guarda o caminho da pasta
from config import DOCS_DIR
# importando pypdf
from pypdf import PdfReader

from pathlib import Path

from src.ingestion.pdf_loader import carregar_pdf



# percorrer e ler os arquivos do docs(pdf)
# iterdir() = vai percorrer tudo que esta na pasta
for arquivo in DOCS_DIR.iterdir():

    # verifica se a extensão é .pdf
    if arquivo.suffix.lower() == '.pdf':
        print(f'\nLendo: {arquivo.name}')

        # aqui cria o objeto
        leitor = PdfReader(arquivo)

        texto = ''

        # percorrer as paginas dos pdfs
        for pagina in leitor.pages:
            # aqui vai extrair somente se for pdf
            texto += pagina.extract_text() or ''

            print(texto[:500]) # exibe os 500 primeiros caracteres


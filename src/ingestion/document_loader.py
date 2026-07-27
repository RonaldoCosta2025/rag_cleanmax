# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa o loader responsável por arquivos PDF.
from src.ingestion.pdf_loader import carregar_pdf

# Importa o loader responsável por arquivos CSV.
from src.ingestion.csv_loader import carregar_csv

from src.ingestion.txt_loader import carregar_txt

from src.ingestion.xlsx_loader import carregar_xlsx

from src.ingestion.docx_loader import carregar_docx


# Define a função que escolhe automaticamente o loader correto.
def carregar_documento(caminho: Path):

    # Obtém a extensão do arquivo e transforma em letras minúsculas.
    extensao = caminho.suffix.lower()

    # verifica o tipo de extensão e carrega
    if extensao == ".pdf":
        # Usa o loader de PDF.
        return carregar_pdf(caminho)       
    elif extensao == ".csv":        
        return carregar_csv(caminho)
    elif extensao == '.txt':       
        return carregar_txt(caminho)
    # xlxs
    elif extensao == '.xlsx':
        return carregar_xlsx(caminho)
    # docx
    elif extensao == '.docx':
        return carregar_docx(caminho)

    # Informa que o formato ainda não é suportado.
    raise ValueError(
        f"Formato de arquivo não suportado: {extensao}"
    )
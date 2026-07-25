# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa o loader responsável por arquivos PDF.
from src.ingestion.pdf_loader import carregar_pdf

# Importa o loader responsável por arquivos CSV.
from src.ingestion.csv_loader import carregar_csv


# Define a função que escolhe automaticamente o loader correto.
def carregar_documento(caminho: Path):

    # Obtém a extensão do arquivo e transforma em letras minúsculas.
    extensao = caminho.suffix.lower()

    # Verifica se o arquivo é um PDF.
    if extensao == ".pdf":

        # Usa o loader de PDF.
        return carregar_pdf(caminho)

    # Verifica se o arquivo é um CSV.
    if extensao == ".csv":

        # Usa o loader de CSV.
        return carregar_csv(caminho)

    # Informa que o formato ainda não é suportado.
    raise ValueError(
        f"Formato de arquivo não suportado: {extensao}"
    )
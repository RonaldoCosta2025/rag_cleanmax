# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa o pandas para ler planilhas Excel.
import pandas as pd

# Importa a classe Documento utilizada em todo o projeto.
from src.ingestion.document import Documento


# Define a função responsável por carregar arquivos XLSX.
def carregar_xlsx(caminho: Path):

    # Lê a planilha utilizando o pandas.
    df = pd.read_excel(caminho)

    # Lista onde serão armazenadas as linhas convertidas em texto.
    linhas = []

    # Percorre todas as linhas da planilha.
    for _, linha in df.iterrows():

        # Lista que armazenará os campos da linha atual.
        campos = []

        # Percorre cada coluna da linha.
        for coluna in df.columns:

            # Cria um texto no formato "coluna: valor".
            campos.append(
                f"{coluna}: {linha[coluna]}"
            )

        # Junta todos os campos da linha utilizando "|".
        linhas.append(" | ".join(campos))

    # Junta todas as linhas da planilha em um único texto.
    texto = "\n".join(linhas)

    # Cria um Documento com o texto gerado.
    documento = Documento(
        texto=texto,
        arquivo=caminho.name
    )

    # Retorna o documento.
    return documento
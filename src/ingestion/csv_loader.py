# Importa Path para trabalhar com o caminho do arquivo.
from pathlib import Path

# Importa o módulo csv para ler arquivos CSV.
import csv

# Importa a estrutura Documento que já tem no projeto.
from src.ingestion.document import Documento


# Define a função responsável por carregar um arquivo CSV.
def carregar_csv(caminho: Path):

    # Cria uma lista vazia para armazenar as linhas do CSV.
    linhas = []

    # Abre o arquivo CSV utilizando UTF-8.
    with open(caminho, "r", encoding="utf-8-sig", newline="") as arquivo:

        # Cria um leitor que interpreta a primeira linha como cabeçalho.
        leitor = csv.DictReader(arquivo)

        # Percorre cada linha encontrada no arquivo.
        for linha in leitor:

            # Converte os dados da linha em texto.
            texto_linha = " | ".join(
                f"{chave}: {valor}"
                for chave, valor in linha.items()
            )

            # Adiciona a linha convertida à lista.
            linhas.append(texto_linha)

    # Junta todas as linhas em um único texto.
    texto = "\n".join(linhas)

    # Cria um objeto Documento com o conteúdo e o nome do arquivo.
    documento = Documento(
        texto=texto,
        arquivo=caminho.name
    )

    # Retorna o documento carregado.
    return documento
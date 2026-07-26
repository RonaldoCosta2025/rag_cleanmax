# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa a classe Documento utilizada em todo o projeto.
from src.ingestion.document import Documento



# Define a função responsável por carregar arquivos TXT.
def carregar_txt(caminho: Path):

    # Abre o arquivo utilizando codificação UTF-8.
    with open(caminho, "r", encoding="utf-8") as arquivo:

        # Lê todo o conteúdo do arquivo.
        texto = arquivo.read()

    # Cria um objeto Documento contendo o texto e o nome do arquivo.
    documento = Documento(
        texto=texto,
        arquivo=caminho.name
    )

    # Retorna o documento carregado.
    return documento
# Importa Path para trabalhar com caminhos.
from pathlib import Path

# Importa a função responsável por carregar arquivos TXT.
from src.ingestion.txt_loader import carregar_txt


# Define o caminho do arquivo de teste.
arquivo = Path("docs/10_Politica_RH.txt")

# Carrega o arquivo TXT.
documento = carregar_txt(arquivo)

# Mostra o nome do arquivo.
print("Arquivo:", documento.arquivo)

# Mostra o conteúdo do documento.
print("\nConteúdo:\n")
print(documento.texto)
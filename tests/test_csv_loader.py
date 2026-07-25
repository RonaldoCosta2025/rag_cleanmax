# Importa Path para trabalhar com o caminho do arquivo.
from pathlib import Path

# Importa a função que criamos para carregar CSV.
from src.ingestion.csv_loader import carregar_csv


# Define o caminho do arquivo CSV que será testado.
arquivo = Path("docs/produtos.csv")

# Carrega o CSV e transforma seu conteúdo em um Documento.
documento = carregar_csv(arquivo)

# Mostra o nome do arquivo carregado.
print("Arquivo:", documento.arquivo)

# Mostra o conteúdo convertido para texto.
print("\nConteúdo:")
print(documento.texto)
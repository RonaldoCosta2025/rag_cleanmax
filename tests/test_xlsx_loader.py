# Importa Path para trabalhar com caminhos.
from pathlib import Path

# Importa o loader de XLSX.
from src.ingestion.xlsx_loader import carregar_xlsx


# Define o caminho da planilha.
arquivo = Path("docs/11_controle_estoque_produtos.xlsx")

# Carrega a planilha.
documento = carregar_xlsx(arquivo)

# Mostra o nome do arquivo.
print("Arquivo:", documento.arquivo)

# Mostra o conteúdo convertido para texto.
print("\nConteúdo:\n")

print(documento.texto)
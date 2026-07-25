# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa o carregador geral de documentos.
from src.ingestion.document_loader import carregar_documento


# Define o caminho do PDF.
arquivo_pdf = Path("docs/01_Apresentacao_Empresa.pdf")

# Define o caminho do CSV.
arquivo_csv = Path("docs/produtos.csv")


# Carrega automaticamente o PDF.
documento_pdf = carregar_documento(arquivo_pdf)

# Carrega automaticamente o CSV.
documento_csv = carregar_documento(arquivo_csv)


# Mostra o resultado do PDF.
print("PDF:")
print("Arquivo:", documento_pdf.arquivo)
print("Caracteres:", len(documento_pdf.texto))


# Mostra o resultado do CSV.
print("\nCSV:")
print("Arquivo:", documento_csv.arquivo)
print("Caracteres:", len(documento_csv.texto))
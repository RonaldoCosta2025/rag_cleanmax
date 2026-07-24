from pathlib import Path

from src.ingestion.pdf_loader import carregar_pdf


arquivo = Path(
    "docs/01_Apresentacao_Empresa.pdf"
)


print("Iniciando teste...")


documento = carregar_pdf(arquivo)


print("Arquivo:")
print(documento.arquivo)


print("\nQuantidade de caracteres:")
print(len(documento.texto))


print("\nConteúdo:")
print(documento.texto[:300])
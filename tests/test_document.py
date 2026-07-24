from src.ingestion.document import Documento


documento = Documento(
    texto="Teste de documento",
    arquivo="teste.pdf"
)


print(documento)
print(documento.texto)
print(documento.arquivo)
# from src.ingestion.pdf_loader import carregar_pdf
# from src.ingestion.text_splitter import dividir_texto


# texto = carregar_pdf(
#     "docs/01_Apresentacao_Empresa.pdf"
# )


# chunks = dividir_texto(texto)


# print("Quantidade de chunks:", len(chunks))


# for i, chunk in enumerate(chunks):

#     print("================")
#     print("Chunk:", i)
#     print(chunk[:200])

# from src.ingestion.pdf_loader import carregar_pdf
# from src.ingestion.text_splitter import dividir_texto


# arquivo = "docs/02_Catalogo_Produtos.pdf"


# # 1 - Carrega o PDF inteiro
# texto = carregar_pdf(arquivo)


# # 2 - Divide o texto em chunks
# chunks = dividir_texto(
#     texto,
#     tamanho=1000,
#     sobreposicao=2
# )


# # 3 - Quantidade de chunks gerados
# print("Quantidade de chunks:", len(chunks))


# # 4 - Mostra tamanho de cada chunk
# print("\nTamanho dos chunks:")

# for i, chunk in enumerate(chunks):

#     print(
#         f"Chunk {i}: {len(chunk)} caracteres"
#     )


# # 5 - Mostra uma amostra do conteúdo
# print("\n==============================")
# print("Primeiro chunk:")
# print(chunks[0][:500])


# if len(chunks) > 1:
#     print("\n==============================")
#     print("Segundo chunk:")
#     print(chunks[1][:500])

# chunks = dividir_texto(
#     texto,
#     tamanho=300,
#     sobreposicao=50
# )


# print("Quantidade de chunks:", len(chunks))


# for i, chunk in enumerate(chunks):
#     print("\nCHUNK", i)
#     print(chunk[:200])



from pathlib import Path
from pypdf import PdfReader

# from src.ingestion.pdf_loader import carregar_pdf
# from src.ingestion.text_splitter import dividir_texto


# arquivo = Path("docs/02_Catalogo_Produtos.pdf")


# texto = carregar_pdf(arquivo)

# texto_teste = texto * 20

# chunks = dividir_texto(texto_teste)

# # chunks = dividir_texto(texto)


# print("Quantidade de chunks:", len(chunks))

# print("\nTamanho total do documento:")
# print(len(texto), "caracteres")


# for i, chunk in enumerate(chunks):

#     print("\n===================")
#     print("CHUNK", i + 1)
#     print("===================")

#     print("Quantidade de caracteres:", len(chunk))

#     print("\nConteúdo:")
#     print(chunk[:500])

from pathlib import Path

from src.ingestion.pdf_loader import carregar_pdf
from src.ingestion.text_splitter import dividir_texto


arquivos = Path("docs").glob("*.pdf")


for arquivo in arquivos:

    documento = carregar_pdf(arquivo)

    chunks = dividir_texto(documento)

    print("\nDocumento:", arquivo.name)
    # print("Caracteres:", len(documento))
    print("Chunks:", len(chunks))

    for i, chunk in enumerate(chunks):

        print("\n===================")
        print("CHUNK", i + 1)
        print("===================")

        print("Arquivo origem:")
        print(chunk.arquivo)

        print("\nQuantidade de caracteres:")
        print(len(chunk.texto))

        print("\nConteúdo:")
        print(chunk.texto[:300])
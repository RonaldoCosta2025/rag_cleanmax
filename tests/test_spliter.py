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

from src.ingestion.pdf_loader import carregar_pdf
from src.ingestion.text_splitter import dividir_texto


arquivo = "docs/02_Catalogo_Produtos.pdf"


# 1 - Carrega o PDF inteiro
texto = carregar_pdf(arquivo)


# 2 - Divide o texto em chunks
chunks = dividir_texto(
    texto,
    tamanho=1000,
    sobreposicao=2
)


# 3 - Quantidade de chunks gerados
print("Quantidade de chunks:", len(chunks))


# 4 - Mostra tamanho de cada chunk
print("\nTamanho dos chunks:")

for i, chunk in enumerate(chunks):

    print(
        f"Chunk {i}: {len(chunk)} caracteres"
    )


# 5 - Mostra uma amostra do conteúdo
print("\n==============================")
print("Primeiro chunk:")
print(chunks[0][:500])


if len(chunks) > 1:
    print("\n==============================")
    print("Segundo chunk:")
    print(chunks[1][:500])

# chunks = dividir_texto(
#     texto,
#     tamanho=300,
#     sobreposicao=50
# )


# print("Quantidade de chunks:", len(chunks))


# for i, chunk in enumerate(chunks):
#     print("\nCHUNK", i)
#     print(chunk[:200])
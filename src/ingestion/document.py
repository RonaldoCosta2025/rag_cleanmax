from dataclasses import dataclass

# O que isso faz?

# Cria uma estrutura:

# Documento(
#     texto="Detergente Industrial IND100 custa R$145,00",
#     arquivo="02_Catalogo_Produtos.pdf"
# )

@dataclass
class Documento:

    # armazena todo o texto do documento
    texto: str

    # armazena o nome do arquivo de origem
    arquivo: str


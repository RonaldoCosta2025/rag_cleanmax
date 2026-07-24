from dataclasses import dataclass

# O que isso faz?

# Criamos uma estrutura:

# Documento(
#     texto="Detergente Industrial IND100 custa R$145,00",
#     arquivo="02_Catalogo_Produtos.pdf"
# )

@dataclass
class Documento:

    texto: str
    arquivo: str


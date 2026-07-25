# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa a função que carrega um índice FAISS salvo no disco.
from src.vectorstore.faiss_store import carregar_indice


# Define o caminho onde o índice FAISS foi salvo.
caminho_indice = Path("vectorstore/index.faiss")

# Carrega o índice FAISS para a memória.
indice = carregar_indice(caminho_indice)

# Mostra quantos vetores existem dentro do índice carregado.
print(f"Quantidade de vetores: {indice.ntotal}")
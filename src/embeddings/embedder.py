# Importa a biblioteca responsável pelos embeddings.
from sentence_transformers import SentenceTransformer

# Carregamento do modelo:
modelo = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Recebe uma lista de textos.
def gerar_embeddings(textos: list[str]):

    # Transforma todos os textos em vetores.
    embeddings = modelo.encode(
        textos,
        show_progress_bar=True
    )

    return embeddings
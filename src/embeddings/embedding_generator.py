# gerando embeddings
from sentence_transformers import SentenceTransformer

# Carrega o modelo uma única vez
modelo = SentenceTransformer("all-MiniLM-L6-v2")


def gerar_embedding(texto: str):
    """
    Gera o embedding de um texto.

    Args:
        texto (str): Texto que será convertido em vetor.

    Returns:
        numpy.ndarray: Vetor de embedding.
    """
    return modelo.encode(texto)

def gerar_embeddings(chunks: list[str]):
    '''
        Gera embeddings para lista de chunks

        chunks: list[str] = lista de textos

        retorna lista de embeddings
    '''

    return modelo.encode(chunks)
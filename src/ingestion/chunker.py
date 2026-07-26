# Importa a classe Chunk.
from src.ingestion.chunk import Chunk

# Importa a classe Documento.
from src.ingestion.document import Documento


# Define a função responsável por criar chunks de vários documentos.
def criar_chunks(
    documentos: list[Documento],
    tamanho_chunk: int = 300,
    overlap: int = 50
) -> list[Chunk]:

    # Lista que armazenará todos os chunks de todos os documentos.
    todos_chunks = []

    # Percorre cada documento carregado.
    for documento in documentos:

        # Define o início do primeiro chunk.
        inicio = 0

        # Continua criando chunks enquanto houver texto.
        while inicio < len(documento.texto):

            # Calcula o final do chunk.
            fim = inicio + tamanho_chunk

            # Extrai o trecho correspondente ao chunk.
            texto_chunk = documento.texto[inicio:fim]

            # Cria um novo objeto Chunk.
            chunk = Chunk(
                texto=texto_chunk,
                arquivo=documento.arquivo
            )

            # Adiciona o chunk à lista geral.
            todos_chunks.append(chunk)

            # Avança considerando o overlap.
            inicio += tamanho_chunk - overlap

    # Retorna todos os chunks gerados.
    return todos_chunks
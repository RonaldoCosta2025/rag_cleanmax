from src.ingestion.chunk import Chunk
from src.ingestion.document import Documento


def criar_chunks(
    documento: Documento,
    tamanho_chunk: int = 500,
    overlap: int = 100
) -> list[Chunk]:

    chunks = []

    inicio = 0

    while inicio < len(documento.texto):

        fim = inicio + tamanho_chunk

        texto_chunk = documento.texto[inicio:fim]

        chunks.append(
            Chunk(
                texto=texto_chunk,
                arquivo=documento.arquivo
            )
        )

        inicio += tamanho_chunk - overlap

    return chunks
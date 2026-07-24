from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.ingestion.document import Documento


def dividir_texto(documento: Documento):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    textos = splitter.split_text(
        documento.texto
    )


    documentos = []


    for texto in textos:

        documentos.append(
            Documento(
                texto=texto,
                arquivo=documento.arquivo
            )
        )


    return documentos
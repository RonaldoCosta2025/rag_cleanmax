# arquivo responsavel para quebra do texto


# texto = o conteudo do pdf
# tamanho = maximo de cada pedaço do texto
# sobreposicao = quantidade de caracteres que vai repetir entre os pedaços
# def dividir_texto(texto, tamanho=1000, sobreposicao=200):
#     chunks = []

#     inicio = 0

#     while inicio < len(texto):
#         fim = inicio + tamanho

#         pedaco = texto[inicio:fim]

#         chunks.append(pedaco)

#         inicio = fim - sobreposicao

#     return chunks

# def dividir_texto(texto, tamanho=1000, sobreposicao=200):

#     # Primeiro separa por parágrafos
#     paragrafos = texto.split("\n")

#     chunks = []

#     chunk_atual = ""


#     for paragrafo in paragrafos:

#         paragrafo = paragrafo.strip()

#         # ignora linhas vazias
#         if not paragrafo:
#             continue


#         # verifica se adicionar esse parágrafo ultrapassa o limite
#         if len(chunk_atual) + len(paragrafo) <= tamanho:

#             chunk_atual += paragrafo + "\n"


#         else:

#             # salva o chunk atual
#             chunks.append(chunk_atual)


#             # cria o próximo chunk
#             chunk_atual = chunk_atual[-sobreposicao:] + paragrafo + "\n"


#     # adiciona o último pedaço
#     if chunk_atual:
#         chunks.append(chunk_atual)


#     return chunks

import re


import re


def dividir_em_frases(texto):

    frases = re.split(
        r'(?<=[.!?])\s+',
        texto
    )

    return [
        frase.strip()
        for frase in frases
        if frase.strip()
    ]


def dividir_texto(texto, tamanho=1000, sobreposicao=2):

    frases = dividir_em_frases(texto)

    chunks = []

    chunk_atual = []


    for frase in frases:

        texto_atual = " ".join(chunk_atual)

        # verifica se a próxima frase cabe
        if len(texto_atual) + len(frase) <= tamanho:

            chunk_atual.append(frase)


        else:

            # salva chunk atual
            if chunk_atual:
                chunks.append(
                    " ".join(chunk_atual)
                )


            # mantém as últimas frases como contexto
            chunk_atual = chunk_atual[-sobreposicao:]


            # adiciona nova frase
            chunk_atual.append(frase)


    # adiciona o último chunk
    if chunk_atual:
        chunks.append(
            " ".join(chunk_atual)
        )


    return chunks
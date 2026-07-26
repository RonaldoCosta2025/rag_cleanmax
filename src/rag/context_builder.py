# A responsabilidade desse arquivo será somente:

# Pegar os chunks encontrados e montar o contexto.

# Cria o contexto que será enviado para o modelo de IA.
def montar_contexto(chunks):

    # Lista que armazenará os textos formatados.
    contexto = []


    # Percorre todos os chunks encontrados.
    for chunk in chunks:

        # Monta cada trecho incluindo sua fonte.
        trecho = (
            f"Fonte: {chunk.arquivo}\n"
            f"{chunk.texto}"
        )

        # Adiciona o trecho na lista.
        contexto.append(trecho)


    # Junta todos os trechos em um único texto.
    return "\n\n".join(contexto)
# Importa a função que monta o contexto com os chunks encontrados.
from src.rag.context_builder import montar_contexto

# Importa a função que chama o Gemini.
from src.llm.gemini import gerar_resposta

# Cria o prompt para o modelo.
def criar_prompt(pergunta, contexto):

    # Monta as instruções que serão enviadas ao Gemini.
    prompt = f"""
Você é um assistente corporativo da CleanMax.

Responda somente utilizando o contexto fornecido.

Caso a resposta não esteja no contexto,
informe que não encontrou a informação.

Contexto:

{contexto}

Pergunta:

{pergunta}"""

    # Retorna o prompt pronto.
    return prompt

# Executa o fluxo completo do RAG.
def responder(pergunta, chunks):

    # Monta o contexto a partir dos chunks encontrados.
    contexto = montar_contexto(chunks)

    # Cria o prompt final.
    prompt = criar_prompt(
        pergunta,
        contexto
    )

    # Envia o prompt para o Gemini.
    resposta = gerar_resposta(prompt)
    
    return resposta
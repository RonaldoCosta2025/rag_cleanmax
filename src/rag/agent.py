# Importa a função que gera embeddings da pergunta.
from src.embeddings.embedding_generator import gerar_embedding

# Importa as funções do banco vetorial.
from src.vectorstore.faiss_store import buscar

# Importa a função que monta o contexto.
from src.rag.context_builder import montar_contexto

# Importa a função que chama o Gemini.
from src.llm.gemini import gerar_resposta

# Classe responsável pelo agente RAG.
class AgenteRAG:

    # Inicializa o agente recebendo o índice e os chunks.
    def __init__(self, indice, chunks):

        # Guarda o índice FAISS.
        self.indice = indice

        # Guarda os chunks carregados.
        self.chunks = chunks

    # Função principal para responder perguntas.
    def perguntar(self, pergunta):

        # Gera o embedding da pergunta.
        embedding_pergunta = gerar_embedding(pergunta)

        # Busca os chunks mais próximos.
        distancias, indices = buscar(
            self.indice,
            embedding_pergunta,
            quantidade=2
        )

        # Lista dos chunks encontrados.
        chunks_encontrados = []

        # Recupera os objetos Chunk.
        for indice_chunk in indices[0]:

            chunk = self.chunks[indice_chunk]

            chunks_encontrados.append(chunk)

        # Monta o contexto para o Gemini.
        contexto = montar_contexto(
            chunks_encontrados
        )

        # Cria o prompt.
        prompt = f"""
Você é um assistente corporativo da CleanMax.

Responda somente utilizando o contexto abaixo.

Não invente informações.

Se a resposta não estiver no contexto,
responda:
"Não encontrei essa informação nos documentos disponíveis."

Contexto:

{contexto}

Pergunta:

{pergunta}
"""
        # Envia para o Gemini.
        resposta = gerar_resposta(prompt)

        # Retorna resposta e fontes.
        # Remove fontes duplicadas.
        fontes = list(
            set(
                chunk.arquivo
                for chunk in chunks_encontrados
            )
        )

        # Cria o retorno estruturado do agente.
        resultado = {
            "resposta": resposta,
            "fontes": fontes,
            "quantidade_chunks": len(chunks_encontrados)
        }

        return resultado
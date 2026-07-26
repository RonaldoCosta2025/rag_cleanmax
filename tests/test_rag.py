# Importa Path para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa a função que transforma a pergunta em embedding.
from src.embeddings.embedding_generator import gerar_embedding

# Importa as funções responsáveis por carregar o FAISS, carregar os chunks e realizar a busca.
from src.vectorstore.faiss_store import carregar_indice, carregar_chunks, buscar

# Importa a função responsável por enviar o prompt para o Gemini.
from src.llm.gemini import gerar_resposta


# Define o caminho do índice FAISS salvo.
caminho_indice = Path("vectorstore/index.faiss")

# Define o caminho dos chunks salvos.
caminho_chunks = Path("vectorstore/chunks.pkl")

# Carrega o índice FAISS para a memória.
indice = carregar_indice(caminho_indice)

# Carrega os chunks salvos para a memória.
chunks = carregar_chunks(caminho_chunks)

# Define a pergunta feita pelo usuário.
#pergunta = "O que é a CleanMax?"

pergunta = "Qual o estoque do Detergente Neutro?"

# Transforma a pergunta em um vetor numérico.
embedding_pergunta = gerar_embedding(pergunta)

# Procura no FAISS os dois chunks mais relevantes para a pergunta.
distancias, indices = buscar(
    indice,
    embedding_pergunta,
    quantidade=2
)

# Cria uma lista para armazenar os textos encontrados.
contextos = []

# Cria uma lista para armazenar os arquivos utilizados como fonte.
fontes = []

# Percorre os índices encontrados pelo FAISS.
# for indice_chunk in indices[0]:

#     # Recupera o Chunk correspondente ao índice encontrado.
#     chunk = chunks[indice_chunk]

#     # Adiciona o texto do chunk à lista de contextos.
#     contextos.append(chunk.texto)

#     # Adiciona o nome do arquivo à lista de fontes.
#     fontes.append(chunk.arquivo)
# Percorre os índices encontrados pelo FAISS.
for indice_chunk in indices[0]:

    # Recupera o Chunk correspondente.
    chunk = chunks[indice_chunk]

    print("\nCHUNK ENCONTRADO")
    print("Arquivo:", chunk.arquivo)
    print(chunk.texto[:500])
    print("----------------")

    # Adiciona o texto do chunk à lista de contextos.
    contextos.append(chunk.texto)

    # Adiciona o nome do arquivo à lista de fontes.
    fontes.append(chunk.arquivo)

# Junta os textos recuperados em um único contexto.
contexto = "\n\n".join(contextos)

# Remove fontes duplicadas.
fontes = list(set(fontes))

# Junta os nomes das fontes em um único texto.
fontes_texto = "\n".join(f"- {fonte}" for fonte in fontes)

# Cria o prompt que será enviado ao Gemini.
prompt = f"""
Você é um assistente corporativo da CleanMax.

Responda à pergunta utilizando SOMENTE as informações
presentes no contexto abaixo.

Não utilize conhecimento externo.

Não invente informações.

Se a resposta não estiver no contexto,
responda exatamente:
"Não encontrei essa informação nos documentos disponíveis."

Se a informação estiver no contexto,
responda de forma clara e objetiva.

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

# Envia o contexto e a pergunta para o Gemini.
resposta = gerar_resposta(prompt)

# Exibe a resposta gerada pelo agente.
print("\nRESPOSTA DO AGENTE:")

# Exibe o texto da resposta.
print(resposta)

# Exibe o título da seção de fontes.
print("\nFONTES:")

# Exibe os documentos utilizados na resposta.
print(fontes_texto)
print(fontes_texto)
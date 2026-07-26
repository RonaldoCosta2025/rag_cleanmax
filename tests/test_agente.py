from pathlib import Path


from src.vectorstore.faiss_store import (
    carregar_indice,
    carregar_chunks
)


from src.rag.agent import AgenteRAG



caminho_indice = Path(
    "vectorstore/index.faiss"
)


caminho_chunks = Path(
    "vectorstore/chunks.pkl"
)



indice = carregar_indice(
    caminho_indice
)


chunks = carregar_chunks(
    caminho_chunks
)



agente = AgenteRAG(
    indice,
    chunks
)



resultado = agente.perguntar(
    "Qual o estoque do Detergente Neutro?"
)


print("\nRESPOSTA:")
print(resultado["resposta"])


print("\nFONTES:")

for fonte in resultado["fontes"]:
    print("-", fonte)


print("\nCHUNKS UTILIZADOS:")
print(resultado["quantidade_chunks"])
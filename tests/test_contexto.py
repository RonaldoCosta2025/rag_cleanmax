# Importa a função que monta o contexto.
from src.rag.context_builder import montar_contexto


# Importa a classe que representa os chunks.
from src.ingestion.chunker import Chunk


# Cria alguns chunks de teste.
chunks = [
    Chunk(
        texto="Valores: Ética, Transparência, Sustentabilidade.",
        arquivo="01_Apresentacao_Empresa.pdf"
    ),
    Chunk(
        texto="Atendimento de segunda a sexta-feira.",
        arquivo="01_Apresentacao_Empresa.pdf"
    )
]


# Monta o contexto.
contexto = montar_contexto(chunks)


# Exibe o resultado.
print(contexto)
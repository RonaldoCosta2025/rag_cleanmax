from sentence_transformers import util

class SimpleVectorStore:

    def __init__(self):
        self.documentos = []


    def adicionar(self, texto, embedding):

        self.documentos.append(
            {
                'texto': texto,
                'embedding': embedding,
            }
        )

    def buscar(self, embedding_consulta):

        melhor_documento = None
        maior_similaridade = -1

        for documento in self.documentos:
            similaridade = util.cos_sim(
                embedding_consulta,
                documento['embedding']
            ).item()

            if similaridade > maior_similaridade:
                maior_similaridade = similaridade
                melhor_documento = documento
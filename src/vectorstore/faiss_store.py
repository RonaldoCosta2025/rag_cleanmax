# Importa a biblioteca responsável pelo índice vetorial.
import faiss

# Importa o NumPy para trabalhar com os vetores.
import numpy as np

# Importa o pickle para salvar e carregar os chunks.
import pickle


# Cria um índice FAISS a partir dos embeddings.
def criar_indice(embeddings):

    # Converte os embeddings para float32.
    embeddings = np.array(embeddings).astype("float32")

    # Normaliza os vetores para usar similaridade de cosseno.
    faiss.normalize_L2(embeddings)

    # Descobre a dimensão dos vetores.
    dimensao = embeddings.shape[1]

    # Cria índice usando produto interno.
    indice = faiss.IndexFlatIP(dimensao)

    # Adiciona os vetores normalizados.
    indice.add(embeddings)

    return indice

# Realiza uma busca no índice FAISS.
def buscar(indice, embedding_consulta, quantidade=3):

    # Converte o embedding da pergunta para um array NumPy.
    embedding_consulta = np.array(
    [embedding_consulta]
    ).astype("float32")

        # Normaliza o vetor da pergunta.
    faiss.normalize_L2(embedding_consulta)

    # Procura os vetores mais próximos da pergunta.
    distancias, indices = indice.search(
        embedding_consulta,
        quantidade
    )

    # Retorna as distâncias e os índices encontrados.
    return distancias, indices


# Salva o índice FAISS no disco.
def salvar_indice(indice, caminho):

    # Grava o índice no caminho informado.
    faiss.write_index(indice, str(caminho))


# Carrega um índice FAISS salvo anteriormente.
def carregar_indice(caminho):

    # Lê o índice salvo no disco.
    indice = faiss.read_index(str(caminho))

    # Retorna o índice carregado.
    return indice


# Salva os chunks no disco.
def salvar_chunks(chunks, caminho):

    # Abre o arquivo no modo de escrita binária.
    with open(caminho, "wb") as arquivo:

        # Serializa os chunks e grava os dados no arquivo.
        pickle.dump(chunks, arquivo)


# Carrega os chunks salvos no disco.
def carregar_chunks(caminho):

    # Abre o arquivo no modo de leitura binária.
    with open(caminho, "rb") as arquivo:

        # Recupera os objetos Chunk armazenados no arquivo.
        chunks = pickle.load(arquivo)

    # Retorna os chunks carregados.
    return chunks
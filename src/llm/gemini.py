# Importa o módulo os para acessar variáveis de ambiente.
import os

# Importa a função que carrega as variáveis do arquivo .env.
from dotenv import load_dotenv

# Importa o cliente da API Gemini.
from google import genai

# Importa a exceção lançada pela API.
from google.genai.errors import ClientError


# Carrega as informações presentes no arquivo .env.
load_dotenv()

# Obtém a chave da API através da variável GEMINI_API_KEY.
api_key = os.getenv("GEMINI_API_KEY")

# Verifica se a chave foi encontrada.
if not api_key:

    # Interrompe a execução caso a chave não exista.
    raise ValueError("GEMINI_API_KEY não encontrada no arquivo .env")


# Cria o cliente do Gemini utilizando a chave encontrada.
client = genai.Client(api_key=api_key)


# Define uma função responsável por enviar prompts para o Gemini.
def gerar_resposta(prompt: str):

    try:

        # Envia o prompt para o modelo Gemini.
        resposta = client.models.generate_content(

            # Modelo utilizado.
            model="gemini-3.6-flash",

            # Prompt enviado ao modelo.
            contents=prompt
        )

        # Retorna apenas o texto gerado.
        return resposta.text

    # Trata erros retornados pela API.
    except ClientError as erro:

        # Converte o erro para texto.
        mensagem = str(erro)

        # Verifica se a cota foi excedida.
        if "RESOURCE_EXHAUSTED" in mensagem:

            return (
                "O limite de utilização da API Gemini foi atingido.\n\n"
                "A busca nos documentos foi realizada com sucesso, "
                "mas não foi possível gerar a resposta porque a cota "
                "gratuita da API foi excedida.\n\n"
                "Tente novamente mais tarde."
            )

        # Retorna uma mensagem genérica para outros erros da API.
        return f"Erro ao comunicar com o Gemini:\n\n{mensagem}"

    # Captura qualquer outro erro inesperado.
    except Exception as erro:

        return f"Erro inesperado:\n\n{erro}"
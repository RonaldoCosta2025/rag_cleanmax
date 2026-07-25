# Importa o módulo os para acessar variáveis de ambiente.
import os

# Importa a função que carrega as variáveis do arquivo .env.
from dotenv import load_dotenv

# Importa o cliente da API Gemini.
from google import genai


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

    # Envia o prompt para o modelo Gemini.
    resposta = client.models.generate_content(

        # Define o modelo que será utilizado.
        model="gemini-3.6-flash",

        # Envia o prompt recebido pela função.
        contents=prompt
    )

    # Retorna somente o texto produzido pelo modelo.
    return resposta.text
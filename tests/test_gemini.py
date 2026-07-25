# Importa o módulo responsável pelas variáveis de ambiente.
import os

# Importa a função que carrega o arquivo .env.
from dotenv import load_dotenv


# Carrega as variáveis do arquivo .env.
load_dotenv()

# Obtém a chave sem mostrar seu conteúdo.
chave = os.getenv("GEMINI_API_KEY")

# Verifica somente se a chave foi encontrada.
print("Chave encontrada:", chave is not None)
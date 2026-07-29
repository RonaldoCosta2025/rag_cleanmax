# 🤖 Assistente Corporativo CleanMax

Um agente de IA baseado em RAG (Retrieval-Augmented Generation) desenvolvido em Python para responder perguntas sobre documentos internos de uma empresa fictícia.

O projeto utiliza busca vetorial com FAISS, embeddings do Sentence Transformers e geração de respostas com a API Gemini.

---

## 🚀 Demonstração

O usuário faz uma pergunta através da interface Streamlit.

Exemplo:

> Qual o estoque do Detergente Neutro?

Resposta:

> O estoque do Detergente Neutro (código DET500) é de 120 unidades.

Fontes:

- produtos.csv
- 02_Catalogo_Produtos.pdf

---

## ✨ Funcionalidades

- Leitura automática de documentos
  - PDF
  - CSV
  - TXT
  - DOCX
  - XLSX

- Geração de embeddings

- Busca semântica utilizando FAISS

- Geração de respostas com Gemini

- Exibição das fontes utilizadas

- Interface web utilizando Streamlit

- Tratamento de erros da API Gemini

---

## 🛠 Tecnologias

- Python 3.12
- Streamlit
- Google Gemini
- FAISS
- Sentence Transformers
- PyMuPDF
- Pandas
- OpenPyXL
- Python-Docx

---

## 📂 Estrutura do projeto

```text
rag-cleanmax/

├── docs/
├── src/
│   ├── embeddings/
│   ├── ingestion/
│   ├── llm/
│   ├── rag/
│   ├── vectorstore/
│   └── config.py
│
├── tests/
├── vectorstore/
├── app.py
└── requirements.txt
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone <https://github.com/RonaldoCosta2025/rag_cleanmax>
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual.

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuração

Crie um arquivo `.env`

```text
GEMINI_API_KEY=SUA_CHAVE
```

---

## 📥 Ingestão dos documentos

Após adicionar arquivos na pasta `docs`, execute:

```bash
python -m tests.test_pipeline
```

Isso irá:

- carregar os documentos;
- gerar os chunks;
- criar os embeddings;
- construir o índice FAISS.

---

## ▶️ Executando a aplicação

```bash
streamlit run app.py
```

---

## 💬 Exemplos de perguntas

- Qual o estoque do Detergente Neutro?
- O que fazer em caso de acidente?
- Quais EPIs são obrigatórios?
- Quais são os horários de trabalho?
- Quem são os fornecedores ativos?


---

---
## 📚 Aprendizado e Desafios

- Funcionamento de um RAG
- Leitura e escrita de arquivos com formatos diferentes
- Estrutura das pastas e organização
- Melhora do entendimento do Python
- Importação de pacotes específicos
- Chamada da API do Gemini
- Um entendimento melhor sobre centralizar as configurações
- Utilizar e construir prompts junto ao Gpt para entendimento 
 da construção do RAG.

> **Observação:** Optei por não utilizar o LangChain neste projeto para compreender melhor como funciona cada etapa de um pipeline RAG, implementando manualmente os principais componentes.
---

## 👨‍💻 Autor

Ronaldo Luis da Costa

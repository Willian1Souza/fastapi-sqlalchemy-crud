# FastAPI CRUD Usuário

Este projeto é uma API REST funcional para gerenciamento de usuários (CRUD), desenvolvida com o framework **FastAPI** e utilizando **SQLAlchemy** para persistência de dados em um banco de dados **SQLite**.

A aplicação segue o **Repository Pattern**, separando a lógica de acesso a dados da lógica de negócio.

## ✨ Funcionalidades

*   **Listagem de Usuários:** Busca paginada com filtro por nome (case-insensitive).
*   **Criação e Atualização:** O método `save` gerencia inteligentemente novos registros e atualizações (Upsert).
*   **Busca por ID:** Recuperação detalhada de um único usuário.
*   **Verificação de Existência:** Checagem performática antes de operações críticas.
*   **Exclusão Segura:** Remove usuários garantindo que o registro exista no banco.

## 🚀 Tecnologias Utilizadas

*   [FastAPI](https://fastapi.tiangolo.com/): Framework moderno e rápido para APIs.
*   [SQLAlchemy](https://www.sqlalchemy.org/): ORM para interação com banco de dados.
*   [SQLite](https://www.sqlite.org/): Banco de dados relacional leve.
*   [Pydantic](https://docs.pydantic.dev/): Validação de dados e tipos.
*   [Uvicorn](https://www.uvicorn.org/): Servidor ASGI para Python.

## 🛠️ Como Executar o Projeto

Siga as instruções abaixo para rodar a aplicação em sua máquina local.

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd crud
```

### 2. Criar um Ambiente Virtual
```bash
python -m venv .venv
```

### 3. Ativar o Ambiente Virtual
*   **Windows:**
    ```bash
    .venv\Scripts\activate
    ```
*   **Linux/macOS:**
    ```bash
    source .venv/bin/activate
    ```

### 4. Instalar e Gerenciar Dependências
Para instalar as dependências necessárias:
```bash
pip install fastapi sqlalchemy uvicorn pydantic
```
*(Ou `pip install -r requirements.txt` caso você já tenha gerado o arquivo)*.

### 5. Iniciar o Servidor
```bash
python main.py
```
A API estará disponível em `http://127.0.0.1:8000`.

## 📖 Documentação (Swagger)

O FastAPI gera automaticamente a documentação interativa da API. Com o servidor rodando, acesse:

*   **Swagger UI:** http://127.0.0.1:8000/docs
*   **Redoc:** http://127.0.0.1:8000/redoc
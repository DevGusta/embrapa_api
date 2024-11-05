# API de Consulta de Dados da Empraba

Este projeto faz parte do Tech Challenge FIAP, que engloba conhecimentos de todas as disciplinas da fase. A tarefa é desenvolver uma API pública para consultar dados de vitivinicultura da Embrapa e fornecer uma base para futuras análises e modelos de Machine Learning.

## Descrição do Projeto

A API foi desenvolvida em Python com o framework **FastAPI** para permitir consultas nos dados das seguintes abas do site da Embrapa:
- Produção
- Processamento
- Comercialização
- Importação
- Exportação

## Estrutura da API

### Endpoints Principais
A API possui endpoints para consultar os dados em cada aba específica do site da Embrapa. 

Exemplo de um endpoint:
```
GET /producao
```

### Autenticação
A API utiliza autenticação JWT para garantir a segurança dos dados.

Para utilizar os endpoints protegidos, siga os passos:
1. **Registre-se no endpoint `/register`** com o seguinte exemplo de payload:
    ```json
    {
      "username": "string",
      "email": "user@example.com",
      "full_name": "string",
      "password": "string"
    }
    ```
    > **Nota**: Os campos `full_name` e `email` não são obrigatórios.

2. **Faça login no endpoint `/login`** com seu `username` e `password`. Após o login bem-sucedido, você receberá um token JWT.

3. **Utilize o token JWT** nas demais requisições protegidas, passando-o no cabeçalho `Authorization` no formato:
    ```
    Authorization: Bearer <seu_token_jwt>
    ```


## Configuração do Projeto

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/username/embrapa_api.git
    cd embrapa_api
    ```

2. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configuração da Base de Dados**:
    Crie uma tabela `users` na sua base de dados MySQL usando o seguinte comando SQL:
    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        full_name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        hashed_password VARCHAR(255) NOT NULL,
        disabled BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    ```

4. **Configuração das Variáveis de Ambiente**:
    Crie um arquivo `.env` na raiz do projeto e adicione a variável `DATABASE_URL` com o URL de conexão ao banco de dados MySQL:
    ```
    DATABASE_URL=mysql+pymysql://user:password@host:port/dbname
    ```

    > **Nota**: Certifique-se de substituir `user`, `password`, `host`, `port` e `dbname` pelos valores corretos do seu banco de dados MySQL.

## Rodando o Projeto

1. **Execute a aplicação**:
    ```bash
    uvicorn main:app --reload
    ```

2. Acesse a documentação da API em:
    ```
    http://127.0.0.1:8000/docs
    ```

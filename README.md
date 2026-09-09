# 📚 StudyManager API

API RESTful para gerenciamento de **usuários, cursos e matrículas**, desenvolvida com FastAPI, SQLAlchemy e PostgreSQL.

## 🛠️ Tecnologias

- Python 3.13+
- FastAPI 0.141.1
- SQLAlchemy 2.0.52
- PostgreSQL
- Pydantic 2.13.5
- Uvicorn 0.52.4
- psycopg2-binary 2.9.12
- python-dotenv 1.2.3

---

## 📁 Estrutura do projeto

```text
StudyManager/
├── app/
│   ├── controllers/
│   ├── infrastructure/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── usecases/
│   └── main.py
├── database/
│   └── schema.sql
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

O projeto utiliza uma organização baseada em Clean Architecture, separando as responsabilidades entre controllers, use cases, repositories, models, schemas e infraestrutura.


# 🚀 Como executar

## 1. Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.13 ou superior
- PostgreSQL
- Git

Verifique a instalação do Python:

```
python --version
```

## 2. Clonar o projeto

Clone o repositório:

```
git clone https://github.com/ArthurPeruchi/StudyManager-API
```
Entre na pasta do projeto:

```
cd StudyManager-API
```

## 3. Criar o ambiente virtual

É recomendado utilizar um ambiente virtual para manter as dependências do projeto isoladas do Python do sistema.

### No Windows

```python
python -m venv .venv
```

Esse comando criará a pasta .venv na raiz do projeto.

### Ativar o ambiente virtual

No PowerShell:

```python
.venv\Scripts\Activate.ps1
```

No CMD:

```python
.venv\Scripts\activate
```

Após a ativação, o terminal deverá apresentar algo semelhante a:

```
(.venv) C:\...\StudyManager-API>
```

## 4. Instalar as dependências

Com o ambiente virtual ativado, execute:

```python
pip install -r requirements.txt
```

O arquivo requirements.txt contém todas as dependências necessárias para executar a aplicação.

# 🗄️ 5. Configurar o PostgreSQL

Crie um banco de dados PostgreSQL para o projeto.

Por exemplo:

`CREATE DATABASE studymanager;`

Depois, execute o arquivo schema.sql nesse banco.

O arquivo schema.sql, localizado em app/database, contém a estrutura necessária para a aplicação, criando as tabelas:

- users
- courses
- enrollments

Também são configuradas as chaves estrangeiras e as restrições necessárias para garantir a integridade dos dados.

A tabela enrollments, por exemplo, possui uma restrição que impede que o mesmo usuário seja matriculado duas vezes no mesmo curso.

### Executando pelo psql

```sql
psql -U postgres -d studymanager -f schema.sql
```

Também é possível executar o conteúdo do schema.sql utilizando ferramentas como o pgAdmin.


# 🔐 6. Configurar as variáveis de ambiente

O projeto utiliza a variável DATABASE_URL para configurar a conexão com o PostgreSQL.

Na raiz do projeto existe o arquivo:

`.env.example`

### Windows — PowerShell

Copie o arquivo .env.example para .env:

```
Copy-Item .env.example .env
```

### Windows — CMD

```
copy .env.example .env
```

Depois de criar o .env, abra o arquivo e configure a conexão com o seu banco.

Substitua:

- postgres pelo usuário do PostgreSQL, caso seja diferente;
- SUA_SENHA pela senha do PostgreSQL;
- study_manager pelo nome do banco criado.

O arquivo .env.example deve ser mantido no repositório apenas como modelo para indicar quais variáveis de ambiente são necessárias.


# ▶️ 7. Executar a aplicação

Com o ambiente virtual ativado, as dependências instaladas e o PostgreSQL configurado, execute:

```python
uvicorn app.main:app --reload
```

Se tudo estiver configurado corretamente, a API estará disponível em:

`http://127.0.0.1:8000`

O parâmetro --reload faz com que o servidor seja reiniciado automaticamente quando alterações forem detectadas durante o desenvolvimento.


# 📖 8. Documentação da API

O FastAPI disponibiliza automaticamente uma documentação interativa através do Swagger UI.

Acesse:

`http://127.0.0.1:8000/docs`

Também é possível acessar a documentação através do ReDoc:

`http://127.0.0.1:8000/redoc`


# 🔗 Endpoints

## 👤 Usuários

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /users | Criar usuário |
| GET | /users | Listar usuários |
| GET | /users/{id} | Buscar usuário |
| PUT | /users/{id} | Atualizar usuário |
| DELETE | /users/{id} | Excluir usuário |
| GET | /users/{id}/courses | Consultar cursos do usuário |

## 📘 Cursos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /courses | Criar curso |
| GET | /courses | Listar cursos |
| GET | /courses/{id} | Buscar curso |
| PUT | /courses/{id} | Atualizar curso |
| DELETE | /courses/{id} | Excluir curso |

## 📝 Matrículas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /enrollments | Criar matrícula |

A criação de uma matrícula verifica:

- Se o usuário existe;
- Se o curso existe;
- Se o usuário já está matriculado no curso.


# 🗃️ Banco de dados

O banco possui três entidades principais:

```
User
 │
 │ 1:N
 ▼
Enrollment
 ▲
 │ N:1
 │
Course
```

Um usuário pode possuir várias matrículas e um curso pode possuir várias matrículas.

Cada matrícula pertence a um único usuário e a um único curso.

O relacionamento entre as entidades é implementado utilizando SQLAlchemy ORM.


# 🧹 Arquitetura

A aplicação é organizada em camadas, seguindo princípios de Clean Architecture:

- Controllers: responsáveis pelas requisições HTTP e respostas da API.
- Use Cases: responsáveis pelas regras de negócio.
- Repositories: responsáveis pelo acesso aos dados através do SQLAlchemy.
- Models: representam as entidades do banco de dados.
- Schemas: responsáveis pela validação e estrutura dos dados utilizando Pydantic.
- Infrastructure: responsável por configurações relacionadas à infraestrutura, como a conexão com o banco.

Essa separação evita que regras de negócio fiquem concentradas nos controllers e facilita a manutenção e evolução da aplicação.


# 🧪 Testando a API

A maneira mais simples de testar os endpoints é utilizando a documentação interativa do Swagger:

http://127.0.0.1:8000/docs

Também é possível utilizar ferramentas como:

- Postman
- Insomnia
- cURL


# 👨‍💻 Autor

**Arthur Gabriel Peruchi Trindade (RA: 2410487)**
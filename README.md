# Validate Password

**Tecnologias e Ferramentas**

- Python 3.10
- PyTest
- Flask
- Docker

## Executando a aplicação

Há duas maneiras de executar a aplicação para desenvolvimento: localmente via pipenv e via Docker.

### via Pipenv

Para executar a aplicação localmente, é necessário a instalação do [pipenv](https://pipenv.pypa.io/en/latest/).

Com o `pipenv` instalado, podemos seguir os passos abaixo, via terminal.

```terminal
# iniciar o ambiente de desenvolvimento
$ pipenv shell

# instalar as dependências
$ pipenv install --system

# executar a aplicação
$ flask --app app --debug run --port=8000
```

### via Docker

Para executar a aplicação via Docker, podemos executar o seguinte comando, via terminal:

```terminal
docker compose up --build
```

---

## Testes

Para executar os testes, executamos o seguinte comando, via terminal:

```terminal
pytest tests.py -v
```

---

## Sobre a aplicação

A aplicação possui as seguintes rotas:

[POST]

- `/verify`: responsável por verificar a senha de acordos com as regras estabelecidas. A senha e as regras são enviadas via JSON no body da requisição. É retornado uma lista com as pendências que a senha informada possui e um valor booleano se ela está apta as regras informadas.

[Rotas de Documentação]

- `/apidoc/redoc`: documentação da API com redoc.
- `/apidoc/swagger`: documetação da API com swagger.

---

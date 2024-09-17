# Projeto Mabuya

O "Projeto Mabuya" foi desenvolvido para oferecer uma solução simples para que a população possa contribuir com o monitoramento das espécies endêmicas de Fernando de Noronha. A aplicação, construída com Python, Flask e SQLite, foi projetada para que o público da Ilha possa cadastrar na plataforma quando avistar uma espécie e assim formar uma rede de mapeamento e monitoramento coletivo.


# Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [SQLite](https://www.sqlite.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)


# Passos para instalação:

É recomendado antes de tudo abrir um [ambiente virtual](https://docs.python.org/pt-br/3/library/venv.html) Python para proceder com a instalação das dependências.

1. Clone este repositório

   ```bash
    $ git clone https://github.com/luizagraciano/Projeto-Mabuya.git
     ```
   

2. Instale as dependências através do arquivo **requirements.txt**
   ```bash
   $ pip install -r requirements.txt
   ```

4. Incialize o banco de dados

     ```bash
    $ flask --app src init-db
     ```

Você verá ser adicionada a pasta **instance** ao projeto, contendo o arquivo do banco de dados.


4. Alimente o banco de dados com uma prévia de espécies catalogadas

     ```bash
    $ flask --app src seed-db
     ```


5. Rode o projeto

     ```bash
    $ flask --app src run
     ```

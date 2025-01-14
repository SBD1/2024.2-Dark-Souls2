# Dark Souls 2 MUD (Multi-User Dungeon)

Este projeto é um MUD (Jogo de Aventura Baseado em Texto) inspirado no universo de **Dark Souls 2**. O jogo é um RPG onde o jogador cria um personagem, escolhe uma classe e explora diferentes locais, enfrentando desafios ao longo do caminho.

## Requisitos

Antes de rodar o jogo, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.7+**
- **PostgreSQL** (ou qualquer outro banco de dados SQL que preferir)
- **psycopg2** (biblioteca para conectar o Python ao PostgreSQL)

### Instalar dependências

1. Instale o `psycopg2` para conectar o Python ao banco de dados PostgreSQL:

   ```bash
   pip install psycopg2

2. Certifique-se de ter o PostgreSQL instalado e configurado na sua máquina.

### COMO RODAR O JOGO

1. ### Configurar o banco de dados
  - Criação do banco de dados:

  Abra o terminal do PostgreSQL e execute o seguinte comando para criar o banco de dados:

      
      CREATE DATABASE dark_souls_mud;

  Após isso utilize o comando para conectar-se ao banco de dados:

      
      \c dark_souls_mud;

  Mesmo não tendo sido utilizado ainda no python é importante ja criarmos e popularmos as nossas tabelas:
    
  Podendo ser feito manualmente copiando e colando o conteúdo do ddl e dml no terminal do PostgreSQL.

  - **Configuração da Conexão no Código:**

  No arquivo `main.py`, altere os seguintes parâmetros para que a conexão com o banco de dados funcione corretamente:

    conn = psycopg2.connect(
        dbname="dark_souls_mud",  # Nome do banco de dados
        user="postgres",          # Nome do usuário do PostgreSQL
        password="password",      # Senha do usuário do PostgreSQL
        host="localhost",         # Host do banco de dados
        port="5432"               # Porta padrão do PostgreSQL
    )

2. ### Rodar o jogo

  - Depois de configurar o banco de dados e a conexão, você pode rodar o jogo executando o seguinte comando:

      python main.py
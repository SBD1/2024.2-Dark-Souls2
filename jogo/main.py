import psycopg2

# Função para conectar ao banco de dados PostgreSQL
def conectar_banco():
    try:
        # Substitua os valores abaixo pelas suas credenciais de conexão
        conn = psycopg2.connect(
            dbname="dark_souls_mud",  # Nome do banco de dados
            user="postgres",          # Nome do usuário
            password="teste",      # Senha do usuário
            host="localhost",         # Host do banco de dados
            port="5432"               # Porta padrão do PostgreSQL
        )
        print("Conexão realizada com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para exibir o título e criar o personagem
def inicio(cursor):
    titulo = r"""
 ______   _______  _______  _          _______  _______           _        _______    _______ 
(  __  \ (  ___  )(  ____ )| \    /\  (  ____ \(  ___  )|\     /|( \      (  ____ \  / ___   )
| (  \  )| (   ) || (    )||  \  / /  | (    \/| (   ) || )   ( || (      | (    \/  \/   )  |
| |   ) || (___) || (____)||  (_/ /   | (_____ | |   | || |   | || |      | (_____       /   )
| |   | ||  ___  ||     __)|   _ (    (_____  )| |   | || |   | || |      (_____  )    _/   / 
| |   ) || (   ) || (\ (   |  ( \ \         ) || |   | || |   | || |            ) |   /   _/  
| (__/  )| )   ( || ) \ \__|  /  \ \  /\____) || (___) || (___) || (____/\/\____) |  (   (__/\
(______/ |/     \||/   \__/|_/    \/  \_______)(_______)(_______)(_______/\_______)  \_______/
    """

    print(titulo, end = '')
    print("\nDark Souls 2 é um jogo de ação e RPG desenvolvido pela FromSoftware, lançado em 2014.")
    print("O jogo é conhecido por seu alto nível de dificuldade e uma história rica e complexa.")
    print("Em Dark Souls 2, o jogador assume o papel de um personagem que busca entender seu destino enquanto enfrenta inimigos poderosos e explora um mundo devastado.")

    # Buscar todos os personagens disponíveis no banco
    query = "SELECT p.idPlayer, pe.nome FROM Player p JOIN Personagem pe on p.idCharacter = pe.idCharacter;"
    cursor.execute(query)
    personagens = cursor.fetchall()

    if not personagens:
        print("Nenhum personagem encontrado. Criando um novo...")
        id_player = criar_personagem(cursor)
        return id_player

    while True:
        try:
            escolha = int(input("1. Criar novo personagem\n2. Escolher personagem já criado\nEscolha uma opção: "))
            if escolha in [1, 2]:
                break  # Sai do loop se a escolha for válida
            print("Opção inválida. Escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
    if escolha == 1:
        id_player = criar_personagem(cursor)
        return id_player
    elif escolha == 2:
        print("\nEscolha um personagem para jogar:")
        for i, (id_player, nome) in enumerate(personagens, 1):
            print(f"{i}. {nome} (ID: {id_player})")

        while True:
            try:
                escolha = int(input("\nDigite o número do personagem que deseja jogar: "))
                if 1 <= escolha <= len(personagens):
                    return personagens[escolha - 1][0]  # Retorna o ID do personagem escolhido
                else:
                    print("Escolha inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")


def criar_personagem(cursor):
    nome = input("\nDigite o nome do seu personagem: ")

    # Exibir as opções de classes
    classes = [
        "Warrior", "Knight", "Swordsman", "Bandit", 
        "Cleric", "Sorcerer", "Explorer", "Deprived"
    ]
    print("\nEscolha uma classe para o seu personagem:")
    for i, classe in enumerate(classes, 1):
        print(f"{i}. {classe}")

    # Validar a escolha da classe
    while True:
        try:
            escolha = int(input(f"\nDigite um número de 1 a {len(classes)} para escolher sua classe: "))
            if 1 <= escolha <= len(classes):
                classe_escolhida = classes[escolha - 1]
                confirmacao = input(f"Sua classe escolhida é {classe_escolhida}. Deseja confirmar? (s/n): ").lower()
                if confirmacao == 's':
                    break
                else:
                    print("Por favor, faça uma nova escolha de classe.")
            else:
                print(f"Por favor, escolha um número de 1 a {len(classes)}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    # Obter os atributos da classe escolhida
    query_classe = """
    SELECT idClasse, levelInicial, dexterityInicial, strengthInicial, vigorInicial, 
           faithInicial, enduranceInicial, intelligenceInicial
    FROM Classe
    WHERE nome = %s;
    """
    cursor.execute(query_classe, (classe_escolhida,))
    classe = cursor.fetchone()

    if not classe:
        print("Erro: Não foi possível encontrar os atributos da classe escolhida no banco de dados.")
        return None  # Retorna None para indicar erro

    id_classe, level, dexterity, strength, vigor, faith, endurance, intelligence = classe

    # Passo 1: Inserir o personagem na tabela Personagem
    query_insert_personagem = """
    INSERT INTO Personagem (tipoCharacter, nome)
    VALUES (%s, %s) RETURNING idCharacter;
    """
    cursor.execute(query_insert_personagem, ("Player", nome))
    id_character = cursor.fetchone()[0]

    # Passo 2: Inserir o jogador na tabela Player e capturar o ID gerado
    query_insert_player = """
    INSERT INTO Player (
        idCharacter, hpAtual, health, dexterity, strength, vigor, faith, endurance, intelligence, 
        idSalaAtual, idClasse
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING idPlayer;
    """
    hp = 100 + (level * 10)  # Exemplo: HP inicial baseado no level
    health = hp  # Health inicial igual ao HP
    id_sala_atual = 1  # Começa na sala inicial (Majula)

    cursor.execute(query_insert_player, (
        id_character, hp, health, dexterity, strength, vigor, faith, endurance, intelligence,
        id_sala_atual, id_classe
    ))

    id_player = cursor.fetchone()[0]  # Capturar o ID do player recém-criado

    # Confirmar as mudanças no banco de dados
    conn.commit()


    print(f"Parabéns! Seu personagem {nome} foi criado como um {classe_escolhida} e salvo no banco de dados.")
    print("\nAgora, você está pronto para começar sua jornada!")
    print("A jornada está apenas começando. Você está em um local seguro, mas as opções à frente são muitas.")
    print("\nVocê se encontra na tranquila cidade de Majula, você está na praça principal da cidade, ao norte encontra-se o poço, à leste o mercado e a sul a floresta.")
    print("Aqui, você pode escolher para onde deseja ir. Você pode se mover para as seguintes direções:")
    return id_player  # Retorna o ID do personagem criado


def buscar_sala_atual(cursor, id_player):
    query = "SELECT idSalaAtual FROM Player WHERE idPlayer = %s;"
    cursor.execute(query, (id_player,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]  # Retorna o ID da sala atual
    else:
        print("Jogador não encontrado.")
        return None

def buscar_detalhes_sala(cursor, id_player):
    query = """
    SELECT s.id, s.nome, s.descricao 
    FROM Player p
    JOIN Sala s ON p.idSalaAtual = s.id
    WHERE p.idPlayer = %s;
    """
    cursor.execute(query, (id_player,))
    resultado = cursor.fetchone()

    if resultado:
        id_sala, nome_sala, descricao_sala = resultado
        return {"id": id_sala, "nome": nome_sala, "descricao": descricao_sala}
    else:
        print("Jogador ou sala não encontrada.")
        return None
    
def movePlayer(cursor, sala_atual_id):
    print(sala_atual_id)
    while True:
        print("\nPara onde deseja se mover?")
        print("1. Norte")
        print("2. Sul")
        print("3. Leste")
        print("4. Oeste")
        print("5. Cancelar")

        escolha = input("\nEscolha uma opção: ")

        direcoes = {
            "1": "norte",
            "2": "sul",
            "3": "leste",
            "4": "oeste"
        }

        if escolha == "5":
            print("\nVocê decidiu permanecer onde está.")
            break

        if escolha in direcoes:
            direcao = direcoes[escolha]

            # Consultar a sala para onde a direção escolhida leva
            query = f"SELECT {direcao} FROM Sala WHERE id = %s;"
            cursor.execute(query, (sala_atual_id,))
            resultado = cursor.fetchone()

            if resultado and resultado[0]:  # Se houver uma sala conectada nessa direção
                nova_sala = resultado[0]

                # Buscar o nome da nova sala
                query_nome_sala = "SELECT nome FROM Sala WHERE id = %s;"
                cursor.execute(query_nome_sala, (nova_sala,))
                nome_sala = cursor.fetchone()[0]

                # Atualizar a sala do jogador
                query_update_player = "UPDATE Player SET idSalaAtual = %s WHERE idPlayer = %s;"
                cursor.execute(query_update_player, (nova_sala, idPlayer))
                conn.commit()

                print(f"\nVocê se move para {nome_sala}.")
                return nova_sala  # Retorna a nova sala para atualização no menu

            else:
                print("\nNão há nada nessa direção. Escolha outro caminho.")
        else:
            print("\nOpção inválida. Escolha novamente.")

def verificaNpc(cursor, sala_atual):
    query = """
    SELECT s.id, s.nome, s.descricao, p.nome, n.tiponpc
    FROM Npc n
    JOIN Sala s ON n.salaAtual = s.id
    JOIN Personagem p ON n.idNpc = p.idCharacter
    WHERE s.id = %s;
    """
    cursor.execute(query, (sala_atual,))
    resultado = cursor.fetchone()
    if resultado:
        id_sala, nome_sala, descricao_sala, nome_npc, tipo_npc = resultado
        return {"id": id_sala, "nome": nome_sala, "descricao": descricao_sala, "nomeNpc": nome_npc, "tipoNpc": tipo_npc}
    else:
        print("Não há NPC nessa sala.")
        return None
    
def combate():
    print("Em construção")

def combateBoss():
    print("Em construção")

def comprarEquipamento():
    print("Em construção")

def aprimorarEquipamento():
    print("Em construção")

def menu(cursor, idPlayer):
    
    while True:
        # Buscar informações da sala atual
        sala_atual = buscar_detalhes_sala(cursor, idPlayer)

        if sala_atual:
            print("\n====================================================================")
            print(f"Você se encontra em: {sala_atual['nome']}")
            print(f"Descrição: {sala_atual['descricao']}")
            print("====================================================================")

        # Exibir opções para o jogador
        print("O que deseja fazer?")
        print("1. Verificar redondezas")
        print("2. Movimentar-se")
        print("3. Sair do jogo")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            npc = verificaNpc(cursor, sala_atual["id"])
            print("\n====================================================================")
            print(f"Você se encontra em: {sala_atual['nome']}")
            print(f"Descrição: {sala_atual['descricao']}")
            print(f"A sala tem o seguinte {npc['tipoNpc']} de nome {npc['nomeNpc']}")
            if npc['tipoNpc']  == 'Inimigo':
                combate()
            elif npc['tipoNpc']  == 'Mercante':
                comprarEquipamento()
            elif npc['tipoNpc']  == 'Ferreiro':
                aprimorarEquipamento()
            elif npc['tipoNpc']  == 'Boss':
                combateBoss()
            else:
                print("Você olhou ao redor e não encontrou nada interessante neste local")
            print("====================================================================")
        
        elif escolha == "2":
            movePlayer(cursor, sala_atual["id"])
        
        elif escolha == "3":
            print("\nVocê decidiu encerrar sua jornada por agora. Até a próxima!")
            break  # Sai do loop e encerra o menu
        
        else:
            print("\nOpção inválida. Tente novamente.")


# Executar o jogo
if __name__ == "__main__":
    conn = conectar_banco()
    cursor = conn.cursor()
    idPlayer = inicio(cursor)
    menu(cursor, idPlayer)
    
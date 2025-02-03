import psycopg2
import random

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
        idSalaAtual, idClasse, coin
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING idPlayer;
    """
    hp = 100 + (level * 10)  # Exemplo: HP inicial baseado no level
    health = hp  # Health inicial igual ao HP
    id_sala_atual = 1  # Começa na sala inicial (Majula)
    coin = 100 # jogador começa com 100 de gold

    cursor.execute(query_insert_player, (
        id_character, hp, health, dexterity, strength, vigor, faith, endurance, intelligence,
        id_sala_atual, id_classe, coin
    ))

    id_player = cursor.fetchone()[0]  # Capturar o ID do player recém-criado

    # Confirmar as mudanças no banco de dados
    conn.commit()


    print(f"Parabéns! Seu personagem {nome} foi criado como um {classe_escolhida} e salvo no banco de dados.")
    print("\nAgora, você está pronto para começar sua jornada!")
    print("A jornada está apenas começando. Você está em um local seguro, mas as opções à frente são muitas.")
    print("\nVocê se encontra na tranquila cidade de Majula, você está na praça principal da cidade, ao norte encontra-se o poço, à leste o mercado e a sul a floresta.")
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
    SELECT s.id, s.nome, s.descricao, p.nome, n.tiponpc, n.idNpc
    FROM Npc n
    JOIN Sala s ON n.salaAtual = s.id
    JOIN Personagem p ON n.idNpc = p.idCharacter
    WHERE s.id = %s;
    """
    cursor.execute(query, (sala_atual,))
    resultado = cursor.fetchone()
    if resultado:
        id_sala, nome_sala, descricao_sala, nome_npc, tipo_npc, idNpc = resultado
        return {"id": id_sala, "nome": nome_sala, "descricao": descricao_sala, "nomeNpc": nome_npc, "tipoNpc": tipo_npc, "idNpc": idNpc}
    else:
        print("Não há NPC nessa sala.")
        return None

def calcular_dano(base_dano, strength, dexterity):
    """Calcula o dano final baseado em força, destreza e chance de crítico"""
    crit_chance = min(25, strength * 1)  # Chance de crítico baseada na força (máx 25%)
    crit_multiplier = 1.5 if random.randint(1, 100) <= crit_chance else 1  # Crítico aumenta 50%
    return int(base_dano * crit_multiplier + dexterity * 0.2)  # Destreza dá leve aumento no dano

def tentativa_esquiva(dexterity):
    """Calcula se o Player consegue esquivar do ataque do inimigo"""
    dodge_chance = min(50, dexterity * 3)  # Chance máxima de esquiva: 30%
    return random.randint(1, 100) <= dodge_chance 

def escolher_arma(cursor, idPlayer):
    """Permite ao jogador escolher uma arma do inventário"""
    query = """
        SELECT i.nomeItem, a.dano, inv.item
        FROM Inventario inv
        JOIN InstanciaItem inst ON inv.item = inst.nroInstancia
        JOIN Item i ON inst.idItem = i.idItem
        JOIN Equipavel e ON i.idItem = e.idItem
        JOIN Arma a ON e.idEquipavel = a.idEquipavel
        WHERE inv.playerId = %s;
    """
    cursor.execute(query, (idPlayer,))
    armas = cursor.fetchall()
    
    if not armas:
        print("⚔️ Você não tem nenhuma arma, usando a espada inicial (30 de dano base).")
        return "Espada Inicial", 30
    
    print("\n🔪 Escolha sua arma:")
    for idx, (nome, dano, _) in enumerate(armas, 1):
        print(f"{idx}. {nome} (Dano: {dano})")
    
    while True:
        escolha = input("Digite o número da arma para usar: ").strip()
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(armas):
                return armas[escolha - 1][0], armas[escolha - 1][1]
            print("Escolha inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def usar_consumivel(cursor, idPlayer):
    """Permite ao jogador usar um consumível durante o combate"""
    query = """
        SELECT i.nomeItem, c.efeito, inv.item
        FROM Inventario inv
        JOIN InstanciaItem inst ON inv.item = inst.nroInstancia
        JOIN Item i ON inst.idItem = i.idItem
        JOIN Consumivel c ON i.idItem = c.idItem
        WHERE inv.playerId = %s;
    """
    cursor.execute(query, (idPlayer,))
    consumiveis = cursor.fetchall()
    
    if not consumiveis:
        print("🚫 Você não tem consumíveis para usar.")
        return
    
    print("\n🧪 Escolha um consumível para usar:")
    for idx, (nome, efeito, _) in enumerate(consumiveis, 1):
        print(f"{idx}. {nome} (Efeito: {efeito})")
    
    while True:
        escolha = input("Digite o número do consumível para usar ou 's' para cancelar: ").strip()
        if escolha.lower() == 's':
            return
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(consumiveis):
                nome, efeito, idInstancia = consumiveis[escolha - 1]
                print(f"Você usou {nome} e recebeu o efeito: {efeito}!")
                cursor.execute("""
                    DELETE FROM Inventario 
                    WHERE playerId = %s AND item = %s;
                """, (idPlayer, idInstancia))
                cursor.connection.commit()
                return
            print("Escolha inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def combate(cursor, idPlayer, idNpc):
    """Mecânica de combate entre Player e Inimigo"""
    # Buscar status do Player
    query = """
    SELECT hpAtual, strength, dexterity, endurance FROM Player WHERE idPlayer = %s;
    """
    cursor.execute(query, (idPlayer,))
    player_data = cursor.fetchone()
    if not player_data:
        print("Erro ao recuperar dados do Player.")
        return
    hpPlayer, strength, dexterity, endurance = player_data

    # Buscar status do Inimigo
    query = """
    SELECT i.hp, i.dano, p.nome
    FROM Inimigo i
    JOIN NPC n ON i.idNpc = n.idNpc
    JOIN Personagem p ON n.idCharacter = p.idCharacter
    WHERE n.idNpc = %s;
    """
    cursor.execute(query, (idNpc,))
    inimigo_data = cursor.fetchone()
    
    if not inimigo_data:
        print("Erro ao recuperar dados do Inimigo.")
        return
    hpInimigo, danoInimigo, nomeNpc = inimigo_data

    arma, danoBase = escolher_arma(cursor, idPlayer)
    print(f"\n⚔️ Você entrou em combate com {nomeNpc}! HP: {hpPlayer} vs Inimigo HP: {hpInimigo}")

    while hpPlayer > 0 and hpInimigo > 0:
        print("\n📜 Escolha sua ação:")
        print("1. Atacar 🗡️")
        print("2. Esquivar 🔄")
        print("3. Fugir 🏃")
        print("4. Usar Consumível 🧪")

        escolha = input("\nDigite sua ação: ").strip()

        if escolha == "1":
            danoPlayer = calcular_dano(danoBase, strength, dexterity)
            hpInimigo -= danoPlayer
            print(f"\n💥 Você atacou com {arma} e causou {danoPlayer} de dano!")
        elif escolha == "2":
            if tentativa_esquiva(dexterity):
                print("\n✨ Você conseguiu esquivar do ataque!")
                continue
            else:
                print("\n❌ Você falhou ao esquivar!")
        elif escolha == "3":
            print("\n🏃 Você fugiu do combate!")
            cursor.execute("UPDATE Player SET hpAtual = %s, coin = coin + 50 WHERE idPlayer = %s;", (hpPlayer, idPlayer))
            cursor.connection.commit()
            return True
        elif escolha == "4":
            usar_consumivel(cursor, idPlayer)
        else:
            print("❌ Opção inválida.")
            continue

        if hpInimigo > 0:
            if danoInimigo < 0:
                danoInimigo = 0
            hpPlayer = hpPlayer - (danoInimigo - endurance)
            print(f"💀 O inimigo atacou e causou {danoInimigo} de dano!")

        print(f"\n🔥 HP Atual: Você {hpPlayer} | Inimigo {hpInimigo}")

    if hpPlayer > 0:
        print(f"\n🎉 Você venceu a batalha! O {nomeNpc} dropou 50 de gold.")
        cursor.execute("UPDATE Player SET hpAtual = %s, coin = coin + 50 WHERE idPlayer = %s;", (hpPlayer, idPlayer))
        cursor.connection.commit()
        if idNpc == 4:
            atualizar_progresso_missao(cursor, idPlayer, 1, incremento=1)
        return True

    print("\n☠️ Você foi derrotado...")
    return False


def combateBoss(cursor, idPlayer, idBoss):
    """Mecânica de combate entre Player e Boss"""
    # Buscar status do Player
    query = """
    SELECT hpAtual, strength, dexterity, endurance FROM Player WHERE idPlayer = %s;
    """
    cursor.execute(query, (idPlayer,))
    player_data = cursor.fetchone()
    if not player_data:
        print("Erro ao recuperar dados do Player.")
        return
    hpPlayer, strength, dexterity, endurance = player_data

    # Buscar status do Boss
    query = """
    SELECT b.hp, b.dano, p.nome
    FROM Boss b
    JOIN NPC n ON b.idNpc = n.idNpc
    JOIN Personagem p ON n.idCharacter = p.idCharacter
    WHERE n.idNpc = %s;
    """
    cursor.execute(query, (idBoss,))
    boss_data = cursor.fetchone()
    
    if not boss_data:
        print("Erro ao recuperar dados do Boss.")
        return
    hpBoss, danoBoss, nomeBoss = boss_data

    arma, danoBase = escolher_arma(cursor, idPlayer)
    print(f"\n🔥 Você entrou em combate com o BOSS {nomeBoss}! HP: {hpPlayer} vs Boss HP: {hpBoss}")

    while hpPlayer > 0 and hpBoss > 0:
        print("\n📜 Escolha sua ação:")
        print("1. Atacar 🗡️")
        print("2. Esquivar 🔄")
        print("3. Fugir 🏃")
        print("4. Usar Consumível 🧪")

        escolha = input("\nDigite sua ação: ").strip()

        if escolha == "1":
            danoPlayer = calcular_dano(danoBase, strength, dexterity)
            hpBoss -= max(1, danoPlayer - 5)  # Boss tem resistência fixa de 5 ao dano
            print(f"\n💥 Você atacou com {arma} e causou {danoPlayer} de dano reduzido para {max(1, danoPlayer - 5)}!")
        elif escolha == "2":
            if tentativa_esquiva(dexterity):
                print("\n✨ Você conseguiu esquivar do ataque do Boss!")
                continue
            else:
                print("\n❌ Você falhou ao esquivar!")
        elif escolha == "3":
            print("\n🏃 Você tentou fugir, mas chefes não permitem fuga!")
            continue
        elif escolha == "4":
            usar_consumivel(cursor, idPlayer)
        else:
            print("❌ Opção inválida.")
            continue

        # Ataque do Boss
        if hpBoss > 0:
            danoFinal = danoBoss
            if random.random() < 0.2:  # 20% de chance de ataque especial
                danoFinal *= 1.1
                print(f"⚡ O Boss {nomeBoss} usou um ataque especial!")
            hpPlayer = hpPlayer - (danoFinal-endurance)
            print(f"💀 O Boss atacou e causou {danoFinal} de dano!\nPorém sua armadura reteve {endurance} de dano e o dano final foi de: {danoFinal-endurance}")

        print(f"\n🔥 HP Atual: Você {hpPlayer} | Boss {hpBoss}")

    if hpPlayer > 0:
        print(f"\n🎉 Você derrotou o BOSS {nomeBoss}! Recebeu 10000 de gold.")
        cursor.execute("UPDATE Player SET hpAtual = %s, coin = coin + 10000 WHERE idPlayer = %s;", (hpPlayer, idPlayer))
        cursor.connection.commit()
        return True

    print("\n☠️ Você foi derrotado pelo BOSS...")
    return False


def comprarEquipamento(cursor, idPlayer, idNpc):
    # Buscar o ID do Mercante associado ao NPC
    query = """
    SELECT idMercante FROM Mercante WHERE idNpc = %s;
    """
    cursor.execute(query, (idNpc,))
    mercante = cursor.fetchone()

    if not mercante:
        print("\nEste NPC não é um mercante.")
        return

    idMercante = mercante[0]

    # Buscar os itens que o mercante vende
    query = """
    SELECT i.idItem, i.nomeItem, i.preco, i.itemDetalhes
    FROM Mercante_Vende mv
    JOIN InstanciaItem ii ON mv.nroInstancia = ii.nroInstancia
    JOIN Item i ON ii.idItem = i.idItem
    WHERE mv.idMercante = %s;
    """
    cursor.execute(query, (idMercante,))
    itens_disponiveis = cursor.fetchall()

    if not itens_disponiveis:
        print("\nO mercante não tem itens para vender no momento.")
        return

    # Mostrar os itens disponíveis
    print("\nItens disponíveis para compra:")
    for i, (idItem, nomeItem, preco, itemDetalhes) in enumerate(itens_disponiveis, 1):
        print(f"{i}. {nomeItem}, Descrição: {itemDetalhes} - {preco} moedas. ")

    # Buscar saldo do jogador
    query = "SELECT coin FROM Player WHERE idPlayer = %s;"
    cursor.execute(query, (idPlayer,))
    saldo = cursor.fetchone()[0]

    while True:
        try:
            escolha = int(input("\nDigite o número do item que deseja comprar (ou 0 para sair): "))
            if escolha == 0:
                print("\nVocê decidiu não comprar nada.")
                return
            
            if 1 <= escolha <= len(itens_disponiveis):
                idItemEscolhido, nomeItem, preco, itemDetalhes = itens_disponiveis[escolha - 1]

                # Verificar se o jogador tem moedas suficientes
                if saldo < preco:
                    print("\nVocê não tem moedas suficientes para comprar este item.")
                    continue

                # Descontar moedas do jogador
                query = "UPDATE Player SET coin = coin - %s WHERE idPlayer = %s;"
                cursor.execute(query, (preco, idPlayer))

                # Criar uma nova instância do item para o jogador
                query = "INSERT INTO InstanciaItem (idItem) VALUES (%s) RETURNING nroInstancia;"
                cursor.execute(query, (idItemEscolhido,))
                nroInstancia = cursor.fetchone()[0]

                # Adicionar o item ao inventário do jogador
                query = """
                INSERT INTO Inventario (playerId, slot, item, itemQtd)
                VALUES (%s, (SELECT COALESCE(MAX(slot), 0) + 1 FROM Inventario WHERE playerId = %s), %s, 1);
                """
                cursor.execute(query, (idPlayer, idPlayer, nroInstancia))

                # Confirmar as alterações
                conn.commit()
                
                print(f"\nVocê comprou {nomeItem} por {preco} moedas!")
                return
            
            else:
                print("\nEscolha inválida. Digite um número da lista.")
        
        except ValueError:
            print("\nEntrada inválida. Digite um número válido.")

def aprimorarEquipamento(cursor, idPlayer):
    """Permite ao jogador aprimorar sua arma se tiver moedas suficientes"""
    query = """
        SELECT i.nomeItem, a.dano, inv.item, p.coin
        FROM Inventario inv
        JOIN InstanciaItem inst ON inv.item = inst.nroInstancia
        JOIN Item i ON inst.idItem = i.idItem
        JOIN Equipavel e ON i.idItem = e.idItem
        JOIN Arma a ON e.idEquipavel = a.idEquipavel
        JOIN Player p ON inv.playerId = p.idPlayer
        WHERE inv.playerId = %s;
    """
    cursor.execute(query, (idPlayer,))
    armas = cursor.fetchall()
    
    if not armas:
        print("⚔️ Você não tem nenhuma arma para aprimorar.")
        return
    
    print("\n🛠️ Escolha uma arma para aprimorar:")
    for idx, (nome, dano, _, coin) in enumerate(armas, 1):
        print(f"{idx}. {nome} (Dano atual: {dano})")
    
    while True:
        escolha = input("Digite o número da arma para aprimorar ou 's' para cancelar: ").strip()
        if escolha.lower() == 's':
            return
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(armas):
                nome, danoAtual, idInstancia, coins = armas[escolha - 1]
                break
            print("Escolha inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
    print("\n💰 Escolha o nível de aprimoramento:")
    print("1. +100 dano (Custo: 1000 coins)")
    print("2. +200 dano (Custo: 2000 coins)")
    
    while True:
        nivel = input("Digite o número do aprimoramento ou 's' para cancelar: ").strip()
        if nivel.lower() == 's':
            return
        if nivel == "1" and coins >= 1000:
            custo = 1000
            incremento = 100
            break
        elif nivel == "2" and coins >= 2000:
            custo = 2000
            incremento = 200
            break
        elif nivel in ["1", "2"]:
            print("Moedas insuficientes!")
        else:
            print("Escolha inválida.")
    
    novoDano = danoAtual + incremento
    
    cursor.execute("""
        UPDATE Arma
        SET dano = %s
        WHERE idEquipavel = (SELECT e.idEquipavel FROM Equipavel e 
                             JOIN Item i ON e.idItem = i.idItem
                             JOIN InstanciaItem inst ON i.idItem = inst.idItem
                             WHERE inst.nroInstancia = %s);
    """, (novoDano, idInstancia))
    
    cursor.execute("UPDATE Player SET coin = coin - %s WHERE idPlayer = %s;", (custo, idPlayer))
    cursor.connection.commit()
    
    print(f"🎉 {nome} foi aprimorada! Novo dano: {novoDano}.")

def obterStatusPlayer(cursor, idPlayer):
    """Retorna os status do player incluindo nome, classe e atributos principais."""
    
    query = """
    SELECT p.nome, pl.hpAtual, pl.health, pl.strength, pl.dexterity, pl.vigor, 
           pl.faith, pl.endurance, pl.intelligence, c.nome AS classe, pl.coin
    FROM Player pl
    JOIN Personagem p ON pl.idCharacter = p.idCharacter
    JOIN Classe c ON pl.idClasse = c.idClasse
    WHERE pl.idPlayer = %s;
    """
    
    cursor.execute(query, (idPlayer,))
    player_data = cursor.fetchone()
    
    if not player_data:
        print("❌ Erro: Player não encontrado.")
        return None

    # Desempacotando os valores
    nome, hpAtual, health, strength, dexterity, vigor, faith, endurance, intelligence, classe, coin = player_data

    # Criando um dicionário para retornar os status
    status = {
        "Nome": nome,
        "Classe": classe,
        "HP Atual": f"{hpAtual}/{health}",
        "Força": strength,
        "Destreza": dexterity,
        "Vigor": vigor,
        "Fé": faith,
        "Endurance": endurance,
        "Inteligência": intelligence,
        "Coin": coin
    }

    return status

def mostrarInventario(cursor, idPlayer):
    # Obter os itens do inventário do jogador
    query = """
        SELECT i.nomeItem, e.tipoEquipavel, inv.itemQtd, c.efeito, c.duracao, c.descricao, inv.item
        FROM Inventario inv
        JOIN InstanciaItem inst ON inv.item = inst.nroInstancia
        JOIN Item i ON inst.idItem = i.idItem
        LEFT JOIN Equipavel e ON i.idItem = e.idItem
        LEFT JOIN Consumivel c ON i.idItem = c.idItem
        WHERE inv.playerId = %s;
    """
    cursor.execute(query, (idPlayer,))
    itens = cursor.fetchall()

    if not itens:
        print("Seu inventário está vazio.")
        return

    print("\nSeu Inventário:")
    for idx, (nome, tipoEquipavel, qtd, efeito, duracao, descricao, idInstancia) in enumerate(itens, 1):
        info_extra = f" - {descricao} (Efeito: {efeito}, Duração: {duracao}s)" if efeito else ""
        print(f"{idx}. {nome} ({tipoEquipavel}) x{qtd}{info_extra}")
    
    # Permitir usar consumíveis ou equipar armaduras
    while True:
        escolha = input("\nDigite o número do item para usar/equipar (ou 'sair' para fechar o inventário): ")
        if escolha.lower() == "sair":
            break
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(itens):
                nome, tipoEquipavel, qtd, efeito, duracao, descricao, idInstancia = itens[escolha - 1]
                if efeito:
                    usarConsumivel(cursor, idPlayer, idInstancia, nome, efeito)
                    break
                elif tipoEquipavel == "Armadura":
                    equiparArmadura(cursor, idPlayer, idInstancia, nome)
                    break
                else:
                    print("Este item não pode ser usado ou equipado.")
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def equiparArmadura(cursor, idPlayer, idInstancia, nome):
    """Equipa uma armadura e atualiza a resistência do jogador."""
    query = """
        SELECT a.resistencia FROM Armadura a
        JOIN Equipavel e ON a.idEquipavel = e.idEquipavel
        JOIN Item i ON e.idItem = i.idItem
        JOIN InstanciaItem inst ON i.idItem = inst.idItem
        WHERE inst.nroInstancia = %s;
    """
    cursor.execute(query, (idInstancia,))
    armadura = cursor.fetchone()
    
    if not armadura:
        print("❌ Esta armadura não pode ser equipada.")
        return
    
    resistencia = armadura[0]
    cursor.execute("UPDATE Player SET endurance = %s WHERE idPlayer = %s;", (resistencia, idPlayer))
    cursor.connection.commit()
    print(f"🛡️ Você equipou {nome} e sua resistência aumentou para {resistencia}!")

def usarConsumivel(cursor, idPlayer, idInstancia, nome, efeito):
    # Aplica o efeito do consumível
    if "HP" in efeito:
        query = "UPDATE Player SET hpAtual = LEAST(health, hpAtual + 50) WHERE idPlayer = %s;"
        cursor.execute(query, (idPlayer,))
        print(f"Você usou {nome} e recuperou HP!")
    elif "stamina" in efeito:
        print(f"Você usou {nome} e sua regeneração de stamina aumentou!")
    
    # Reduz a quantidade do item no inventário
    query = """
        UPDATE Inventario SET itemQtd = itemQtd - 1
        WHERE playerId = %s AND item = %s AND itemQtd > 0;
    """
    cursor.execute(query, (idPlayer, idInstancia))
    
    # Remover o item do inventário se a quantidade for 0
    query = """
        DELETE FROM Inventario WHERE playerId = %s AND item = %s AND itemQtd <= 0;
    """
    cursor.execute(query, (idPlayer, idInstancia))
    
    cursor.connection.commit()


def atualizar_progresso_missao(cursor, idPlayer, idMissao, incremento=1):
    """Atualiza o progresso da missão e concede a recompensa se completada."""
    
    # Verificar se o jogador já tem a missão ativa
    cursor.execute("""
        SELECT progressoAtual, concluida FROM ProgressoMissao
        WHERE idPlayer = %s AND idMissao = %s;
    """, (idPlayer, idMissao))
    
    progresso = cursor.fetchone()
    
    if not progresso:
        # Se a missão ainda não foi iniciada, cria um progresso para ela
        cursor.execute("""
            INSERT INTO ProgressoMissao (idPlayer, idMissao, progressoAtual)
            VALUES (%s, %s, %s);
        """, (idPlayer, idMissao, incremento))
        cursor.connection.commit()
        print(f"📜 Missão iniciada: Derrote 5 lobos!")
        return False

    progressoAtual, concluida = progresso
    
    if concluida:
        print("✅ Você já completou essa missão.")
        return True
    
    # Atualizar progresso da missão
    progressoAtual += incremento
    cursor.execute("""
        UPDATE ProgressoMissao
        SET progressoAtual = %s
        WHERE idPlayer = %s AND idMissao = %s;
    """, (progressoAtual, idPlayer, idMissao))
    
    # Verificar se a missão foi concluída
    cursor.execute("SELECT objetivoQuantidade FROM Missao WHERE idMissao = %s;", (idMissao,))
    objetivoQuantidade = cursor.fetchone()[0]
    
    if progressoAtual >= objetivoQuantidade:
        # Marcar a missão como concluída
        cursor.execute("""
            UPDATE ProgressoMissao
            SET concluida = TRUE
            WHERE idPlayer = %s AND idMissao = %s;
        """, (idPlayer, idMissao))
        
        # Conceder recompensa
        cursor.execute("""
            SELECT coins FROM Missao_Recompensa WHERE idMissao = %s;
        """, (idMissao,))
        recompensa = cursor.fetchone()
        
        if recompensa:
            moedas = recompensa[0]
            cursor.execute("""
                UPDATE Player SET coin = coin + %s WHERE idPlayer = %s;
            """, (moedas, idPlayer))
            print(f"🎉 Missão concluída! Você recebeu {moedas} coins.")
    
    cursor.connection.commit()

def jogador_ja_falou_com_npc(cursor, idPlayer, idNpc):
    """Verifica se o jogador já interagiu com o NPC."""
    
    cursor.execute("""
        SELECT 1 FROM Player_NPC_Interacao 
        WHERE idPlayer = %s AND idNpc = %s;
    """, (idPlayer, idNpc))
    
    return cursor.fetchone() is not None  # Retorna True se já falou, False caso contrário

def registrar_interacao_npc(cursor, idPlayer, idNpc):
    """Registra que o jogador falou com o NPC pela primeira vez."""
    
    if not jogador_ja_falou_com_npc(cursor, idPlayer, idNpc):
        cursor.execute("""
            INSERT INTO Player_NPC_Interacao (idPlayer, idNpc)
            VALUES (%s, %s);
        """, (idPlayer, idNpc))
        cursor.connection.commit()
        print("📜 Você falou com esse NPC pela primeira vez!")
    else:
        print("👀 Você já falou com esse NPC antes.")

def descansar_em_bonfire(cursor, id_player, sala_atual):
    """Tenta descansar na bonfire, só funciona se o Player estiver na sala principal (id = 1)"""
    try:
        cursor.execute("CALL descansar_em_bonfire(%s, %s);", (id_player, sala_atual))
        cursor.connection.commit()
        print("🔥 Você descansou na bonfire. HP restaurado!")
        return True  # Indica sucesso
    except Exception as e:
        print(f"❌ Erro: {e}")  # Exibe o erro de forma amigável
        cursor.connection.rollback()  # Reseta o estado da transação
        return False  # Indica falha, mas o jogo continua


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
        print("3. Verificar status do player")
        print("4. Verificar inventário")
        print("5. Descansar na fogueira")
        print("6. Sair do jogo")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            npc = verificaNpc(cursor, sala_atual["id"])
            print("\n====================================================================")
            print(f"Você se encontra em: {sala_atual['nome']}")
            print(f"Descrição: {sala_atual['descricao']}")
            print(f"A sala tem o seguinte {npc['tipoNpc']} de nome {npc['nomeNpc']}")
            print("\n====================================================================")
            if npc['tipoNpc']  == 'Inimigo':
                while True:
                    escolha = int(input("1. Entrar em combate\n2. Recusar combate\n: "))
                    if escolha == 1:
                        print(f"Você irá entrar em combate com {npc['nomeNpc']}")
                        resultadoCombate = combate(cursor, idPlayer, npc['idNpc'])
                        if resultadoCombate == False:
                            print(f"\nVocê foi derrotado pelo {npc['nomeNpc']}... Sua jornada ainda não acabou!")
                            print("Você desperta no salão principal, sentindo a derrota, mas pronto para lutar novamente.")
                            
                            query = """
                            UPDATE Player
                            SET idSalaAtual = 1, hpAtual = health
                            WHERE idPlayer = %s;
                            """
                            cursor.execute(query, (idPlayer,))
                            conn.commit()
                        break
                    if escolha == 2:
                        print(f"Você escolheu não entrar em combate com {npc['nomeNpc']}")
                        break
                    else:
                        print('Digite um comando válido')
            elif npc['tipoNpc']  == 'Mercante':
                while True:
                    escolha = int(input("1. Falar com mercante\n2. Não fazer nada\n: "))
                    if escolha == 1:
                        comprarEquipamento(cursor, idPlayer, npc['idNpc'])
                        break
                    elif escolha == 2:
                        print("Você escolheu não fazer nada e continuar sua jornada!")
                        break
                    else:
                        print("Comando inválido, tente novamente!")
            elif npc['tipoNpc']  == 'Ferreiro':
                aprimorarEquipamento(cursor, idPlayer)
            elif npc['tipoNpc']  == 'Boss':
                while True:
                    escolha = int(input("1. Entrar em combate\n2. Recusar combate\n: "))
                    if escolha == 1:
                        print(f"Você irá entrar em combate com {npc['nomeNpc']}")
                        resultadoCombate = combateBoss(cursor, idPlayer, npc['idNpc'])
                        if resultadoCombate == False:
                            print(f"\nVocê foi derrotado pelo {npc['nomeNpc']}... Sua jornada ainda não acabou!")
                            print("Você desperta no salão principal, sentindo a derrota, mas pronto para lutar novamente.")
                            
                            query = """
                            UPDATE Player
                            SET idSalaAtual = 1, hpAtual = health
                            WHERE idPlayer = %s;
                            """
                            cursor.execute(query, (idPlayer,))
                            conn.commit()
                        break
                    if escolha == 2:
                        print(f"Você escolheu não entrar em combate com {npc['nomeNpc']}")
                        break
                    else:
                        print('Digite um comando válido')
            elif npc['tipoNpc'] == '':
                if not jogador_ja_falou_com_npc(cursor, idPlayer, 6):
                    print("Seja Bem-Vindo a Majula, tenho uma missão para você!")
                    atualizar_progresso_missao(cursor, idPlayer, 1, incremento=0)
                    registrar_interacao_npc(cursor, idPlayer, 6)
                    print("Os lobos ficam a sul da Praça Principal!")
                else:
                    concluida = atualizar_progresso_missao(cursor, idPlayer, 1, incremento=0)
                    if concluida == True:
                        print("Missão ja foi concluida!")
                    else:
                        print("Olá Andarilho\nParece que você tem uma missão em progresso!")
            else:
                print("Você olhou ao redor e não encontrou nada interessante neste local")
            print("====================================================================")
        
        elif escolha == "2":
            movePlayer(cursor, sala_atual["id"])

        elif escolha == "3":
            status = obterStatusPlayer(cursor, idPlayer)
            if status:
                print("\n📜 Status do Player:")
                for atributo, valor in status.items():
                    print(f"{atributo}: {valor}")
        elif escolha == "4":
            mostrarInventario(cursor, idPlayer)
        elif escolha == "5":
            sucesso = descansar_em_bonfire(cursor, idPlayer, sala_atual["id"])
            if not sucesso:
                # Trate o erro de forma amigável, sem quebrar o jogo
                print("⚠️ Dica: Só tem fogueira na Praça Principal, onde você inicia o jogo!")
  
        elif escolha == "6":
            print("\nVocê decidiu encerrar sua jornada por agora. Até a próxima!")
            break  # Sai do loop e encerra o menu
        
        else:
            print("\nOpção inválida. Tente novamente.")


# Executar o jogo
if __name__ == "__main__":
    conn = conectar_banco()
    if conn:
        try:
            cursor = conn.cursor()
            idPlayer = inicio(cursor)
            menu(cursor, idPlayer)
        finally:
            print("Fechando conexão com o banco de dados.")
            cursor.close()
            conn.close()
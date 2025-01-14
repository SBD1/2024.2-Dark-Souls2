import psycopg2

# Função para conectar ao banco de dados PostgreSQL
def conectar_banco():
    try:
        # Substitua os valores abaixo pelas suas credenciais de conexão
        conn = psycopg2.connect(
            dbname="dark_souls_mud",  # Nome do banco de dados
            user="postgres",          # Nome do usuário
            password="password",      # Senha do usuário
            host="localhost",         # Host do banco de dados
            port="5432"               # Porta padrão do PostgreSQL
        )
        print("Conexão realizada com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para exibir o título e criar o personagem
def criar_personagem():
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
    print("A jornada está apenas começando. Você está em um local seguro, mas as opções à frente são muitas.")
    
    nome = input("\nDigite o nome do seu personagem: ")

    # Exibir as opções de classes
    classes = [
        "Warrior", "Knight", "Swordman", "Bandit", 
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

    print(f"Parabéns! Seu personagem {nome} é um {classe_escolhida}.")
    print("\nAgora, você está pronto para começar sua jornada!")
    print("\nVocê se encontra na tranquila cidade de Majula. Esta cidade é um refúgio para almas perdidas como você.")
    print("Aqui, você pode escolher para onde deseja ir. Você pode se mover para as seguintes direções:")
    # Direções disponíveis
    direcoes = {
        "norte": "n", 
        "sul": "s", 
        "leste": "l", 
        "oeste": "o"
    }
    
    # Localizações e descrições
    locais = {
        "norte": ("A Floresta dos Gigantes Caídos", "Uma floresta densa e perigosa, cheia de criaturas hostis."),
        "sul": ("A Fortaleza de Heide", "Uma antiga fortaleza em ruínas, cheia de inimigos e mistérios."),
        "leste": ("A Necrópolis de Shulva", "Um cemitério sombrio, onde as almas perdidas descansam em paz."),
        "oeste": ("O Castelo de Drangleic", "Um imponente castelo de pedra, lar de inúmeros desafios e segredos.")
    }
    
    # Mapeando abreviações para as direções completas
    abreviacoes_para_direcao = {v: k for k, v in direcoes.items()}
    
    # Escolha de movimento
    while True:
        escolha_direcao = input("\nDigite uma direção (norte, sul, leste, oeste ou suas abreviações): ").lower()
        
        # Se a escolha for abreviação, converte para a direção completa
        if escolha_direcao in abreviacoes_para_direcao:
            direcao_escolhida = abreviacoes_para_direcao[escolha_direcao]
        elif escolha_direcao in locais:
            direcao_escolhida = escolha_direcao
        else:
            print("Direção inválida. Por favor, escolha uma direção válida (norte, sul, leste, oeste ou abreviações).")
            continue
        
        # Obter nome e descrição do local escolhido
        local_nome, local_descricao = locais[direcao_escolhida]

        print(f"\nVocê escolheu ir para {local_nome}.")
        print(f"Descrição: {local_descricao}")
        
        confirmacao = input(f"Deseja confirmar essa escolha? (s/n): ").lower()
        if confirmacao == 's':
            print(f"\nVocê começa a sua jornada para o {local_nome}.")
            break
        else:
            print("Escolha de direção cancelada. Vamos tentar novamente.")

# Executar o jogo
if __name__ == "__main__":
    conectar_banco()
    criar_personagem()
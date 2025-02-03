-- Tabela principal de personagens
CREATE TABLE IF NOT EXISTS Personagem (
    idCharacter SERIAL PRIMARY KEY,
    tipoCharacter VARCHAR(20) NOT NULL,
    nome VARCHAR(100) NOT NULL
);

-- Especialização NPC
CREATE TABLE IF NOT EXISTS NPC (
    idNpc SERIAL PRIMARY KEY,
    tipoNpc VARCHAR(20) NOT NULL,
    salaAtual INT,
    idCharacter INT REFERENCES Personagem(idCharacter)
);

-- Subtipos de NPC
CREATE TABLE IF NOT EXISTS Mercante (
    idMercante SERIAL PRIMARY KEY,
    idNpc INT REFERENCES NPC(idNpc)
);

CREATE TABLE IF NOT EXISTS Inimigo (
    idInimigo SERIAL PRIMARY KEY,
    hp INT NOT NULL,
    dano INT NOT NULL,
    idNpc INT REFERENCES NPC(idNpc)
);

CREATE TABLE IF NOT EXISTS Ferreiro (
    idFerreiro SERIAL PRIMARY KEY,
    idNpc INT REFERENCES NPC(idNpc)
);

CREATE TABLE IF NOT EXISTS Boss (
    idBoss SERIAL PRIMARY KEY,
    hp INT NOT NULL,
    dano INT NOT NULL,
    idNpc INT REFERENCES NPC(idNpc)
);

-- Classe
CREATE TABLE IF NOT EXISTS Classe (
    idClasse SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    levelInicial INT NOT NULL,
    dexterityInicial INT NOT NULL,
    strengthInicial INT NOT NULL,
    vigorInicial INT NOT NULL,
    faithInicial INT NOT NULL,
    enduranceInicial INT NOT NULL,
    intelligenceInicial INT NOT NULL
);

-- Player
CREATE TABLE IF NOT EXISTS Player (
    idPlayer SERIAL PRIMARY KEY,
    hpAtual INT NOT NULL,
    health INT NOT NULL,
    dexterity INT NOT NULL,
    strength INT NOT NULL,
    vigor INT NOT NULL,
    faith INT NOT NULL,
    endurance INT NOT NULL,
    intelligence INT NOT NULL,
    idSalaAtual INT NOT NULL,
    coin INT,
    idCharacter INT REFERENCES Personagem(idCharacter),
    idClasse INT REFERENCES Classe(idClasse)
);

-- InstanciaInimigo
CREATE TABLE IF NOT EXISTS InstanciaInimigo (
    nroInstancia SERIAL PRIMARY KEY,
    idInimigo INT REFERENCES Inimigo(idInimigo),
    idArea INT REFERENCES Area(areaNro)
);

-- Item e suas especializações
CREATE TABLE IF NOT EXISTS Item (
    idItem SERIAL PRIMARY KEY,
    nomeItem VARCHAR(100) NOT NULL,
    tipoItem VARCHAR(20) NOT NULL,
    itemDetalhes TEXT,
    preco INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Equipavel (
    idEquipavel SERIAL PRIMARY KEY,
    tipoEquipavel VARCHAR(20) NOT NULL,
    idItem INT REFERENCES Item(idItem)
);

CREATE TABLE IF NOT EXISTS Arma (
    idArma SERIAL PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    dano INT NOT NULL,
    attackSpeed INT NOT NULL,
    efeito TEXT,
    idEquipavel INT REFERENCES Equipavel(idEquipavel)
);

CREATE TABLE IF NOT EXISTS Armadura (
    idArmadura SERIAL PRIMARY KEY,
    resistencia INT NOT NULL,
    bonus TEXT,
    idEquipavel INT REFERENCES Equipavel(idEquipavel)
);

CREATE TABLE IF NOT EXISTS Consumivel (
    idConsumivel SERIAL PRIMARY KEY,
    efeito TEXT,
    duracao INT,
    descricao TEXT,
    idItem INT REFERENCES Item(idItem)
);

-- InstanciaItem
CREATE TABLE IF NOT EXISTS InstanciaItem (
    nroInstancia SERIAL PRIMARY KEY,
    idItem INT REFERENCES Item(idItem)
);

-- Combate
CREATE TABLE IF NOT EXISTS Combate (
    idCombate SERIAL PRIMARY KEY,
    playerId INT REFERENCES Player(idPlayer),
    bossId INT REFERENCES Boss(idBoss),
    derrotado BOOLEAN NOT NULL
);

-- ItemUpgrade
CREATE TABLE IF NOT EXISTS ItemUpgrade (
    idItem INT REFERENCES Item(idItem),
    upgradeDetalhes TEXT NOT NULL
);

-- Região e sala
CREATE TABLE regiao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL
);

CREATE TABLE sala (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    regiao_id INT NOT NULL,
    norte INT,
    sul INT,
    leste INT,
    oeste INT,
    FOREIGN KEY (regiao_id) REFERENCES regiao (id),
    FOREIGN KEY (norte) REFERENCES sala (id),
    FOREIGN KEY (sul) REFERENCES sala (id),
    FOREIGN KEY (leste) REFERENCES sala (id),
    FOREIGN KEY (oeste) REFERENCES sala (id)
);


-- Inventário
CREATE TABLE IF NOT EXISTS Inventario (
    playerId INT REFERENCES Player(idPlayer),
    slot INT NOT NULL,
    item INT REFERENCES InstanciaItem(nroInstancia),
    itemQtd INT NOT NULL,
    PRIMARY KEY (playerId, slot)
);

-- Relacionamentos adicionais
CREATE TABLE IF NOT EXISTS Mercante_Vende (
    idMercante INT REFERENCES Mercante(idMercante),
    nroInstancia INT REFERENCES InstanciaItem(nroInstancia),
    PRIMARY KEY (idMercante, nroInstancia)
);

CREATE TABLE IF NOT EXISTS Ferreiro_Aprimora (
    idFerreiro INT REFERENCES Ferreiro(idFerreiro),
    nroInstancia INT REFERENCES InstanciaItem(nroInstancia),
    PRIMARY KEY (idFerreiro, nroInstancia)
);

CREATE TABLE IF NOT EXISTS Missao (
    idMissao SERIAL PRIMARY KEY,
    nomeMissao VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    objetivoTipo VARCHAR(50) NOT NULL,  -- 'derrotar', 'coletar', etc.
    objetivoQuantidade INT NOT NULL
);

CREATE TABLE IF NOT EXISTS ProgressoMissao (
    idProgresso SERIAL PRIMARY KEY,
    idPlayer INT REFERENCES Player(idPlayer),
    idMissao INT REFERENCES Missao(idMissao),
    progressoAtual INT DEFAULT 0,
    concluida BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS Missao_Recompensa (
    idMissao INT REFERENCES Missao(idMissao),
    coins INT DEFAULT 0,
    PRIMARY KEY (idMissao)
);

-- tabela pra verificar se o player ja falou com o npc
CREATE TABLE IF NOT EXISTS Player_NPC_Interacao (
    idPlayer INT REFERENCES Player(idPlayer),
    idNpc INT REFERENCES NPC(idNpc),
    interagiu BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (idPlayer, idNpc)
);

CREATE OR REPLACE PROCEDURE descansar_em_bonfire(id_player INT, sala_atual INT) AS $$
BEGIN
    IF sala_atual = 1 THEN
        -- Restaura o HP do jogador
        UPDATE Player SET hpAtual = health WHERE idPlayer = id_player;
        RAISE NOTICE 'Você descansou na bonfire e recuperou todo o HP!';
    ELSE
        RAISE EXCEPTION 'Voce so pode descansar na bonfire na sala principal!';
    END IF;
END;
$$ LANGUAGE plpgsql;

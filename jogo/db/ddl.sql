-- Tabela principal de personagens
CREATE TABLE IF NOT EXISTS Character (
    idCharacter SERIAL PRIMARY KEY,
    tipoCharacter VARCHAR(20) NOT NULL,
    nome VARCHAR(100) NOT NULL
);

-- Especialização NPC
CREATE TABLE IF NOT EXISTS NPC (
    idNpc SERIAL PRIMARY KEY,
    tipoNpc VARCHAR(20) NOT NULL,
    idCharacter INT REFERENCES Character(idCharacter)
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

-- Player
CREATE TABLE IF NOT EXISTS Player (
    idPlayer SERIAL PRIMARY KEY,
    hp INT NOT NULL,
    health INT NOT NULL,
    dexterity INT NOT NULL,
    strength INT NOT NULL,
    vigor INT NOT NULL,
    faith INT NOT NULL,
    endurance INT NOT NULL,
    intelligence INT NOT NULL,
    idCharacter INT REFERENCES Character(idCharacter),
    idClasse INT REFERENCES Classe(idClasse)
);

-- Classe
CREATE TABLE IF NOT EXISTS Classe (
    idClasse SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    healthInicial INT NOT NULL,
    dexterityInicial INT NOT NULL,
    strengthInicial INT NOT NULL,
    vigorInicial INT NOT NULL,
    faithInicial INT NOT NULL,
    enduranceInicial INT NOT NULL,
    intelligenceInicial INT NOT NULL
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

-- Região e Área
CREATE TABLE IF NOT EXISTS Regiao (
    regiaoId SERIAL PRIMARY KEY,
    nomeRegiao VARCHAR(100) NOT NULL,
    detalhes TEXT
);

CREATE TABLE IF NOT EXISTS Area (
    areaNro SERIAL PRIMARY KEY,
    nomeArea VARCHAR(100) NOT NULL,
    idRegiao INT REFERENCES Regiao(regiaoId)
);

-- Inventário
CREATE TABLE IF NOT EXISTS Inventario (
    characterId INT REFERENCES Character(idCharacter),
    slot INT NOT NULL,
    item INT REFERENCES InstanciaItem(nroInstancia),
    itemQtd INT NOT NULL,
    PRIMARY KEY (characterId, slot)
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
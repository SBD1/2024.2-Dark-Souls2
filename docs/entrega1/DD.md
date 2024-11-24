# Dicionário de Dados

## **Tabela: Character**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idCharacter         | SERIAL       | PRIMARY KEY      | Identificador único do personagem.            |
| tipoCharacter       | VARCHAR       | NOT NULL, até 50 caracteres        | Tipo do personagem (Player, NPC, etc.).       |
| name                | VARCHAR       | NOT NULL, até 100 caracteres        | Nome do personagem.                           |

---

## **Tabela: Player**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idPlayer            | SERIAL       | PRIMARY KEY      | Identificador único do jogador.               |
| hp                  | INT          | NOT NULL         | Quantidade de pontos de vida atual.           |
| health              | INT          | NOT NULL         | Saúde total do jogador.                       |
| dexterity           | INT          | NOT NULL         | Destreza do jogador.                          |
| strength            | INT          | NOT NULL         | Força do jogador.                             |
| vigor               | INT          | NOT NULL         | Vigor do jogador.                             |
| faith               | INT          | NOT NULL         | Fé do jogador.                                |
| endurance           | INT          | NOT NULL         | Resistência do jogador.                       |
| inteligence         | INT          | NOT NULL         | Inteligência do jogador.                      |

---

## **Tabela: Classe**
| Campo (Atributo)       | Tipo         | Restrição        | Descrição                                  |
|-------------------------|--------------|------------------|-------------------------------------------|
| idClasse               | SERIAL       | PRIMARY KEY      | Identificador único da classe.            |
| name                   | VARCHAR       | NOT NULL, até 100 caracteres         | Nome da classe.                           |
| healthInicial          | INT          | NOT NULL         | Valor inicial de saúde.                   |
| dexterityInicial       | INT          | NOT NULL         | Valor inicial de destreza.                |
| strengthInicial        | INT          | NOT NULL         | Valor inicial de força.                   |
| vigorInicial           | INT          | NOT NULL         | Valor inicial de vigor.                   |
| faithInicial           | INT          | NOT NULL         | Valor inicial de fé.                      |
| enduranceInicial       | INT          | NOT NULL         | Valor inicial de resistência.             |
| inteligenceInicial     | INT          | NOT NULL         | Valor inicial de inteligência.            |

---

## **Tabela: NPC**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idNpc               | SERIAL       | PRIMARY KEY      | Identificador único do NPC.                   |
| tipoNpc             | VARCHAR       | NOT NULL, até 50 caracteres         | Tipo do NPC (Mercante, Ferreiro, Boss, etc.). |

---

## **Tabela: Mercante**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idMercante          | SERIAL       | PRIMARY KEY      | Identificador único do mercante.              |

---

## **Tabela: Ferreiro**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idFerreiro          | SERIAL       | PRIMARY KEY      | Identificador único do ferreiro.              |

---

## **Tabela: Boss**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idBoss              | SERIAL       | PRIMARY KEY      | Identificador único do boss.                  |

---

## **Tabela: Inimigo**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idInimigo           | SERIAL       | PRIMARY KEY      | Identificador único do inimigo.               |

---

## **Tabela: Recompensa**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idRecompensa        | SERIAL       | PRIMARY KEY      | Identificador único da recompensa.            |
| expDropado          | INT          | NOT NULL         | Experiência concedida pela recompensa.        |
| itemDropado         | TEXT       |         | Nome do item concedido pela recompensa.       |

---

## **Tabela: Missão**
| Campo (Atributo)       | Tipo         | Restrição        | Descrição                                  |
|-------------------------|--------------|------------------|-------------------------------------------|
| idMissao               | SERIAL       | PRIMARY KEY      | Identificador único da missão.            |
| descricaoMissao        | TEXT       |          | Descrição da missão.                      |
| expMissao              | INT          | NOT NULL         | Experiência concedida ao completar.       |

---

## **Tabela: Mundo**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idMundo             | SERIAL       | PRIMARY KEY      | Identificador único do mundo.                 |
| nomeMundo           | VARCHAR       | NOT NULL, até 100 caracteres         | Nome do mundo.                                |
| descricaoMundo      | TEXT       |          | Descrição do mundo.                           |

---

## **Tabela: Local**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idLocal             | SERIAL       | PRIMARY KEY      | Identificador único do local.                 |
| nomeLocal           | VARCHAR       | NOT NULL, até 50 caracteres        | Nome do local.                                |
| tamanhoLocal        | INT          | NOT NULL         | Tamanho do local.                             |
| descricaoLocal      | TEXT       |          | Descrição do local.                           |

---

## **Tabela: Inventário**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idInventario        | SERIAL       | PRIMARY KEY      | Identificador único do inventário.            |
| qtdItens            | INT          | NOT NULL         | Quantidade de itens no inventário.            |

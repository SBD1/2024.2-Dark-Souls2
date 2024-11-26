# Dicionário de Dados

## **Tabela: Character**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idCharacter         | SERIAL       | PRIMARY KEY      | Identificador único do personagem.            |
| tipoCharacter       | VARCHAR      | NOT NULL         | Tipo do personagem.                           |
| nome                | VARCHAR      | NOT NULL         | Nome do personagem.                           |

---

## **Tabela: NPC**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idNpc               | SERIAL       | PRIMARY KEY      | Identificador único do NPC.                   |
| tipoNpc             | VARCHAR      | NOT NULL         | Tipo do NPC.                                  |

---

## **Tabela: Mercante**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idMercante          | SERIAL       | PRIMARY KEY      | Identificador único do mercante.              |

---

## **Tabela: Inimigo**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idInimigo           | SERIAL       | PRIMARY KEY      | Identificador único do inimigo.               |
| hp                  | INT          | NOT NULL         | Pontos de vida do inimigo.                    |
| dano                | INT          | NOT NULL         | Dano causado pelo inimigo.                    |

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
| hp                  | INT          | NOT NULL         | Pontos de vida do boss.                       |
| dano                | INT          | NOT NULL         | Dano causado pelo boss.                       |

---

## **Tabela: Player**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| hp                  | INT          | NOT NULL         | Pontos de vida atuais do jogador.             |
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
| nome                   | VARCHAR      | NOT NULL         | Nome da classe.                           |
| healthInicial          | INT          | NOT NULL         | Valor inicial de saúde.                   |
| dexterityInicial       | INT          | NOT NULL         | Valor inicial de destreza.                |
| strengthInicial        | INT          | NOT NULL         | Valor inicial de força.                   |
| vigorInicial           | INT          | NOT NULL         | Valor inicial de vigor.                   |
| faithInicial           | INT          | NOT NULL         | Valor inicial de fé.                      |
| enduranceInicial       | INT          | NOT NULL         | Valor inicial de resistência.             |
| intelligenceInicial    | INT          | NOT NULL         | Valor inicial de inteligência.            |

---

## **Tabela: InstanciaInimigo**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| nroInstancia        | SERIAL       | PRIMARY KEY      | Número da instância do inimigo.              |

---

## **Tabela: Item**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| idItem              | SERIAL       | PRIMARY KEY      | Identificador único do item.                 |
| nomeItem            | VARCHAR      | NOT NULL         | Nome do item.                                |
| tipoItem            | VARCHAR      | NOT NULL         | Tipo do item.                                |
| itemDetalhes        | TEXT         |                  | Detalhes do item.                            |
| preco               | INT          | NOT NULL         | Preço do item.                               |

---

## **Tabela: Equipavel**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| tipoEquipavel       | VARCHAR      | NOT NULL         | Tipo de item equipável.                      |

---

## **Tabela: Arma**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| tipo                | VARCHAR      | NOT NULL         | Tipo de arma.                                |
| dano                | INT          | NOT NULL         | Dano causado pela arma.                      |
| attackSpeed         | INT          | NOT NULL         | Velocidade de ataque da arma.                |
| efeito              | VARCHAR      |                  | Efeito adicional da arma.                    |

---

## **Tabela: Armadura**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| resistencia         | INT          | NOT NULL         | Resistência da armadura.                     |
| bonus               | VARCHAR      |                  | Bônus concedido pela armadura.               |

---

## **Tabela: Consumivel**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| efeito              | VARCHAR      | NOT NULL         | Efeito do consumível.                        |
| duracao             | INT          | NOT NULL         | Duração do efeito.                           |
| descricao           | TEXT         |                  | Descrição do consumível.                     |

---

## **Tabela: InstanciaItem**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| nroInstancia        | SERIAL       | PRIMARY KEY      | Número da instância do item.                 |

---

## **Tabela: Regiao**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| regiaoId            | SERIAL       | PRIMARY KEY      | Identificador único da região.               |
| nomeRegiao          | VARCHAR      | NOT NULL         | Nome da região.                              |
| detalhes            | TEXT         |                  | Detalhes da região.                          |

---

## **Tabela: Area**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| areaNro             | SERIAL       | PRIMARY KEY      | Número da área.                              |

---

## **Tabela: Inventario**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| characterId         | INT          | NOT NULL         | Identificador do personagem dono do inventário. |
| slot                | INT          | NOT NULL         | Número do slot no inventário.                |
| item                | INT          | NOT NULL         | Identificador do item.                       |
| itemQtd             | INT          | NOT NULL         | Quantidade do item no inventário.            |

---

## **Tabela: Combate**
| Campo (Atributo)   | Tipo         | Restrição        | Descrição                                     |
|---------------------|--------------|------------------|-----------------------------------------------|
| playerId            | INT          | NOT NULL         | Identificador do jogador.                    |
| bossId              | INT          | NOT NULL         | Identificador do boss.                       |
| derrotado           | BOOLEAN      | NOT NULL         | Indica se o boss foi derrotado.              |

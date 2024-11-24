# Modelo Entidade-Relacionamento

## 1. Entidades

- **Character**
  - **NPC**
    - **Mercante**
    - **Inimigo**
    - **Ferreiro**
    - **Boss**
  - **Player**
- **Classe**
- **Item**
- **Recompensa**
- **Missão**
- **Mundo**
- **Local**
- **Inventário**

## 2. Atributos

- **Personagem**: <ins>idCharacter</ins>, tipoCharacter, name;
  - **NPC**: <ins>idNpc</ins>, tipoNpc;
    - **Mercante**: <ins>idMercante</ins>;
    - **Inimigo**: <ins>idInimigo</ins>;
    - **Ferreiro**: <ins>idFerreiro</ins>;
    - **Boss**: <ins>idBoss</ins>;
  - **Player**: <ins>idPlayer</ins>, hp, health, dexterity, strength, vigor, faith, endurance, inteligence;
- **Classe**: <ins>idClasse</ins>, name, healthInicial, dexterityInicial, strengthInicial, vigorInicial, faithInicial, enduranceInicial, inteligenceInicial;
- **Item**: <ins>idItem</ins>, nomeItem, descricaoItem, levelMinimo, poderItem, defesaItem, vidaAdicional;
- **Recompensa**: <ins>idRecompensa</ins>, expDropado, itemDropado;
- **Missão**: <ins>idMissao</ins>, descricaoMissão, expMissao;
- **Mundo**: <ins>idMundo</ins>, nomeMundo, descricaoMundo;
- **Local**: <ins>idLocal</ins>, nomeLocal, tamanhoLocal, descricaoLocal;
- **Inventário**: <ins>idInventario</ins>, qtdItens;

## 3. Relacionamentos

**Player _cumpre_ uma Missao**

- Um player cumpre nenhuma ou várias missões (0,N)
- A missão é cumprida por um ou vários players (1,N)

**Player _conversa_ com um NPC**

- O player conversa com um NPC (1,1)
- O NPC conversa com um player (1,1)

**Player _abre_ Inventário**

- O player abre um inventário (1,1)
- O inventário é aberto por um player (1,1)

**Player _recebe_ Recompensa**

- O player recebe nenhuma ou várias recompensas (0,N)
- O inventário é recebida por nenhum ou um player (0,1)
  
**Player _ataca_ Inimigo**

- O player ataca um ou vários inimigos (1,N)
- O inimigo é atacado por um ou vários players (1,N)

**Player _está_ em um Local**

- O player está em um local (1,1)
- O local pode ter nenhum ou vários players (0,N)

**Player _equipa_ um Item**

- O player equipa um ou vários itens (1,N)
- O item é equipado por um player (1,1)

**Player _viaja_ para um Local**

- O player viaja para um ou vários locais (1,N)
- O local foi destino final de nenhum ou vários players (0,N)

**Mundo _possui_ um Local**

- O mundo possui nenhum ou vários locais (0,N)
- O local está em um mundo (1,1)

**Monstro _dropa_ uma Recompensa**

- O monstro dropa uma recompensa (1,1)
- A recompensa é dropada por um ou vários mosntros (1,N)

**Local _possui_ um Monstro**

- O local possui nenhum ou vários monstros (0,N)
- O monstro está em um local (1,1)

**Inventário _possui_ Item**

- O inventário possui nenhum ou vários itens (0,N)
- O item está em um inventário (1,1)

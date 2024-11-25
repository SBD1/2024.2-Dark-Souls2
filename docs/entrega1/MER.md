# Modelo Entidade-Relacionamento

## 1. Entidades

- **Character**
  - **NPC**
    - **Mercante**
    - **Inimigo**
    - **Ferreiro**
    - **Boss**
  - **Player**
- **_InstanciaInimigo_**
- **Classe**
- **Item**
  - **Equipavel**
    - **Arma**
    - **Armadura**
  - **Consumivel**
- **_InstanciaItem_**
- **Regiao**
- **_Area_**
- **Inventario**
- **Combate**
- **ItemUpgrade**

## 2. Atributos

- **Character**: <ins>idCharacter</ins>, tipoCharacter, nome;
  - **NPC**: <ins>idNpc</ins>, tipoNpc;
    - **Mercante**: <ins>idMercante</ins>;
    - **Inimigo**: <ins>idInimigo</ins>, hp, dano;
    - **Ferreiro**: <ins>idFerreiro</ins>;
    - **Boss**: <ins>idBoss</ins>, hp, dano;
  - **Player**:  hp, health, dexterity, strength, vigor, faith, endurance, inteligence;
- **Classe**: <ins>idClasse</ins>, nome, healthInicial, dexterityInicial, strengthInicial, vigorInicial, faithInicial, enduranceInicial, intelligenceInicial;
- **_InstanciaInimigo_**: <ins>nroInstancia</ins>
- **Item**: <ins>idItem</ins>, nomeItem, tipoItem, itemDetalhes, Preço;
  - **Equipavel**: tipoEquipavel;
    - **Arma**: tipo, dano, attackSpeed, efeito;
    - **Armadura**: resistencia, bonus;
  - **Consumivel**: efeito, duração, descrição;
- **_InstanciaItem_**: <ins>nroInstancia</ins>;
- **Regiao**: <ins>regiaoId</ins>, nomeRegiao, detalhes;
- **_Area_**: <ins>areaNro</ins>
- **Inventario**: <ins>characterId</ins>, <ins>slot</ins>, item, itemQtd;
- **Combate**: <ins>playerId</ins>, <ins>bossId</ins>, derrotado;



## 3. Relaciontos

**Player _possui_ uma Classe**

- Um player possui uma classe (1,1)
- A classe é possuida por nenhum ou vários players (0,N)

**Inimigo _possui_ uma InstanciaInimigo**

- Um Inimigo possui nenhuma ou várias InstanciasInimigo (0,N)
- A InstanciaInimigo é possuida por um Inimigo (1,1)

**Player _enfrenta_ uma InstanciaInimigo**

- Um player enfrenta nenhuma ou várias instanciaInimigo (0,N)
- A InstanciaInimigo é enfrentada por nenhum ou vários players (0,N)

**Player _enfrenta_ um Boss**

- Um player enfrenta nenhum ou vários Boss (0,N)
- O boss é enfrentado por nenhum ou vários players (0,N)
  
**Boss _dropa_ uma InstanciaItem**

- Um boss dropa uma InstanciaItem (1,1)
- A instanciaItem é dropada por nenhum ou um Boss (0,1)

**Boss _está_ em uma Area**

- Um boss dropa uma InstanciaItem (1,1)
- A instanciaItem é dropada por nenhum ou um Boss (0,1)
  
**Character _possui_ Inventário**

- O player possui um inventário (1,1)
- O inventário é possuido por um player (1,1)

**Player _está_ em um Area**

- O player está em uma Area (1,1)
- A Area pode ter nenhum ou vários players (0,N)

**Player _consome_InstanciaItem **

- O player consome InstanciaItem (0,1)
- A InstanciaItem pode ser consumida por player (1,N)

**Player _equipa_ uma InstanciaItem**

- O player equipa um ou vários itens (1,N)
- O item é equipado por um player (1,1)

**Player _consome_ uma InstanciaItem**

- O Player consome um ou várias InstanciaItem (1,N)
- A InstanciaItem é equipado por um Player (1,1)

- **Player _equipa_InstanciaItem **

- O player equipa um InstanciaItem (0,1)
- A InstanciaItem pode ser equipada por player (1,N)


**Player _viaja_ para um Area**

- O player viaja para um ou vários locais (1,N)
- A area foi destino final de nenhum ou vários players (0,N)

**A Area _pertence_ a uma Regiao**

- A Area pertence a uma Regiao (1,1)
- A Regiao pertence uma ou várias Area (1,1)


**A InstanciaInimigo _está_ em uma Area**

- A InstanciaInimigo está em nenhuma ou uma Area (0,1)
- A Area tem nenhuma ou várias InstanciaInimigo (0,n)

**O Mercante _está_ em uma Area**

- O  Mercante está em uma Area (1,1)
- A Area tem nenhum ou um Mercante (0,1)

**O Ferreiro _está_ em uma Area**

- O  Ferreiro está em uma Area (1,1)
- A Area tem nenhum ou um Ferreiro (0,1)

**Mercante _vende_ InstanciaItem**

- O mercante vende nenhum ou várias InstanciaItem (0,n)
- O item é vendido por nenhum ou vários Mercante (0,n)

**Ferreiro _aprimora_ InstanciaItem**

- O Ferreiro aprimora nenhum ou várias InstanciaItem (0,n)
- O item é aprimorado por nenhum ou vários Ferreiro (0,n)

**Inventario _contem_ InstanciaItem**

- O inventário possui nenhum ou várias InstanciaItem (0,N)
- O InstanciaItem está em nenhum ou um Inventario (0,1)

# Modelo Entidade-Relacionamento

## 1. Entidades

- **Character**
  - **NPC**
    - **Mercante**
    - **Inimigo**
    - **Ferreiro**
    - **Boss**
  - **Player**
- **InstanciaInimigo**
- **Classe**
- **Item**
  - **Equipavel**
  - **Consumivel**
- **InstanciaItem**
- **Recompensa**
- **Missao**
- **Mundo**
- **Local**
- **Inventario**
- **Combate**
- **ItemUpgrade**

## 2. Atributos

- **Personagem**: <ins>idCharacter</ins>, tipoCharacter, nome;
  - **NPC**: <ins>idNpc</ins>, tipoNpc;
    - **Mercante**: <ins>idMercante</ins>;
    - **Inimigo**: <ins>idInimigo</ins>, hp, dano;
    - **Ferreiro**: <ins>idFerreiro</ins>;
    - **Boss**: <ins>idBoss</ins>, hp, dano;
  - **Player**: <ins>idPlayer</ins>, hp, health, dexterity, strength, vigor, faith, endurance, inteligence;
- **Classe**: <ins>idClasse</ins>, nome, healthInicial, dexterityInicial, strengthInicial, vigorInicial, faithInicial, enduranceInicial, inteligenceInicial;
- **InstanciaInimigo**: <ins>nroInstancia</ins>
- **Item**: <ins>idItem</ins>, nomeItem, tipoItem;
  - **Equipavel**:
  - **Consumivel**:
- **InstanciaItem**: <ins>nroInstancia</ins>;
- **Recompensa**: <ins>idRecompensa</ins>, expDropado, itemDropado;
- **Missao**: <ins>idMissao</ins>, descricaoMissão, expMissao;
- **Mundo**: <ins>idMundo</ins>, nomeMundo, descricaoMundo;
- **Local**: <ins>idLocal</ins>, nomeLocal, tamanhoLocal, descricaoLocal;
- **Inventario**: <ins>idInventario</ins>, <ins>slot</ins>;
- **Combate**: <ins>idPlayer</ins>, <ins>bossId</ins>, derrotado;
- **ItemUpgrade**: <ins>idItem</ins>, upgradeDetalhes;



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
  
**Character _possui_ Inventário**

- O player possui um inventário (1,1)
- O inventário é possuido por um player (1,1)

**Mercante _vende_ InstanciaItem**

- O mercante vende nenhum ou várias InstanciaItem (0,n)
- O item é vendido por nenhum ou vários Mercante (0,n)

**Ferreiro _aprimora_ InstanciaItem**

- O Ferreiro aprimora nenhum ou várias InstanciaItem (0,n)
- O item é aprimorado por nenhum ou vários Ferreiro (0,n)

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


**Local _possui_ um Inimigo**

- O local possui nenhum ou vários Inimigo (0,N)
- O Inimigo está em um local (1,1)

**Inventario _contem_ InstanciaItem**

- O inventário possui nenhum ou várias InstanciaItem (0,N)
- O InstanciaItem está em nenhum ou vários Inventario (1,1)

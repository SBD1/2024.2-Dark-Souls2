INSERT INTO Classe (nome, levelInicial, dexterityInicial, strengthInicial, vigorInicial, faithInicial, enduranceInicial, intelligenceInicial)
VALUES
('Warrior', 12, 11, 15, 7, 5, 6, 5),
('Knight', 13, 8, 11, 12, 6, 6, 3),
('Swordsman', 12, 16, 9, 4, 5, 8, 7),
('Bandit', 11, 14, 9, 9, 8, 7, 1),
('Cleric', 14, 5, 11, 10, 12, 3, 4),
('Sorcerer', 11, 7, 3, 5, 4, 6, 14),
('Explorer', 10, 6, 6, 7, 5, 6, 5),
('Deprived', 1, 6, 6, 6, 6, 6, 6);

-- Inserindo personagens na tabela Personagem
INSERT INTO Personagem (tipoCharacter, nome)
VALUES
('NPC', 'Emerald Herald'), -- Mercante
('NPC', 'Blacksmith Lenigrast'), -- Ferreiro
('NPC', 'Straid of Olaphis'), -- Mercante
('NPC', 'Hollow Soldier'), -- Inimigo
('NPC', 'The Pursuer'); -- Boss

-- Associando Personagens à tabela NPC
INSERT INTO NPC (tipoNpc, idCharacter)
VALUES
('Mercante', 1), -- Emerald Herald
('Ferreiro', 2), -- Blacksmith Lenigrast
('Mercante', 3), -- Straid of Olaphis
('Inimigo', 4), -- Hollow Soldier
('Boss', 5); -- The Pursuer

-- Inserindo detalhes em subtipos de NPC
-- Mercante
INSERT INTO Mercante (idNpc) VALUES (1); -- Emerald Herald
INSERT INTO Mercante (idNpc) VALUES (3); -- Straid of Olaphis

-- Ferreiro
INSERT INTO Ferreiro (idNpc) VALUES (2); -- Blacksmith Lenigrast

-- Inimigo
INSERT INTO Inimigo (hp, dano, idNpc)
VALUES
(300, 30, 4); -- Hollow Soldier

-- Boss
INSERT INTO Boss (hp, dano, idNpc)
VALUES
(3200, 150, 5); -- The Pursuer

-- Inserindo itens na tabela Item
INSERT INTO Item (nomeItem, tipoItem, itemDetalhes, preco)
VALUES
('Estus Flask', 'Consumível', 'Frasco que restaura HP ao ser consumido', 0), -- Consumível
('Claymore', 'Equipável', 'Espada longa com alto alcance e versatilidade', 1500), -- Arma
('Drangleic Shield', 'Equipável', 'Escudo resistente com alta defesa física', 2000), -- Armadura
('Green Blossom', 'Consumível', 'Aumenta temporariamente a regeneração de stamina', 300), -- Consumível
('Elite Knight Armor', 'Equipável', 'Conjunto de armadura robusto com boa resistência', 5000); -- Armadura

-- Associando itens à tabela Equipavel
INSERT INTO Equipavel (tipoEquipavel, idItem)
VALUES
('Arma', 2), -- Claymore
('Armadura', 3), -- Drangleic Shield
('Armadura', 5); -- Elite Knight Armor

-- Inserindo detalhes na tabela Arma
INSERT INTO Arma (tipo, dano, attackSpeed, efeito, idEquipavel)
VALUES
('Espada Longa', 150, 100, 'Causa dano físico e bônus em força', 1); -- Claymore

-- Inserindo detalhes na tabela Armadura
INSERT INTO Armadura (resistencia, bonus, idEquipavel)
VALUES
(75, 'Aumenta a resistência a impactos', 2), -- Drangleic Shield
(120, 'Concede resistência moderada a fogo', 3); -- Elite Knight Armor

-- Inserindo detalhes na tabela Consumivel
INSERT INTO Consumivel (efeito, duracao, descricao, idItem)
VALUES
('Restaura 50% do HP total', NULL, 'Usado para recuperar saúde durante o combate', 1), -- Estus Flask
('Aumenta regeneração de stamina', 60, 'Ideal para combates prolongados ou fuga rápida', 4); -- Green Blossom

-- Inserindo regiões na tabela Regiao
INSERT INTO Regiao (nomeRegiao, detalhes)
VALUES
('Majula', 'A pacata vila que serve como o principal ponto de encontro para os viajantes.'),
('Forest of Fallen Giants', 'Uma floresta em ruínas repleta de soldados ocos e segredos.'),
('Heides Tower of Flame', 'Uma área costeira com torres antigas iluminadas por chamas.'),
('The Lost Bastille', 'Uma fortaleza sombria repleta de prisioneiros enlouquecidos.'),
('Drangleic Castle', 'O castelo majestoso e sombrio do reino de Drangleic.');

-- Inserindo áreas associadas às regiões na tabela Area
INSERT INTO Area (nomeArea, idRegiao)
VALUES
('The Far Fire', 1), -- Majula
('Cardinal Tower', 2), -- Forest of Fallen Giants
('Heides Ruins', 3), -- Heides Tower of Flame
('Sinners Rise', 4), -- The Lost Bastille
('Throne Room', 5); -- Drangleic Castle
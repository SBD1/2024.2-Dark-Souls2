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
('NPC', 'The Last Giant'); -- Boss

-- Associando Personagens à tabela NPC
INSERT INTO NPC (tipoNpc, idCharacter)
VALUES
('Mercante', 1), -- Emerald Herald
('Ferreiro', 2), -- Blacksmith Lenigrast
('Mercante', 3), -- Straid of Olaphis
('Inimigo', 4), -- Hollow Soldier
('Boss', 5); -- The Last Giant

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
INSERT INTO Regiao (nome, descricao)
VALUES
('Majula', 'A pacata vila que serve como o principal ponto de encontro para os viajantes.'),
('Forest of Fallen Giants', 'Uma floresta em ruínas repleta de soldados ocos e segredos.'),
('Heides Tower of Flame', 'Uma área costeira com torres antigas iluminadas por chamas.'),
('The Lost Bastille', 'Uma fortaleza sombria repleta de prisioneiros enlouquecidos.'),
('Drangleic Castle', 'O castelo majestoso e sombrio do reino de Drangleic.');

-- Salas em Majula
INSERT INTO sala (nome, descricao, regiao_id) VALUES
('Praça Principal', 'O ponto central de Majula, com vista para o oceano, há um Homem com barba e cabelo grisalho ao lado de uma carroça.', 1),
('Poço', 'Um poço profundo com rumores de conter segredos.', 1),
('Mercado', 'Local onde os mercantes ficam.', 1);

-- Salas na Forest of Fallen Giants
INSERT INTO sala (nome, descricao, regiao_id) VALUES
('Entrada da Floresta', 'A entrada coberta por árvores densas.', 2),
('Ruínas', 'Estruturas antigas parcialmente cobertas por vegetação, há alguns lobos.', 2),
('Ponte', 'Uma ponte estreita conectando partes da floresta.', 2),
('Cavernas', 'Um sistema de cavernas escuras e úmidas, aranhas por todo o lado.', 2),
('Sala do Chefe', 'Um espaço amplo onde está adormecido em um grande trono um grande inimigo conhecido como The Last Giant.', 2);

-- Salas em Heide's Tower of Flame
INSERT INTO sala (nome, descricao, regiao_id) VALUES
('Costa', 'A costa com o som relaxante das ondas.', 3),
('Torre Iluminada', 'Uma torre antiga que brilha com uma luz misteriosa.', 3),
('Passagem Submersa', 'Uma passagem parcialmente coberta por água.', 3),
('Sala do Dragão', 'Um local onde uma poderosa criatura reside.', 3);

-- Salas em The Lost Bastille
INSERT INTO sala (nome, descricao, regiao_id) VALUES
('Entrada do Forte', 'Uma entrada pesada, protegida por grandes portas.', 4),
('Celas', 'Pequenos quartos sombrios para prisioneiros.', 4),
('Corredor Principal', 'Um longo corredor com pouca iluminação.', 4),
('Torre de Vigia', 'Uma torre alta usada para observação.', 4);

-- Salas em Drangleic Castle
INSERT INTO sala (nome, descricao, regiao_id) VALUES
('Entrada', 'O imponente portão principal do castelo.', 5),
('Sala do Trono', 'Um salão majestoso com um trono ao fundo.', 5),
('Biblioteca', 'Uma sala cheia de livros antigos e poeira.', 5),
('Sala do Guarda Real', 'Uma sala onde os guardas do rei repousam.', 5),
('Masmorras', 'Uma área fria e úmida usada para manter prisioneiros.', 5);


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
('NPC', 'Black Wolf'), -- Inimigo
('NPC', 'The Last Giant'); -- Boss

-- Associando Personagens à tabela NPC
INSERT INTO NPC (tipoNpc, idCharacter, salaAtual)
VALUES
('Mercante', 1, 1), -- Emerald Herald
('Ferreiro', 2, 2), -- Blacksmith Lenigrast
('Mercante', 3, 3), -- Straid of Olaphis
('Inimigo', 4, 4), -- Black Wolf
('Boss', 5, 8); -- The Last Giant

-- Inserindo detalhes em subtipos de NPC
-- Mercante
INSERT INTO Mercante (idNpc) VALUES (1); -- Emerald Herald
INSERT INTO Mercante (idNpc) VALUES (3); -- Straid of Olaphis

-- Ferreiro
INSERT INTO Ferreiro (idNpc) VALUES (2); -- Blacksmith Lenigrast

-- Inimigo
INSERT INTO Inimigo (hp, dano, idNpc)
VALUES
(50, 5, 4); -- Black wolf

-- Boss
INSERT INTO Boss (hp, dano, idNpc)
VALUES
(1500, 30, 5); -- The Pursuer

-- Inserindo itens na tabela Item
INSERT INTO Item (nomeItem, tipoItem, itemDetalhes, preco)
VALUES
('Estus Flask', 'Consumível', 'Frasco que restaura HP ao ser consumido', 0), -- Consumível
('Claymore', 'Equipável', 'Espada longa com alto alcance e versatilidade', 500), -- Arma
('Drangleic Shield', 'Equipável', 'Escudo resistente com alta defesa física', 500), -- Armadura
('Green Blossom', 'Consumível', 'Aumenta temporariamente a regeneração de stamina', 300), -- Consumível
('Elite Knight Armor', 'Equipável', 'Conjunto de armadura robusto com boa resistência', 1000); -- Armadura

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
('Heides Tower of Flame', 'Uma area costeira com torres antigas iluminadas por chamas.'),
('The Lost Bastille', 'Uma fortaleza sombria repleta de prisioneiros enlouquecidos.'),
('Drangleic Castle', 'O castelo majestoso e sombrio do reino de Drangleic.');

-- Salas em Majula
INSERT INTO sala (nome, descricao, regiao_id) VALUES
('Praca Principal', 'O ponto central de Majula, com vista para o oceano, ha um Homem com barba e cabelo grisalho ao lado de uma carroca.', 1),
('Lago', 'Um lago profundo com rumores de conter segredos.', 1),
('Mercado', 'Local onde os mercantes ficam.', 1);

-- Salas na Forest of Fallen Giants
INSERT INTO sala (nome, descricao, regiao_id) VALUES
('Entrada da Floresta', 'A entrada coberta por arvores densas.', 2),
('Ruinas', 'Estruturas antigas parcialmente cobertas por vegetação, ha alguns lobos.', 2),
('Ponte', 'Uma ponte estreita conectando partes da floresta.', 2),
('Cavernas', 'Um sistema de cavernas escuras e umidas, aranhas por todo o lado.', 2),
('Sala do Chefe', 'Um espaço amplo onde esta adormecido em um grande trono um grande inimigo conhecido como The Last Giant.', 2);

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
('Corredor Principal', 'Um longo corredor com pouca iluminacao.', 4),
('Torre de Vigia', 'Uma torre alta usada para observacao.', 4);

-- Salas em Drangleic Castle
INSERT INTO sala (nome, descricao, regiao_id) VALUES
('Entrada', 'O imponente portao principal do castelo.', 5),
('Sala do Trono', 'Um salao majestoso com um trono ao fundo.', 5),
('Biblioteca', 'Uma sala cheia de livros antigos e poeira.', 5),
('Sala do Guarda Real', 'Uma sala onde os guardas do rei repousam.', 5),
('Masmorras', 'Uma área fria e úmida usada para manter prisioneiros.', 5);

-- Majula
UPDATE sala SET norte = 2, sul = 4, leste = 3, oeste = NULL WHERE id = 1; -- Praça Principal
UPDATE sala SET norte = NULL, sul = 1, leste = NULL, oeste = NULL WHERE id = 2; -- Lago
UPDATE sala SET norte = NULL, sul = NULL, leste = NULL, oeste = 1 WHERE id = 3; -- Mercado

-- Forest of Fallen Giants
UPDATE sala SET norte = 1, sul = 5, leste = 1, oeste = 9 WHERE id = 4; -- Entrada da Floresta
UPDATE sala SET norte = 4, sul = 6, leste = NULL, oeste = NULL WHERE id = 5; -- Ruínas
UPDATE sala SET norte = 5, sul = 7, leste = NULL, oeste = NULL WHERE id = 6; -- Ponte
UPDATE sala SET norte = 6, sul = 8, leste = NULL, oeste = NULL WHERE id = 7; -- Cavernas
UPDATE sala SET norte = 7, sul = NULL, leste = NULL, oeste = NULL WHERE id = 8; -- Sala do Chefe

-- Heide's Tower of Flame
UPDATE sala SET norte = NULL, sul = 10, leste = 4, oeste = 13 WHERE id = 9; -- Costa
UPDATE sala SET norte = 9, sul = 11, leste = NULL, oeste = NULL WHERE id = 10; -- Torre Iluminada
UPDATE sala SET norte = 10, sul = 12, leste = NULL, oeste = NULL WHERE id = 11; -- Passagem Submersa
UPDATE sala SET norte = 11, sul = NULL, leste = NULL, oeste = NULL WHERE id = 12; -- Sala do Dragão

-- The Lost Bastille
UPDATE sala SET norte = NULL, sul = 14, leste = 9, oeste = 17 WHERE id = 13; -- Entrada do Forte
UPDATE sala SET norte = 13, sul = 15, leste = NULL, oeste = NULL WHERE id = 14; -- Celas
UPDATE sala SET norte = 14, sul = 16, leste = NULL, oeste = NULL WHERE id = 15; -- Corredor Principal
UPDATE sala SET norte = 15, sul = NULL, leste = NULL, oeste = NULL WHERE id = 16; -- Torre de Vigia

-- Drangleic Castle
UPDATE sala SET norte = NULL, sul = 18, leste = 13, oeste = NULL WHERE id = 17; -- Entrada
UPDATE sala SET norte = 17, sul = 19, leste = NULL, oeste = NULL WHERE id = 18; -- Sala do Trono
UPDATE sala SET norte = 18, sul = 20, leste = NULL, oeste = NULL WHERE id = 19; -- Biblioteca
UPDATE sala SET norte = 19, sul = 21, leste = NULL, oeste = NULL WHERE id = 20; -- Sala do Guarda Real
UPDATE sala SET norte = 20, sul = NULL, leste = NULL, oeste = NULL WHERE id = 21; -- Masmorras

INSERT INTO InstanciaItem (idItem) VALUES (1), (2), (3), (4), (5);

-- Associando os itens vendidos por cada mercante
INSERT INTO Mercante_Vende (idMercante, nroInstancia) 
VALUES
(1, 1),
(1, 4), 
(2, 2), 
(2, 3), 
(2, 5);

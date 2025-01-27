from criacao_personagem import Personagem

Teste =  Personagem(nome = 'Durin Thunderaxe',
                         forca = 6,
                         destreza = 16,
                         constituicao = 12,
                         inteligencia = 18,
                         sabedoria = 14,
                         carisma = 12,
                         raca = 'anão',
                         classe = 'mago',
                         nivel = 8,
                         pericia1 = 'conhecimento',
                         linguagem = 'Valkar | Gnomica | Abissal | Terran | Celestial',
                         conhecimentos = 'Arcano | Natureza | História | Religião',
                         tipo_oficio = 'Alquimia'
                         )

Teste.add_equipamento('Armadura completa')
Teste.add_equipamento('Escudo leve')
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
                         tipo_oficio = 'Alquimia',
                         img = 'images/avatar.jpg'
                         )

Teste.add_equipamento('Armadura completa')
Teste.add_equipamento('Escudo leve')

Teste.add_magia('Abençoar Água')
Teste.add_magia('Abrir/Fechar')
Teste.add_magia('Adivinhação')

Teste.add_musica('Fascinar')
Teste.add_musica('Inspirar Coragem')

Teste.add_talento('Acerto Crítico Aprimorado')
Teste.add_talento('Acuidade com Arma')

Teste2 =  Personagem(nome = 'Tundra',
                         forca = 2,
                         destreza = 4,
                         constituicao = 5,
                         inteligencia = 2,
                         sabedoria = 19,
                         carisma = 25,
                         raca = 'humano',
                         classe = 'bardo',
                         nivel = 8,
                         pericia1 = 'conhecimento',
                         conhecimentos = 'Geografia',
                         tipo_oficio = 'Alquimia'
                         )
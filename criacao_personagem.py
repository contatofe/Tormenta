from dicionario_equipamentos import equipamentos_lista
from dicionario_golpes import golpes
from dicionario_habilidades_classe import habilidades_classe_descritivos
from dicionario_habilidades_raca import habilidades_raca_descritivos
from dicionario_magias import magias
from dicionario_musicas import musicas
from dicionario_talentos import talentos_descritivos

class Personagem:

    # Modificadores por raça

    modificadores_de_raca = {
        'anão': {'constituicao': 4, 'sabedoria': 2, 'destreza': -2},
        'elfo': {'destreza': 4, 'inteligencia': 2, 'constituicao': -2},
        'goblin': {'destreza': 4, 'constituicao': 2, 'carisma': -2},
        'halfling': {'destreza': 4, 'carisma': 2, 'forca': -2},
        'minotauro': {'forca': 4, 'constituicao': 2, 'carisma': -2},
        'qareen': {'carisma': 4, 'inteligencia': 2, 'sabedoria': -2},
        'gnomo': {'destreza': 2, 'habilidade': 2},
        'lefou': {'carisma': 4, 'habilidade': 2, 'habilidade2': 2},
        'meio elfo': {'destreza': 2, 'habilidade': 2},
        'meio orc': {'forca': 2, 'habilidade': 2}
    }
   
    # Bônus base de ataque por classe

    bba_classe = {
        'bárbaro': {i: {'BBA': i} for i in range(1, 21)},
        'bardo': {1: {'BBA': 0}, 2: {'BBA': 1}, 3: {'BBA': 2}, 4: {'BBA': 3}, 5: {'BBA': 3},
                  6: {'BBA': 4}, 7: {'BBA': 5}, 8: {'BBA': 6}, 9: {'BBA': 6}, 10: {'BBA': 7},
                  11: {'BBA': 8}, 12: {'BBA': 9}, 13: {'BBA': 9}, 14: {'BBA': 10}, 15: {'BBA': 11},
                  16: {'BBA': 12}, 17: {'BBA': 12}, 18: {'BBA': 13}, 19: {'BBA': 14}, 20: {'BBA': 15}},
        'clerigo': {1: {'BBA': 0}, 2: {'BBA': 1}, 3: {'BBA': 2}, 4: {'BBA': 3}, 5: {'BBA': 3},
                    6: {'BBA': 4}, 7: {'BBA': 5}, 8: {'BBA': 6}, 9: {'BBA': 6}, 10: {'BBA': 7},
                    11: {'BBA': 8}, 12: {'BBA': 9}, 13: {'BBA': 9}, 14: {'BBA': 10}, 15: {'BBA': 11},
                    16: {'BBA': 12}, 17: {'BBA': 12}, 18: {'BBA': 13}, 19: {'BBA': 14}, 20: {'BBA': 15}},
        'druida': {1: {'BBA': 0}, 2: {'BBA': 1}, 3: {'BBA': 2}, 4: {'BBA': 3}, 5: {'BBA': 3},
                   6: {'BBA': 4}, 7: {'BBA': 5}, 8: {'BBA': 6}, 9: {'BBA': 6}, 10: {'BBA': 7},
                   11: {'BBA': 8}, 12: {'BBA': 9}, 13: {'BBA': 9}, 14: {'BBA': 10}, 15: {'BBA': 11},
                   16: {'BBA': 12}, 17: {'BBA': 12}, 18: {'BBA': 13}, 19: {'BBA': 14}, 20: {'BBA': 15}},
        'feiticeiro': {1: {'BBA': 0}, 2: {'BBA': 1}, 3: {'BBA': 1}, 4: {'BBA': 2}, 5: {'BBA': 2},
                       6: {'BBA': 3}, 7: {'BBA': 3}, 8: {'BBA': 4}, 9: {'BBA': 4}, 10: {'BBA': 5},
                       11: {'BBA': 5}, 12: {'BBA': 6}, 13: {'BBA': 6}, 14: {'BBA': 7}, 15: {'BBA': 7},
                       16: {'BBA': 8}, 17: {'BBA': 8}, 18: {'BBA': 9}, 19: {'BBA': 9}, 20: {'BBA': 10}},
        'guerreiro': {i: {'BBA': i} for i in range(1, 21)},
        'ladino': {1: {'BBA': 0}, 2: {'BBA': 1}, 3: {'BBA': 2}, 4: {'BBA': 3}, 5: {'BBA': 3},
                   6: {'BBA': 4}, 7: {'BBA': 5}, 8: {'BBA': 6}, 9: {'BBA': 6}, 10: {'BBA': 7},
                   11: {'BBA': 8}, 12: {'BBA': 9}, 13: {'BBA': 9}, 14: {'BBA': 10}, 15: {'BBA': 11},
                   16: {'BBA': 12}, 17: {'BBA': 12}, 18: {'BBA': 13}, 19: {'BBA': 14}, 20: {'BBA': 15}},
        'mago': {1: {'BBA': 0}, 2: {'BBA': 1}, 3: {'BBA': 1}, 4: {'BBA': 2}, 5: {'BBA': 2},
                 6: {'BBA': 3}, 7: {'BBA': 3}, 8: {'BBA': 4}, 9: {'BBA': 4}, 10: {'BBA': 5},
                 11: {'BBA': 5}, 12: {'BBA': 6}, 13: {'BBA': 6}, 14: {'BBA': 7}, 15: {'BBA': 7},
                 16: {'BBA': 8}, 17: {'BBA': 8}, 18: {'BBA': 9}, 19: {'BBA': 9}, 20: {'BBA': 10}},
        'monge': {i: {'BBA': i} for i in range(1, 21)},
        'paladino': {i: {'BBA': i} for i in range(1, 21)},
        'ranger': {i: {'BBA': i} for i in range(1, 21)},
        'samurai': {i: {'BBA': i} for i in range(1, 21)},
        'swashbuckler': {i: {'BBA': i} for i in range(1, 21)}
    }


    graduacao_nao_treinada = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]

    def __init__(self, nome, forca, destreza, constituicao, inteligencia, sabedoria, carisma, raca, classe, nivel, habilidade='inteligencia', habilidade2 = 'destreza', pericia1 = 0, pericia2 = 0, pericia3 = 0, pericia4 = 0, pericia5 = 0, pericia6 = 0, deformidade_lefou = 0, tipo_oficio = 0, conhecimentos = 0, linguagem = 0, img = None):
        self.nome = nome

        # infos gerais
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.raca = raca
        self.classe = classe
        if self.raca in ['gnomo', 'halfling', 'goblin']:
            self.tamanho = 1
        else:
            self.tamanho = 0

        # Modificadores de atributos
        self.mod_forca = (self.forca - 10) // 2
        self.mod_destreza = (self.destreza - 10) // 2
        self.mod_constituicao = (self.constituicao - 10) // 2
        self.mod_inteligencia = (self.inteligencia - 10) // 2
        self.mod_sabedoria = (self.sabedoria - 10) // 2
        self.mod_carisma = (self.carisma - 10) // 2
        self.nivel = nivel

        # Outros
        self.pv = 0
        self.bba = 0
        self.tipo_oficio = tipo_oficio
        self.linguagem = linguagem
        self.conhecimentos = conhecimentos

        self.img = img

        # Raça
        if raca:
            self.aplicar_modificadores_de_raca(habilidade)
            self.calcular_modificadores()

        # PV e PM
        if classe:
            self.setar_pv()
            self.setar_bba()

        if classe == 'bardo':
            self.pm = 1 + self.mod_carisma + (2 * (self.nivel - 1))
        elif classe == 'clerigo' or classe == 'druida':
          self.pm = 1 + self.mod_sabedoria + (3 * (self.nivel - 1))
        elif classe == 'feiticeiro':
          self.pm = 3 + self.mod_carisma + (3 * (self.nivel - 1))
        elif classe == 'mago':
          self.pm = 1 + self.mod_inteligencia + (3 * (self.nivel - 1))
        else:
          self.pm = 'N/A'

        # Resistências
        self.fortitude = (self.nivel//2) + self.mod_constituicao
        self.reflexo = (self.nivel//2) + self.mod_destreza
        self.vontade = (self.nivel//2) + self.mod_sabedoria

        # Armaduras
        self.armadura = 0
        self.escudo = 0
        self.classe_armadura = self.mod_destreza + (self.nivel//2) + 10 + self.armadura + self.escudo

        # Ataques
        self.corpo_a_corpo = self.bba + self.mod_forca + self.tamanho
        self.distancia = self.bba + self.mod_destreza + self.tamanho

        # Perícias
        self.pericias_modificadores = {
            'acrobacia': 'mod_destreza',
            'adestrar_animais': 'mod_carisma',
            'atletismo': 'mod_forca',
            'atuacao': 'mod_carisma',
            'cavalgar': 'mod_destreza',
            'conhecimento': 'mod_inteligencia',
            'cura': 'mod_sabedoria',
            'diplomacia': 'mod_carisma',
            'enganacao': 'mod_carisma',
            'furtividade': 'mod_destreza',
            'identificar_magia': 'mod_inteligencia',
            'iniciativa': 'mod_destreza',
            'intimidacao': 'mod_carisma',
            'intuicao': 'mod_sabedoria',
            'ladinagem': 'mod_destreza',
            'obter_info': 'mod_carisma',
            'oficio': 'mod_inteligencia',
            'percepcao': 'mod_sabedoria',
            'sobrevivencia': 'mod_sabedoria'
        }

        self.graduacao_nt = Personagem.graduacao_nao_treinada[self.nivel - 1]
        self.graduacao_t = self.nivel + 3

        for pericia, modificador in self.pericias_modificadores.items():
            setattr(self, pericia, self.graduacao_nt + getattr(self, modificador))

        self.adestrar_animais = 'N/A'
        self.conhecimento = 'N/A'
        self.identificar_magia = 'N/A'
        self.ladinagem = 'N/A'

        pericias = [pericia1, pericia2, pericia3, pericia4, pericia5, pericia6]

        for pericia in pericias:
            if pericia in self.pericias_modificadores:
                setattr(self, pericia, self.graduacao_t + getattr(self, self.pericias_modificadores[pericia]))

    # Traços raciais
        if self.raca == 'elfo':
            setattr(self, 'identificar_magia', getattr(self, 'identificar_magia') + 4)
            setattr(self, 'percepcao', getattr(self,'percepcao') + 4)
        elif self.raca == 'goblin':
            setattr(self, 'ladinagem', getattr(self, 'ladinagem') + 4)
            setattr(self, 'oficio', getattr(self, 'oficio')+ 4)
        elif self.raca == 'halfling':
            setattr(self, 'furtividade', getattr(self, 'furtividade') + 4)
            setattr(self, 'atletismo', getattr(self, 'atletismo') - self.mod_forca + self.mod_destreza )
            for item in ['fortitude', 'reflexo', 'vontade', 'enganacao']:
             setattr(self, item, getattr(self, item) + 2)
        elif self.raca == 'lefou':
            if self.deformidade_lefou == 'articulacoes flexiveis':
              setattr(self, 'acrobacia', getattr(self, 'acrobacia') + 4)
            elif self.deformidade_lefou == 'dentes afiados':
              setattr(self, 'intimidacao', getattr(self, 'intimidacao') + 4)
            elif self.deformidade_lefou == 'olhos vermelhos':
              setattr(self, 'percepcao', getattr(self, 'percepcao') + 4)
            elif self.deformidade_lefou == 'pele rigida':
              setattr(self, 'classe_armadura', getattr(self, 'classe_armadura') + 1)
        elif self.raca == 'minotauro':
            setattr(self, 'classe_armadura', getattr(self, 'classe_armadura') + 1)
        elif self.raca == 'lefou':
            setattr(self, 'identificar_magia', getattr(self, 'identificar_magia') + 4)
        elif self.raca == 'gnomo':
            setattr(self, 'furtividade', getattr(self, 'furtividade') + 4)
            setattr(self, 'intuicao', getattr(self, 'intuicao')+ 4)
            if self.tipo_oficio == 'alquimia':
              setattr(self, 'oficio', getattr(self, 'oficio') + 4)
        elif self.raca == 'meio elfo':
            for item in ['identificar_magia','percepcao']:
                setattr(self, item, getattr(self, item) + 2)
        elif self.raca == 'meio orc':
            setattr(self, 'intimidacao', getattr(self, 'intimidacao') + 4)

    # Descritivos
        self.talentos = {}
        self.habilidade_classe = {}
        self.habilidade_raca = {}
        self.magias = {}
        self.musicas = {}
        self.equipamento = {}
        self.add_habilidade_raca(raca)
        self.add_habilidade_classe(classe,nivel)

    #Funções

    def setar_pv(self):
        if self.classe == 'bárbaro':
            self.pv = 24 + self.mod_constituicao + ((6 + self.mod_constituicao) * (self.nivel - 1))
        elif self.classe == 'guerreiro' or self.classe == 'paladino' or self.classe == 'samurai':
            self.pv = 20 + self.mod_constituicao + ((5 + self.mod_constituicao) * (self.nivel - 1))
        elif self.classe == 'clerigo' or self.classe == 'druida' or self.classe == 'monge' or self.classe == 'ranger' or self.classe == 'swashbuckler':
            self.pv = 16 + self.mod_constituicao + ((4 + self.mod_constituicao) * (self.nivel - 1))
        elif self.classe == 'bardo' or self.classe == 'ladino':
            self.pv = 12 + self.mod_constituicao + ((3 + self.mod_constituicao) * (self.nivel - 1))
        elif self.classe == 'feiticeiro' or self.classe == 'mago':
            self.pv = 8 + self.mod_constituicao + ((2 + self.mod_constituicao) * (self.nivel - 1))

    def setar_bba(self):
         self.bba = self.bba_classe[self.classe][self.nivel]['BBA']

    def calcular_modificadores(self):
        self.mod_forca = (self.forca - 10) // 2
        self.mod_destreza = (self.destreza - 10) // 2
        self.mod_constituicao = (self.constituicao - 10) // 2
        self.mod_inteligencia = (self.inteligencia - 10) // 2
        self.mod_sabedoria = (self.sabedoria - 10) // 2
        self.mod_carisma = (self.carisma - 10) // 2

    def aplicar_modificadores_de_raca(self, habilidade, habilidade2=None):
        modificadores = self.modificadores_de_raca.get(self.raca, {})
        for atributo, modificador in modificadores.items():
            if atributo == 'habilidade':
                setattr(self, habilidade, getattr(self, habilidade) + modificador)
            elif atributo == 'habilidade2' and habilidade2 is not None:
                setattr(self, habilidade2, getattr(self, habilidade2) + modificador)
            else:
                setattr(self, atributo, getattr(self, atributo) + modificador)

    #Funções de add

    def add_habilidade_raca(self, raca):
        if raca in habilidades_raca_descritivos:
            for habilidade, descricao in habilidades_raca_descritivos[raca].items():
                self.habilidade_raca[habilidade] = descricao

    def add_habilidade_classe(self, classe, nivel):
        if classe in habilidades_classe_descritivos:
            for nivel_habilidade in range(1, nivel + 1):
                if nivel_habilidade in habilidades_classe_descritivos[classe]:
                    for habilidade, descricao in habilidades_classe_descritivos[classe][nivel_habilidade].items():
                        if habilidade not in self.habilidade_classe:
                            self.habilidade_classe[habilidade] = descricao

    def add_talento(self, talento):
        if talento not in self.talentos:
            self.talentos[talento] = talentos_descritivos[talento]
    
    def add_musica(self, musica):
      if musica not in self.musicas:
          self.musicas[musica] = musicas[musica]

    def add_magia(self, magia):
        if magia not in self.magias:
            self.magias[magia] = magias[magia]

    def add_equipamento(self, equip):

        if equip in equipamentos_lista:
            self.equipamento[equip] = equipamentos_lista[equip]

            tipo = self.equipamento[equip]['Tipo']
            if tipo == 'Armadura':
                self.armadura = self.equipamento[equip]['Bônus em CA']
            elif tipo == 'Escudo':
                self.escudo = self.equipamento[equip]['Bônus em CA']

            if self.equipamento[equip]['Máximo em destreza'] < self.mod_destreza:
                self.mod_destreza = self.equipamento[equip]['Máximo em destreza']
                
            self.classe_armadura = self.mod_destreza + (self.nivel // 2) + 10 + self.armadura + self.escudo
            
            penalidade = int(self.equipamento[equip].get('Penalidade da armadura', 0))
            for habilidade in ['acrobacia', 'atletismo', 'furtividade', 'ladinagem']:
                valor_atual = getattr(self, habilidade, 0)  # Valor padrão de 0 se não existir
                if isinstance(valor_atual, int):
                    setattr(self, habilidade, valor_atual + penalidade)
        else:
            print(f"Equipamento '{equip}' não encontrado.")
      
    #Funções de mostrar

    def mostrar_talentos(self):
        print(self.talentos)

    def mostrar_magias(self):
        print("Lista de Magias:\n")
        for magia, detalhes in self.magias.items():
            print(f'Magia: {magia}')
            print(f'Descrição: {detalhes["Descrição"]}\n')      

    def mostrar_musicas(self):
        print("Lista de Músicas:\n")
        for musica, descricao in self.musicas.items():
            print(f'Música: {musica}')
            print(f'Descrição: {descricao}\n')
            
    def mostrar_habilidades(self):
        print("Habilidades de Raça:\n")
        for habilidade, descricao in self.habilidade_raca.items():
            print(f"{habilidade}")
            #print(f'{descricao}')

        print("Habilidades de Classe:\n")
        for habilidade, descricao in self.habilidade_classe.items():
            print(f'{habilidade}')
            #print(f'{descricao}')

    def mostrar_infos(self):
        print(f"{self.nome}:")
        print('-' * 30)
        print(f'Nível: {self.nivel}')
        print(f'PV: {self.pv}')
        print(f'PM: {self.pm}')
        print('-' * 30)
        print(f"Mod/Força: {self.mod_forca}")
        print(f"Mod/Destreza: {self.mod_destreza}")
        print(f"Mod/Constituição: {self.mod_constituicao}")
        print(f"Mod/Inteligência: {self.mod_inteligencia}")
        print(f"Mod/Sabedoria: {self.mod_sabedoria}")
        print(f"Mod/Carisma: {self.mod_carisma}")
        print('-' * 30)
        print(f'fortitude: {self.fortitude}')
        print(f'reflexos: {self.reflexo}')
        print(f'vontade: {self.vontade}')
        print('-' * 30)
        print(f'CAC: {self.corpo_a_corpo}')
        print(f'Distância: {self.distancia}')
        print(f'Classe de armadura: {self.classe_armadura}')
        print('-' * 30)

    def pericia(self):
        pericia_textos =[]
        for pericia in self.pericias_modificadores:
            valor = getattr(self, pericia)
            pericia_textos.append(f'{pericia.capitalize()}: {valor}')
        return pericia_textos

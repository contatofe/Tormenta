import flet as ft
from personagens import Teste, Teste2

Personagem = Teste

def main(page: ft.Page):


    def aplicar_alteracao_pv():
        # Atualiza PV com base no dano e cura
        try:
            dano = int(dano_atq.value) if dano_atq.value else 0
            cura = int(cura_atq.value) if cura_atq.value else 0
        except ValueError:
            # Em caso de erro na conversão, não faz nada
            return
        
        # Calcula o novo valor de PV
        novo_pv = Personagem.pv - dano + cura
        
        # Verifica se o PV passou do limite
        novo_pv = min(novo_pv, Personagem.pv)
        
        # Atualiza o texto na interface
        pv_atual.value = f"PV: {novo_pv}|{Personagem.pv}"
        page.update()

    def aplicar_alteracao_pm():

        if Personagem.pm != 'N/A':
            try:
                gasta = int(mana_gasta.value) if mana_gasta.value else 0
                rec = int(mana_rec.value) if mana_rec.value else 0
            except ValueError:
                return
            
            # Calcula o novo valor de PM
            novo_pm = Personagem.pm - gasta + rec
            
            # Verifica se o PM passou do limite
            novo_pm = min(novo_pm, Personagem.pm)
            
            # Atualiza o texto na interface
            pm_atual.value = f"PV: {novo_pm}|{Personagem.pm}"
            page.update()

    def calculate_text_width(text: str, font_size: int) -> int:
        # Estimativa simples: ajuste o fator multiplicador conforme necessário
        return len(text) * font_size * 0.6
    
    def update_text_field_width():
        # Garante que o sufixo tenha uma largura calculada
        page.update()
        
        # Obtém a largura calculada do sufixo
        suffix_width = suffix.width or 0
        
        # Calcula a largura do TextField com base no texto atual
        text_width = calculate_text_width(text_field.value, 40)
        # Define uma largura mínima para o TextField
        min_width = 0
        # Ajusta a largura do TextField
        text_field.width = max(text_width + suffix_width + 30, min_width)
        page.update()    

    #Funções para dropdown de magias

    def get_options():
        options = []
        for magia in Personagem.magias:
            options.append(ft.dropdown.Option(text=magia))
        return options

    def dropdown_changed(e):
        magia_selecionada.value = f"{e.control.value}"
        descricao_magia.value = f"{Teste.magias[e.control.value]['Descrição']}"
        alcance_magia.value = f"{Teste.magias[e.control.value]['Alcance']}"
        tempo_magia.value = f"{Teste.magias[e.control.value]['Tempo de Execução']}"
        page.update()
    
    #Funções para dropdown de musicas

    def get_options_music():
        options = []
        for musica in Personagem.musicas.keys():
            options.append(ft.dropdown.Option(text=musica))
        return options

    def dropdown_changed_music(e):
        musica_selecionada.value = f"{e.control.value}"
        descricao_musica.value = f"{Teste.musicas[e.control.value]}"
        page.update()

    #Funções para dropdown de talentos

    def get_options_talento():
        options = []
        for talento in Personagem.talentos.keys():
            options.append(ft.dropdown.Option(text=talento))
        return options

    def dropdown_changed_talento(e):
        talento_selecionado.value = f"{e.control.value}"
        descricao_talento.value = f"{Teste.talentos[e.control.value]}"
        page.update()        

    page.bgcolor = ft.colors.BLACK
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.assets_dir = "assets"
    page.theme = ft.Theme(font_family="Albertus MT")

    page.fonts = {
        "Albertus MT": "fonts/AlbertusMT.otf",
    }

    infos_gerais = ft.Container(
        padding=ft.padding.all(50),
        aspect_ratio=9/16,
        col={'xs': 12, 'md': 4},
        content=ft.Column(
            alignment = ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls=[
                    ft.CircleAvatar(
                        foreground_image_src = Personagem.img,
                        width = 250,
                        height = 250),
                    ]),
                ft.Container(
                    height = 10
                ),
                ft.Row(
                    
                    controls=[
                        ft.Text(
                            value=f'{Personagem.nome}',
                            style=ft.TextStyle(
                                font_family="Albertus MT",
                                color=ft.colors.WHITE,
                                size=45,
                                weight='Bold',
                                letter_spacing=2,
                                word_spacing=-2
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            value=f'Raça: {Personagem.raca.capitalize()} | Classe: {Personagem.classe.capitalize()} | Nível: {Personagem.nivel}',
                            style=ft.TextStyle(
                                font_family="Albertus MT",
                                color='#e9cca6',
                                size=20,
                                letter_spacing=1,
                                word_spacing=-3
                            )
                        )
                    ],
                    
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ]
        )
    )

    #Tab Info

    text_field = ft.TextField(
        animate_offset=None,
        value='1000',
        border_color=ft.colors.TRANSPARENT,
        height=80,
        border_width=0,  
        text_style=ft.TextStyle(color='#e9cca6', size=40),
        suffix_text="",  # Inicialmente sem sufixo
        width=110  # Largura inicial
    )

    suffix = ft.Column(
        spacing=0,
        controls = [
                ft.Text(
                    value="tibares",
                    color='#e9cca6',
                    size=20,
                    # Ajuste o padding para criar o efeito de espaçamento entre linhas
                    height=22  # Ajuste o padding conforme necessário
            ),
                ft.Text(
                    value="de ouro",
                    color='#e9cca6',
                    size=20,
                    # Ajuste o padding para criar o efeito de espaçamento entre linhas
                    height=22  # Ajuste o padding conforme necessário
            ),
        ]

    )

    row = ft.Row(
        controls=[text_field, suffix],
        alignment=ft.MainAxisAlignment.START,
        spacing=0
    )

    text_field.on_change = lambda e: update_text_field_width()

    dano_atq = ft.TextField(label="Dano", on_change=lambda e: aplicar_alteracao_pv(), border_color = '#e9cca6', width=120, text_style=ft.TextStyle(color='#e9cca6'))
    cura_atq = ft.TextField(label="Cura", on_change=lambda e: aplicar_alteracao_pv(), border_color = '#e9cca6', width=120, text_style=ft.TextStyle(color='#e9cca6'))

    mana_gasta = ft.TextField(label="Gasto", on_change=lambda e: aplicar_alteracao_pm(), border_color = '#e9cca6', width=120, text_style=ft.TextStyle(color='#e9cca6'))
    mana_rec = ft.TextField(label="Recuperado", on_change=lambda e: aplicar_alteracao_pm(), border_color = '#e9cca6', width=120, text_style=ft.TextStyle(color='#e9cca6'))

    pv_atual = ft.Text(
        f"PV: {Personagem.pv}|{Personagem.pv}", 
        color = '#e9cca6', 
        weight = ft.FontWeight.NORMAL, 
        size = 40)

    pm_atual = ft.Text(
        f"PM: {Personagem.pm}|{Personagem.pm}" if Personagem.pm != 'N/A' else "Não possui PM",
        color='#e9cca6',
        weight=ft.FontWeight.NORMAL,
        size=40
    )

    tab_info = ft.Tab(
        text="Informações",
        content=ft.Container(
            padding=ft.padding.all(40),
            content=ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                spacing=80,  # Ajuste o espaçamento conforme necessário
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Row(
                                                spacing=0,
                                                controls=[
                                                    pv_atual,
                                                ]
                                            ),
                                            ft.Row(
                                                controls=[
                                                    dano_atq, cura_atq
                                                ]
                                            ),
                                        ]
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Row(
                                                spacing=0,
                                                controls=[
                                                    pm_atual
                                                ]
                                            ),
                                            ft.Row(
                                                controls=[
                                                    mana_gasta, mana_rec
                                                ]
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                        ]
                    ),
                    ft.Divider(height=100, thickness=1, color='#e9cca6'),
                    ft.Text(value='Resistências', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    ft.Text(value=f'Fortitude: {Personagem.fortitude} | Reflexos: {Personagem.reflexo} | Vontade: {Personagem.vontade}', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40),
                    ft.Divider(height=100, thickness=1, color='#e9cca6'),
                    ft.Row(
                        spacing = 70,
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text(value='Ataques', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20, height=53),
                                    ft.Text(value=f'CAC: {Personagem.corpo_a_corpo} | Distância: {Personagem.distancia}', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40),
                                ]
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(value=' Dinheiro', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                                    row,
                                    #ft.TextField(value='1000', suffix_text="tibares de ouro", border_color = ft.colors.TRANSPARENT, height = 60, width = 250, text_style=ft.TextStyle(color='#e9cca6', size = 40), suffix_style=ft.TextStyle(color = '#e9cca6', size = 20,), text_vertical_align = ft.VerticalAlignment.START, ),
                                ]
                            ),
                        ]
                    )
                ]
            )
        )
    ) 




    #Tab Perícias

    pericia_textos = Personagem.pericia()

    textos_pericias = [ft.Text(value=texto,size = 19,color = '#e9cca6', col=4) for texto in pericia_textos]

    linguagem = ft.Row(
        controls = [
            ft.Text(value='Línguas', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
            ft.Text(value= Personagem.linguagem, color='#e9cca6', weight=ft.FontWeight.NORMAL, size=35),
        ]
    )

    oficio = ft.Row(
        controls = [
            ft.Text(value='Ofício', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
            ft.Text(value= Personagem.tipo_oficio, color='#e9cca6', weight=ft.FontWeight.NORMAL, size=35),
        ]
    )

    conhecimentos = ft.Row(
        controls = [
            ft.Text(value='Conhecimentos', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
            ft.Text(value= Personagem.conhecimentos, color='#e9cca6', weight=ft.FontWeight.NORMAL, size=35)
        ] 
    )

    coluna_controles = [
    ft.ResponsiveRow(
        spacing=30,
        controls=textos_pericias
    ),
    ft.Divider(height=50, thickness=1, color='#e9cca6'),
    ]

    if Personagem.linguagem != 0:
        coluna_controles.append(linguagem)

    if Personagem.tipo_oficio != 0:
        coluna_controles.append(oficio)

    if Personagem.conhecimentos != 0:
        coluna_controles.append(conhecimentos)

    
    tab_pericias = ft.Tab(
        text="Perícias",
        content=ft.Container(
            expand = True,
            padding=ft.padding.all(40),
            content=ft.Column(
                spacing = 20,
                controls=coluna_controles
            )
        )
    )


    #Tab equipamentos

    equipamentos = Personagem.equipamento

    nomes_equipamentos = list(equipamentos.keys())

    tab_equipamentos = ft.Tab(
        text="Equipamentos",
        content=ft.Container(
            padding=ft.padding.all(40),
            content=ft.Column(
                controls=[
                    ft.Text(value='Arma', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    ft.Text(value='Lorem ipsum dolor sit', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40),
                    ft.Divider(height=100, thickness=1, color='#e9cca6'),  # Ajustei a altura do divisor
                    ft.Text(value='Armadura', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    ft.Text(value=nomes_equipamentos[0] if len(nomes_equipamentos) > 0 else "Não equipado",
                            color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40),
                    ft.Divider(height=100, thickness=1, color='#e9cca6'),  # Ajustei a altura do divisor
                    ft.Text(value='Escudo', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    ft.Text(value=nomes_equipamentos[1] if len(nomes_equipamentos) > 1 else "Não equipado",
                            color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40),
                ]
            )
        )
    )

    magia_selecionada = ft.Text(value='Nenhuma magia selecionada', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40)
    descricao_magia = ft.Text(value= 'Nenhuma magia selecionada', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=30)
    tempo_magia = ft.Text(value= 'Nenhuma magia selecionada', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=30)
    alcance_magia = ft.Text(value= 'Nenhuma magia selecionada', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=30)

    tab_magias = ft.Tab(
         text="Magias",
         content = ft.Container(
            padding = ft.padding.all(40),
            content = ft.Column(
                scroll=True,
                controls=[
                    ft.Dropdown(
                        label="Magias",
                        label_style=ft.TextStyle(color="#e9cca6", weight=ft.FontWeight.NORMAL),
                        options=get_options(),
                        on_change=dropdown_changed,
                        width = 800,
                        color = '#e9cca6',
                        border_color = '#e9cca6',
                        text_size = 24,

                    ),
                    ft.Divider(color=ft.colors.TRANSPARENT, height=30),
                    ft.Text(value='Descrição', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    descricao_magia,
                    ft.Divider(height=30, thickness=1, color='#e9cca6'),
                    ft.Text(value='Tempo de execução', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    tempo_magia,
                    ft.Divider(height=30, thickness=1, color='#e9cca6'),
                    ft.Text(value='Alcance da magia', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    alcance_magia
                ]

            )
         )
    )

    musica_selecionada = ft.Text(value='Nenhuma música selecionada', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40)
    descricao_musica = ft.Text(value= 'Nenhuma música selecionada', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=30)

    tab_musicas = ft.Tab(
         text="Músicas",
         content = ft.Container(
            padding = ft.padding.all(40),
            content = ft.Column(
                scroll=True,
                controls=[
                    ft.Dropdown(
                        label="Músicas",
                        label_style=ft.TextStyle(color="#e9cca6", weight=ft.FontWeight.NORMAL),
                        options=get_options_music(),
                        on_change=dropdown_changed_music,
                        width = 800,
                        color = '#e9cca6',
                        border_color = '#e9cca6',
                        text_size = 24,

                    ),
                    ft.Divider(color=ft.colors.TRANSPARENT, height=30),
                    ft.Text(value='Descrição', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    descricao_musica,
                ]
            )
         )
    )

    talento_selecionado = ft.Text(value='Nenhum talento selecionado', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40)
    descricao_talento = ft.Text(value= 'Nenhum talento selecionado', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=30)

    tab_talentos = ft.Tab(
         text="Talentos",
         content = ft.Container(
            padding = ft.padding.all(40),
            content = ft.Column(
                scroll=True,
                controls=[
                    ft.Dropdown(
                        label="Talentos",
                        label_style=ft.TextStyle(color="#e9cca6", weight=ft.FontWeight.NORMAL),
                        options=get_options_talento(),
                        on_change=dropdown_changed_talento,
                        width = 800,
                        color = '#e9cca6',
                        border_color = '#e9cca6',
                        text_size = 24,

                    ),
                    ft.Divider(color=ft.colors.TRANSPARENT, height=30),
                    ft.Text(value='Descrição', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    descricao_talento,
                ]
            )
         )
    )
    
    itens_tabs = ft.Tabs(
                    animation_duration = 300,
                    label_color='#e9cca6',
                    unselected_label_color='#e9cca6',
                    divider_color='#e9cca6',
                    divider_height=1.3,
                    indicator_color='#e9cca6',
                    indicator_thickness=2,
                    scrollable=False,
                    tabs=[
                        tab_info,
                        tab_pericias,
                        tab_equipamentos,
                        tab_magias,
                        tab_musicas,
                        tab_talentos
                    ],
                    expand=1,
                )   

    #Container Detalhes

    detalhes = ft.Container(
        col = {'xs': 12, 'md': 8},
        padding=ft.padding.only(right = 50, top = 70 , bottom = 70),
        aspect_ratio = 18/16,
        content=ft.Column(
            controls =[itens_tabs    
            ]
        )
    )

    layout = ft.Container(
        image_src='images/BG_tormenta.png',
        image_fit=ft.ImageFit.FILL,
        expand=True,
        width = 1400,
        margin = ft.margin.all(30),
        content = ft.ResponsiveRow(
            columns = 12,
            spacing = 0,
            run_spacing = 0,
            controls = [
                infos_gerais,
                detalhes
            ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        layout
    )

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")
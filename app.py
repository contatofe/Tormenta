import flet as ft
from personagens import Teste

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
        novo_pv = Teste.pv - dano + cura
        
        # Verifica se o PV passou do limite
        novo_pv = min(novo_pv, Teste.pv)
        
        # Atualiza o texto na interface
        pv_atual.value = f"PV: {novo_pv}|{Teste.pv}"
        page.update()

    def aplicar_alteracao_pm():

        if Teste.pm != 'N/A':
            try:
                gasta = int(mana_gasta.value) if mana_gasta.value else 0
                rec = int(mana_rec.value) if mana_rec.value else 0
            except ValueError:
                return
            
            # Calcula o novo valor de PM
            novo_pm = Teste.pm - gasta + rec
            
            # Verifica se o PM passou do limite
            novo_pm = min(novo_pm, Teste.pm)
            
            # Atualiza o texto na interface
            pm_atual.value = f"PV: {novo_pm}|{Teste.pm}"
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

    page.bgcolor = ft.colors.BLACK
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
                        foreground_image_src = 'images/avatar.jpg',
                        width = 250,
                        height = 250),
                    ]),
                ft.Container(
                    height = 10
                ),
                ft.Row(
                    
                    controls=[
                        ft.Text(
                            value=f'{Teste.nome}',
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
                            value=f'Raça: {Teste.raca.capitalize()} | Classe: {Teste.classe.capitalize()} | Nível: {Teste.nivel}',
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
        f"PV: {Teste.pv}|{Teste.pv}", 
        color = '#e9cca6', 
        weight = ft.FontWeight.NORMAL, 
        size = 40)

    pm_atual = ft.Text(
        f"PM: {Teste.pm}|{Teste.pm}" if Teste.pm != 'N/A' else "Não possui PM",
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
                    ft.Text(value=f'Fortitude: {Teste.fortitude} | Reflexos: {Teste.reflexo} | Vontade: {Teste.vontade}', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40),
                    ft.Divider(height=100, thickness=1, color='#e9cca6'),
                    ft.Row(
                        spacing = 70,
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text(value='Ataques', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20, height=53),
                                    ft.Text(value=f'CAC: {Teste.corpo_a_corpo} | Distância: {Teste.distancia}', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40),
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

    pericia_textos = Teste.pericia()

    textos_pericias = [ft.Text(value=texto,size = 19,color = '#e9cca6', col=4) for texto in pericia_textos]

    linguagem = ft.Row(
        controls = [
            ft.Text(value='Línguas', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
            ft.Text(value= Teste.linguagem, color='#e9cca6', weight=ft.FontWeight.NORMAL, size=35),
        ]
    )

    oficio = ft.Row(
        controls = [
            ft.Text(value='Ofício', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
            ft.Text(value= Teste.tipo_oficio, color='#e9cca6', weight=ft.FontWeight.NORMAL, size=35),
        ]
    )

    conhecimentos = ft.Row(
        controls = [
            ft.Text(value='Conhecimentos', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
            ft.Text(value= Teste.conhecimentos, color='#e9cca6', weight=ft.FontWeight.NORMAL, size=35)
        ] 
    )

    coluna_controles = [
    ft.ResponsiveRow(
        spacing=30,
        controls=textos_pericias
    ),
    ft.Divider(height=50, thickness=1, color='#e9cca6'),
    ]

    if Teste.linguagem != 0:
        coluna_controles.append(linguagem)

    
    if Teste.tipo_oficio != 0:
        coluna_controles.append(oficio)

    if Teste.conhecimentos != 0:
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

    equipamentos = Teste.equipamento

    nomes_equipamentos = list(equipamentos.keys())

    tab_equipamentos = ft.Tab(
        text="Equipamentos",
        content=ft.Container(
            padding=ft.padding.all(40),
            content=ft.Column(
                controls=[
                    ft.Text(value='Arma', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=20),
                    ft.Text(value='Lorem ipsum', color='#e9cca6', weight=ft.FontWeight.NORMAL, size=40),
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


    tab_magias = ft.Tab(
         text="Magias",
    )

    tab_musicas = ft.Tab(
         text="Músicas",
    )

    tab_talentos = ft.Tab(
         text="Talentos",
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
            controls =[ itens_tabs    
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
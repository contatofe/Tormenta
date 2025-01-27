import flet as ft

def main(page: ft.Page):
    # Função para calcular a largura do texto
    def calculate_text_width(text: str, font_size: int) -> int:
        # Estimativa simples: ajuste o fator multiplicador conforme necessário
        return len(text) * font_size * 0.6

    # Criação do TextField com uma largura inicial
    text_field = ft.TextField(
        value='1000',
        border_color=ft.colors.TRANSPARENT,
        height=80,
        text_style=ft.TextStyle(color='#e9cca6', size=40),
        suffix_text="",  # Inicialmente sem sufixo
        width=200  # Largura inicial
    )

    # Criação do sufixo com um valor de texto
    suffix = ft.Text(
        value="tibares de ouro",
        color='#e9cca6',
        size=20
    )
    
    # Ajuste do sufixo com um Container para adicionar alinhamento
    suffix_container = ft.Container(
        content=suffix,
        alignment=ft.Alignment(1, 0.5)  # Alinha o texto verticalmente no centro
    )

    # Criação do Row para alinhar o TextField e o sufixo
    row = ft.Row(
        controls=[text_field, suffix_container],
        alignment=ft.MainAxisAlignment.START,
        spacing=0
    )

    # Função para atualizar a largura do TextField e reposicionar o sufixo
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
        text_field.width = max(text_width + suffix_width + 20, min_width)
        page.update()

    # Configura um evento para atualizar a largura do TextField
    text_field.on_change = lambda e: update_text_field_width()

    # Adiciona o Row à página
    page.add(row)
    # Atualiza a largura do TextField inicialmente
    update_text_field_width()

ft.app(target=main)

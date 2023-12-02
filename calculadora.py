import ipywidgets as widgets #interatividade em notebooks
from IPython.display import display

button_layout = [      #lista
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '0', '.', '=', '+',
    'C', 'apg tudo'
]

buttons_per_row = 4

#|lista de objetos|   |classe|     |descricao nos botoes|         |recebe os nomes dos botoes|
button_widgets = [   widgets.Button(description=button) for button in button_layout]

# Adicionar borda colorida aos botões
button_color = "pink"
for button in button_widgets:
    button.style.button_color = button_color
    button.layout.width = '100px'  # Ajuste a largura de cada botao

# Dividir os botões em linhas de 4
button_rows = [button_widgets[i:i + buttons_per_row] for i in range(0, len(button_widgets), buttons_per_row)]

# Criar linhas de botões em uma HBox (horizontal)
button_boxes = [widgets.HBox(row) for row in button_rows]

from termcolor import colored
print("\33[3;95mCalculadora Polishop 2000\033[5m") #titulo

# Visor   obj da classe widgets
display_text = widgets.Text(value='', layout=widgets.Layout(width='36.7%'))

# Função para atualizar o visor com o texto do botão
def on_button_click(button): #obj button(classe widgets)
    button_text = button.description
    current_text = display_text.value # salvar a expressao criada no visor
    if button_text == '=':
        try:
            display_text.value = str(eval(current_text))
        except:
            display_text.value = 'Erro. primeiro o(s) número(s), depois operador, núm seguinte'

    elif button_text == 'C':
      expressao = display_text.value
      def apagar_ultimo_caractere(expressao):
        if len(expressao) > 0:
         expressao = expressao[:-1]
         display_text.value = expressao

      apagar_ultimo_caractere(expressao)

    elif button_text == 'apg tudo':
            display_text.value = ''  # Limpa o visor
    else:
        display_text.value = current_text + button_text

# Adicionar a função de clique aos botões
for button in button_widgets:
    button.on_click(lambda _, button=button: on_button_click(button))

# Exibir a calculadora
display(widgets.VBox([display_text] + button_boxes))


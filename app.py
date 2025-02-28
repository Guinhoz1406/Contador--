import customtkinter as ctk

# Aparência
ctk.set_appearance_mode('dark')

# Funções
def Calculo():
    try:
        valor = float(campo_valor.get())
        desconto = float(campo_desconto.get())
        valor_final = valor - (valor * (desconto / 100))
        resultado_label.configure(text=f'Valor final: R$ {valor_final:.2f}')
    except ValueError:
        resultado_label.configure(text='Entrada inválida')

# Janela principal
app = ctk.CTk() 
app.title('Contador de desconto')
app.geometry('500x500')

# Caixa de instrução de valor
label_preco = ctk.CTkLabel(app, text='Valor do produto')
label_preco.pack(pady=10)

                                                           #GUINHO!#

# Caixa de digitação de valor
campo_valor = ctk.CTkEntry(app, placeholder_text='Digite o valor')
campo_valor.pack(pady=10)

# Caixa de instrução de desconto
label_desconto = ctk.CTkLabel(app, text='Valor do Desconto (%)')
label_desconto.pack(pady=10)

# Caixa de digitação de desconto
campo_desconto = ctk.CTkEntry(app, placeholder_text='Digite o Desconto')
campo_desconto.pack(pady=10)

# Botão de cálculo
botao_calculo = ctk.CTkButton(app, text='Calcular', command=Calculo)
botao_calculo.pack(pady=10)

# Label para exibir o resultado
resultado_label = ctk.CTkLabel(app, text='') 
resultado_label.pack(pady=10)

# Iniciar a aplicação
app.mainloop()
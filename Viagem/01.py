import customtkinter as ctk

ctk.set_appearance_mode('dark')

def calcular():
    d = int(distancia.get())
    c = int(consumo.get())
    p = float(preco.get())
    calculo = (d / c) * p
    resultado.configure(text=f'O valor gasto na viagem é: R${calculo:.2f}')

#aqui começa a janela.
janela = ctk.CTk()
janela.geometry('600x400')
janela.resizable(False, False)
janela.title('APP VIAGEM')
janela.iconbitmap('InterFace/01.ico')

titulo = ctk.CTkLabel(janela,
                      text='APP VIAGEM',
                        text_color='blue', 
                        font=('Verdana', 40
                         ))
titulo.pack(pady=20)

distancia = ctk.CTkEntry(janela,
                     width=400,
                        height=40,
                        placeholder_text='Digite a distância da viagem em KM',
                        border_color='blue',
                        text_color='black')
distancia.pack(pady=20)

consumo = ctk.CTkEntry(janela,
                     width=400,
                        height=40,
                        placeholder_text='Digite o consumo do veículo: ',
                        border_color='blue',
                        text_color='black')
consumo.pack(pady=20)

preco = ctk.CTkEntry(janela,
                     width=400,
                        height=40,
                        placeholder_text='Digite o nível atual do combustível: ',
                        border_color='blue',
                        text_color='black')
preco.pack(pady=20)

botao = ctk.CTkButton(janela,
                     text='Calcular',
                        width=150,
                        height=30,
                        font=('verdana',20),
                        fg_color='blue',
                        text_color='black',
                        command=calcular
                        )
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                        text='',
                        text_color='blue', 
                        font=('Verdana', 20
                         ))
resultado.pack(pady=10)

janela.mainloop()
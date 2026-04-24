import customtkinter as ctk

ctk.set_appearance_mode('dark')

#aqui começa a janela.
janela = ctk.CTk()
janela.geometry('600x400')
janela.resizable(False, False)
janela.title('Sistema de Acesso')
janela.iconbitmap('01.ico')

#elementos de dentro da janela.

titulo = ctk.CTkLabel(janela,
                      text='Sisteme da Acesso',
                      text_color='blue',
                      font=('Verdana', 40
                         ))
titulo.pack(pady=20) 


login = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='Digite o seu Login',
                     border_color='blue')
login.pack()

senha = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     placeholder_text='Digite o sua senha',
                     border_color='blue',
                     show='🥈')
senha.pack(pady=20)

botao = ctk.CTkButton(janela,
                     text='Acessar',
                     width=150,
                     height=40,
                     font=('verdana',20),
                     fg_color='yellow',
                     text_color='black')
botao.pack(pady=30)



janela.mainloop()
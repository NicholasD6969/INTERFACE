import customtkinter as ctk
ctk.set_appearance_mode("dark")

#função para calcular a média
def calcular():
    media = (float(unidade1.get()) + float(unidade2.get()) + float(unidade3.get())) / 3
    if media >= 5:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    resultado.configure(text=f"Média: {media:.2f} - \n Situação: {situacao}")

janela = ctk.CTk()
janela.geometry("600x450")
janela.title("Boletim Escolar 2026")
janela.resizable(False, False)

titulo = ctk.CTkLabel(janela,
                      text="Boletim Escolar 2026",
                      font=('Verdana', 35),
                      text_color="White")
titulo.pack(pady=20)

unidade1 = ctk.CTkEntry(janela,
                       width=300,
                       height=35,
                       placeholder_text="Nota da 1º Unidade",
                       border_color="White",
                       border_width=4)

unidade1.pack(pady=10)

unidade2 = ctk.CTkEntry(janela,
                       width=300,
                       height=35,
                       placeholder_text="Nota da 2º Unidade",
                       border_color="White",
                       border_width=4)

unidade2.pack(pady=10)

unidade3 = ctk.CTkEntry(janela,
                       width=300,
                       height=35,
                       placeholder_text="Nota da 3º Unidade",
                       border_color="White",
                       border_width=4)

unidade3.pack(pady=10)

botao = ctk.CTkButton(janela,
                      text="Calcular Média",
                      width=300,
                      height=35,
                      fg_color="White",
                    text_color="Black",
                        command=calcular
                    )

botao.pack(pady=20)

resultado = ctk.CTkLabel(janela,
                         text="",
                        font=('Verdana', 25),
                        text_color="White",)

resultado.pack(pady=20)

janela.mainloop()   
from tkinter import *
from ttkthemes import ThemedTk

def on_button_click():
    print("Botão clicado!")

master = ThemedTk(theme="arc")  # Escolha um tema que não tenha bordas
master.geometry("500x600")
master.resizable(width=False, height=False)
# Importar imagens
img_fundo = PhotoImage(file="photoFif.png")
img_botao = PhotoImage(file="botao.png")

# Exibir imagem em um Canvas
canvas = Canvas(master, width=500, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=img_fundo)

# Calcular a posição central para o botão
pos_x = (489 - img_botao.width()) // 2
pos_y = (448 - img_botao.height()) // 2

# Criar botão com imagem
botao = Button(master, image=img_botao, command=on_button_click, bd=0)
botao.image = img_botao  # Garante que a imagem não seja destruída pela coleta de lixo
botao.place(x=pos_x, y=pos_y)

master.mainloop()

import tkinter as tk
from cProfile import label

janela = tk.Tk()  # Desenha a tela

janela.title("Minha Primera Janela")

texto = tk.Label(janela, text="Este texto está dentro da janela")
texto2 = tk.Label(janela, text="Este é outro texto")
texto3 = tk.Label(janela, text="SENAI Jandira")

texto.grid(column=0, row=0)
texto2.grid(column=1, row=1)
texto3.grid(column=2, row=2)












janela.mainloop()  # Mantém a tela vizível em loop infinito



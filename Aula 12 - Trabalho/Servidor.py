from tkinter import *
from tkinter import messagebox

def muda():
    frame.destroy()
    frame2 = Frame(tk)
    frame2.grid()
    tk.title("Inscrever||Entrar")
    Label(frame2, text="Para se inscrever ou entrar digite").grid(row=1, columnspan=4)
    Label(frame2, text="Seu nome:").grid(row=2, column=1)
    Label(frame2, text="Sua senha").grid(row=3, column=1)
    nome = Entry(frame2)
    nome.grid(row=2, column=2)
    senha = Entry(frame2)
    senha.grid(row=3, column=2, columnspan=2)
    Button(frame2, text="entrar", command=lambda: frame2.quit()).grid(row=4, column=2)

tk = Tk()
tk.title("Key Manager")
tk.grid()

titulo = Label(tk, text="Gerenciador de Chaves")
titulo.grid()

frame = Frame(tk)
frame.grid()
txt = """aqui é possivel armazenar suas senhas em um lugar seguro
trocar se estiverem fracas
checar sua segurança
criar senhas aleatórias a acessa-las se necessario"""
Label(frame,text= txt).grid()
Button(frame, text="Vamos começar", command=lambda:muda()).grid()


sair = Button(text="sair", command=lambda: tk.quit())
sair.grid()
mainloop()
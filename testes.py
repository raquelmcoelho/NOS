from tkinter import *
window = Tk()
window.grid()
window.geometry("600x500")
window["bg"]="black"
frame = Frame(window, bg="black", padx=40, pady=50)
frame.grid(sticky=W)
txt = [
"""
Seja bem-vindo(a) ao Gerenciador de senhas!!""",
"""
Aqui você pode armazenar suas senhas de uma maneira organizadada,
checar se suas senhas atuais estão seguras, 
criar senhas novas totalmente fortes
e substituir senhar fracas ☺
"""]
texto = """
%50s
%60s %20s
%50s
    """ % (7*"\n", txt[1], 50*"-", 7*"\n")
lbl= Label(frame, text=texto)
lbl.grid()
mainloop()



r"""from tkinter import *
from tkinter import messagebox


# Funções
# todo
def start():
    texto = """
"""%s
Seja bem-vindo(a) ao Gerenciador de senhas!!

Aqui você pode armazenar suas senhas de uma maneira organizadada,
checar se suas senhas atuais estão seguras, 
criar senhas novas totalmente fortes
e substituir senhar fracas ☺
%s"""
"""
    messagebox.showinfo('Bem-Vindo', texto)
    frame.destroy()
    frame2, frame3 = Frame(window), Frame(window)



def ajuda():
    texto2 = "Instruções"
    messagebox.showinfo('Intruções', texto2)



# Interface gráfica
window = Tk()
window.configure(bg="lightpink")
window.title("Gerenciador de Senhas")
window.geometry("400x400")
window.grid()

# todo
frame = Frame(window, bg="lightpink", borderwidth=10,  cursor="dotbox", relief=RAISED, bd=10)
frame.grid()

# bem vindo
#lblimg = PhotoImage(file="C:que\Pictures\chave.png")
lbl = Label(frame, text="Gerenciador de Senhas", bg = "lightpink")
lbl.grid()

# botão de intruções, começar, sair
comecar = Button(frame, text="começar", command=lambda: start())
comecar.grid()
instrucoes = Button(window, text="Instruções", command=lambda: ajuda())
instrucoes.grid()
sair = Button(window, text="sair", command=lambda: window.quit())
sair.grid()
mainloop()




"""
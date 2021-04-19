"""1. Utilizar exercícios das aulas anteriores e criar interfaces gráficas
para eles."""
from tkinter import *

# matriz com o que precisa estar escrito na tabela
Azeite = ["Azeite de oliva - Extra Virgem LAT 500 ml", 100, 40, 21.90, 1314]
Castanha = ["Castanha do Pará Granel (Gr)", 100, 5, 6.00, 300]
Flocos = ["Flocos de Aveia CXA 500g", 1000, 200, 10.90, 872]
Pacoca = ["Paçoca de Amendoim - CXA 30 Und", 100, 8, 1.50, 30]
Panetone = ["Panetone sem  Gluten - CXA 1 Und", 100, 60, 17.30, 692]
Pao = ["Pão Sirio Integral Saco 500g", 100, 70, 5.90, 177]
Polpa = ["Polpa de Açai Natural PCT 5L", 100, 1, 7.10, 639]
Queijo = ["Queijo Vegano PCT 450g", 100, 30, 25.00, 1750]
categorias = ["Nome do produto", "QTD entrada", "QTD saida", "Preço", "Subtotal"]
produtos = [categorias, Azeite, Castanha, Flocos, Pacoca, Panetone, Pao, Polpa, Queijo]

# criando janela
total = 0
tk = Tk()
tk.geometry("970x600")
tk.configure(bg="black")
tk.title("TABELA DE PRODUTOS")
fram = Frame(tk)
fram.configure(bg="black")
fram.pack()

# linha
k = 0
# passar pela matrizes de produtor
for m, i in enumerate(produtos):
    # se for a primeira matriz, que contém as categorias, terá fontes diferentes
    if m == 0:
        fonte = ("Impact", "15")
        espaco1 = 20*"-"+"|"
        espaco2 = 70*"-"+"|"
    else:
        fonte = ('Times', '15', "italic")
        espaco1 = 17*"-"+"|"
        espaco2 = 60*"-"+"|"

    # passar pelo produto
    for n, j in enumerate(i):
        Label(fram, text=str(j)+"|", font=fonte,  fg="deeppink", bg="black").grid(row=k, column=n, sticky=E)
        if n != 0:
            Label(fram, text=espaco1, font=fonte,  fg="deeppink", bg="black").grid(row=k+1, column=n, sticky=N)
        else:
            Label(fram, text=espaco2, font=fonte,  fg="deeppink", bg="black").grid(row=k + 1, column=n, sticky=NE)
    if type(i[4]) != str:
        total += i[4]
    k += 2


# função que retorna o total
def totalf():
    fram.pack_forget()
    Label(tk, text="R$ %d" % total, fg="deeppink", bg="black", font=("times", "13")).pack()
    Button(tk, text="Sair", font="times", bg="deeppink", command=tk.quit).pack()


Button(fram, text="Preço Total", font="times", bg="deeppink", command=totalf).grid(row=k+1, column=1)
Button(fram, text="Sair", font="times", bg="deeppink", command=tk.quit).grid(row=k+2, column=1)
mainloop()

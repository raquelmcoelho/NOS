"""
Reproduza o conteúdo da tabela mostrada usando comandos a
saída formatada do Python para exibir os dados em formato texto.
Ver exemplo.
"""
def tabela():
    Azeite = ["Azeite de oliva - Extra Virgem LAT 500 ml", 100, 40, 21.90, 1314]
    Castanha = ["Castanha do Pará Granel (Gr)", 100, 5, 6.00, 300]
    Flocos = ["Flocos de Aveia CXA 500g", 1000, 200, 10.90, 872]
    Pacoca = ["Paçoca de Amendoim - CXA 30 Und", 100, 8, 1.50, 30]
    Panetone = ["Panetone sem  Gluten - CXA 1 Und", 100, 60, 17.30, 692]
    Pao = ["Pão Sirio Integral Saco 500g", 100, 70, 5.90, 177]
    Polpa = ["Polpa de Açai Natural PCT 5L", 100, 1, 7.10, 639]
    Queijo = ["Queijo Vegano PCT 450g", 100, 30, 25.00, 1750]
    produtos = [Azeite, Castanha, Flocos, Pacoca, Panetone, Pao, Polpa, Queijo]
    total = 0
    a = "|%45s | %15s | %15s | %15s | %15s | %15s |"
    d = "|"+(46*"-" + "+") + 5*(17*"-" + "+")

    print(d)
    print(a % ("nome do produto", "QTD entrada", "QTD saida", "saldo estoque", "preço unitário", "subtotal"))
    for i in produtos:
        c = i[1] - i[2]
        total += i[4]
        print(d)
        print("|%45s | %15s | %15s | %15s | %15.2f | %15.2f |" % (i[0], i[1], i[2], c, i[3], i[4]))
    print(d)
    print("| %116s | %15.2f |" % ("total", total))
    print(d)

tabela()
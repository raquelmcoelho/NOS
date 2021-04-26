import Funções

#QUARTA QUESTÃO
#4.Escrever uma função que receba uma data no formato DD/MM/AAAA, caso contrário uma mensagem
#de erro é exibida ao usuário, e ainda que retorne uma string no formato "D, (mês por extenso) de XXXX"

def extenso(data):
    lista = data.split("/")
    lista = [float(x) for x in lista]
    lista = [Funções.checar(x) for x in lista]
    if len(lista) < 3:
        print("erro, números insuficientes")
    else:
        lista= [int(x) for x in lista]
        dia, mes, ano = lista
        list2= [0, "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        mes = list2[mes]
        print(f"{dia} {mes} de {ano}")

a = input("insira uma data válida:")
extenso(a)
print("""6°). Escrever um programa que coleta a senha do usuário (previamente ajustada)
armazena a senha digitada em uma lista e retorna a quantidade de vezes que o
usuário precisou para digitar a senha correta.""")

lista = []
h = input("\nqual a senha: ")
lista.append(h)
while h != "senha correta":
    h = input("tente novamente: ")
    lista.append(h)
print("\n Quantidade de tentativas:\n ", len(lista), "\n Tentativas:\n ",  lista)


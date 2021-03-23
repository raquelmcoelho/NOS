#AULA 02 DE SOR
#PRIMEIRA QUESTÃO
print("1°) Um código que soma todos os valores de uma lista")

lista1 = [1, 2, 3]
print("\nlista:\n", lista1, "\nsoma:\n", sum(lista1))


#SEGUNDA QUESTÃO
print("\n \n2°) Dividir uma lista em 3 listas de mesmo tamanho")

lista2 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("lista:\n", lista2)
if len(lista2) % 3.0 == 0.0:
    a = int(len(lista2)/3)
    b = 0
    print("\ndivisões:")
    while b < len(lista2):
          print(lista2[b:b+a])
          b += a
else:
    print("não é divisível por 3")


#TERCEIRA QUESTÃO
print("\n \n 3°) maior e menor valor e mediana de uma lista")
lista3 = [5,2,3,4,1,6]
print("lista:", lista3)
lista3 = sorted(lista3)
max= lista3[-1]
min= lista3[0]
c = len(lista3)
if c % 2.0 == 0.0:
    mediana = ( lista3[int(c/2)] + lista3[(int(c/2)-1)])/2
else:
    mediana = lista3[int((c-1)/2)]
print("lista organizada:", lista3)
print("\nmax:", max, "\nmin:", min, "\nmediana:", mediana)


#QUARTA QUESTÃO
print("\n\n4°) tirar duplicatas de uma lista")
lista4 = [1,2,3,4,5,6,7,8,9,10, 2, 2, 2, 2]
print("lista:", lista4, "\nsem duplicatas:",list(set(lista4)))


#QUARTA QUESTÃO (outros métodos)
print("\noutro médodo de realizar a quarta:\n")

lista4_1 = [ 1, 1 , 1 , 1, 1.1, "1", "1", 22, 22, 34, 12, 34]
print("lista:", lista4_1)
for d in lista4_1:
    while lista4_1.count(d) > 1:
        lista4_1.remove(d)
print("sem duplicatas:", lista4_1)


#QUINTA QUESTÃO
print("\n\n5°)lista com números inteiros, retorna uma nova lista com os números ímpares (ou pares) contidos nesta lista.\n")
lista5 = [1,2,3,4,5,6,7,8]
print("lista original:",lista5)
pares = list(filter(lambda e: e % 2 == 0, lista5))
for f in pares:
  lista5.remove(f)
impares = lista5
print("pares:", pares, "\nímpares:", impares)


#QUINTA QUESTÃO (outros métodos)
print("\noutra forma de realizar a quinta:")
lista5_1, pares2, impares2= [7,6,5,4,3,2,1], [], []
for g in lista5_1:
    pares2.append(g) if g % 2 ==0 else impares2.append(g)
print("\nlista:", lista5_1, "\npares:", pares2, "\nímpares", impares2)



#SEXTA QUESTÃO
print("""\n\n6°). Escrever um programa que coleta a senha do usuário (previamente ajustada)
armazena a senha digitada em uma lista e retorna a quantidade de vezes que o
usuário precisou para digitar a senha correta.""")
lista6=[]
h = input("qual a senha: ")
lista6.append(h)
while h != "senha":
    h = input("tente novamente: ")
    lista6.append(h)
print("\n Quantidade de tentativas:\n ", len(lista6), "\n Tentativas:\n ",  lista6)


#SÉTIMA QUESTÃO
print("""\n\n7°. A partir de uma faixa de números, fazer a varredura a partir do enésimo número até o
final e imprima a soma do número atual e os anteriores.""")
lista7=[4, 3, 2, 1]
print(lista7)
i = int(input("número que você quer começar a soma na lista:\n"))
soma = 0
for j in range(i, len(lista7)):
    soma += lista7[j]
    print(j, "número da lista", "= ", lista7[j])
print("soma:", soma)



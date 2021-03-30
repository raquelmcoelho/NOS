from Funções import checar
import math

#SEGUNDA QUESTÃO
#2. Escrever uma função que calcule a raiz quadrada de um número positivo.
def raiz(n2):
    n2 = checar(n2)
    return print(math.sqrt(n2))


raiz(input("\nMe dê um numero e lhe retornarei a raiz quadrada:\n"))

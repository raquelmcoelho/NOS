import math
from Funções import checar

#PRIMEIRA QUESTÃO
#1. Escrever uma função que calcule o fatorial de um número inteiro. Uma mensagem de erro deve ser
#exibida, caso um número inteiro não positivo seja passado.

def fatorial(n):
        n = checar(n)
        fat = 1
        while n > 0:
           print(f"{n} * ", end=" ")
           fat = fat * n
           n-=1
        print(f"= {fat}")


n = input("\nMe dê um valor e lhe retornarei seu fatorial:")
fatorial(n)
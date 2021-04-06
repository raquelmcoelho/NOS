
"""5.Qual o tamanho ocupado na memória por um inteiro? Uma String vazia? Uma string de um único
caractere? E por um Byte de um caractere? """

import sys
lista = [1, "", "1", b"1"]
lista2 = ["inteiro", "string vazia", "string com 1 caractere", "byte de um caractere"]
for x in zip(lista, lista2):
    print(x[1], ":", x[0])
    print("tamanho ocupado na memória : ", sys.getsizeof(x[0]), "\n")


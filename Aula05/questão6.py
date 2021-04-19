"""
6. Criar um script que exiba a quantidade de memória ocupada por uma lista vazia, lista com
apenas um elemento de 1 caractere, com dois caracteres, três, até 10 caracteres.
Depois repita o exemplo anterior para inteiros de 1, 2, 3, 4, 5, 6...
"""
print("caracteres:")
lista = []
while len(lista) < 10:
    for i in range(1, 12):
        print("memória ocupada:", lista.__sizeof__(), lista)
        lista.append(i * "a")

print("\ninteiros:")
lista.clear()
while len(lista) < 10:
    for i in range(12):
        print("memória ocupada:", lista.__sizeof__(), lista)
        lista.append(i)

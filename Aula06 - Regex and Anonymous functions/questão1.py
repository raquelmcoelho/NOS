"""
01- Dada a lista [‘abc’, ‘def’, ‘ghi’] aplique uma função para converter cada ítem da
lista em letras maiúsculas, criando uma nova lista. Depois repita a operação convertendo
o primeiro caractere de cada ítem em caractere maiúsculo. Exemplo: 'Abc'.
"""

lista = ['abc', 'def', 'ghi']
print( list(map(lambda x: x.upper(), lista)),list(map(lambda x: x.capitalize(), lista)) )
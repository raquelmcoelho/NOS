print("2°) Dividir uma lista em 3 listas de mesmo tamanho")

lista = [11, 45, 8, 23, 14, 12, 78, 45, 89, 11, 12, 13]
print("lista:\n", lista)

if len(lista) % 3.0 == 0.0:
    a = int(len(lista)/3)
    b = 0
    print("\ndivisões:")
    while b < len(lista):
        print(lista[b:b+a])
        b += a
else:
    print("não é divisível por 3")

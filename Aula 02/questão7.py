print("""7°. A partir de uma faixa de números, fazer a varredura a partir do enésimo número até o
final e imprima a soma do número atual e os anteriores.""")

lista = [16, 15, 53, 12, 4, 3, 2, 1]
print(lista)
i = int(input(f"\níndice que você quer começar a soma na lista (0-{len(lista)-1}):\n"))
for j in range(i, len(lista)):
    print(j, "número da lista", "= ", lista[j])
print("soma:", sum(lista[i::1]))

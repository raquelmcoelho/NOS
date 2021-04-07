print("5°)lista com números inteiros, retorna uma nova lista com os números (ím)pares contidos nesta lista.\n")

lista, pares, impares = [7, 1, 2, 54, 0, 6, 5, 4, 3, 2, 1], [], []
for g in lista:
    pares.append(g) if g % 2 == 0 else impares.append(g)
print("\nlista:", lista, "\npares:", pares, "\nímpares", impares)

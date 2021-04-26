print("3°) maior e menor valor e mediana de uma lista")

lista = [5, 2, 3, 4, 1, 6]
print("lista:", lista)
lista = sorted(lista)
maximo = lista[-1]
minimo = lista[0]
a = len(lista)
if a % 2.0 == 0.0:
    mediana = (lista[int(a/2)] + lista[(int(a/2)-1)])/2
else:
    mediana = lista[int((a-1)/2)]
print("lista organizada:", lista)
print("\nmax:", maximo, "\nmin:", minimo, "\nmediana:", mediana)


#TERCEIRA QUESTÃO
#3. Criar funções que retornem a área e perímetro de um triângulo retângulo e em um novo script importar essas funções.

import Funções as f

def triangulo(l1, l2):
    l1, l2= f.checar(l1), f.checar(l2)
    print("\n\nCatetos:",l1,",", l2, "\nHipotenusa:", f.hipotenusa(l1,l2))
    print("Área", f.area(l1,l2), "\nPerimetro:", f.perimetro(l1,l2))

triangulo(input("cateto 1:"), input("cateto 2:"))


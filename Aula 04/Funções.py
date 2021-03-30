import math

def checar(n1):
    while float(n1) % 1 != 0.0 or int(n1) < 0:
        print(f"!!!{n1} precisa ser um número inteiro e ser positivo!!!\n")
        n1 = input("tente novamente:\n")
    else:
        n1 = int(n1)
    return n1

def hipotenusa(l1,l2):
    return math.sqrt(l1**2 + l2**2)

def area(l1,l2):
    area = (l1 * l2)/2
    return area

def perimetro(l1, l2):
    perimetro = l1 + l2 + hipotenusa(l1, l2)
    return perimetro
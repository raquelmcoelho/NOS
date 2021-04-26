"""
2. Criar uma lista (angulos) com os ângulos do círculo trigonométrico (0-359) para, a partir
dela criar 3 novas listas (sen, cos, tan) contendo o valor das funções trigonométricas de
cada ângulo como um elemento das listas. Exemplo sen = [0, 0,017, 0,034, ...], cos = [1,
0,9998, 0,9993], tan = [0, 0,01745, 0,3492]
"""

import math
lista = []
[lista.append(i) for i in range(0,360)]
lista = list(map(math.radians, lista))
sen = list(map(math.sin, lista))
cos = list(map(math.cos, lista))
tan = list(map(math.tan, lista))
print("lista:\n",lista, "\nsen:\n", sen, "\ncos:\n", cos, "\ntan:\n", tan)

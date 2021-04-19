"""
4.Defina uma variável inteira, um float e um decimal atribuindo valores a cada um deles. Qual a
quantidade de memória utilizada por cada um deles?
"""

from decimal import Decimal
i = 1
f = 1.0
d = Decimal(1)
print("espaço ocupado na memória por um:")
print("int:", i.__sizeof__(), "\nfloat:", f.__sizeof__(), "\ndecimal:", d.__sizeof__())












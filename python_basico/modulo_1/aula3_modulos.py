# import math
from math import sqrt, ceil
import random
num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é igual á {raiz:.2f}') # setando apenas 2 numero após a vingula
print(f'A raiz de {num} é igual á {ceil(raiz)}') # arredondando para cima

print('=' * 45)

# Gerando numeros aliatórios
numero = random.randint(1, 10)
print(numero)

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é igual á {raiz:.2f}') # setando apenas 2 numero após a vingula
print(f'A raiz de {num} é igual á {math.ceil(raiz)}') # arredondando

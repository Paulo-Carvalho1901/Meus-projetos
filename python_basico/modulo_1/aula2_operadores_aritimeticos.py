# Operadores aritiméricos

"""
+ adição
- subtração
* multiplicação
/ Divisão
** potencia
// divisão inteira
% moduo ou resto
"""

"""
Ordem de precedencia
1.()
2.**
3.* / // %
4 + -
"""

# expresão
ex1 = 5 + (3 * 2)
print(ex1)

ex2 = (3 * 5) + (4 ** 2)
print(ex2)

ex3 = 3 * (5 + 4) ** 2
print(ex3)

print('=' * 30)
print('PRATIICA')
print()

nome = input('Qual é seu nome: ')
print(f'É uma prazer te conhecer {nome:=^34}!')

print()
print('=' * 30)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3}', end=' ')
print(f'A divisão inteira é {di} e potencia é {e}')

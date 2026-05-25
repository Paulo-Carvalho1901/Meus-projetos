"""
Crie um programa que leia quantos
dinheiro uma pessoa tem na carteira e
mostre quantos Dolares ela pode comprar.
"""

valor = float(input('Digite quanto de dinheiro voce quer converter R$: '))

resultado = valor / 5.02

print(f'Voce tem R${valor} e em dollar daria ${resultado:.2f}')

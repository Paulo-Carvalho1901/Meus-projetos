"""
Faça um algoritimo que leia
o preço de um produto e mostre
seu novo preço, com 5% de desconto.
"""

preco_original = float(input('Digite o valor: '))

novo_preco = preco_original * 1.05
print(f'Seu valor original é R$ {preco_original},')
print(f'Seu novo preço com aumento de 5% é de R$ {novo_preco}')

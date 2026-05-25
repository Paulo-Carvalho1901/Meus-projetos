"""
Faça um programa que leia a largura e a
altura de uma parede e mostre, calcule a sua
área e a quantidade de tinta necessaria para 
píntá-la, sabendo que cada litro de tinta
pinta uma área de 2 metros quadrados.
"""

lagura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = lagura * altura
tinta = area / 2

print(f'Sua parede tem {lagura}x{altura}.')
print(f'Com uma área no total de {area} metros quadrados')
print(f'A quantidade necessaria para pinta-la seria de {tinta} litros de tinta')

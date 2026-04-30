"""
Faça um programa que leia algo pelo
teclado e mostre na tela o seu tipo
primitivo e todas as informações
possiveis sobre ele
"""

entrada = input('Digite algo para ser avaliado: ')

print(f'O seu tipo primitivo é {type(entrada)}')
print(f'É númerico? {entrada.isdigit()}')
print(f'É alfabetico? {entrada.isalpha()}')
print(f'É numerico? {entrada.isnumeric()}')
print(f'É decimal? {entrada.isdecimal()}')
print(f'É alfanumerico? {entrada.isalnum()}')
print(f'É Maiusculo? {entrada.isupper()}')
print(f'É Minusculo? {entrada.islower()}')

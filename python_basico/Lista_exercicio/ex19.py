"""
Crie um programa que leia o nome
completo de uma pessoa e mostre:

O nome com todas as letras minusculas

O nome com todas as letras maisculas

Quantas letras ao todo sem considerar os espaços

Quantas letras tem o primeiro nome
"""

nome_completo = input('Digite seu nome completo: ')

print(f'Seu nome todas as letras maiuscula {nome_completo.upper()}')
print(f'Seu nome todas as letras minuscula {nome_completo.lower()}')
total_letra = len(nome_completo.replace(" ", "")) # replace corta os espaços.
print(f'Total letra (sem espaço) {total_letra}')
"""
Crie um programa que leia o
nome de uma cidade e diga se ela
começa com o nome "SANTO"
"""

nome_cidade = input('Digite da sua cidade: ')
primeiro_nome_cidade = nome_cidade.split()[0]

print('O nome da cidade começa com Santo', primeiro_nome_cidade in 'Santo')

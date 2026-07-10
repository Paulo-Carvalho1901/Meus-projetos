"""
Faça um programa que leia o nome completo
de uma pessoa mostrando em seguinda o primeiro e o ultimo
nome separadamente.

ex: Ana Maria de Souza
Primeiro: Ana
Segundo: Maria
"""
nome_completo = input('Digite seu nome: ')
primeiro_nome = nome_completo.split()[0]
ultimo_nome = nome_completo.split()[-1]

print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu ultimo nome é {ultimo_nome}')


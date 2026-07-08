"""
Crie um programa que leia o nome
de uma pessoa e diga se ela
tem "Silva" no nome
"""

nome = input("Digite seu nome: ")

validando_nome = "silva" in nome.lower()
print(validando_nome)
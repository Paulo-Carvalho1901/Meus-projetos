"""
Faça um programa que leia um frase pelo
teclado e mostre:

Quantas vezes apareceu a palavra 'a'

Em qual posição ela apareceua primeira vez

Em qual posição ela apareceu a ultima vez

"""

frase = input('Digite uma frase: ').lower().strip()

print('Quantidade de "a" na frase:', frase.count('a'))
print('Primeiro posição de "a"  na frase:', frase.find('a') + 1)
print('A ultima posição de "a"', frase.rfind('a') + 1)

# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor da seno, cosseno e tangente
# desse ângulos.

import math

angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo)) # Calculando o seno do ângulo
cosseno = math.cos(math.radians(angulo)) # Calculando o cosseno


print(f'O ângulo de {angulo} de o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} de o COSSENO de {cosseno:.2f}')

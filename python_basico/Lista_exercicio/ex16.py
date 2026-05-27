# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor da seno, cosseno e tangente
# desse ângulos.

import math

angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo)) # Calculando o seno do ângulo


print(f'O ângulo de {angulo} de o SENO de {seno:.2f}')

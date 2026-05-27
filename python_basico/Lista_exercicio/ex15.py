# Faça um programa que leia o comprimento
# do cateto aposto e da coteto adjacente de um
# triângulo retângulo. Calcule e mostre comprimento
# da hipotenusa

# Calculo matematico da hipotenusa
co = float(input('Comprimento do coteto aposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')

print('=' * 40)

print('CALCULO COM IMPORTAÇÃO')
import math
co_2 = float(input('Comprimento do cateto aposto: '))
ca_2 = float(input('Comprimento do cateto adjacente: '))
hi_2 = math.hypot(co_2, ca_2)
print(f'A hipotenusa vai medir {hi_2:.2f}')

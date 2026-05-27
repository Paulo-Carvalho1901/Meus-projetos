# Faça um programa que leia o comprimento
# do cateto aposto e da coteto adjacente de um
# triângulo retângulo. Calcule e mostre comprimento
# da hipotenusa

co = float(input('Comprimento do coteto aposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')

# O mesmo professor do desafio anterior
# quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa
# que leia o nome dos quadro alunos e mostre a
# ordem sorteada

import random

alu1 = input('Digite o nome do primeiro aluno: ')
alu2 = input('Digite o nome do segundo aluno: ')
alu3 = input('Digite o nome do terceiro aluno: ')
alu4 = input('Digite o nome do quarto aluno: ')

lista = [alu1, alu2, alu3, alu4]

random.shuffle(lista)
    
print('A ordem de apresentação é de:')
for aluno in lista:
    print(aluno)

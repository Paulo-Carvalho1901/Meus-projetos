# um professor quer sortear um dos
# seus quadro alunos para apagar
# o quedro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo 
# o nome do escolhido.

import random

nome_alunos = ['Paulo', 'Andreia', 'Flavio', 'Davi']

sorteio = random.choices(nome_alunos)
print(*sorteio)

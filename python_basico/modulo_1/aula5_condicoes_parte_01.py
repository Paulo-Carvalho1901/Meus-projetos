"""
Estrutura condicional if else elif

Onde mudamos o fluxo de acordo com as condições
quando temos apenas if - estrutura condiocnal simples

quando temos else - estrutura condicional composta
"""

# nome = input('Qual é seu nome? ').capitalize()
# if nome == 'Paulo':
#     print('Que belo nome!')
# else:
#     print('Seu nome é normal!')
# print(f'Bom dia {nome}!', )

################################################################

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Sua média foi {media:.1f}')

# if media >= 6.0:
#     print(f'sua média de {media} foi boa! Parabéns! você passou!!!')
# else:
#     print('Desculpa sua média foi ruin! refaça a matéria!!!')

print(f'Parabéns você passou!' if media >= 6 else 'Estude mais!')

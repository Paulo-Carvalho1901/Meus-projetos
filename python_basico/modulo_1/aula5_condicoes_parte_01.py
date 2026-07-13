"""
Estrutura condicional if else elif

Onde mudamos o fluxo de acordo com as condições
quando temos apenas if - estrutura condiocnal simples

quando temos else - estrutura condicional composta
"""

nome = input('Qual é seu nome? ').capitalize()
if nome == 'Paulo':
    print('Que belo nome!')
else:
    print('Seu nome é normal!')
print(f'Bom dia {nome}!', )

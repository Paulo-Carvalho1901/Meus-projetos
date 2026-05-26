# Escreva um programa que pergunte 
# a quantidade de Km percoridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.

# Calcule o preço a pagar, sabendo que o carro custa 
# R$60 por dia e R$0,15 por km rodado.

km = float(input('Quantos Km utilizados? '))
dia = float(input('Quantos dias utilizado? '))

diaria = 60
km_rodado = 0.15

valor_diaria = dia * diaria
valor_km_rodado = km_rodado * km

soma_final = valor_diaria + valor_km_rodado

print(f'A soma das diarias a pagar é de R$ {valor_diaria}')
print(f'Valor do km rodado é R$ {valor_km_rodado}')
print(f'Sua conta foi de: R$ {soma_final}')

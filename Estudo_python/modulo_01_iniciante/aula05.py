# ==========================================================
# Aula 05 - Estruturas condicionais
# ==========================================================


# Programas podem tomar decisões.


idade = int(input("Digite sua idade: "))


# Estrutura de decisão

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


# ==========================================================
# EXERCÍCIO
#
# Faça um programa que verifique se um número
# é par ou ímpar.
# ==========================================================


numero = int(input("Digite um número: "))


# O operador % retorna o resto da divisão

if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")
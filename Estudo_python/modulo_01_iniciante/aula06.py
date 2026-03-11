# ==========================================================
# Aula 06 - Exercício final do módulo
# ==========================================================


# Vamos juntar tudo que aprendemos:
#
# - input
# - variáveis
# - cálculos
# - if / else


# Sistema simples de média escolar


nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


# Calculando média

media = (nota1 + nota2) / 2


print("Média do aluno:", media)


# Verificando aprovação

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")


# ==========================================================
# DESAFIO EXTRA
#
# Mostre também o nome do aluno junto com o resultado.
# ==========================================================
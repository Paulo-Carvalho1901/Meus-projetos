# Manipulando strings em Python

print("""
Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever is may be) can pick up Python very quickly.
Its also easy for beginner to use and learn, so junp in!
""")

# Fatiamento
frase = 'Curso em Video Python'
frase_2 ='   Aprenda Python   '
print(frase)
# frase[inicio:final:passo]
print('=' * 45)
# Fatiamento com range
print('Range do fatiamento')
print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])
print(frase[:5])
print(frase[15:])
print('=' * 45)
# escolhendo o passo do fatiamento
print('Escolhendo um passo')
print(frase[9:21:2])
print(frase[9::3])
print('=' * 45)
# Métodos da String
print('Analisando String')
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))

print('Operadores com fatiamento')
print('Curso' in frase)

print('=' * 45)
print('Transformação')
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase_2.strip())
print(frase_2.rstrip())
print(frase_2.lstrip())
print(frase.split())
print('-'.join(frase))

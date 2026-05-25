# Escreva um programa que converta 
# uma temperatura digitada em °C para °F

# A fórmula matemática para converter graus Celsius (C) para graus 
# Fahrenheit (F) é: F = (C * 9/5) + 32.

graus_c = float(input('Digite uma temperatura: '))

# Calculo
graus_f = (graus_c * 9/5) + 32

print(f'Temperatura em {graus_c}°C, corresponde à {graus_f}°F')

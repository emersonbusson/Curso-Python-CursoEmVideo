#Desafio 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Utilizando a estrutura while.
numero = int(input('Digite um número para calcular seu Factorial: '))

factorial = 1
print('Calculando {}! = '.format(numero), end=' ')
while numero > 0:
    print('{}'.format(numero), end=' ')
    print('X' if numero > 1 else ' = ', end= ' ')
    factorial *= numero
    numero -= 1
print('{}'.format(factorial))
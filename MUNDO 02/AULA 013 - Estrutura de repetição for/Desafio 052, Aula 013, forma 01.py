# Desafio 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero_entrada = int(input('Digite um número: '))

divisores = 0

cor = '\33[31'
for cont in range(1, numero_entrada + 1):
    if numero_entrada % cont == 0:
        print('\33[31m', end=' ') 
        divisores += 1
    else:
        print('', end=' ')
    print(f'{cont}\33[m', end=' ')

print(f'\nO nº: {numero_entrada}, foi divisivel: {divisores} vezes.')

if numero_entrada % 2 == 1 and numero_entrada != 1 or numero_entrada == 2 or numero_entrada == 5:
    print(' -= È um número PRIMO =-')
else:
    print(' -= Não é um número PRIMO =-')

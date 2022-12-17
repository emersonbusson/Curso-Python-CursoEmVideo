''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo '''

(print('===' *15))
numero = int(input('Digite um número para saber se ele é primo: '))
(print('===' *15))

cont = 0 # Váriavel (acumulador), vai acumular os divisiveis da variavel número.

for c in range(1, numero +1):
    if numero % c == 0:
        print('\33[31m', end=' ')
        cont += 1
    else:
        print(f'\33[35m', end=' ')
    print(f'{c}', end=' ')



print(f'\n\n \33[mO Nº \33[34m{numero}\33[m, foi divisivel: \33[33m{cont}\33[m vezes.')

if numero % 2 == 1 and numero != 1 or numero == 2 or numero == 5:
    print(f' -= Ele é um número \33[31mPRIMO\33[m =-')
else:
    print(f' -= Ele é \33[31mNão é número \33[35mPRIMO\33[m =-')





''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo '''

numero = int(input('Digite um número para saber se ele é primo: '))
cont = 0
soma = 0
print('-=' *30)

if numero % 2 == 1 and numero != 1 or numero == 2 or numero == 5:
    print(f'Número Digitado: {numero}, ele é \33[31mPRIMO\33[m')
    for c in range(1, numero + 1):
        soma += c
        cont += 1
        print(f' \33[32m{cont}\33[m')
        #print(c)
else:
    print(f'Esse {numero} não é primo ou inteiro')
    for c in range(1,numero + 1):
        cont += 1
        print(cont)
    print(f' o número {numero}foi divisivel {cont}')


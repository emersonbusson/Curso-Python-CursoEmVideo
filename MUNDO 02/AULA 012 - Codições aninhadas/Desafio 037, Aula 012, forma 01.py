# Desafio 037 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

import time
print('-' * 30)
print('CONVERSOR DE BASES NUMÉRICAS')
print('''
Escolha uma das opções abaixo para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
print('-' * 30)

base_conversao = int(input('Qual é a sua opção?  '))
numero_int = int(input('Digite um número inteiro: '))

print()
print('\033[:31mCONVERTENDO, POR FAVOR, AGUARDE...\033[m')
time.sleep(1.5)
print()

if base_conversao == 1:
    print('Conversão para BINÁRIO, resultado: {:b} '.format(numero_int))
elif base_conversao == 2:
    print('Conversão para OCTAL, resultado: {:o}'.format(numero_int))
elif base_conversao == 3:
    print('Conversão para HEXADECIMAL, resultado: {:x}'.format(numero_int))
else:
    print('\033[:33m OPÇÃO INVALIDA, TENTE NOVAMENTE...\033[m')

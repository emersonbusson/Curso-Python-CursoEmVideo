''' Desafio 037'''

'''Escrava um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de conversão: '''


''' 1 para binário'''
''' 2 para octal'''
''' 3 para hexadecimal'''

import time

nunero_int = int(input('Digite um número inteiro:'.title()))

base = int(input('Escolha uma das beses para conversão: \n [ 1 ] converter para BINÁRIO. \n [ 2 ] Converter para OCTAL. \n [ 3 ] convertar para HEXADECIMAL. \n Sua Opção: '.title()))

print('\033[:31mCONVERTENDO, POR FAVOR, AGUARDE...\033[m')
time.sleep(3)


if base == 1:
    print('Conversão para BINÁRIO, RESULTADO: {:b} '.format(nunero_int))
elif base == 2:
    print('Conversão para OCTAL, RESULTADO: {:o}'.format(nunero_int))
elif base == 3:
    print('Conversão para HEXADECIMAL, RESULTADO: {:x}'.format(nunero_int))
else:
    print('\033[:33m OPÇÃO INVALIDA, TENTE NOVAMENTE...\033[m')

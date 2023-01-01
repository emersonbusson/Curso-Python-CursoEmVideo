# Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo ou não.

print('___'*20)
print('TRIANGULAR ANALISADOR')
print('___'*20)
reta1 = float(input('DIGITE O VALOR DO PRIMEIRO SEGMENTO(RETA): '))
print('___'*20)
reta2 = float(input('DIGITE O VALOR DA SEGUNDO SEGEMENTO(RETA): '))
print('___'*20)
reta3 = float(input('DIGITE O VALOR DA TERCEIRO SEGMENTO(RETA): '))
print('___'*20)

import time
print('CALCULANDO.......')
time.sleep(2)
print('-='*25)
if (reta1 + reta2) > reta3 and (reta3 + reta2) > reta1 and (reta1 + reta3) > reta2:
    print('OS SEGMENTOS CITADOS, PODEM FORMAR UM TRIANGULO! ')
else:
    print('OS SEGMENTOS CITADOS, NÃO PODEM FORMATAR UM TRIANGULO!')
print('-='*25)
'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo ou não.'''

print('___'*20)
print('TRIANGULAR ANALISADOR')
print('___'*20)
r1 = float(input('DIGITE O VALOR DO PRIMEIRO SEGMENTO(RETA):'))
print('___'*20)
r2 = float(input('DIGITE O VALOR DA SEGUNDO SEGEMENTO(RETA):'))
print('___'*20)
r3 = float(input('DIGITE O VALOR DA TERCEIRO SEGMENTO(RETA):'))
print('___'*20)

import time
print('CALCULANDO.......')
time.sleep(2)
print('-='*25)
if (r1 + r2) > r3 and (r3 + r2) > r1 and (r1 + r3) > r2:
    print('OS SEGMENTOS CITADOS, PODEM FORMAR UM TRIANGULO! ')
else:
    print('OS SEGMENTOS CITADOS, NÃO PODEM FORMATAR UM TRIANGULO')
'''Refarça o Desafio 035, dos triângulos, acrecetando o recurso de mostar que tipo de triângulo será formado:'''
# Equílatero: todos os lados iguais.
# ISósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

import time

print('___'*20)
print('TRIANGULAR ANALISADOR')
print('___'*20)
r1 = float(input('DIGITE O VALOR DO PRIMEIRO SEGMENTO(RETA):'))
print('___'*20)
r2 = float(input('DIGITE O VALOR DA SEGUNDO SEGEMENTO(RETA):'))
print('___'*20)
r3 = float(input('DIGITE O VALOR DA TERCEIRO SEGMENTO(RETA):'))
print('___'*20)

print('CALCULANDO.......')
time.sleep(2)
print('-='*25)


if (r1 + r2) > r3 and (r3 + r2) > r1 and (r1 + r3) > r2:
     print('OS SEGMENTOS CITADOS, PODEM FORMAR UM TRIANGULO! ')
     if r1 == r2 and r3 == r1 and r3 == r2:
        print('Este é: #Equilátero.')
     elif r1 != r2 and r3 != r1 and r3 != r2:
        print('Este é: #Escaleno.')
     else:
        print('Este é: #ISósceles ')
else:
    print('OS SEGMENTOS CITADOS, NÃO PODEM FORMATAR UM TRIANGULO')

''' if r1 == r2 == r3:
        
     elif r1 != r2 != r3 != r1:
        print('Este é: #Escaleno.')'''
#outra forma de utilizar os operadores relacionais sem escrever os operadores logicos.
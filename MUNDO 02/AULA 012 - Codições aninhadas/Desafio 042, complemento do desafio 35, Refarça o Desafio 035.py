#Desafio 042 - Refazer o desafio 035 de triângulos, adicionando a funcionalidade de identificar o tipo de triângulo formado: se todos os lados são iguais, trata-se de um triângulo EQUILÁTERO; se dois lados são iguais, trata-se de um triângulo ISÓSCELES; se todos os lados são diferentes, trata-se de um triângulo ESCALENO."

import time

print(f'{("TRIANGULAR ANALISADOR"):=^50}')

reta_ladoA = float(input('Digite o lado "A" do triângulo: '))
print()
reta_ladoB = float(input('Digite o lado "B" do triângulo: '))
print()
reta_ladoC = float(input('Digite o lado "C" do triângulo: '))
print()
print('CALCULANDO.......')
time.sleep(1.5)
print()

if (reta_ladoA < (reta_ladoB + reta_ladoC)) and (reta_ladoB < (reta_ladoA + reta_ladoC)) and (reta_ladoC < (reta_ladoA + reta_ladoB)):
     print('Os segmentos citados, podem formar um triângulo!')
     print()
     if reta_ladoA == reta_ladoB == reta_ladoC:
        print('Este triângulo é: #EQUILATERO - um triângulo com lados de comprimento igual. ')
     elif reta_ladoA != reta_ladoB and reta_ladoC != reta_ladoA and reta_ladoC != reta_ladoB:
        print('Este triângulo é: #ESCALENO - um triângulo com todos os lados de comprimento diferente.')
     else:
        print('Este triângulo é: #ISÓSCELES - um triângulo com pelo menos dois lados de comprimento igual.')
else:
    print('os segmentos citados, não podem formar um triângulo')
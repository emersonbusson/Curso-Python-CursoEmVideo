'''Faça um programa que mostre na tela um contagem regressima para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles. '''

import time

for c in range(10,-1,-1,):
    time.sleep(1)
    print(c)
print('BUMM BUMMM POWW')

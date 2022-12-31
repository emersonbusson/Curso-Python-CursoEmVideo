# Desafio 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

import time

print('=-' *20)
velocidade_carro = int(input('Digite a velocidade do carro: '))
print('=-' *20)

print('PROCESSANDO...')
time.sleep(1.5)
if velocidade_carro <= 80:
    print('Você está em uma velocidade permitida: {} km/h, não foi multado.'.format(velocidade_carro))
else:
    valor_multa = (velocidade_carro - 80) * 7
    print(' Você está acima da velocidade permitida que é de 80 km/h, você foi multado em R$: {:.2f} '.format(valor_multa))
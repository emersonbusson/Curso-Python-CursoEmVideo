'''Escreve um programa que leia a velocidade de um carro.'''

'''Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.'''

'''A multa vai custar R$ 7, por cada km acima do limite'''

import time

print('=-' *20)
multa = int(input('Digite a velocidade de um carro:'))
print('=-' *20)

print('PROCESSANDO...')
time.sleep(3)
if multa <= 80:
    print('Você está na velocidade permitida, não foi multado.'.format(multa))
else:
    valor = (multa - 80)*7
    print(' Você está acima da velocidade permitida que é de 80km/h, você foi multado em: R$ {}.'.format(valor))


# Desafio 031 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

import time

distancia_km = float(input('Digite a distância em kM da Sua Viagem: '))
print('Calculando...')
time.sleep(1.0)
preco_menor_200km = 0.50
preco_acima_200km = 0.45

if distancia_km <= 200 :
    print('O valor por kM desta viagem é R$: {:.2f}'.format(preco_menor_200km))
    print('O preço da passagem é: R$ {:.2f}'.format(distancia_km * preco_menor_200km))
else:
    print('O valor por kM a ser pago com desconto por longa distância: R$ {:.2f} '.format(preco_acima_200km))
    print('O preço da passagem é: R$ {:.2f}'.format(distancia_km * preco_acima_200km))
'''DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM.'''


'''CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0,50, POR KM, PARA VIAGENS DE ATÉ 200KM, E R$ 0,45, PARA VIAGENS MAIS LONGAS.'''

import time
print('___' *20)
kmdiguser = float(input('Digite a quantidade de KM da Sua Viagem:'))
print('___' *20)
print('CALCULANDO O VALOR A SER PAGO POR "KM", POR FAVOR, AGUARDE...')
time.sleep(2)
print('___' *20)

km200 = 0.50
kmmais200 = 0.45

if kmdiguser <= 200 :
    print('O valor da Viagem é de R$: {:.2f}'.format(kmdiguser * km200 ))
else:
    print('O valor da Viagem a ser pago com desconto por .KM. devido a longa distancia é de R$ {:.2f}'.format(kmmais200 * kmdiguser))






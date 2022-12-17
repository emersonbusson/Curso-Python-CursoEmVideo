
'''FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISEXTO'''


import datetime
import time

print('___'*20)
anobisexto = int(input('Digite o Ano Desejado ou ZERO(0) para Analisar o Ano Atual: '.title()))
print('___' *20)
print('PROCESSANDO E CALCULANDO INFORMAÇÕES PARA OBTENÇÃO DO RESULTADO...')
time.sleep(2)
print('___' *20)


if anobisexto == 0:
    anobisexto = datetime.date.today().year
if  anobisexto %4 == 0 and anobisexto %100 != 0 or anobisexto % 400 == 0:
    print('O ANO DE {:.0f} É BISEXTO.'.format(anobisexto))
else:
    print('O ANO DE {:.0f} NÃO É BISEXTO.'.format(anobisexto))



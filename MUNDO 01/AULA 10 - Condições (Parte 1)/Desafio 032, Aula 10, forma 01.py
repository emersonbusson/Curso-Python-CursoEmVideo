# Desafio 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime
import time

ano_bisexto = int(input('Digite o ano desejado ou Zero(0) para analisar o ano atual: '))

if ano_bisexto == 0:
    ano_bisexto = datetime.date.today().year
if  ano_bisexto %4 == 0 and ano_bisexto %100 != 0 or ano_bisexto % 400 == 0:
    print('O ANO DE {:.0f} É BISEXTO.'.format(ano_bisexto))
else:
    print('O ANO DE {:.0f} NÃO É BISEXTO.'.format(ano_bisexto))
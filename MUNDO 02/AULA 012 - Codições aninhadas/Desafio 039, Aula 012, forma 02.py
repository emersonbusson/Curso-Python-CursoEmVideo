'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar no serviço militar.
- se é a hora de se alistar.
- se já passou do tempo de alistamento.
Seu programa também, deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime

dias_atuais = datetime.date.today().year
ano_nascimento_user = int(input('Digite o ano de seu nascimento: '.title()))
calculo = (dias_atuais - ano_nascimento_user)

if calculo == 18:
    print('você tem que fazer o alistamento militar imediatamente!!'.upper())

elif calculo < 18:
    print('Você não tem 18 anos, ainda faltam: {} anos para o seu alistamento Militar.'.format(18 - calculo).title())

elif calculo > 18:
    print('Você já deveria ter se alistado a {} anos. '.format(calculo - 18).title())

print('Quem nasceu em: {}, você tem {} anos em {}.'.format(ano_nascimento_user, calculo, dias_atuais).title())


# Desafio 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e, de acordo com sua idade, exiba a sua categoria: até 9 anos a categoria é "MIRIM", até 14 anos a categoria é "INFANTIL", até 19 anos a categoria é "JÚNIOR", até 25 anos a categoria é "SÊNIOR" e acima de 25 anos a categoria é "MASTER".

import datetime

ano_atual = (datetime.date.today().year)

data_nacimento = int(input('Qual o ano de nascimento do atleta [00/00/0000]: '))
idade_atleta = (ano_atual - data_nacimento)

print(f'O atleta que nasceu em {data_nacimento} tem {idade_atleta} anos no ano de {ano_atual}.')

if idade_atleta <= 9:
    print('Clasificação: MIRIM ')

elif idade_atleta <= 14:
    print('Clasificação: INFANTIL')

elif idade_atleta <= 19:
    print('Classificação: JUNIOR')

elif idade_atleta <= 25:
    print('Classificação: SÊNIOR')

else:
    print('Classificação: MASTER')

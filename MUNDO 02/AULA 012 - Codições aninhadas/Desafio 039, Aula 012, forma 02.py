# Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# utilizando o módulo datetime.

import datetime

ano_atual = datetime.date.today().year
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade_user = (ano_atual - ano_nascimento)

if idade_user == 18:
    print('Você tem que fazer o alistamento militar imediatamente!')

elif idade_user < 18:
    print('Você não tem 18 anos e ainda faltam {} anos para o seu alistamento militar.'.format(18 - idade_user))
    
elif idade_user > 18:
    print('Você já deveria ter se alistado no serviço militar a {} anos. '.format(idade_user - 18))

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade_user, ano_atual))

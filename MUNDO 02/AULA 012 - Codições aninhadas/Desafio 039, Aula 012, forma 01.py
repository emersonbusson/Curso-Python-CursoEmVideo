# Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_nascimento = int(input('Digite seu ano de nascimento: '))

idade_atual = (2017 - ano_nascimento)

if idade_atual < 18:
    print('Quem nasceu em: {}, tem {} anos em 2017.'.format(ano_nascimento, idade_atual))
    print('Ainda faltam {} ano(s) para o alistamento militar.'.format(18 - idade_atual))
    print('Seu alistamento militar será em: {}'.format((18 - idade_atual) + 2017))
    
elif idade_atual > 18:
    print('Quem nasceu em {} tem {} anos em 2017.'.format(ano_nascimento, idade_atual))
    print('Você já deveria ter se alistado no serviço militar há {} ano(s).'.format(idade_atual - 18))
    print('Seu alistamento foi em: {}.'.format((18 - idade_atual) + 2017))

else:
    print('Quem nasceu em {}, tem {} anos em 2017.'.format(ano_nascimento, idade_atual))
    print('você tem que ir se alistar imediatamente.')

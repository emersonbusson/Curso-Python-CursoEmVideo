'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar no serviço militar.
- se é a hora de se alistar.
- se já passou do tempo de alistamento.
Seu programa também, deverá mostrar o tempo que falta ou que passou do prazo.
'''


ano_nascimento = int(input('Digite seu ano de nascimento:'.title()))

idade_atual = (2017 - ano_nascimento)

if idade_atual < 18:
    print('Quem nasceu em {}, tem {} anos em 2017.'.title().format(ano_nascimento, idade_atual))
    print('Ainda fatam {} ano(s) para o alistamento.'.title().format(18 - idade_atual))
    print('Seu alistamento será em {}'.title().format((18 - idade_atual) + 2017))
elif idade_atual > 18:
    print('quem nasceu em {}, tem {} anos em 2017.'.title().format(ano_nascimento, idade_atual))
    print('você já deveria ter se alistado há {} ano(s).'.title().format(idade_atual - 18))
    print('seu alistamento foi em {}.'.title().format((18 - idade_atual) + 2017))

else:
    print('quem nasceu em {}, tem {} anos em 2017.'.title().format(ano_nascimento, idade_atual))
    print('você tem que ir se alistar imediatamente.'.upper())

''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto: NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. '''


print('-' *30)
def voto(ano=0):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        print(f'Com {idade} anos: \33[31mNÃO VOTA.\33[31m')
    elif 16 <= idade < 18:
        print(f'Com {idade} anos: \33[33mVOTO OPCIONAL.')
    elif  18 <= idade <= 65:
        print(f'Com {idade} anos: \33[35mVOTO OBRIGATORIO\33[m')
    else:
        print(f'Com {idade} anos: \33[33mVOTO OPCIONAL.')

anonasc = int(input('Em que ano você nasceu?: '))
voto(anonasc)
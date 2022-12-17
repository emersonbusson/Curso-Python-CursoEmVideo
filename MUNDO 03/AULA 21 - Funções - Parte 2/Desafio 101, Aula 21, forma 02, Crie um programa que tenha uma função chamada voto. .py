''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto: NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. '''
#Forma Gunabara.

from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


#programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

''' A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.'''

#até 09 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 20 anos: sênior
#-acima: master

import datetime


ano_nascimento = int(input('Digite o ano de nascimento do atleta:'.title()))

print('=-' * 20)

ano_atual = datetime.datetime.today().year

resultado_atual_nascimento = (ano_atual - ano_nascimento)

anos_9 = 'atleta mirim'
anos_14 = 'atleta infantil'
anos_19 = 'atleta junior'
anos_20ate = 'atleta senior'
acima_20 = 'atleta master'


if resultado_atual_nascimento <= 9:
    print(f'O atleta tem: {resultado_atual_nascimento} anos, ele está na categoria: {anos_9}, na confederação.'.title())

elif 9 < resultado_atual_nascimento <= 14:
    print(f'O atleta tem: {resultado_atual_nascimento} anos, ele está na categoria: {anos_14}, na confederação.'.title())

elif 14 < resultado_atual_nascimento <= 19:
    print(f'O atleta tem: {resultado_atual_nascimento} anos, ele está na categoria: {anos_19}, na confederação.'.title())

elif 19 < resultado_atual_nascimento <= 20:
    print(f'O atleta tem: {resultado_atual_nascimento} anos, ele está na categoria: {anos_20ate}, na confederação.'.title())

elif resultado_atual_nascimento > 20:
    print(f'O atleta tem: {resultado_atual_nascimento} anos, ele está na categoria: {acima_20}, na confederação.'.title())

print('-=' *20)



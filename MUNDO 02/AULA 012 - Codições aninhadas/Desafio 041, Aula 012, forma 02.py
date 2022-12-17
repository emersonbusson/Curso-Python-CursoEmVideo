''' A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.'''

#até 09 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 25 anos: sênior
#-acima: master

import datetime
ano_atual = (datetime.date.today().year)
nascimento_atleta = int(input('Qual o ano de nascimento do atleta?'.title()))
resultado_idade_atleta = (ano_atual - nascimento_atleta)

print('-=' *20)
print(f'O atleta tem {resultado_idade_atleta} anos.'.title())
print('-=' *20)

if resultado_idade_atleta <= 9:
    print('Clasificação: mirim '.upper())

elif resultado_idade_atleta <= 14:
    print('Clasificação: infantil'.upper())

elif resultado_idade_atleta <= 19:
    print('Classificação: junior'.upper())

elif resultado_idade_atleta <= 25:
    print('Classificação: sênior'.upper())

else:
    print('Classificação: master'.upper())

print('=-' *20)


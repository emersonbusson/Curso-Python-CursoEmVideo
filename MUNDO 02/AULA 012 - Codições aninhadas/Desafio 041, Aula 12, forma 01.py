# Desafio 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e, de acordo com sua idade, exiba a sua categoria: até 9 anos a categoria é "MIRIM", até 14 anos a categoria é "INFANTIL", até 19 anos a categoria é "JÚNIOR", até 25 anos a categoria é "SÊNIOR" e acima de 25 anos a categoria é "MASTER".
import datetime

ano_nascimento = int(input('Digite o ano de nascimento do atleta:'))

print('=-' * 20)

ano_atual = datetime.datetime.today().year

idade_atleta = (ano_atual - ano_nascimento)

idade_max9 = 'atleta mirim'
idade_max14 = 'atleta infantil'
idade_max19 = 'atleta junior'
idade_max25 = 'atleta senior'
maior_25 = 'atleta master'

if idade_atleta <= 9:
    print(f'O atleta tem: {idade_atleta} anos, ele está na categoria: {idade_max9}, na confederação.')

elif 9 < idade_atleta <= 14:
    print(f'O atleta tem: {idade_atleta} anos, ele está na categoria: {idade_max14}, na confederação.')

elif 14 < idade_atleta <= 19:
    print(f'O atleta tem: {idade_atleta} anos, ele está na categoria: {idade_max19}, na confederação.')

elif 19 < idade_atleta <= 20:
    print(f'O atleta tem: {idade_atleta} anos, ele está na categoria: {idade_max25}, na confederação.')

elif idade_atleta > 20:
    print(f'O atleta tem: {idade_atleta} anos, ele está na categoria: {maior_25}, na confederação.')

print('-=' *20)
''' Crie um programa que leia o ano de nascimento de 7 pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores '''

from datetime import date



soma_nao_atingiram = int(0)
soma_atingiram = int(0)

for c in range(1,8):
    pessoa = (c)
    ano_nascimento = int(input('Digite o ano de nascimento da {}º pessoa: '.format(pessoa).strip()))
    calculo = (date.today().year - ano_nascimento)
    if calculo < 21:
        soma_nao_atingiram += 1

    elif calculo > 21:
        soma_atingiram += 1



print('\33[32mA quantidade de pessoas que não atingiram a maioridade: {}\33[m'.format(soma_nao_atingiram))
print('\33[31mA quantidade de pessoas que atingiram a maioridade: {}\33[m'.format(soma_atingiram))
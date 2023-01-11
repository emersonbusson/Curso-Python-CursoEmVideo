# Desafio 054 - Crie um programa que leia o ano de nascimento de 7 pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores '''


from datetime import date

adultos = 0
menores = 0

for cont in range(1,8):
    
    ano_nascimento = int(input(f'Digite o ano de nascimento da {cont}º pessoa: '))
    calculo = (date.today().year - ano_nascimento)
    
    if calculo < 21: #Maioridade aqui é considerada para maiores de 21 anos.
        adultos += 1

    else:
        menores += 1

print(f'Ainda não atingiram a maioridade: {adultos} pessoas')
print(f'Já são maiores de idade: {menores} pessoas')
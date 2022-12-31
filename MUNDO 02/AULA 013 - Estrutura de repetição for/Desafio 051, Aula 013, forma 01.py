''' Desemvolva um programa que leia o primeiro termo e a razão de uma pa, no final, mostre os 10 primeiros termos dessa progressão.  '''


print('\33[31m===\033[m' * 30)
print('\33[35m10 TERMOS DE UMA P.A (PROGRESSSÃO ARITMÉDICA)\33[m')
print('\33[31m===\033[m' * 30)

primeiro_termo = int(input('\33[32mDigite o primeiro termo: \33[m'))
print('=-' *20)
razão = int(input('\33[35mDigite a razão: \33[m'))
print('-=' *20)
décimo = primeiro_termo +(10 -1) * razão  #fomula progressão?
for c in range(primeiro_termo, décimo + razão, razão):
    print(f'{c}', end= ' > ')
print('ACABOU')
# Desafio 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print(f'{" 10 TERMOS DE UMA P.A (PROGRESSSÃO ARITMÉDICA ":=^50}')
print()

primeiro_termo = int(input('Digite o primeiro termo: '))

razão = int(input('Digite a razão: '))

décimo = primeiro_termo +(10 -1) * razão  #fomula progressão?
for c in range(primeiro_termo, décimo + razão, razão):
    print(f'{c}', end= ' > ')
print('ACABOU')
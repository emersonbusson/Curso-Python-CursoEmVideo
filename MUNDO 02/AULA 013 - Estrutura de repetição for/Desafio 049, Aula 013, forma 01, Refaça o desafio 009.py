'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

print('\33[32m-=\33[m' * 30)
print('...\33[31mBATUBADA DE MULTIPLICAÇÃO\33[m...')
print('\33[32m-=\33[m' * 30)
num_escolhido_user = int(input('Digite um número para ver sua: '.title()))

for c in range(0, 11):
    print(f'{num_escolhido_user} X {c} = {num_escolhido_user * c}')


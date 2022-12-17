''' Refaça o desafio 051, lendo o primeiro terma e a razão de uma PA,
mostrando os 10 primeiro termos da progressão usando a estrutura while.'''

#Forma Guanabara

print('\33[31m===\033[m' * 30)
print('\33[35m10 TERMOS DE UMA P.A (PROGRESSSÃO ARITMÉDICA)\33[m')
print('\33[31m===\033[m' * 30)

p_t = int(input('\33[32mDigite o primeiro termo: \33[m'))
print('=-' *20)
termo = p_t
rz = int(input('\33[35mDigite a razão: \33[m'))
print('-=' *20)
c = 1

while c <= 10:
    print(f'{termo}', end= ' > ')
    termo += rz
    c += 1
print('ACABOU')
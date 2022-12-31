'''Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
o programa encerra quando ele disser que quer mostrar 0 termos..'''

''' Refaça o desafio 051, lendo o primeiro terma e a razão de uma PA,
mostrando os 10 primeiro termos da progressão usando a estrutura while.'''

print('\33[31m===\033[m' * 30)
print('\33[35m10 TERMOS DE UMA P.A (PROGRESSSÃO ARITMÉDICA)\33[m')
print('\33[31m===\033[m' * 30)

p_t = int(input('\33[32mDigite o primeiro termo: \33[m'))
print('=-' *20)
rz = int(input('\33[35mDigite a razão: \33[m'))
print('-=' *20)
dcm = p_t +(10 -1) * rz  #fomula progressão?
c = 10
termos_mostrados = 0
#while c <=10:
#for c in range(p_t, dcm + rz, rz):
while c != 0:
    print(f'{p_t}', end= ' > ')
    p_t += rz
    #print(dcm)
    c -= 1
    termos_mostrados += 1
    if c == 0:
        print('ACABOU')
        outros_termos = int(input('Você acabou de ver os 10 primeiros termos, deseja ver mais quantos termos?  '))
        c = outros_termos
        if c == 0:
            print('PROGRAMA FINALIZADO!')
print('Quantidade de termos mostrados: {}'.format(termos_mostrados))
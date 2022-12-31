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
#while c <=10:
#for c in range(p_t, dcm + rz, rz):
while c != 0:
    print(f'{p_t}', end= ' > ')
    p_t += rz
    #print(dcm)
    c -= 1
print('ACABOU')
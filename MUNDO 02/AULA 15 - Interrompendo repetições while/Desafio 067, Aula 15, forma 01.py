'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuario.
O programa será interrompido quando o número solicitado for negativo.'''

print('-' *30,'\33[35mTABUADA\33[m','-'*30)
print('-' *20,'\33[35mDIGITE QUALQUER NÚMERO NEGATIVO PARA PARAR [-1]. \33[m','-'*20)
x = 0

while True:
    print('*' * 40)
    numero = int(input('\33[33mDigite um número para ver sua tabuada: \33[m'))
    print('*' * 40)
    x = 0
    if numero < 0:
        break
    while x < 10: # poderia também ser utilizado a estrutura 'for'. [ for c in range(1,11): ]
        x += 1
        print(f'\33[31m {numero} X {x} = { x * numero}\33[m')
print('\33[32m-' *15, 'SOLICITAÇÃO DE ENCERRAMENTO ATENDIDA, PROGRAMA ENCERRADO...', '-' *15)

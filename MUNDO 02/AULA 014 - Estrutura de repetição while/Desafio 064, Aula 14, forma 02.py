''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. no final mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando a flag).'''
#forma Guanabara.


print('--'* 32)
print('leitor de números inteiros, mostra a soma e quantos foram lidos.'.upper())
print('Digite: 999, para Acionar a parada.'.upper())
print('--'* 32)
c = soma = n = 0
n = int(input('Digite um número [999 para parar]: '.format(c)))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '.format(c)))
    if n == (999):
        print('\33[35mDIGITADO: 999, PARADA ACIONADA!\33[m')
print('\33[31mForam digitados o total de: \33[33m{} \33[31m números e a soma entre esses números é: \33[33m{} \33[m'.format(c, soma))
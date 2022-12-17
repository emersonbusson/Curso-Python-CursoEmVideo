''' Crie um programa que leia vários números inteiros pelo teclado.
o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

soma = quant = 0
cont = 1

print('Digite: [999] para o programa parar.')
while True:
    num = int(input('Digite o {}° número: '.format(cont)))
    cont += 1
    # soma += num               # o código dentro do while e antes do break, o valor será do flag será incluido na soma.
    # quant += 1
    if num == 999: # laço de soma só será executado quando o comando 'Break foi ativado digitando 999'
        break
    soma += num
    quant += 1
print('---Número de parada solicitado ---'.upper())
print('A quantidade de números digitados é: {}. \nA soma de todos os números digitados é: {}.'.format(quant, soma))
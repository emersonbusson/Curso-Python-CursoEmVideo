'''Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo. '''

import random
cont1 = total1 = 0
cont2 = total2 = 0

print('\33[01m-' *10,'Jogo do PAR OU IMPAR', '-' *10)
while True:
    numero = int(input('Escolha seu número: '))
    escolha_jogador = str(input('\33[35mPar ou Impar? [P/I]: \33[m')).upper().strip()[0]
    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('\33[31mEscolha incorreta, digite a opção correta, Par ou Impar? [P/I]: \33[m')).upper()[0]
    print('\33[34mEscolha: \33[31m{}\33[34m, registrada com sucesso...\33[m'.format(escolha_jogador))
    print('--' * 30)
    escolhas = 'PI'
    if escolha_jogador == 'P':
        escolha_computador = 'I'
        print('Visto que você escolheu: \33[31mPar\33[m, O Computador Escolheu: \33[33mImpar\33[m. ')
    else:
        escolha_computador = 'P'
        print('Visto que você escolheu: \33[31mIMPAR\33[m, O Computador Escolheu: \33[33mPar\33[m. ')
    print('--' * 30)
    computador = random.randint(1, 10)
    soma = numero + computador
    if soma % 2 == 0:
        print('\33[31mO número: \33[36m[{}]\33[31m é igual a \33[36m[Par].\33[m'.format(soma))
        resu = 'P'
        if escolha_jogador == 'P':
            print('--' * 30)
            print('\33[7mO jogador Ganhou!\33[m')
            cont1 += 1
            print('Vamos jogar novamente...')
            print('--' * 30)
        else:
            print('\33[35mO Computador Ganhouu\33[m')
            t = '\33[31mPAR\33[m'
            cont2 += 1
            break
    else:
        print('\33[31mO número: \33[36m[{}]\33[31m é igual a \33[36m[Impar].\33[m'.format(soma))
        resu = 'I'
        if escolha_jogador == 'I':
            print('--' * 30)
            print('\33[7mJogador Ganhou\33[m')
            print('--' * 30)
            t = '\33[33mIMPAR\33[m'
            cont1 += 1
            print('Vamos Jogar Novamente...')
            print('--' * 30)
        else:
            print('--' * 30)
            print('\33[35mO Computador Ganhouu.\33[m')
            t = '\33[33mIMPAR\33[m'
            cont2 += 1
            break
print('\33[33m-' *15, 'GAMER OVER MEU PARCEIROO !', '\33[m-' *15)
print('Você Jogou: {}.  \nO Computador Jogou: {}.\nTotal Deu: {}. \nResultado: {}.'.format(numero, computador,soma,t))
print('Jogador Venceu: {} Vezes / Computador Venceu {} Vezes.'.format(cont1, cont2))

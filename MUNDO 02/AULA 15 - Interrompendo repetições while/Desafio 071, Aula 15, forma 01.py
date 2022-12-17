''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''
print('='*15)
print('BRANCO CEV')
print('=' *15)
valor = int(input('Que valor você quer sacar?: '))
cedulas = 0
nota_atual = 50
pagar = valor
while True:
    if nota_atual <= pagar:
        pagar -= nota_atual
        cedulas += 1
    else:
        print(f' {cedulas} cédulas(s) de R$: {nota_atual}')
        if pagar == 0:
            break
        if nota_atual == 50:
            nota_atual = 20
        elif nota_atual == 20:
            nota_atual = 10
        elif nota_atual == 10:
            nota_atual = 1
        # elif nota_atual == 5:
        #     nota_atual = 1
        cedulas = 0
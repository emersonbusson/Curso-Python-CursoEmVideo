'''Desafio 099, Aula 20, forma 03, Faça um programa que tenha um função chamada maior, que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
 '''

def valores(* nums):
    from time import sleep
    print('-=' * 30)
    print('Analisando valores passados...')
    sleep(1)
    for n in nums:
        print(f'{n}',end=' ')
        sleep(0.5)
    print(f'Foram informados {len(nums)} valores ao todo.')
    sleep(0.3)
    print(f'O maior valor informado foi {max(nums)}.')
    sleep(2.5)

#programa principal
valores(2,9,4,5,7,1)
valores(4,7,0)
valores(1,2)
valores()
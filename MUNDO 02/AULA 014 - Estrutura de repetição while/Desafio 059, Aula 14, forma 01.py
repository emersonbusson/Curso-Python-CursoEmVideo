import time


primeiro_valor = float(input('Digite o primeiro valor: '))
segundo_valor = float(input('Digite o segundo valor: '))

valido = False

while not valido:
    menu = int(input(''' 
    Digite (1) para SOMAR.
    Digite (2) para MULTIPLICAR.
    Digite (3) para Saber o MAIOR.
    Digite (4) para novos NUMEROS.
    Digite (5) para SAIR DO PROGRAMA.  
    Qual sua opção?:  '''))

    print( 20 * '-=')

    if menu == 1:
        print('A soma entre {} + {} é {}. '.format(primeiro_valor, segundo_valor, (primeiro_valor + segundo_valor)))

    elif menu == 2:
        print('O resultado de {} x {} é {}'.format(primeiro_valor, segundo_valor, (primeiro_valor * segundo_valor)))

    elif menu == 3:
        print('Entre os valores {} e {} o maior é {}'.format(primeiro_valor, segundo_valor, max(primeiro_valor,segundo_valor)))

    elif menu == 4:
        print('Você solicitou novos valores!')
        primeiro_valor = float(input('Digite o primeiro novo valor: '))
        segundo_valor = float(input('Digite o segundo novo valor: '))

    elif menu == 5:
        valido = True
        time.sleep(1)
        print('Finalizando...')
        time.sleep(1)
        print('Fim do programa! Volte Sempre!')

    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE...')

    print( 20 * '-=')
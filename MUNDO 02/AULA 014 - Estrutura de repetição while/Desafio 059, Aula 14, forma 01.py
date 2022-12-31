import time
primeiro_valor = float(input('Digite o primeiro valor: '))
segundo_valor = float(input('Digite o segundo valor: '))
blool = False
while not blool:
    menu = int(input(''' 
    Digite (1) para SOMAR.
    Digite (2) para MULTIPLICAR.
    Digite (3) para Saber o MAIOR.
    Digite (4) para novos NUMEROS.
    Digite (5) para SAIR DO PROGRAMA.  
    Qual sua opção?:  '''))

    if menu == 1:
        print( 20 * '-=')
        print('\33[31mA soma entre {} + {} é {}. \33[m'.format(primeiro_valor, segundo_valor, (primeiro_valor + segundo_valor)))
        print(20 * '-=')
    elif menu == 2:
        print(20 * '-=')
        print('\33[32mO resultado de {} x {} é {}\33[m'.format(primeiro_valor, segundo_valor, (primeiro_valor * segundo_valor)))
        print(20 * '-=')
    elif menu == 3:
        print(20 * '-=')
        print('\33[35mEntre os valores {} e {} o maior é {}\33[m'.format(primeiro_valor, segundo_valor, max(primeiro_valor,segundo_valor)))
        print(20 * '-=')
    elif menu == 4:
        print(20 * '-=')
        print('\33[33mVocê solicitou novos valores!\33[m')
        primeiro_valor = float(input('\33[31mDigite o primeiro novo valor: \33[m'))
        print(20 * '-=')
        segundo_valor = float(input('\33[34mDigite o segundo novo valor: \33[m'))
        print(20 * '-=')
    elif menu == 5:
        blool = True
        time.sleep(1)
        print(20 * '-=')
        time.sleep(1)
        print('\33[7mFinalizando...\33[m')
        time.sleep(1)
        print('\33[7m Fim do programa! Volte Sempre! \33[m')
        time.sleep(1)
        print(20 * '-=')
    else:
        print(20 * '-=')
        print('\33[7mOPÇÃO INVÁLIDA, TENTE NOVAMENTE...\33[m')
        print(20 * '-=')
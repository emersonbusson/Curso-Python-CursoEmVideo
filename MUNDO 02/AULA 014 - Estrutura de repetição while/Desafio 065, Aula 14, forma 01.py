''' Crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre execução,
mostre a média entre todos os válores e qual foi o maior e o menor valores lidos. o programa
 deve perguntar ao usuário se ele quer ou não continuar a digitar os valores '''
print('-='* 30)
print('''\33[34m---- ANALISADOR ----
    - IRÁ CALCULAR A MÉDIA DE TODOS OS VALORES DIGITADOS;
    - VAI MOSTRAR QUAL O MENOR E MAIOR VALOR.\33[m''')
print('-='* 30)
cont1 = 1 #para mostrar "Digite o 1º, 2°, 3º e assim sucessivamente.
cont2 = 0
soma = 0
flag = True
maior = int()
menor = int()
list = []
while flag:
    n = int(input('\33[7mDigite o {}º valor \33[m: '.format(cont1)))
    print('-=' * 30)
    cont2 += 1
    soma += n
    cont1 += 1
    list = list + [n]
    if cont2 == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input('\33[36mDigite [Y] para continuar e [N] para finalizar:  \33[m')).upper().strip()[0]  # [0] vai pegar somente a primeira letra.
    while continua not in 'YN':
        continua = str(input('Opção incorreta, digite a opção correta [Y/N]: ')).upper().strip()[0]
    print('\33[35mOPÇÃO: {}, registrado com sucesso...\33[m'.format(continua))
    if continua in 'Y':
        print('\33[31mContinuando....\33[m')
        print('-=' * 30)
    else:
        flag = False
        print('\33[33mFinalizando...\33[m')
        print('-=' * 30)
media = soma / cont2
print('\33[31mA soma é: {}.. \n\33[32mA média é: {}.\33[m'.format(soma, media))
print('O maior número digitado é: {}'.format(max(list))) # maior com lista.
print('O menor número digitado é: {}'.format(min(list))) # menor com lista.
#______________________________________________________________________________
print('[\33[31mUTILIZANDO IF\33[m]O maior número digitado é: {}'.format(maior)) # maior com if
print('[\33[31mUTILIZANDO IF\33[m]O menor número digitado é: {}'.format(menor)) # menor sem if



''' Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos dos os valores únicos digitados em ordem crescente. '''
numeros = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num not in numeros:
        print('Valor adicionado com sucesso!')
        numeros.append(num)
    else:
        print(f'O Elemento {num} já Existe na Lista, Não será adicionado!')
    r = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
    numeros.sort()
print(f'Os valores Cadastrados São: {sorted(numeros)}.')

 
''' Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos dos os valores únicos digitados em ordem crescente. '''
lista = []

while True:
    num = (int(input('Digite um valor: ')))
    if num in lista:
        print(f'O Elemento {num} já Existe na Lista, Não será adicionado!')
    else:
        print('Valor adicionado com sucesso!')
        lista.append(num)
    S_N = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    while S_N not in 'SN':
        S_N = str(input('Valor inválido, digite um valor válido > [S/N]: ')).upper().strip()[0]
    if S_N == 'N':
        break
print(f'Os valores Cadastrados São: {sorted(lista)}.')


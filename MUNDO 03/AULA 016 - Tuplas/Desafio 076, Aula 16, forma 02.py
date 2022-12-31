'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular.
'''
#Utilizando For.
listagem = ('Lápis', 1.75, 'Borracha', 2.0,
            'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila',120.32, 'Canetas', 22.30,
            'Livro', 34.90)
x = 0
y = 1
print('---'*16)
print('{:^43}'.format('LISTAGEM DE PREÇOS'))
print('---'*16)
while x in range(0,18):
    print(f'{listagem[x]:.<39}R${listagem[y]:6.2f}')
    x += 2
    y += 2
print('---'*16)
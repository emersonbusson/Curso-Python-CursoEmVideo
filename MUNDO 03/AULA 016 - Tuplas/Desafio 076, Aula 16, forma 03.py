'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular.
'''
#Forma sem repetições.
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
print(f'{listagem[0]:.<39}R${listagem[1]:6.2f}')
print(f'{listagem[2]:.<39}R${listagem[3]:6.2f}')
print(f'{listagem[4]:.<39}R${listagem[5]:6.2f}')
print(f'{listagem[6]:.<39}R${listagem[7]:6.2f}')
print(f'{listagem[8]:.<39}R${listagem[9]:6.2f}')
print(f'{listagem[10]:.<39}R${listagem[11]:6.2f}')
print(f'{listagem[12]:.<39}R${listagem[13]:6.2f}')
print(f'{listagem[14]:.<39}R${listagem[15]:6.2f}')
print(f'{listagem[16]:.<39}R${listagem[17]:6.2f}')
print('---'*16)
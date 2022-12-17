'''Crie um programa que leia o nome completo de uma pessoa e mostre:'''

'''O nome com todas as letras maiúsculas'''
'''O nome com todas as letras minúsculas'''
'''Quantas letras ao todo (Sem considerar espaços'''
'''Quantas letras tem o primeiro nome'''

nome = str(input("Digite o nome completo da pessoa:")).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem o total de: {} de letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem: {}, letras!'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é: {} , e ele tem {}, letras!'.format(separa[0], len(separa[0])))







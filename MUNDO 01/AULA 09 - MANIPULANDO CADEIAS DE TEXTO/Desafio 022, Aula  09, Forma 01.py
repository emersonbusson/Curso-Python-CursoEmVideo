#Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras ao todo (Sem considerar espaços), quantas letras tem o primeiro nome.

nome = str(input("Digite o nome completo da pessoa: ")).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem o total de: {} de letras.'.format(len(nome) - nome.count(' ')))

# print('Seu primeiro nome tem: {}, letras!'.format(nome.find(' '))) o trecho de string " " (espaço em branco) foi encontrado na posição 7 da string nome.

nome_separado_lista = nome.split() # o método split separou o nome pelos espaços (em branco) e colocou cada pedaço em uma lista.
print('Seu primeiro nome é: {} , e ele tem {}, letras!'.format(nome_separado_lista[0], len(nome_separado_lista[0])))
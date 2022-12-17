'''Desafio 107, Aula 22, forma 01, Crie um módulo chamado moeda.py que
tenha as funções incorporadas:
aumentar(), diminuir(),dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

#desafio 108
'''Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.'''



import moeda

preço = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço,porcento=10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.dininuir(preço,porcento=13))}')
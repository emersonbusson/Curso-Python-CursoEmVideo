'''Desafio 107, Aula 22, forma 01, Crie um módulo chamado moeda.py que
tenha as funções incorporadas:
aumentar(), diminuir(),dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''



import moeda

preço = float(input('Digite o preço R$: '))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço,porcento=10)}')
print(f'Reduzindo 13%, temos {moeda.dininuir(preço,porcento=13)}')
'''Desafio 107, Aula 22, forma 01, Crie um módulo chamado moeda.py que
tenha as funções incorporadas:
aumentar(), diminuir(),dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

#Desafio 108
'''Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.'''

#Desafio 109, forma 01
'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no Desafio 108. '''

import moeda
print()
preço = float(input('Digite o preço R$: '))
print()
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço,moeda=True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço,moeda=True)}')
print(f'Aumentando 10%, temos \33[31m{moeda.aumentar(preço,porcento=10, moeda=False)}\33[m')
print(f'Reduzindo 13%, temos {moeda.dininuir(preço,porcento=13, moeda=True)}')
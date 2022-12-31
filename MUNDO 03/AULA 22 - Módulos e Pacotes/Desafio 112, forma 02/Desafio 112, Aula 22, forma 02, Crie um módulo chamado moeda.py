#Desafio 107
'''Crie um módulo chamado moeda.py que
tenha as funções incorporadas:
aumentar(), diminuir(),dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

#Desafio 108
'''Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.'''

#Desafio 109
'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no Desafio 108. '''

#Desafio 110
'''Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
informações geradas pelas funções que já temos no módulo criado até aqui'''

#Desafio 111
'''Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados: moeda e dado.
Transfira todas funções utilizadas nos desafios 107,108,109 para o primeiro pacote e matenha tudo funcionando.'''
#Desafio 112 #forma guanabara.
'''Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.'''


from utilidadescev import dado
from utilidadescev import moeda
print()
preço = dado.leiadinheiro('Digite o preço R$: ')
moeda.resumo(preço,80,35)
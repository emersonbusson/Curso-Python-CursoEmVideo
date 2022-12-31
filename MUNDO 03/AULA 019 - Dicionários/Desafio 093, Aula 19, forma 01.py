'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador de futebol e quantas partidas ele jogou. depois
vai ler a quantidade de gols feitos em cada partida. no final, tudo isso será guardado em um dicionario,
incluindo o total de gols feitos durante o campeonato. '''
soma = int()
todos = dict()
cont = 1
todos['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {todos["nome"]} jogou: '))
todos['gols'] = list()
for g in range(0, partidas):
    todos['gols'].append(int(input(f'quantos gols na partida {g+1}? ')))
for e in todos['gols']:
    soma += e
todos['total'] = soma
print('-=' * 30)
print(todos)
print('-=' * 30)
for k, v in todos.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'o jogador {todos["nome"]} jogou {partidas} partidas.')
for e in todos['gols']:
    print(f' => na partida {cont}, fez {e} gols.')
    cont += 1
print(f'Foi um total de {todos["total"]} gols.')
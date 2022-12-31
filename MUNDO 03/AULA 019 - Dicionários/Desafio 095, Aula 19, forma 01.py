''' Desafio 095, aprimore o desafio 093 para que ele fauncione com vários jogadores, incluindo um sistema de visualização
 de detalhes do aproveitamento de cada jogador '''
todos = dict()
todoslista = list()
cont = 1
while True:
    todos['nome'] = str(input('Nome do jogador: ')).upper()
    partidas = int(input(f'Quantas partidas {todos["nome"]} jogou: '))
    todos['gols'] = list()
    for g in range(0, partidas):
        todos['gols'].append(int(input(f'quantos gols na partida {g+1}? ')))
    todos['total'] = sum(todos['gols'])
    todoslista.append(todos.copy())
    while True:
        resp = str(input('Quer continuar?  [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('\33[31mResposta incorreta, tente novamente...\33[m')
    if resp == 'N':
        break
    else:
        print('--' * 20)
print('-=' * 50)
print(f'{"Cod":<4}  {"NOME":<10}{"Gols":<10}{"Total":>17}')
print('--' * 22)
for i, j in enumerate(todoslista):
    print(f'{i:<4}  {j["nome"]:<10}{j["gols"]!s:<15s}{j["total"]:>13}')

while True:
    print('-=' * 50)
    opção = int(input('Mostrar dados de qual jogador? (999 o programa é Finalizado): '))
    if opção == 999:
        print('\33[35mFinalizando...\33[m')
        break
    if opção <= len(todoslista) -1:
        print(f'-- LEVANTAMENTO DO JOGADOR {todoslista[opção]["nome"]}: ')
        for i, e in enumerate(todoslista[opção - 1]["gols"]):
            print(f' => Na partida {i+1}, fez {e} gols. ')
    else:
        print(f'\33[31mErro! Não existe jogador com o código: {opção}, Tente novamente...\33[m')
print('<<< VOLTE SEMPRE >>>')
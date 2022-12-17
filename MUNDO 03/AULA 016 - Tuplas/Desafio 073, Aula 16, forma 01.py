''' Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato braisileiro de futebol, na ordem de colocação.
Depois mostre:
A- Apenas os 5 primerios colocados.
B- Os últimos 4 colocados da tablela
C- uma lista com os times em ordem alfabética
D- Em que posição na tabela está o time da Chapecoense. '''





times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio',
         'Bahia', 'Sport', 'Chapecoense')
print(f'Lista de times do Brasileirão: {times} ')
print('=-' * 30)
print(f'Os 5 primeiros são: {times[0:5]}.')
print('=-' * 30)
print(f'Os 4 útimos são: {times[-4:]}')
print('=-' * 30)
print(f'Times em ordem alfabética: {sorted(times)} ')
print(f'O time Chapecoense está na pisição: {times.index("Chapecoense")+1}º.')

# for cont in range(0, len(times)):                            #utilizando o Range + LEN
#     print(f'O time {times[19:]} na posição: {cont}')
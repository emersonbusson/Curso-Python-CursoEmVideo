itens = list()
for num in range(0,5):
    itens.append(int(input('Digite um valor: ')))

for i, v in enumerate(itens):
    print(f'Na posição: {i}, do indice tem o valor: {v}')
print('Cheguei ao fim da lista. ')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end=' ') #Lista Mostrada de Outra maneira, utilizando a estutura for.

for c, v in enumerate(valores):
    print(f'\nIndice: {c}') #Valor do Indice foi para 'c'
    print(f'Valor: {v}') # Valor dentro do indice foi para 'v', por conta da função 'Enumerate'
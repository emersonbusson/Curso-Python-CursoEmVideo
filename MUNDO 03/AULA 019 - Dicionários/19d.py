#DICIONARIOS DENTRO DE LISTAS.

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print('-=' *30)
print(estado2)
print('-=' *30)
print(brasil)
print('-=' *30)
print(brasil[0])
print('-=' *30)
print(brasil[1])
print('-=' *30)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
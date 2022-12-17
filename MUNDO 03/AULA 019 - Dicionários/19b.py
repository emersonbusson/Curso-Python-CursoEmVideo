pessoas = {'nome':'Gustavo','sexo':'M','idade':22}
for k in pessoas.keys(): # para cada(key) em pessoas.keys
    print(k) #mostra nome, sexo, idade.

print('-='*30)

for v in pessoas.values(): # para cada(value) em pessoas.values
    print(v) # mostra, gustavo, M, 22.

print('-='*30)

for i in pessoas.items(): #para cada(items) em pessoas.items
    print(i) #Mostra >  ('nome', 'Gustavo')('sexo', 'M')('idade', 22)

print('-='*30)

for k, v in pessoas.items(): #seria como se fosse um enumerate, mas em dicionarios tem de ser usado o metodo items.
    print(f'{k} = {v}')
pessoas = {'nome':'Gustavo','sexo':'M','idade':22}
print(pessoas)
print('-=' *30)
print(pessoas['nome'])
print('-=' *30)
print(pessoas['idade'])
print('-=' *30)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #quando utilizar o f-string colocar aspás duplas.
print('-=' *30)
print(pessoas.keys())
print('-=' *30)
print(pessoas.values())
print('-=' *30)
print(pessoas.items())
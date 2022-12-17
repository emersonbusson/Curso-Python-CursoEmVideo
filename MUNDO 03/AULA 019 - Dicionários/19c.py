pessoas = {'nome':'Gustavo','sexo':'M','idade':22}
del pessoas['sexo'] #apaga a key e o value em pessoas.
print(pessoas)

print('-=' * 30)

pessoas['nome'] = 'Leandro' # o nome value gustavo na key nome, foi substituido por leandro.
print(pessoas)

print('-=' * 30)

pessoas['peso'] = 98.5 # adicionado outra key(peso) e value(98.5) no dicionario pessoas.
print(pessoas)
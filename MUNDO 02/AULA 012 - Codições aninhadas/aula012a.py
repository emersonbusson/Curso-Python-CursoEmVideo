nome = str(input('Qual é o seu nome?')).upper()

if nome == 'GUSTAVO':
    print('Que nome bonito você tem {}.'.format(nome))

elif nome == 'ADRIANA' and 'PEDRO' and 'GILSON':
    print('O nome {} é muito popular no BRASIL:'.format(nome))
elif nome in 'ANA CLAUDIA JESSICA JULINANA':
    print('Seu nome: {}, é FEMININO.'.format(nome))
else:
    print('Seu nome é bem normal {}.'.format(nome))
    
print('Tenha um bom dia')

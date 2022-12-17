def leiadinheiro(msg='<DIGITE A MENSAGEM AQUI>',dado=''):
    indices = list()
    dado = input(f'{msg}')
    if ',' or '.' in dado:
        for i,e in enumerate(dado):
           if e == ',' or e == '.':
               indices.append(i)
    dado = dado.replace('.','')
    dado = dado.replace(',','')

    while dado.isnumeric() == False:
        print(f'\33[31mERRO: "{dado}" é um preço invalido.\33[m')
        dado = input(f'{msg}')
        if ',' or '.' in dado:
            for i, e in enumerate(dado):
                if e == ',' or e == '.':
                    indices.append(i)
        dado = dado.replace('.', '')
        dado = dado.replace(',', '')

    dado = list(dado)
    for v in indices:
        dado.insert(v,'.')
    tuple(dado)
    for c in dado:
       dado = "".join(dado)
    r = float(dado)
    return r

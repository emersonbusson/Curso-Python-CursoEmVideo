def test():
    x = 8
    print(f'Na função teste, N vale: {n}')
    print(f'Na função teste, X vale {x}')

# PROGRAMA PRINCIPAL
n = 2                                           #mesmo o 'N' sendo definido embaixo e fora do 'def' ele vai funcionar em toda area fora do '#"
print(f'No programa principal, N vale: {n}')
test()

###################################################################################################################################################

''' print(f'No programa principal, X vale o valor de {X} ')  ''' # A variavel 'X' foi declarada(existe) somente dentro da função 'teste', ela irá funcionar somente dentro da 'def (test)'
                        # NameError: name 'X' is not defined        ''' 'X' tem o ESCOPO LOCAL. '''

                        # n = a variavel Global.
                        # x = variavel Local.
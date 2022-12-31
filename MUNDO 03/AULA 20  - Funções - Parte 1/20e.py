#empacotar Parâmetros: (*num), quando você quer permitir uma quantidade indefinida(varios) de argumentos, você usa o '*' para isso.
# vai gerar uma tupla que pode até ser percorrida pela estrutura for.
def contador(*num):
    for valor in num:
        print(f'{valor} ',end='')
    print(' - FIM')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
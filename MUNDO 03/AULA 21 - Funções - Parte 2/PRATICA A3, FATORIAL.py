def par(n=0): # verificar se ele é par ou não, utilizando valor lógico com o return dentro da função.
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num))

if par(num) == True:
    print(f'O {num} é PAR.')
else:
    print(f'O {num} é Impar. ')
# obs: para o python, todo arquivo ".py", pode ser um módulo.

# Em seguida esse código será desmenbrado, e as funções serão chamadas
# De outro arquivo ".py".
def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


#programa principal
num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}.')
print(f'O triplo de {num} é {triplo(num)}.')

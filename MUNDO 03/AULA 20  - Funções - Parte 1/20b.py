a = 4
b = 5
s = a + b
print(s)
print('-' * 30)

a = 8
b = 9
s = a + b
print(s)
print('-' * 30)

a = 2
b = 1
s = a + b
print(s)
print('-' *30)

print(f'{"- UTILIZANDO FUNÇÃO (DEF) -":^50}')
def soma(a, b):
    print('-' *30)
    s = a + b
    print(s)
# entre a def(função) e o programa principal, tem que ter duas linhas vazias.
#programa principal
soma(4,5)
soma(8,9)
soma(2,1)
#soma(4)  > se tentar executar assim dá erro, porque foi passado dois parâmetros e não somente 1.
soma(a=4, b=5) # esplicidamente dizer qual é qual a=4 e b=5 ou
soma(b=4, a=5) # b=4 e a=5.

def somar(a=0,b=0,c=0):
    s = a + b + c
    # print(f'A soma é: {s}')
    return s # com o comando 'return', quando chamado a função 'somar', outra variavel de fora, pode receber o valor de 's'

resp = somar(3,2,5) # visto em existe um 'return' na variavel 's', a variavel 'resp' vai receber 's'.
somar(2,2)
somar(6)

print(resp)

print(somar(3,2,2)) # utilizando o 'return' na variavel 's', posso usar o print para mostrar a variavel 's' de fora da função, sem um print interno dentro da propria função.

# exemplos de outras coisas que podem ser feitas visto que existe o return em 's'.

r1 = somar(10,20,30)
r2 = somar(5,5,5)
r3 = somar(1,2,3)

print(f'O resultados dos calculos deram: {r1} e {r2} e {r3}.')
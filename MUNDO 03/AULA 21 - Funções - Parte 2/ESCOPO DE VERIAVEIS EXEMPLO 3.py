def test(b):
    a = 8                                   # 'a = 8' Escopo Local
    b += 4
    c = 2
    print(f'A dentro vele {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5                                        # 'a = 5' Escopo Global

test(a) #parametro b recebeu a variavel 'a' de Escopo Global.  fazendo b receber 5 + 4 = 9.
print(f'A Fora vale {a}')
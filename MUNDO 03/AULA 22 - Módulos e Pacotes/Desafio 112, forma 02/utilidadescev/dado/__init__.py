#Desafio 112 #forma guanabara.
'''Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.'''

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha():                                   # if entrada.isalpha() or entrada.strip() == '':
            print(f'\33[31mERRO: \"{entrada}\" é um preço inválido!\33[m')
        else:
            valido = True
    return float(entrada)
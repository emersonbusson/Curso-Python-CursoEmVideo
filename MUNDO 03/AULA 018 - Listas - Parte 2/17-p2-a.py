teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste) #lista dentro de lista.
print(galera)
teste[0] = 'Maria'
teste[1] = 22
print(teste)
galera.append(teste) #repete duas vezes o nome maria, porque houve uma ligação entre as duas listas e não uma cópia.
print(galera) #repete duas vezes o nome maria, porque houve uma ligação entre as duas listas e não uma cópia.
print('-=' * 30)
del galera[0:2] #deletou do indice 0 ao 1.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
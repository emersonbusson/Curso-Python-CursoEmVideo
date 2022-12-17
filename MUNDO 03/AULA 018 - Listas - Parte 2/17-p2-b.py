galera = [['Joao', 19],['Ana',33],['Joaguim', 13],['Maria', 45]] #4 Estruturas compostas, dentro de uma estrutura principal.
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print('-='*30)
for p in galera:
    print(f'\33[31m{ p }\33[m')
for p in  galera:
    print(f'\33[32m{ p[0] }\33[m')
for p in  galera:
    print(f'\33[33m{ p[1] }\33[m')
for p in  galera:
    print(f'\33[34m { p[0] } tem { p[1] } anos de idade \33[m')
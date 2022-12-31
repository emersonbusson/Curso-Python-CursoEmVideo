galera = list() # lista
dado = list() # esturaura dados, que vai pegar temporiariamente os dados da lista
for p in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado) # sem os '[:]', as listas dado e galera foraM interligadas com esse append.
    dado.clear() #visto que as listas estão interligadas(são as mesmas, dado e galera), galera também foi limpada com esse comando.
print(galera)
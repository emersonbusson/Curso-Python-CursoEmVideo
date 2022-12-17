galera = list() # lista
dado = list() # esturaura dados, que vai pegar temporiariamente os dados da lista
for p in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # cópia de dados foi jogado dentro da lista galera.
print(galera)
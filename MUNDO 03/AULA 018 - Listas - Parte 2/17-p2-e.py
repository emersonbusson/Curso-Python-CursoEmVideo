galera = list() # lista
dado = list() # esturaura dados, que vai pegar temporiariamente os dados da lista
totalmai = totalmen = 0
for n in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # cópia de dados foi jogado dentro da lista galera.
    dado.clear() # Caso não tenha '.clear' a cada repetição do for, vai repetir quem for maior. variável composta temporaria.
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmai += 1
    else:
        print(f' {p[0]} é menor de idade. ')
        totalmen += 1
print(f' Temos {totalmai} maiores.\n Temos {totalmen} menores.')
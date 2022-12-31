'''Desafio 115, Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''


while True:
    print('-' * 50)
    print(F'{"MENU PRINCIPAL":^50}')
    print('-' * 50)
    print('\33[33m1 -\33[34m Ver pessoas cadastradas\n\33[33m2 -\33[34m Cadastrar nova pessoas\n\33[33m3 -\33[34m Sair do sistema\33[m')

    try:
        opção = int(input('\33[33mSua Opção: \33[m'))
    except KeyboardInterrupt:
        print('\n\33[35mIMTERROMPENDO PROGRAMA!\33[m')
        break
    except:
        print('\33[31mErro! Digite uma opção válida válida!\33[m')
    else:
        if opção == 1:
            print('-' * 50)
            print(f'{"PESSOAS CADASTRADAS":^40}')
            print('-' * 50)

            try:
                arquivo = open('dados.txt')
                arquivo.close()
            except FileNotFoundError:
                verifica = True
            else:
                verifica = False
            if verifica == True:
                with open('dados.txt', 'x') as arquivo:
                    arquivo.write()


            with open('dados.txt', 'r') as arquivo:
                print(arquivo.read())
        elif opção == 2:
            print('-' * 50)
            print(f'{"NOVO CADASTRO":^40}')
            print('-'* 50)
            while True:
                try:
                    nome = str(input('Nome: ')).upper()
                    idade = int(input('idade: '))
                except ValueError:
                    print('\33[31mERRO, por favor, digite um número inteiro válido.\33[m')
                else:
                    break

            pessoa = f'{nome:<25} {idade:>16} Anos\n'
            print(f'\33[35mRegistro de: \33[31m{nome}\33[35m efetuado com sucesso!\33[m')
            with open('dados.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(pessoa)
        elif opção == 3:
            break
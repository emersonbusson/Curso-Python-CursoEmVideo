nome1 = 'EMERSON BRUNO BUSSON'
nome2 = 'ADRIANA BRUNO MONTEIRO'
nome3 = str(input('\33[0:31:40mQUAL É O TERCEIRO NOME PARA O EXEMPLO: \33[m'))
nome4 = str(input('\33[0:34:40mQUAL É O OUTRO NOME A SER EXIBIDO: \33[m'))



cores = {'limpa':          '\33[m',
         'azul':           '\033[4:34m',
         'amarelo':        '\33[0:33m',
         'pretoebranco':   '\33[7m'
         }

print('Muito prazer em te conhecer:{}{}{} '.format('\33[4:35m' ,nome1, '\33[m'))

## OUTRO EXEMPLO DE CORES COM VARIAVEIS.

print('MUITO PRAZER EM TE CONHERCER 001: {}{}{}'.format(cores['pretoebranco'], nome2 , cores['limpa']))

print('MUITO PRAZER EM TE CONHECER 002: {}{}{}'.format(cores['amarelo'], nome4 , cores['limpa']))

print('MUITO PRAZER EM TE CONHECER 003: {}{}{}'.format(cores['azul'], nome3 , cores['limpa']))
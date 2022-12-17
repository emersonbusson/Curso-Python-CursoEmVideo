'''Desafio 114, Crie um código em python que teste se o site pudim está acessivel pelo computador usado. '''
#forma guanabara.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\33[31mO site Pudim não está acessível no momento.\33[m')
else:
    print('\33[33mO site pudim está acessivel.\33[m')
    print(site.read())
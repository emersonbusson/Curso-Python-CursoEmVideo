'''Desafio 114, Crie um código em python que teste se o site pudim está acessivel pelo computador usado. '''
import requests
try:
    resposta = requests.get(url='http://www.pudim.com.br')
except Exception as erro:
    print('\33[31mO site Pudim não está acessível no momento.\33[m')
else:
    print('\33[33mO site pudim está acessivel.\33[m')
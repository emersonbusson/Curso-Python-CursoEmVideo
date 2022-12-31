pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa) # vai dá o seguinte erro: NameError: name 'pessoa' is not defined.  MOTIVO: quando foi dado o comando: ('del' na 'váriavel' composta: tupla), não só apagou os dados de dentro da váriavél como também a prória variavél em si.

# a tupla é literalmente imútavél, somente pode ser apagado a tupla inteira ou seja a própria: a váriavél toda, e não somente um dado dentro da tupla ou váriavel.
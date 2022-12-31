#import math
from math import sqrt, floor

num = int(input('digite um número:'))
raiz = sqrt(num)
#print('A raiz de {} é igual a {}'.format(num,raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
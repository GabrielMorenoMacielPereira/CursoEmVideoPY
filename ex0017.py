import math
cateto_oposto=float(input('Qual o valor do cateto oposto?'))
cateto_adjacente=float(input('Qual o valor do cateto adjacente?'))
print(f'A hipotenusa desse triângulo retângulo tem valor {math.sqrt(cateto_adjacente**2+cateto_oposto**2):.2f}')
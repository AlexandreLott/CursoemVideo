import random

x1 = random.randint(1, 10)
x2 = random.randint(1, 10)
x3 = random.randint(1, 10)
lista = x1,x2,x3
print(lista)
print('Maior: {}'.format(max(lista)))
print('Menor: {}'.format(min(lista)))

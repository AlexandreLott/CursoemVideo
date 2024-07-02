from random import randint

numeros_aleatorios = (randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999))
print(numeros_aleatorios)
menor = maior = 0
for c in numeros_aleatorios:
    if menor == 0 or menor > c:
        menor = c
    if maior == 0 or maior < c:
        maior = c
print('O maior valor dessa tupla é {}'.format(maior))
print('O menor valor dessa tupla é {}'.format(menor))

import random

entrada = input('Nomes dos alunos separados por virgula: ')
lista = entrada.split(',')
lista = [elemento.strip() for elemento in lista]
print(lista)
random.shuffle(lista)
for i, ele in enumerate(lista):
    print('{}º {}'.format((i+1), ele))
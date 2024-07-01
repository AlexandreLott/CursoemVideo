import random

entrada = input('Nomes dos alunos separados por virgula: ')
lista = entrada.split(',')
lista = [elemento.strip() for elemento in lista]
print(lista)
print(random.choice(lista))

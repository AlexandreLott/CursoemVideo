frase = ('Maria comeu arroz ontem').lower().strip()
print("A frase contem {} a's".format(frase.count('a')))
print('O primeiro "a" se encontra na posição {}'.format(frase.find('a')+1))
print('O ultimo "a" se encontra na posição {}'.format(frase.rfind('a')+1))

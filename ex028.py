import random

numero = random.randint(0, 5)
print(numero)
guess = int(input('Qual o numero da vez (entre 0 e 5): '))
if numero == guess:
    print('Parabens você acertou')
else:
    print('Voce errou dessa vez')

import random

digit = random.randint(0000, 9999)
print(digit)
print('Unidade: {}'.format(digit // 1 % 10))
print('dezena: {}'.format(digit // 10 % 10))
print('centena: {}'.format(digit // 100 % 10))
print('milhar: {}'.format(digit // 1000 % 10))

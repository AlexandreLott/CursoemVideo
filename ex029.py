import random

vel = random.randint(60, 90)
print(vel)
if vel > 80:
    print('Voce recebeu uma multa de {}'.format(7*(vel-80)))

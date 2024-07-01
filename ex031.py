import random

dist = random.randint(1, 999)
if dist <= 200:
    print('Essa viagem cobra R$0,50 por km, então {}km fica {:.2f}'.format(dist, dist/0.5))
else:
    print('Essa viagem cobra R$0,45 por km, então {}km fica {:.2f}'.format(dist, dist / 0.45))
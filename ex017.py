import math
cop = float(input('Cateto oposto: '))
caj = float(input('Cateto adjacente: '))
print(math.sqrt(math.pow(cop, 2) + math.pow(caj, 2)))
print(math.hypot(cop, caj))

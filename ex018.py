import math
import random
ang = random.randint(0, 90)
angR = math.radians(ang)
print("o seno de {} e: {:.2f}".format(ang, math.sin(angR)))
print('O cosseno de {} é: {:.2f}'.format(ang, math.cos(angR)))
print('A tangente de {} é {:.2f}'.format(ang, math.tan(angR)))

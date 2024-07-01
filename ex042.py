print('Digite os 3 lados do suposto triangulo: ')
r1 = float(input())
r2 = float(input())
r3 = float(input())
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas três retas formam um tiangulo ',end='')
    if r1 == r2 and r2 == r3:
        print('equilatero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('isosceles')
    else:
        print('escaleno')
else:
    print('Essas três retas não formam um triangulo')

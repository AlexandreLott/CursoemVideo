r1 = float(input())
r2 = float(input())
r3 = float(input())
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas três retas formam um tiangulo')
else:
    print('Essas três retas não formam um triangulo')

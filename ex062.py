pt = int(input())
pa = int(input())
i = int(input('Quantos termos voce quer ver: '))
t=1
while t != 0:
    while i > 0:
        print(pt)
        pt += pa
        i -= 1
    t = int(input('Quantos termos a mais voce quer ver(0 para nunhum): '))
    i = t
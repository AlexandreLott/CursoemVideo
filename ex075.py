numeros = (int(input()), int(input()), int(input()), int(input()),)
print(numeros)
print(numeros.count(9))
if 3 in numeros:
    print(numeros.index(3) + 1)
else:
    print("Não foi digitado valor 3")
print('Os numeros pares são: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')

idade = 0
cont_maior = 0
cont_menor = 0
for c in range(0, 7):
    idade = int(input('digite a idade da pessoa {}: '.format(c+1)))
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print('{} pessoas são maiores de idade.'.format(cont_maior))
print('{} pessoas são menores de idade.'.format(cont_menor))

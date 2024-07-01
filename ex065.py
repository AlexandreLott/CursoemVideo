num = int(input('Digite um numero: '))
media = soma = count = 0
maior = menor = num
i = True
while i:
    soma += num
    count += 1
    if  num > maior:
        maior = num
    if num < menor:
        menor = num
    if input('Quer continuar?(s/n): ') == 'n':
        i = False
    else:
        num = int(input('Digite um numero: '))
media = soma / count
print('A media dos valores é {}'.format(media))
print('O maior valor é {}'.format(maior))
print('Omenor valor é {}'.format(menor))

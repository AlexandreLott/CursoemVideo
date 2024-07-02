count_numeros = soma = 0
while True:
    num = int(input('Digite um valor:(999 para parar)'))
    if num == 999:
        break
    count_numeros += 1
    soma += num
print('A quantidade de numeros apresentados: {}'.format(count_numeros))
print('A media dos valores apresntados: {:.2f}'.format(soma / count_numeros))

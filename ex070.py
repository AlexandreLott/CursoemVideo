total = count_1000 = cond_barato = 0
nome_barato = ''
cond = True
while cond:
    print('-' * 20)
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    print('-' * 20)
    total += preco
    if preco > 1000:
        count_1000 += 1
    if cond_barato == 0 or cond_barato > preco:
        cond_barato = preco
        nome_barato = nome
    while True:
        continua = input('Quer continuar?(S/N) ')
        if continua.lower() == 's':
            break
        if continua.lower() == 'n':
            cond = False
            break
print('Total da compra: {}'.format(total))
print('{} produtos custam mais de R$1000'.format(count_1000))
print('O produto mais caro {} e custa {}'.format(nome_barato, cond_barato))

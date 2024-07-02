while True:
    num = int(input('Insira um numero para saber a tabuada(negativo para encerrar): '))
    if num < 0:
        print('Programa tabuada encerrado, volte sempre!!')
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(num, c, num*c))


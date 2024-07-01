i = 0
num1 = float(input('Número 1: '))
num2 = float(input('Numero 2: '))
while i != 5:
    print("""MENU
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa""")
    i = int(input('O que deseja: '))
    if i == 1:
        soma = num1 + num2
        print('A soma dos dois valores é {}'.format(soma))
    if i == 2:
        mult = num1 * num2
        print('A multiplicação dos valores é {}'.format(mult))
    if i == 3:
        if num1 > num2:
            print('{} é maior'.format(num1))
        elif num2 > num1:
            print('{} é maior'.format(num2))
        else:
            print('Os numeros são iguais')
    if i == 4:
        num1 = float(input('Número 1: '))
        num2 = float(input('Numero 2: '))


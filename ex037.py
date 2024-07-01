num = int(input('Digite um numero inteiro que queria converter: '))
i = int(input("""Escolha a opção de converção:
1 - Binario
2 - Octal
3 - Hexadecimal
"""))
if i == 1:
    print('{} em binario: {}'.format(num, bin(num)[2:]))
if i == 2:
    print('{} em octal: {}'.format(num, oct(num)[2:]))
if i == 3:
    print('{} em hexadecimal: {}'.format(num, hex(num)[2:].upper()))
if i != 1 and i != 2 and i != 3:
    print('Voce escolheu uma opcão inexistente.')

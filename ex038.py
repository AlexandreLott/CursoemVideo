num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O primeiro e maior.')
elif num2 > num1:
    print('O segundo e maior.')
else:
    print('Não existe valor maior, os dois são iguais')
salario = int(input())
if salario > 1250:
    print('Com o aumento de 10% fica {:.2f}'.format(salario * 1.10))
else:
    print('Com o aumento de 15% fica {:.2f}'.format(salario * 1.15))

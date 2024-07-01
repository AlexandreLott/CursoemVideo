casav = float(input())
salario = float(input())
panos = int(input())
parcela = casav/(panos*12)
if parcela/salario > 0.3:
    print('O financiamento nao pode ser efetuado pois a parcela esta maior que 30% do salario ({:.2f}).'.format(parcela/salario))
else:
    print('O financiamento ficara R${:.2f} por parcela.'.format(parcela))
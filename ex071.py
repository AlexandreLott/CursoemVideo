notas_50 = notas_20 = notas_10 = notas_1 = 0
saque = int(input())
while saque > 0:
    if (saque/50).__trunc__() > 0:
        notas_50 = (saque/50).__trunc__()
        saque -= notas_50 * 50
    if (saque/20).__trunc__() > 0:
        notas_20 = (saque/20).__trunc__()
        saque -= notas_20 * 20
    if (saque/10).__trunc__() > 0:
        notas_10 = (saque/10).__trunc__()
        saque -= notas_10 * 10
    if saque > 0:
        notas_1 = saque
        saque -= notas_1
print('{} cedulas de R$50 | {} cedulas de R$20 | {} cedulas de R$10 | {} cedulas de R$1'.format(notas_50, notas_20, notas_10, notas_1))
dias = int(input('Quantos dias o carro foi alugado '))
km = float(input('Quantos Km esse carro rodou '))
print('O alugue fica em {:.2f}'.format(dias * 60 + km * 0.15))

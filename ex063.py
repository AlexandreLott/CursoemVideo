n = int(input('Quantos elementos da sequencio de fibonacci quer ver: '))
fibo = [0, 1]
i = 0
while i < n:
    if i == 0:
        print(fibo[i], end='')
    if i == 1:
        print(' → {}'.format(fibo[i]), end='')
    if i > 1:
        soma = fibo[i-1] + fibo[i-2]
        fibo.append(soma)
        print(' → {}'.format(fibo[i]), end='')
    i += 1


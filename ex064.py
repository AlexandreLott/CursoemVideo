num = soma = count_numeros = 0
print('Digite quantos numeros quiser(999 caso queira parar): ', end='')
while num != 999:
    num = int(input())
    if num != 999:
        count_numeros += 1
        soma += num
print(count_numeros)
print(soma)
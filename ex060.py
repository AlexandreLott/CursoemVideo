num = int(input())
result = 1
i = num
while i != 1:
    result *= i
    i -= 1
print('o fatorial de {} é {}'.format(num, result))

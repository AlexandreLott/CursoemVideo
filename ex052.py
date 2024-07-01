num = int(input())
valid = True
for c in range(2, float(num**0.5).__trunc__() + 1):
    if num % c ==  0:
        valid = False
        break
if valid:
    print('{} é um numero primo.'.format(num))
else:
    print('{} não é primo.'.format(num))
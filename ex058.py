import random

num_jogador = int(input('Tente um numero: '))
num_computador = random.randint(0, 10)
print(num_computador)
cont_tentativas = 0
while num_jogador != num_computador:
    print('Numero errado tente novamente: ')
    num_jogador = int(input())
    cont_tentativas += 1
print('Parabens voce acertou o número {} em {} tentativas'.format(num_computador, cont_tentativas+1))
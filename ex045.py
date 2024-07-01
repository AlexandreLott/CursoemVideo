import random

jogador = int(input())
computador = random.randint(1, 3)
if jogador == 1:
    print('Jogador escolheu pedra e ', end='')
if jogador == 2:
    print('Jogador escolheu papel e ', end='')
if jogador == 3:
    print('Jogador escolheu tesoura e ', end='')
if computador == 1:
    print('computador escolheu pedra')
if computador == 2:
    print('computador escolheu papel')
if computador == 3:
    print('computador escolheu tesoura')
if jogador == 1 and computador == 3:
    print('Jogador venceu!')
if jogador == 2 and computador == 1:
    print('Jogador venceu!')
if jogador == 3 and computador == 2:
    print('Jogador venceu!')
if computador == 1 and jogador == 3:
    print('Computador venceu!')
if computador == 2 and jogador == 1:
    print('Computador venceu!')
if computador == 3 and jogador == 2:
    print('Computador venceu!')
if jogador == computador:
    print('Empate')
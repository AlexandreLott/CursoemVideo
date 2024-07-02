import random

count_venceu = 0
while True:
    num_jogador = int(input('Escolha o numero que quer jogar: '))
    num_computador = random.randint(0,10)
    while True:
        par_impar = input('Voce quer par ou impar(P/I): ')
        if par_impar.lower() == 'p':
            break
        if par_impar.lower() == 'i':
            break
    if par_impar.lower() == 'p':
        if (num_jogador + num_computador) % 2 == 0:
            print('O computador jogou {}'.format(num_computador))
            print('Parabens você ganhou, vamos de novo!')
            count_venceu += 1
        else:
            print('O computador jogou {}'.format(num_computador))
            print('Que pena você perdeu.')
            break
    if par_impar.lower() == 'i':
        if (num_jogador-num_computador)%2==1:
            print('O computador jogou {}'.format(num_computador))
            print('Parabens você ganhou, vamos de novo!')
            count_venceu += 1
        else:
            print('O computador jogou {}'.format(num_computador))
            print('Que pena, você perdeu.')
            break
print('Você obteve uma sequencia de {} vitorias!!'.format(count_venceu))


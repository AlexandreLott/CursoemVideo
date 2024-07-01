preco = float(input())
metodo_pagamento = int(input("""Escolha a forma de pagamento:
1 - A vista(dinheiro ou cheque)
2 - A vista(catão)
3 - Ate 2x no cartão
4 - 3x ou mais no cartão
5 - Calcelar operação
"""))
if metodo_pagamento == 1:
    print('O valor do produto a vista(dineiro ou cheque) tem 10% de desconto e fica R${:.2f}'.format(preco*0.9))
elif metodo_pagamento == 2:
    print('O valor do produto a vista(cartão) tem 5% de desconto e fica R${:.2f}'.format(preco*0.95))
elif metodo_pagamento == 3:
    print('O valor do produto em ate 2x no cartão fica R${:.2f}'.format(preco))
elif metodo_pagamento == 4:
    print('O valor do produta em 3x ou mais no cartão fica R${:.2f}'.format(preco*1.2))
else:
    print('Opção invalida ou cancelado.')
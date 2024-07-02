produtos_precos = (
    'Sabão', 15.90,
    'Arroz', 23.50,
    'Feijão', 8.75,
    'Macarrão', 4.50,
    'Óleo', 7.20,
    'Açúcar', 3.99,
    'Café', 18.00,
    'Farinha', 5.60,
    'Leite', 4.80,
    'Sal', 1.50
)
for i in range(0, len(produtos_precos)-1, 2):
    print('{:.<30} R${:>6.2f}'.format(produtos_precos[i], produtos_precos[i+1]))
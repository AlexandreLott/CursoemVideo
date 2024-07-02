classificacao_brasileirao = (
    "Botafogo",
    "Flamengo",
    "Palmeiras",
    "Grêmio",
    "Fluminense",
    "Athletico-PR",
    "Fortaleza",
    "São Paulo",
    "Cruzeiro",
    "Internacional",
    "Red Bull Bragantino",
    "Santos",
    "Corinthians",
    "Bahia",
    "Vasco da Gama",
    "Cuiabá",
    "Coritiba",
    "Goiás",
    "América-MG",
    "Avaí"
)
print('Os cinco primeiros colocados são {}'.format(classificacao_brasileirao[0:5]))
print('Os ultimos quatro colocados são {}'.format(classificacao_brasileirao[-4]))
print('Os times em ordem alfabetica fica {}'.format(tuple(sorted(classificacao_brasileirao))))
print('O Corinthians esta na {}ª posição(Chapecoense nao estava na serie A)'.format(classificacao_brasileirao.index("Corinthians")+1))

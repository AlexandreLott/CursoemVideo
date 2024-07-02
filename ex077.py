palavras = (
    "abacaxi", "banana", "cachorro", "dente", "elefante",
    "foguete", "gato", "hipopotamo", "igreja", "janela",
    "kiwi", "leite", "manga", "navio", "ovo",
    "pato", "quadro", "rosa", "sol", "tigre"
)
vogais = 'aeiou'
for c in palavras:
    print('A palavra {} tem as vogais '.format(c), end='')
    for l in c:
        if l in vogais:
            print(l.upper(),end=' ')
    print('')

frase = input()
frase_sem_espaco = frase.replace(' ','')
frase_invertida = frase_sem_espaco[::-1].lower()
if frase_sem_espaco.lower() == frase_invertida.lower():
    print('{} é um palindromo'.format(frase))

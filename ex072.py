numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    i = int(input('Digite um valor entre 0 e 20: '))
    if i < 0 or i > 20:
        print("Tente novamente! ")
    else:
        print('Voce digitou o numero {}'.format(numeros_por_extenso[i]))
        break
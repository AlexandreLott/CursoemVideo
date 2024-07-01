sexo = input()
if sexo != 'm' and sexo != 'f':
    i = True
    while i:
        sexo = input('Informção errada, digite novamente: ')
        if sexo == 'm' or sexo == 'f':
            i = False
print(sexo)

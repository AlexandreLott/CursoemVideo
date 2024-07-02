
count_maior = 0
count_homem = 0
count_mulher = 0
cond = True

while cond:
    idade = int(input('Qual a idade: '))
    while True:
        sexo = input('Qual o sexo(H/M): ')
        if sexo.lower() == 'h':
            break
        if sexo.lower() == 'm':
            break
    if idade > 18:
        count_maior += 1
    if sexo.lower() == 'h':
        count_homem += 1
    if sexo.lower() == 'm' and idade < 20:
        count_mulher += 1
    while True:
        continua = input('Quer continuar(S/N): ')
        if continua.lower() == 'n':
            cond = False
            break
        if continua.lower() == 's':
            break

print('{} pessoas tem mais de 18 anos.'.format(count_maior))
print('{} homem foram cadastrados.'.format(count_homem))
print('{} mulheres tem menos de 20 anos.'.format(count_mulher))

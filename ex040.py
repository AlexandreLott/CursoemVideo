nota1 = float(input())
nota2 = float(input())
media = (nota1 + nota2) / 2
if media >= 7:
    print('Aprovada')
elif media < 5:
    print('Reprovada')
else:
    print('Recuperação')
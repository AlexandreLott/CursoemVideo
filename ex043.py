peso = float(input())
altura = float(input())
imc = peso / (altura/100)**2
print(imc)
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('"Peso ideal"')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

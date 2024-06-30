peso = float(input())
maior = peso
menor = peso
for c in range(0, 4):
    peso = float(input())
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(maior)
print(menor)

idade_velho = 0
media_idade = 0
count_m_jovem = 0
nome_h_velho = 0
for c in range(0,4):
    nome = input()
    idade = int(input())
    sexo = input()
    media_idade += idade
    if sexo.lower() == 'h' and idade_velho < idade:
        nome_h_velho = nome
        idade_velho = idade
    if sexo.lower() == 'm' and idade < 20:
        count_m_jovem += 1
print('{:.0f}'.format(media_idade/4))
print(nome_h_velho)
print(count_m_jovem)

import datetime

ano_nascimento = int(input('Digite a sua data de nascimento: '))
ano_atual = datetime.date.today().year
if ano_atual - ano_nascimento <= 9:
    print('Mirim')
elif ano_atual - ano_nascimento <=14:
    print('infatil')
elif ano_atual - ano_nascimento <=19:
    print('Junior')
elif ano_atual - ano_nascimento <=20:
    print('Senior')
else:
    print('Master')

import datetime

ano_nascimento = int(input('Qual seu ano de nascimento? '))
ano_atual = datetime.date.today().year
if ano_atual-  ano_nascimento == 18:
    print('Esse e o ano do seu alistamento.')
elif ano_atual - ano_nascimento < 18:
    print('Ainda nao chegou o meomento de se alistar, faltam {} anos para o seu alistamento'.format((ano_atual - ano_nascimento - 18) * (-1)))
else:
    print('Já passou o tempo de seu alistamento, CORRA!!! Voce deveria ter se alistado {} anos atras'.format((ano_atual - ano_nascimento - 18)))

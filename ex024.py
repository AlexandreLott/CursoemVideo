cidade = input('Qual sua cidade? ').strip()
if cidade.lower().find('santo') == 0:
    print('O nome da cidade começa com santo')
    print(cidade.lower().find('santo'))
else:
    print('o nome da cidade nao começa com santo')

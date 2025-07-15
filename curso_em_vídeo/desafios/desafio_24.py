cidade = str(input('Digite o nome da sua cidade: '))
print('O nome da sua cidade começa com a palavra SANTO?')
div = cidade.split()
print('SANTO' in div[0])

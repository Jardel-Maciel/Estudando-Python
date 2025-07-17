nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'jardel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'nome' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')

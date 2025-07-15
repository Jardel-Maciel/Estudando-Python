nome = str(input('Qual é o seu nome? ')).strip()
print(f'Seu nome maiusculo é: {nome.upper()}')
print(f'Seu nome menuscuo é: {nome.lower()}')
print(f'seu nome tem {len(nome)-nome.count(' ')} letras')
'''dividido = nome.split()
print(f'Seu primeiro nome é: {dividido[0]}')'''
print(f'Seu primeiro nome tem, {nome.find(' ')} letras')



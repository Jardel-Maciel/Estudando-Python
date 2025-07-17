from datetime import date
ano_nascimento = int(input('Qual seu ano de nascimento? '))
ano_atual = date.today().year
idade =  ano_atual - ano_nascimento 
if idade < 18:
    print('Você ainda vai se alista ou serviço militar.')
    print(f'Faltam {18 - idade} anos para você se alistar')
elif idade == 18:
    print('Já está na hora de se alistar ao serviço miçitar!')
else:
    print('Já passou da hora de se  alistar ao serviço militar')
    print(f'Já de passaram {idade - 18} ano do tempo certo para voccê se alistar. ')
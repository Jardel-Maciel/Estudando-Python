from datetime import date
ano_nasciemento = int(input('Qual o ano de nascimento do atleta? '))
ano_atual = date.today().year
idade = ano_atual - ano_nasciemento
if idade <= 9:
    print(f'O atleta tem {idade} anos de idade, sua categoria é MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos de idade, sua categoria é INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos de idade, sua categoria é JUNIO.')
elif idade == 20:
    print(f'O atleta tem {idade} anos de idade, sua categoria é SÊNIOR.')
elif idade > 20:
    print(f'O atleta tem {idade} anos de idade, sua categoria é MASTER.') 

'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo.')
else:
    print('carro velho.')
print('--FIM--')'''

#condição simplificada
'''tempo = int(input('Quanto temopo tem seu carro? '))
print('carro novo'if tempo <=3 else 'carro velho')
print('---FIM---')'''

'''nome = str(input('Qual seu nome? '))
if nome == 'jardel':
    print('que nome lindo que você tem.')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia! {nome}')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua media foi {m:.1f}')
if m >= 6:
    print('Média boa!')
else:
    print('Média ruim!')

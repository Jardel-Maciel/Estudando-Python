dist = int(input('Qual a dis tância da sua viagem: km '))
if dist <= 200:
    print(f'O valor da passagem é R$ {dist * 0.50:.2f}')
else:
    print(f'O valor da passagem é R${dist * 0.45:.2f}')
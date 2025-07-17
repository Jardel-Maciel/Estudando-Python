vel = float(input('Qual a velocidade do seu carro? '))
if vel > 80:
    print('Você foi multado!!!')
    multa = (vel - 80) * 7
    print(f'A multa vai custar R${multa}')
else:
    print('Tenha um bom dia, dirija com segurança!')

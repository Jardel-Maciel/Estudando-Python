vel = int(input('Qual a velocidade do seu carro? '))
if vel > 80:
    print('Você foi multado!!!')
    multa = (vel)+ 1 * 7
    print(f'A multa vai ustar R${multa}')

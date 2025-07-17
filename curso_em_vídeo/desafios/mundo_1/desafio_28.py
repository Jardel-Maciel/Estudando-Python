from random import randint
num = randint(0,5)
print('Olá eu sou seu computador e pensei em um número de 0 a 5, você consegue adivinhar?')
n = int(input('Digite seu numero: '))
if n == num:
    print('Você ganhou PARABÉNS!!')
else:
    print('Você PREDEU KKKKKKKKK!!')
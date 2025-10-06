from random import randint
num = randint(1, 10)
palpite = 0
tentativas = 0
while palpite != num:
    print('Ola pensei em um numero de 1 a 10 sera que você advinha qual numero eu pensei? \n')
    palpite = int(input('Digite seu Palpite: '))
    if palpite == num:
        print(f'Parabens você acertou, e precisou de {tentativas} tentativas para acertar. \n')
    if palpite != num:
        tentativas += 1
        print('Você errou, tente novamente.\n')
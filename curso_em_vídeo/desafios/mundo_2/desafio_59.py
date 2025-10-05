
numero1 = int(input('Digite o 1º numero: '))
numero2 = int(input('Digite o 2º numero: '))

menu = True
calculo = 0
while menu: 
    print()
    print('=' * 10 + 'Menu' + '=' * 10)
    print('escolha a operação desejada: ')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa \n')

    menu = int(input('Digite a sua opção: '))
    print('=' * 30)
    if menu == 1:
        calculo = numero1 + numero2
        print(f'O resultado da soma é de {calculo}')
    elif menu == 2:
        calculo = numero1 * numero2
        print(f'A multiplicação de {numero1} * {numero2} é igual a {calculo}') 
    elif menu == 3:
        if numero1 > numero2:
            print('O 1º número é maior que o 2º número. ')
        elif numero2 > numero1:
            print('O 2º número é maior que o 1º número. ')
        else:
            print('Os dois números são iguais') 
    elif menu == 4:
        numero1 = int(input('Digite o novo 1º numero: '))
        numero2 = int(input('Digite o novo 2º numero: '))

    elif menu == 5:
        menu = False

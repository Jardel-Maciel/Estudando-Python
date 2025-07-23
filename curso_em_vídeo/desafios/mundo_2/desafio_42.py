r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite outro valor: '))
r3 =  float(input('Digite oultimo valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores acima podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('O triangulo não pode ser formado: ')

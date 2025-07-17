sal = float(input('Qual o salario do funcionario? R$'))
almento = 10 /100 
almento1 = 15 /100
if sal >= 1250:
    print(f'Seu salario vai almentar 10% e ficara, R$ {sal + sal * almento } ')
else:
    print(f'Seu salario vai almentar 15% e ficara, R$ {sal + sal * almento1}')


#captação dos dados
print('-=-'*20)
print(' '*15 + 'BEM VINDO AO BANCO MACIEL')
print('-=-'*20)
valor_casa = float(input('Qual o valor da casa? R$'))
sal_comprador = float(input('Qual o salario do comprador? R$'))
anos_pagamento = int(input('Em quantos anos sera paga? '))

#tratamento dos dados
meses = anos_pagamento * 12
parcela = valor_casa / meses

#condições aninhadas
if parcela > sal_comprador * 0.30:    
    print('Infelizmente o imprestimo foi negado o valor da parcela ultrapassa 30% do seu salario.')
elif parcela < sal_comprador * 0.30:
    print('PARABENS SEU IMPRESTIMO FOI APROVADO!!!')
print(f'O valor da parcela é de {parcela:.2f}')

    
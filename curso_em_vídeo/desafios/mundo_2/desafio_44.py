print('=' * 15 + ' LOJA MACIEL ' + '='*15)
valor = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print(f'Sua compra foi parcelada em 2x de {parcela}, SEM JUROS')
elif opcao == 4:    
    total = valor + (valor * 20 / 100)
    total_de_parcelas = int(input('Quantas parcelas você deseja? '))
    parcela = total / total_de_parcelas
    print(f'Sua compra sera parcelada em {total_de_parcelas}x de R$ {parcela:.2f}, COM JUROS')
else:
    total = valor
    print('OPÇÃO INVÁLIDA de pagamento tente novamente')

print(f'Sua compra de R$ {valor:.2f}, vai custar R$ {total:.2f} no final')

    

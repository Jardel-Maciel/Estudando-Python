dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos kms rodados? '))
pago = dias * 60 + (km * 0.15)
print(f'O tatal a pagar é de R${pago:.2f}')

soma = 0 
for c in range(1, 7):
    num = int(input('Escolha um numero: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos numeros pares é igual a {soma}')    
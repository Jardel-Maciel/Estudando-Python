soma = 0
cont = 0
for numero in range(1, 501, 2):  # apenas ímpares
    if numero % 3 == 0:
        cont = cont + 1
        soma += numero
print(f'A soma de todos os {cont} valores é igual a {soma}') 
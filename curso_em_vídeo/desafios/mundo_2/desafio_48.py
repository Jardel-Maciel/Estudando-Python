soma = 0
for numero in range(1, 501, 2):  # apenas ímpares
    if numero % 3 == 0:
        soma += numero
print(f'A soma de todos o multiplos por 3 e igual a {soma}') 
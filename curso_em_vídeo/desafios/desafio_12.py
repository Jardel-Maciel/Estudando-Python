"""
faça um algoritimo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.

"""

preco = float(input('qual o valor do produto? '))
desconto = 5 / 100
valor_final = preco - (desconto * 100)

print(f'O valor do produto é de R$ {preco:.2f}')

print(f'O valor com desconto fica R$ {valor_final}')
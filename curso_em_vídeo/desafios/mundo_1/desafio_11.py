altura = float(input('Qual e a altura da parede? '))
largura = float(input('Qual e a largura da parede? '))
area = altura * largura

litros_de_tinta = area / 2

print(f'Sua parede tem {altura} X {largura} e sua area é de {area}m²')
print(f'Para pintar essa parede, você precisará de  {litros_de_tinta}l de tinta.')


